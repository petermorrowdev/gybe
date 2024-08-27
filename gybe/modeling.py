"""Make models from functions for downstream tooling."""

import inspect
from dataclasses import make_dataclass
from typing import Callable

from gybe.k8s.types import Manifest


def create_input_model(func: Callable[..., Manifest]) -> type:
    """Create dataclass input model from a decorated function."""
    argspec = inspect.getfullargspec(func)
    if argspec.defaults:
        positional_count = len(argspec.args) - len(argspec.defaults)
        defaults = dict(zip(argspec.args[positional_count:], argspec.defaults))
    else:
        defaults = dict()

    fields = [(k, t, defaults.get(k, ...)) for k, t in argspec.annotations.items() if k != 'return']
    return make_dataclass(f'{func.__name__}', fields)
