import inspect

from pydantic import create_model


def create_input_model(func):
    argspec = inspect.getfullargspec(func)
    if argspec.defaults:
        positional_count = len(argspec.args) - len(argspec.defaults)
        defaults = dict(zip(argspec.args[positional_count:], argspec.defaults))
    else:
        defaults = dict()

    pyd_params = {
        k: (t, defaults.get(k, ...))
        for k, t in argspec.annotations.items()
        if k != 'return'
    }

    return create_model(f'{func.__name__}', **pyd_params)
