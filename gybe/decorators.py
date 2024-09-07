"""Decorators for building CLI commands."""

import inspect
import sys
from dataclasses import fields
from typing import Any, Callable

import click
from cattrs import Converter, transform_error

from gybe.exceptions import InvalidOutputError
from gybe.k8s.types import K8sResource, K8sSpec, Manifest
from gybe.modeling import create_input_model
from gybe.yaml import yaml_dumps, yaml_loads


def _omit_none_values(obj: K8sSpec) -> dict[str, Any]:
    u = {}
    for f in fields(obj):
        v = getattr(obj, f.name)
        if v is not None:
            if inspect.isclass(f.type) and issubclass(f.type, K8sSpec):
                u[f.name] = _c.unstructure(v, f.type)
            else:
                u[f.name] = _c.unstructure(v)
    return u


_c = Converter()
_c.register_unstructure_hook(K8sSpec, _omit_none_values)


def _bind_function(f):
    @click.argument('file', required=True, type=click.File('r'))
    def func(file):
        input_data = yaml_loads(file.read()) or dict()
        input_model = create_input_model(f)
        try:
            input_obj = _c.structure(input_data, input_model)
        except Exception as exc:
            print('validation errors:')
            for m in transform_error(exc):
                print('-', m)
            sys.exit(-1)

        input_fields = [f.name for f in fields(input_model)]
        _kwargs = {kwarg: getattr(input_obj, kwarg) for kwarg in input_fields}
        manifest = f(**_kwargs)

        # Validate outputs
        if not isinstance(manifest, list):
            raise InvalidOutputError()

        for resource in manifest:
            if not isinstance(resource, K8sResource):
                raise InvalidOutputError()

        # Print manifest
        print('---\n'.join([yaml_dumps(_c.unstructure(r)) for r in manifest]))

    func.__name__ = f.__name__
    return func


def transpiler(f: Callable[..., Manifest]):
    """Command that takes in a YAML file and outputs a Kubernetes manifest YAML file."""
    func = _bind_function(f)
    return click.command()(func)
