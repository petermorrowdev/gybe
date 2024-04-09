"""Type aliases for JSON serializable objects."""
from typing import TypeAlias, Union

JSONObj: TypeAlias = Union[dict[str, 'JSONObj'], list['JSONObj'], str, int, float, bool, None]
JSONDict: TypeAlias = dict[str, Union['JSONObj', 'JSONDict']]
