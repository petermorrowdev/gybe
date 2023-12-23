from __future__ import annotations
from typing import Dict, List, Optional
from pydantic import BaseModel, Field
from ...apimachinery.pkg.apis.meta import v1
from ...apimachinery.pkg.util import intstr


class Eviction(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description=(
            "APIVersion defines the versioned schema of this representation of an"
            " object. Servers should convert recognized schemas to the latest internal"
            " value, and may reject unrecognized values. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources"
        ),
    )
    deleteOptions: Optional[v1.DeleteOptions] = Field(
        None, description="DeleteOptions may be provided"
    )
    kind: Optional[str] = Field(
        None,
        description=(
            "Kind is a string value representing the REST resource this object"
            " represents. Servers may infer this from the endpoint the client submits"
            " requests to. Cannot be updated. In CamelCase. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"
        ),
    )
    metadata: Optional[v1.ObjectMeta] = Field(
        None, description="ObjectMeta describes the pod that is being evicted."
    )


class PodDisruptionBudgetSpec(BaseModel):
    maxUnavailable: Optional[intstr.IntOrString] = Field(
        None,
        description=(
            'An eviction is allowed if at most "maxUnavailable" pods selected by'
            ' "selector" are unavailable after the eviction, i.e. even in absence of'
            " the evicted pod. For example, one can prevent all voluntary evictions by"
            ' specifying 0. This is a mutually exclusive setting with "minAvailable".'
        ),
    )
    minAvailable: Optional[intstr.IntOrString] = Field(
        None,
        description=(
            'An eviction is allowed if at least "minAvailable" pods selected by'
            ' "selector" will still be available after the eviction, i.e. even in the'
            " absence of the evicted pod.  So for example you can prevent all voluntary"
            ' evictions by specifying "100%".'
        ),
    )
    selector: Optional[v1.LabelSelector] = Field(
        None,
        description=(
            "Label query over pods whose evictions are managed by the disruption"
            " budget. A null selector will match no pods, while an empty ({}) selector"
            " will select all pods within the namespace."
        ),
    )
    unhealthyPodEvictionPolicy: Optional[str] = Field(
        None,
        description=(
            "UnhealthyPodEvictionPolicy defines the criteria for when unhealthy pods"
            " should be considered for eviction. Current implementation considers"
            " healthy pods, as pods that have status.conditions item with"
            ' type="Ready",status="True".\n\nValid policies are IfHealthyBudget and'
            " AlwaysAllow. If no policy is specified, the default behavior will be"
            " used, which corresponds to the IfHealthyBudget policy.\n\nIfHealthyBudget"
            ' policy means that running pods (status.phase="Running"), but not yet'
            " healthy can be evicted only if the guarded application is not disrupted"
            " (status.currentHealthy is at least equal to status.desiredHealthy)."
            " Healthy pods will be subject to the PDB for eviction.\n\nAlwaysAllow"
            ' policy means that all running pods (status.phase="Running"), but not yet'
            " healthy are considered disrupted and can be evicted regardless of whether"
            " the criteria in a PDB is met. This means perspective running pods of a"
            " disrupted application might not get a chance to become healthy. Healthy"
            " pods will be subject to the PDB for eviction.\n\nAdditional policies may"
            " be added in the future. Clients making eviction decisions should disallow"
            " eviction of unhealthy pods if they encounter an unrecognized policy in"
            " this field.\n\nThis field is alpha-level. The eviction API uses this"
            " field when the feature gate PDBUnhealthyPodEvictionPolicy is enabled"
            " (disabled by default)."
        ),
    )


class PodDisruptionBudgetStatus(BaseModel):
    conditions: Optional[List[v1.Condition]] = Field(
        None,
        description=(
            "Conditions contain conditions for PDB. The disruption controller sets the"
            " DisruptionAllowed condition. The following are known values for the"
            " reason field (additional reasons could be added in the future): -"
            " SyncFailed: The controller encountered an error and wasn't able to"
            " compute\n              the number of allowed disruptions. Therefore no"
            " disruptions are\n              allowed and the status of the condition"
            " will be False.\n- InsufficientPods: The number of pods are either at or"
            " below the number\n                    required by the"
            " PodDisruptionBudget. No disruptions are\n                    allowed and"
            " the status of the condition will be False.\n- SufficientPods: There are"
            " more pods than required by the PodDisruptionBudget.\n                 "
            " The condition will be True, and the number of allowed\n                 "
            " disruptions are provided by the disruptionsAllowed property."
        ),
    )
    currentHealthy: int = Field(..., description="current number of healthy pods")
    desiredHealthy: int = Field(
        ..., description="minimum desired number of healthy pods"
    )
    disruptedPods: Optional[Dict[str, v1.Time]] = Field(
        None,
        description=(
            "DisruptedPods contains information about pods whose eviction was processed"
            " by the API server eviction subresource handler but has not yet been"
            " observed by the PodDisruptionBudget controller. A pod will be in this map"
            " from the time when the API server processed the eviction request to the"
            " time when the pod is seen by PDB controller as having been marked for"
            " deletion (or after a timeout). The key in the map is the name of the pod"
            " and the value is the time when the API server processed the eviction"
            " request. If the deletion didn't occur and a pod is still there it will be"
            " removed from the list automatically by PodDisruptionBudget controller"
            " after some time. If everything goes smooth this map should be empty for"
            " the most of the time. Large number of entries in the map may indicate"
            " problems with pod deletions."
        ),
    )
    disruptionsAllowed: int = Field(
        ..., description="Number of pod disruptions that are currently allowed."
    )
    expectedPods: int = Field(
        ..., description="total number of pods counted by this disruption budget"
    )
    observedGeneration: Optional[int] = Field(
        None,
        description=(
            "Most recent generation observed when updating this PDB status."
            " DisruptionsAllowed and other status information is valid only if"
            " observedGeneration equals to PDB's object generation."
        ),
    )


class PodDisruptionBudget(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description=(
            "APIVersion defines the versioned schema of this representation of an"
            " object. Servers should convert recognized schemas to the latest internal"
            " value, and may reject unrecognized values. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources"
        ),
    )
    kind: Optional[str] = Field(
        None,
        description=(
            "Kind is a string value representing the REST resource this object"
            " represents. Servers may infer this from the endpoint the client submits"
            " requests to. Cannot be updated. In CamelCase. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"
        ),
    )
    metadata: Optional[v1.ObjectMeta] = Field(
        None,
        description=(
            "Standard object's metadata. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata"
        ),
    )
    spec: Optional[PodDisruptionBudgetSpec] = Field(
        None,
        description="Specification of the desired behavior of the PodDisruptionBudget.",
    )
    status: Optional[PodDisruptionBudgetStatus] = Field(
        None, description="Most recently observed status of the PodDisruptionBudget."
    )


class PodDisruptionBudgetList(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description=(
            "APIVersion defines the versioned schema of this representation of an"
            " object. Servers should convert recognized schemas to the latest internal"
            " value, and may reject unrecognized values. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources"
        ),
    )
    items: List[PodDisruptionBudget] = Field(
        ..., description="Items is a list of PodDisruptionBudgets"
    )
    kind: Optional[str] = Field(
        None,
        description=(
            "Kind is a string value representing the REST resource this object"
            " represents. Servers may infer this from the endpoint the client submits"
            " requests to. Cannot be updated. In CamelCase. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"
        ),
    )
    metadata: Optional[v1.ListMeta] = Field(
        None,
        description=(
            "Standard object's metadata. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata"
        ),
    )
