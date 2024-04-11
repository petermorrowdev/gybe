from typing import Callable

import pytest
from click.testing import CliRunner


def _run_cli(cli_fn: Callable, yaml: str):
    runner = CliRunner()
    with runner.isolated_filesystem():
        values_file_name = 'values.yaml'
        with open(values_file_name, 'w') as values_file:
            values_file.write(yaml)
        return runner.invoke(cli_fn, [values_file_name])


@pytest.fixture
def run_cli():
    return _run_cli
