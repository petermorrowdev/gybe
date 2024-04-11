import gybe
from gybe.exceptions import InvalidOutputError


@gybe.transpiler
def invalid_output_not_list():
    return 'foo'


def test_invalid_output_not_list_raises_error(run_cli):
    result = run_cli(invalid_output_not_list, '')
    assert isinstance(result.exception, InvalidOutputError)
