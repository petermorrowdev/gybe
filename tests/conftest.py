import pytest
from click import Command
from click.testing import CliRunner, Result


def _run_cli(cli_fn: Command, yaml: str, *args: str) -> Result:
    runner = CliRunner()
    with runner.isolated_filesystem():
        values_file_name = 'values.yaml'
        with open(values_file_name, 'w') as values_file:
            values_file.write(yaml)
        return runner.invoke(cli_fn, [values_file_name, *args])


@pytest.fixture
def run_cli():
    """Invoke test CLI"""
    return _run_cli
