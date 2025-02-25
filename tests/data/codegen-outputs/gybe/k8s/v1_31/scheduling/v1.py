"""Models generated from Kubernetes OpenAPI Spec."""
from __future__ import annotations
from typing import List, Optional, Literal
from dataclasses import dataclass
from gybe.k8s.types import JSONObj, JSONDict, K8sSpec, K8sResource
import gybe.k8s.v1_31.meta.v1

@dataclass
class PriorityClass(K8sResource):
    """
    PriorityClass defines mapping from a priority class name to the priority integer value. The value can
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
    apiVersion: Literal['scheduling.k8s.io/v1'] = 'scheduling.k8s.io/v1'
    kind: Literal['PriorityClass'] = 'PriorityClass'
    description: Optional[str] = None
    globalDefault: Optional[bool] = None
    metadata: Optional[gybe.k8s.v1_31.meta.v1.ObjectMeta] = None
    preemptionPolicy: Optional[str] = None