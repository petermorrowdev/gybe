from gybe.exceptions import InvalidOutputError
import gybe


@gybe.transpiler
def invalid_output_not_list():
    return 'foo'


def test_invalid_output_not_list_raises_error(run_cli):
    result = run_cli(invalid_output_not_list, '')
    assert isinstance(result.exception, InvalidOutputError)


@gybe.transpiler
def invalid_output_items():
    return [1, 2, 3]


def test_invalid_output_items_raises_error(run_cli):
    result = run_cli(invalid_output_items, '')
    assert isinstance(result.exception, InvalidOutputError)
