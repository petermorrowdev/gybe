"""Models generated from Kubernetes OpenAPI Spec."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Literal, Optional

import gybe.k8s.v1_35.meta.v1 as _meta_v1
from gybe.k8s.types import K8sResource, K8sSpec


@dataclass
class BasicSchedulingPolicy(K8sSpec):
    """BasicSchedulingPolicy indicates that standard Kubernetes scheduling behavior should be used."""


@dataclass
class GangSchedulingPolicy(K8sSpec):
    """GangSchedulingPolicy defines the parameters for gang scheduling.

    Attributes:
        minCount: MinCount is the minimum number of pods that must be schedulable or scheduled at the same
            time for the scheduler to admit the entire group. It must be a positive integer.

    """

    minCount: int


@dataclass
class PodGroup(K8sSpec):
    """PodGroup represents a set of pods with a common scheduling policy.

    Attributes:
        name: Name is a unique identifier for the PodGroup within the Workload. It must be a DNS label. This
            field is immutable.
        policy: Policy defines the scheduling policy for this PodGroup.

    """

    name: str
    policy: PodGroupPolicy


@dataclass
class PodGroupPolicy(K8sSpec):
    """PodGroupPolicy defines the scheduling configuration for a PodGroup.

    Attributes:
        basic: Basic specifies that the pods in this group should be scheduled using standard Kubernetes
            scheduling behavior.
        gang: Gang specifies that the pods in this group should be scheduled using all-or-nothing semantics.

    """

    basic: Optional[BasicSchedulingPolicy] = None
    gang: Optional[GangSchedulingPolicy] = None


@dataclass
class TypedLocalObjectReference(K8sSpec):
    """TypedLocalObjectReference allows to reference typed object inside the same namespace.

    Attributes:
        apiGroup: APIGroup is the group for the resource being referenced. If APIGroup is empty, the specified
            Kind must be in the core API group. For any other third-party types, setting APIGroup is required.
            It must be a DNS subdomain.
        kind: Kind is the type of resource being referenced. It must be a path segment name.
        name: Name is the name of resource being referenced. It must be a path segment name.

    """

    kind: str
    name: str
    apiGroup: Optional[str] = None


@dataclass
class Workload(K8sResource):
    """Workload allows for expressing scheduling constraints that should be used when managing lifecycle of
    workloads from scheduling perspective, including scheduling, preemption, eviction and other phases.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object's metadata. Name must be a DNS subdomain.
        spec: Spec defines the desired behavior of a Workload.

    """

    spec: WorkloadSpec
    apiVersion: Literal['scheduling.k8s.io/v1alpha1'] = 'scheduling.k8s.io/v1alpha1'
    kind: Literal['Workload'] = 'Workload'
    metadata: Optional[_meta_v1.ObjectMeta] = None


@dataclass
class WorkloadSpec(K8sSpec):
    """WorkloadSpec defines the desired state of a Workload.

    Attributes:
        controllerRef: ControllerRef is an optional reference to the controlling object, such as a Deployment
            or Job. This field is intended for use by tools like CLIs to provide a link back to the original
            workload definition. When set, it cannot be changed.
        podGroups: PodGroups is the list of pod groups that make up the Workload. The maximum number of pod
            groups is 8. This field is immutable.

    """

    podGroups: List[PodGroup]
    controllerRef: Optional[TypedLocalObjectReference] = None
