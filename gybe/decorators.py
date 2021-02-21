import click
import json
import sys

from pydantic import BaseModel, ValidationError

from gybe.exceptions import InvalidOutputError
from gybe.modeling import create_input_model
from gybe.yaml import yaml_loads, yaml_dumps


def _bind_function(f):
    @click.argument('file', required=True, type=click.File('r'))
    def func(file):
        # Prepare inputs
        _InputModel = create_input_model(f)
        input_data = yaml_loads(file.read()) or dict()

        # Validate inputs
        try:
            input_obj = _InputModel(**input_data)
        except ValidationError as e:
            print('Validation Error:')
            print(e)
            sys.exit(-1)

        # Execute
        _kwargs = {k: getattr(input_obj, k) for k in input_obj.dict().keys()}
        manifest = f(**_kwargs)

        # Validate outputs
        if not isinstance(manifest, list):
            raise InvalidOutputError()

        if not all(isinstance(r, BaseModel) for r in manifest):
            raise InvalidOutputError()

        # Print manifest
        print(
            '---\n'.join(
                [
                    yaml_dumps(json.loads(r.json(exclude_none=True)))
                    for r in manifest
                ]
            )
        )

    func.__name__ = f.__name__
    return func


def transpiler(f):
    func = _bind_function(f)
    return click.command()(func)
