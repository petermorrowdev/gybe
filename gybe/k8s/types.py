"""Type aliases for JSON serializable objects."""

from dataclasses import dataclass
from typing import Mapping, TypeAlias, Union

JSONObj: TypeAlias = Union[Mapping[str, 'JSONObj'], list['JSONObj'], str, int, float, bool, None]
JSONDict: TypeAlias = Mapping[str, Union['JSONObj', 'JSONDict']]


# decorating the base classes with @dataclass has no runtime effect but tells `mypy` to
# expect subclasses to each be a dataclass
@dataclass
class K8sSpec:
    """Base model class for all kubernetes dataclasses."""


@dataclass
class K8sResource(K8sSpec):
    """Base model for kubernetes resources, like Deployment, Service and StatefulSet"""


Manifest: TypeAlias = list[K8sResource]
