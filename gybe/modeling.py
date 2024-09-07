"""Make models from functions for downstream tooling."""

import inspect
from dataclasses import make_dataclass
from typing import Any, Callable, Union

from gybe.k8s.types import Manifest


def create_input_model(func: Callable[..., Manifest]) -> type:
    """Create dataclass input model from a decorated function."""
    argspec = inspect.getfullargspec(func)
    if argspec.defaults:
        positional_count = len(argspec.args) - len(argspec.defaults)
        defaults = dict(zip(argspec.args[positional_count:], argspec.defaults))
    else:
        defaults = dict()

    fields: list[Union[tuple[str, type, Any], tuple[str, type]]] = []
    for k, t in argspec.annotations.items():
        if k != 'return':
            if k in defaults:
                fields.append((k, t, defaults[k]))
            else:
                fields.append((k, t))
    return make_dataclass(f'{func.__name__}', fields)
