import sys
import click
from cattrs import Converter, transform_error

from gybe.exceptions import InvalidOutputError
from gybe.modeling import create_input_model
from gybe.yaml import yaml_dumps, yaml_loads

c = Converter(omit_if_default=True)


def _bind_function(f):
    @click.argument('file', required=True, type=click.File('r'))
    def func(file):
        input_data = yaml_loads(file.read()) or dict()
        try:
            input_obj = c.structure(input_data, create_input_model(f))
        except Exception as exc:
            print('Validation Error:')
            for m in transform_error(exc):
                print('-', m)
            sys.exit(-1)

        _kwargs = c.unstructure(input_obj)
        manifest = f(**_kwargs)

        # Validate outputs
        if not isinstance(manifest, list):
            raise InvalidOutputError()

        # Print manifest
        print('---\n'.join([yaml_dumps(c.unstructure(r)) for r in manifest]))

    func.__name__ = f.__name__
    return func


def transpiler(f):
    """Command that takes in a YAML file and outputs a Kubernetes manifest YAML file."""
    func = _bind_function(f)
    return click.command()(func)
