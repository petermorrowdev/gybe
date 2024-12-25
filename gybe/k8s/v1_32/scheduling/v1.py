"""Models generated from Kubernetes OpenAPI Spec."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

import gybe.k8s.v1_32.meta.v1
from gybe.k8s.types import JSONObj, K8sSpec


@dataclass
class PriorityClass(K8sSpec):
    """PriorityClass defines mapping from a priority class name to the priority integer value. The value can
    be any valid integer.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        description: description is an arbitrary string that usually provides guidelines on when this priority
            class should be used.
        globalDefault: globalDefault specifies whether this PriorityClass should be considered as the default
            priority for pods that do not have any priority class. Only one PriorityClass can be marked as
            `globalDefault`. However, if more than one PriorityClasses exists with their `globalDefault` field
            set to true, the smallest value of such global default PriorityClasses will be used as the default
            priority.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object's metadata.
        preemptionPolicy: preemptionPolicy is the Policy for preempting pods with lower priority. One of
            Never, PreemptLowerPriority. Defaults to PreemptLowerPriority if unset.
        value: value represents the integer value of this priority class. This is the actual priority that
            pods receive when they have the name of this class in their pod spec.

    """

    value: int
    apiVersion: Optional[str] = None
    description: Optional[str] = None
    globalDefault: Optional[bool] = None
    kind: Optional[str] = None
    metadata: Optional[gybe.k8s.v1_32.meta.v1.ObjectMeta] = None
    preemptionPolicy: Optional[str] = None


@dataclass
class PriorityClassList(K8sSpec):
    """PriorityClassList is a collection of priority classes.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        items: items is the list of PriorityClasses
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard list metadata

    """

    items: List[PriorityClass]
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[JSONObj] = None
