"""Type aliases for JSON serializable objects."""

from typing import Union

JSONObj = Union[dict[str, 'JSONObj'], list['JSONObj'], str, int, float, bool, None]
JSONDict = dict[str, Union['JSONObj', 'JSONDict']]
