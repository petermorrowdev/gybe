from __future__ import annotations

import argparse
import ast
import json
import textwrap
from pathlib import Path
from typing import Optional, TypeAlias, TypedDict, Union

k8s_openapi_dir = Path('kubernetes/api/openapi-spec/v3')
failed_keys = set()
# a json-serializable dict
JSONObj: TypeAlias = Union[dict[str, 'JSONObj'], list['JSONObj'], str, int, float, bool, None]
JSONDict: TypeAlias = dict[str, Union['JSONObj', 'JSONDict']]
schema_type_map = dict(
    string='str',
    boolean='bool',
    integer='int',
    number='float',
    object='JSONDict',
)
# ignored models fallback to `JSONObj`
ignore_models = {
    # includes hyphenated fields
    'JSONSchemaProps',
    # 'except` reserved: `IPBlock.except`
    'IPBlock',
    # `from` reserved: `NetworkPolicyIngressRule.from`
    'NetworkPolicyIngressRule',
    # `continue` reserved: `ListMeta.continue`
    'ListMeta',
    # `RawExtension` is strange
    'RawExtension',
    # Undefined models
    'CustomResourceSubresourceStatus',
    'StorageVersionSpec',
    'FieldsV1',
}


class JSONSchemaProperties(TypedDict):
    type: str
    items: JSONSchemaProperties
    allOf: Optional[list[JSONSchemaProperties]]


class K8sModel:
    def __init__(self, name: str, properties: JSONSchemaProperties):
        self.name = name
        self.properties = properties

    @property
    def module_name(self):
        return _ref_to_module_name(self.name)


class K8sModule:
    def __init__(self, version_module: str, module_name: str):
        self._version_module = version_module
        self._module_name = module_name
        self._module_path = Path(self._module_name.replace('.', '/') + '.py')
        self._module_path.parent.mkdir(exist_ok=True)
        self._module_imports: set[str] = set()
        self._class_defs: list[ast.ClassDef] = []
        self._line_length = 110

    def write_module(self):
        with open(self._module_path, 'w') as f:
            f.write(self._unparse())

    def add_model(self, name, properties, description, required):
        model_def = self._model_def(
            name.split('.')[-1],
            properties,
            description or f'Schema model {name}.',
            required or [],
        )
        self._class_defs.append(model_def)

    def _unparse(self):
        imports = [
            '"""Models generated from Kubernetes OpenAPI Spec."""',
            'from __future__ import annotations',
            'from typing import List, Optional',
            'from dataclasses import dataclass',
            'from gybe.k8s.types import JSONObj, JSONDict',
        ] + sorted(list(self._module_imports))
        mod = ast.parse('\n'.join(imports))
        for c in self._class_defs:
            mod.body.append(c)
        return ast.unparse(mod)

    def _model_def(
        self,
        name: str,
        properties: dict[str, JSONSchemaProperties],
        description: str,
        required: list[str],
    ) -> ast.ClassDef:
        cdef = ast.parse('@dataclass\nclass ' + name + ':\n    pass').body[0]
        if not isinstance(cdef, ast.ClassDef):
            raise ValueError(f'{cdef} is not expected ast.ClassDef')
        sections = [
            '\n'.join(textwrap.wrap(description, width=self._line_length - 8)),
            'Attributes:',
            self._prop_desc(properties),
            '',
        ]
        docstring = '\n'.join(sections).replace('"', "'").replace('\\', '')
        docstring = textwrap.indent(docstring, '    ')
        cdef.body = [ast.parse(f'"""\n{docstring}\n"""').body[0]]

        fields = []
        for k in required:
            field_type = self._type_hint_for(properties[k])
            field = f'{k}: {field_type}'
            fields.append(field)

        for k, v in properties.items():
            if k not in required:
                field_type = self._type_hint_for(v)
                field = f'{k}: Optional[{field_type}] = None'
                fields.append(field)

        for field in fields:
            try:
                cdef.body.append(ast.parse(field).body[0])
            except SyntaxError:
                failed_keys.add(
                    (
                        k,
                        name,
                    ),
                )
        return cdef

    def _prop_desc(self, properties: dict[str, JSONSchemaProperties]) -> str:
        descriptions = []
        for k, v in properties.items():
            d = str(v.get('description', '...'))
            # Removes noisy "More info:" links
            n = 'More info:'
            if n in d:
                d = d[: d.index(n)]
            description = '\n'.join(
                textwrap.wrap(f'{k}: {d}', width=self._line_length - 8, subsequent_indent='    ')
            )
            descriptions.append(description)
        fd = '\n'.join(descriptions)
        return textwrap.indent(fd, '    ')

    def _type_hint_for(self, v: JSONSchemaProperties) -> str:
        json_type = v.get('type')
        if json_type == 'array':
            item_type = self._type_hint_for(v['items'])
            return f'List[{item_type}]'
        elif json_type is not None:
            try:
                return schema_type_map[json_type]
            except KeyError as e:
                raise NotImplementedError(json_type) from e

        ref = v.get('$ref')
        if ref is None:
            allof = v.get('allOf')
            if allof is not None:
                ref = allof[0].get('$ref')
        if ref is not None:
            ref = str(ref)
            import_ = _ref_to_module_name(ref, version_module=self._version_module)
            for m in ignore_models:
                if m in ref:
                    return 'JSONObj'
            if ref.endswith('IntOrString') or 'Time' in ref:
                return 'str'
            if import_ != self._module_name:
                self._module_imports.add('import ' + import_)
                return _ref_to_model_path(ref, version_module=self._version_module)
            else:
                return ref.split('.')[-1]

        return schema_type_map['string']


def write_k8s_models(k8s_version_module: str) -> None:
    model_schemas = dict()
    for p in k8s_openapi_dir.iterdir():
        with p.open() as f:
            spec = json.load(f)
        schemas = spec.get('components', dict()).get('schemas') or dict()
        for name, schema in schemas.items():
            is_ignored = any(m in name for m in ignore_models)
            if name.startswith('io.k8s') and not is_ignored:
                model_schemas[name] = schema

    k8s_modules = dict()
    for name in model_schemas.keys():
        if name not in k8s_modules:
            module_name = _ref_to_module_name(name, k8s_version_module)
            k8s_modules[module_name] = K8sModule(k8s_version_module, module_name)

    for name, schema in model_schemas.items():
        properties = schema.get('properties')
        description = schema.get('description')
        required = schema.get('required')
        if properties:
            k8s_module = k8s_modules[_ref_to_module_name(name, k8s_version_module)]
            k8s_module.add_model(name, properties, description, required)

    for k8s_module in k8s_modules.values():
        k8s_module.write_module()


def _ref_to_model_path(ref: str, version_module: str) -> str:
    return f'gybe.k8s.{version_module}.' + '.'.join(ref.split('/')[-1].split('.')[-3:])


def _ref_to_module_name(ref: str, version_module: str) -> str:
    return '.'.join(_ref_to_model_path(ref, version_module).split('.')[:-1])


def _remove_if_first(d: list[str], v: str) -> list[str]:
    if len(d) and d[0] == v:
        return d[1:]
    else:
        return d


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('k8s_version_module')
    args = parser.parse_args()
    Path('gybe/k8s/' + args.k8s_version_module).mkdir(exist_ok=True)
    write_k8s_models(args.k8s_version_module)
