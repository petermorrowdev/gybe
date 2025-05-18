"""Decorators for building CLI commands."""

import inspect
import sys
from dataclasses import fields
from typing import IO, Any, Callable

import click
from cattrs import Converter, transform_error

from gybe.exceptions import InvalidOutputError
from gybe.k8s.types import JSONDict, JSONObj, K8sResource, K8sSpec, Manifest
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


def set_nested_arg(path: str, value: str, data: JSONObj) -> None:
    """Set value in nested JSON object using a basic "." path."""
    keys = path.split('.')
    for key in keys[:-1]:
        if isinstance(data, dict):
            data = data[key]
        elif isinstance(data, list):
            try:
                data = data[int(key)]
            except ValueError:
                raise KeyError(f'Expected integer but recieved "{key}"')

    last_key: str | int
    if isinstance(data, dict):
        last_key = keys[-1]
    elif isinstance(data, list):
        last_key = int(keys[-1])
    else:
        raise KeyError('Path leads to unindexable location')

    if isinstance(data, list) and isinstance(last_key, int):
        data[last_key] = value
    elif isinstance(data, dict) and isinstance(last_key, str):
        data[last_key] = value
    else:
        raise ValueError('Path leads to unexpected data type')


def _bind_function(f):
    @click.argument('file', required=True, type=click.File('r'))
    @click.option('--set', 'set_nested_args', type=str, multiple=True)
    def func(file: IO[str], set_nested_args: list[str]):
        inputs: JSONDict = yaml_loads(file.read()) or dict()

        input_model = create_input_model(f)
        try:
            input_obj: Any = _c.structure(inputs, input_model)
        except Exception as exc:
            print('validation errors:')
            for m in transform_error(exc):
                print('-', m)
            sys.exit(-1)

        if len(set_nested_args):
            patched_inputs = _c.unstructure(input_obj)
            for arg in set_nested_args:
                try:
                    path, value = arg.split('=')
                except (ValueError, IndexError):
                    print('\nERROR: --set expects this format: path.to.arg=value')
                    sys.exit(-1)

                try:
                    set_nested_arg(path, value, patched_inputs)
                except KeyError:
                    print(f'\nERROR: path "{path}" does not exist in the input data')
                    sys.exit(-1)

            input_obj = _c.structure(patched_inputs, input_model)

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
