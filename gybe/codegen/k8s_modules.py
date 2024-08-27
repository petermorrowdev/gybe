"""Code generation logic for k8s modules."""

from __future__ import annotations

import ast
import json
import textwrap
from pathlib import Path
from typing import Optional, TypeAlias, TypedDict, Union

k8s_openapi_dir = Path('kubernetes/api/openapi-spec/v3')
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
# NOTE: The expected `apiVersion` values for k8s resources are documented here:
# https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/
# in the tables with `Group`, `Version` and `Kind`. This data does not exist in
# the kubernetes JSON schema, so it's manually mapped below.
resource_api_versions = {
    'io.k8s.api.admissionregistration': 'admissionregistration.k8s.io',
    'io.k8s.api.apiserverinternal': 'admissionregistration.k8s.io',
    'io.k8s.api.apps': 'apps',
    'io.k8s.api.authentication': 'authentication.k8s.io',
    'io.k8s.api.authorization': 'rbac.authorization.k8s.io',
    'io.k8s.api.autoscaling': 'autoscaling',
    'io.k8s.api.batch': 'batch',
    'io.k8s.api.certificates': 'certificates.k8s.io',
    'io.k8s.api.core': '',  # `apiVersion: v1`, `apiVersion: v2`, ect.
    'io.k8s.api.flowcontrol': 'flowcontrol.apiserver.k8s.io',
    'io.k8s.api.networking': 'networking.k8s.io',
    'io.k8s.api.policy': 'policy',
    'io.k8s.api.resource': 'policy',
    'io.k8s.api.storage': 'storage.k8s.io',
    'io.k8s.api.storagemigration': 'storage.k8s.io',
    'io.k8s.apiextensions-apiserver.pkg.apis.apiextensions': 'apiextensions.k8s.io',
    'io.k8s.kube-aggregator.pkg.apis.apiregistration': 'apiregistration.k8s.io',
}
resource_prop_names = {'apiVersion', 'kind', 'metadata', 'spec', 'status'}


class JSONSchemaProperties(TypedDict):
    """A subset of attributes expected in kubernetes' JSON schema spec."""

    type: str
    items: JSONSchemaProperties
    allOf: Optional[list[JSONSchemaProperties]]


class K8sModule:
    """An abstract representation of a kubernetes module in gybe."""

    def __init__(self, version_module: str, module_name: str):
        """Initialize a K8sModule.

        Attributes
        ----------
        version_module: Python version submodule under the k8s module (ex: 'v1_30')
        module_name: Python non-relative import path (ex: 'gybe.k8s.v1_30.apps.v1').

        """
        self._version_module = version_module
        self._module_name = module_name
        self._module_path = Path(self._module_name.replace('.', '/') + '.py')
        self._module_path.parent.mkdir(exist_ok=True)
        self._module_imports: set[str] = set()
        self._class_defs: list[ast.ClassDef] = []
        self._line_length = 110

    def write_module(self):
        """Write abstract module to python file."""
        with open(self._module_path, 'w') as f:
            f.write(self._unparse())

    def add_model(
        self,
        name: str,
        properties: dict[str, JSONSchemaProperties],
        description: str,
        required: list[str],
    ) -> None:
        """Add a kubernetes JSON schema specification to the module as a dataclass ast."""
        name_parts = name.split('.')
        prop_names = set(properties.keys())
        literal_properties = dict()
        if len(resource_prop_names - prop_names) == 0:
            k = '.'.join(name_parts[:-2])
            api_group = resource_api_versions.get(k)
            if api_group:
                api_version = api_group + '/' + name_parts[-2]
            else:
                api_version = name_parts[-2]
            literal_properties['apiVersion'] = api_version
            literal_properties['kind'] = name_parts[-1]
        model_def = self._model_def(
            name=name_parts[-1],
            properties=properties,
            description=description or f'Schema model {name}.',
            required=required or [],
            resource_properties=literal_properties,
        )
        self._class_defs.append(model_def)

    def _unparse(self):
        if self._module_name.endswith('api.resource'):
            return '"""Models generated from Kubernetes OpenAPI Spec."""\nQuantity = str | int | float'

        imports = [
            '"""Models generated from Kubernetes OpenAPI Spec."""',
            'from __future__ import annotations',
            'from typing import List, Optional, Literal',
            'from dataclasses import dataclass',
            'from gybe.k8s.types import JSONObj, JSONDict, K8sSpec, K8sResource',
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
        resource_properties: dict[str, str],
    ) -> ast.ClassDef:
        base_cls = 'K8sSpec' if len(resource_properties) == 0 else 'K8sResource'
        cdef = ast.parse('@dataclass\nclass ' + name + f'({base_cls}):\n    pass').body[0]
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

        literal_props = resource_properties or dict()
        fields: list[tuple[str, int]] = []
        for k, v in properties.items():
            if k in literal_props:
                literal_value = literal_props[k]
                fields.append((f"{k}: Literal['{literal_value}'] = '{literal_value}'", 200))
            elif k in required:
                field_type = self._type_hint_for(properties[k])
                field = f'{k}: {field_type}'
                fields.append((field, required.index(k)))
            else:
                field_type = self._type_hint_for(v)
                field = f'{k}: Optional[{field_type}] = None'
                fields.append((field, 300))

        for field, _ in sorted(fields, key=lambda f: f[1]):
            cdef.body.append(ast.parse(field).body[0])
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


def _write_k8s_models(k8s_version_module: str) -> None:
    model_schemas = dict()
    for p in k8s_openapi_dir.iterdir():
        with p.open() as f:
            spec = json.load(f)
        schemas = spec.get('components', dict()).get('schemas') or dict()
        for name, schema in schemas.items():
            if name.startswith('io.k8s'):
                if not any(m in name for m in ignore_models):
                    model_schemas[name] = schema

    k8s_modules: dict[str, K8sModule] = dict()
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


def _write_module_init(k8s_version_module: str) -> None:
    module_path = Path('gybe/k8s/' + k8s_version_module)
    module_path.mkdir(exist_ok=True)
    with open(module_path / '__init__.py', 'w') as f:
        f.write('"""k8s dataclass models generated by gybe"""')


def _ref_to_model_path(ref: str, version_module: str) -> str:
    return f'gybe.k8s.{version_module}.' + '.'.join(ref.split('/')[-1].split('.')[-3:])


def _ref_to_module_name(ref: str, version_module: str) -> str:
    return '.'.join(_ref_to_model_path(ref, version_module).split('.')[:-1])


def write_module(k8s_version_module):
    """Write generated k8s module based on kubernetes JSON schema."""
    _write_module_init(k8s_version_module)
    _write_k8s_models(k8s_version_module)
