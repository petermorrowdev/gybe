"""Models generated from Kubernetes OpenAPI Spec."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Literal, Optional

import gybe.k8s.v1_30.meta.v1
from gybe.k8s.types import JSONDict, JSONObj, K8sResource, K8sSpec


@dataclass
class Eviction(K8sSpec):
    """Eviction evicts a pod from its node subject to certain policies and safety constraints. This is a
    subresource of Pod.  A request to cause such an eviction is created by POSTing to .../pods/<pod
    name>/evictions.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        deleteOptions: DeleteOptions may be provided
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: ObjectMeta describes the pod that is being evicted.

    """

    apiVersion: Optional[str] = None
    deleteOptions: Optional[gybe.k8s.v1_30.meta.v1.DeleteOptions] = None
    kind: Optional[str] = None
    metadata: Optional[gybe.k8s.v1_30.meta.v1.ObjectMeta] = None


@dataclass
class PodDisruptionBudget(K8sResource):
    """PodDisruptionBudget is an object to define the max disruption that can be caused to a collection of
    pods
    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object's metadata.
        spec: Specification of the desired behavior of the PodDisruptionBudget.
        status: Most recently observed status of the PodDisruptionBudget.

    """

    apiVersion: Literal['policy/v1'] = 'policy/v1'
    kind: Literal['PodDisruptionBudget'] = 'PodDisruptionBudget'
    metadata: Optional[gybe.k8s.v1_30.meta.v1.ObjectMeta] = None
    spec: Optional[PodDisruptionBudgetSpec] = None
    status: Optional[PodDisruptionBudgetStatus] = None


@dataclass
class PodDisruptionBudgetList(K8sSpec):
    """PodDisruptionBudgetList is a collection of PodDisruptionBudgets.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        items: Items is a list of PodDisruptionBudgets
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object's metadata.

    """

    items: List[PodDisruptionBudget]
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[JSONObj] = None


@dataclass
class PodDisruptionBudgetSpec(K8sSpec):
    """PodDisruptionBudgetSpec is a description of a PodDisruptionBudget.

    Attributes:
        maxUnavailable: An eviction is allowed if at most 'maxUnavailable' pods selected by 'selector' are
            unavailable after the eviction, i.e. even in absence of the evicted pod. For example, one can
            prevent all voluntary evictions by specifying 0. This is a mutually exclusive setting with
            'minAvailable'.
        minAvailable: An eviction is allowed if at least 'minAvailable' pods selected by 'selector' will still
            be available after the eviction, i.e. even in the absence of the evicted pod.  So for example you
            can prevent all voluntary evictions by specifying '100%'.
        selector: Label query over pods whose evictions are managed by the disruption budget. A null selector
            will match no pods, while an empty ({}) selector will select all pods within the namespace.
        unhealthyPodEvictionPolicy: UnhealthyPodEvictionPolicy defines the criteria for when unhealthy pods
            should be considered for eviction. Current implementation considers healthy pods, as pods that
            have status.conditions item with type='Ready',status='True'.  Valid policies are IfHealthyBudget
            and AlwaysAllow. If no policy is specified, the default behavior will be used, which corresponds
            to the IfHealthyBudget policy.  IfHealthyBudget policy means that running pods
            (status.phase='Running'), but not yet healthy can be evicted only if the guarded application is
            not disrupted (status.currentHealthy is at least equal to status.desiredHealthy). Healthy pods
            will be subject to the PDB for eviction.  AlwaysAllow policy means that all running pods
            (status.phase='Running'), but not yet healthy are considered disrupted and can be evicted
            regardless of whether the criteria in a PDB is met. This means perspective running pods of a
            disrupted application might not get a chance to become healthy. Healthy pods will be subject to
            the PDB for eviction.  Additional policies may be added in the future. Clients making eviction
            decisions should disallow eviction of unhealthy pods if they encounter an unrecognized policy in
            this field.  This field is beta-level. The eviction API uses this field when the feature gate
            PDBUnhealthyPodEvictionPolicy is enabled (enabled by default).

    """

    maxUnavailable: Optional[str] = None
    minAvailable: Optional[str] = None
    selector: Optional[gybe.k8s.v1_30.meta.v1.LabelSelector] = None
    unhealthyPodEvictionPolicy: Optional[str] = None


@dataclass
class PodDisruptionBudgetStatus(K8sSpec):
    """PodDisruptionBudgetStatus represents information about the status of a PodDisruptionBudget. Status may
    trail the actual state of a system.

    Attributes:
        conditions: Conditions contain conditions for PDB. The disruption controller sets the
            DisruptionAllowed condition. The following are known values for the reason field (additional
            reasons could be added in the future): - SyncFailed: The controller encountered an error and
            wasn't able to compute               the number of allowed disruptions. Therefore no disruptions
            are               allowed and the status of the condition will be False. - InsufficientPods: The
            number of pods are either at or below the number                     required by the
            PodDisruptionBudget. No disruptions are                     allowed and the status of the
            condition will be False. - SufficientPods: There are more pods than required by the
            PodDisruptionBudget.                   The condition will be True, and the number of allowed
            disruptions are provided by the disruptionsAllowed property.
        currentHealthy: current number of healthy pods
        desiredHealthy: minimum desired number of healthy pods
        disruptedPods: DisruptedPods contains information about pods whose eviction was processed by the API
            server eviction subresource handler but has not yet been observed by the PodDisruptionBudget
            controller. A pod will be in this map from the time when the API server processed the eviction
            request to the time when the pod is seen by PDB controller as having been marked for deletion (or
            after a timeout). The key in the map is the name of the pod and the value is the time when the API
            server processed the eviction request. If the deletion didn't occur and a pod is still there it
            will be removed from the list automatically by PodDisruptionBudget controller after some time. If
            everything goes smooth this map should be empty for the most of the time. Large number of entries
            in the map may indicate problems with pod deletions.
        disruptionsAllowed: Number of pod disruptions that are currently allowed.
        expectedPods: total number of pods counted by this disruption budget
        observedGeneration: Most recent generation observed when updating this PDB status. DisruptionsAllowed
            and other status information is valid only if observedGeneration equals to PDB's object
            generation.

    """

    disruptionsAllowed: int
    currentHealthy: int
    desiredHealthy: int
    expectedPods: int
    conditions: Optional[List[gybe.k8s.v1_30.meta.v1.Condition]] = None
    disruptedPods: Optional[JSONDict] = None
    observedGeneration: Optional[int] = None
