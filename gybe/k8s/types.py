"""Type aliases for JSON serializable objects."""

from dataclasses import dataclass
from typing import Mapping, TypeAlias, Union

JSONObj: TypeAlias = Union[Mapping[str, 'JSONObj'], list['JSONObj'], str, int, float, bool, None]
JSONDict: TypeAlias = Mapping[str, Union['JSONObj', 'JSONDict']]


@dataclass
class K8sSpec:
    """Base model class for all kubernetes dataclasses."""
