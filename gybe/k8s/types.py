"""Type aliases for JSON serializable objects."""

from typing import Mapping, TypeAlias, Union

JSONObj: TypeAlias = Union[Mapping[str, 'JSONObj'], list['JSONObj'], str, int, float, bool, None]
JSONDict: TypeAlias = Mapping[str, Union['JSONObj', 'JSONDict']]


class K8sSpec:
    """Base model class for all kubernetes dataclasses."""


class K8sResource(K8sSpec):
    """Base model for kubernetes resources, like Deployment, Service and StatefulSet"""
