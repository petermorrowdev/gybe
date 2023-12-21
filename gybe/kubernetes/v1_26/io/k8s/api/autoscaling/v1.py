from __future__ import annotations
from typing import List, Optional
from pydantic import BaseModel, Field
from ...apimachinery.pkg.apis.meta import v1


class ScaleSpec(BaseModel):
    replicas: Optional[int] = Field(
        None,
        description=(
            "replicas is the desired number of instances for the scaled object."
        ),
    )


class ScaleStatus(BaseModel):
    replicas: int = Field(
        ...,
        description=(
            "replicas is the actual number of observed instances of the scaled object."
        ),
    )
    selector: Optional[str] = Field(
        None,
        description=(
            "selector is the label query over pods that should match the replicas"
            " count. This is same as the label selector but in the string format to"
            " avoid introspection by clients. The string will be in the same format as"
            " the query-param syntax. More info about label selectors:"
            " https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/"
        ),
    )


class CrossVersionObjectReference(BaseModel):
    apiVersion: Optional[str] = Field(
        None, description="apiVersion is the API version of the referent"
    )
    kind: str = Field(
        ...,
        description=(
            "kind is the kind of the referent; More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"
        ),
    )
    name: str = Field(
        ...,
        description=(
            "name is the name of the referent; More info:"
            " https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names"
        ),
    )


class HorizontalPodAutoscalerSpec(BaseModel):
    maxReplicas: int = Field(
        ...,
        description=(
            "maxReplicas is the upper limit for the number of pods that can be set by"
            " the autoscaler; cannot be smaller than MinReplicas."
        ),
    )
    minReplicas: Optional[int] = Field(
        None,
        description=(
            "minReplicas is the lower limit for the number of replicas to which the"
            " autoscaler can scale down.  It defaults to 1 pod.  minReplicas is allowed"
            " to be 0 if the alpha feature gate HPAScaleToZero is enabled and at least"
            " one Object or External metric is configured.  Scaling is active as long"
            " as at least one metric value is available."
        ),
    )
    scaleTargetRef: CrossVersionObjectReference = Field(
        ...,
        description=(
            "reference to scaled resource; horizontal pod autoscaler will learn the"
            " current resource consumption and will set the desired number of pods by"
            " using its Scale subresource."
        ),
    )
    targetCPUUtilizationPercentage: Optional[int] = Field(
        None,
        description=(
            "targetCPUUtilizationPercentage is the target average CPU utilization"
            " (represented as a percentage of requested CPU) over all the pods; if not"
            " specified the default autoscaling policy will be used."
        ),
    )


class HorizontalPodAutoscalerStatus(BaseModel):
    currentCPUUtilizationPercentage: Optional[int] = Field(
        None,
        description=(
            "currentCPUUtilizationPercentage is the current average CPU utilization"
            " over all pods, represented as a percentage of requested CPU, e.g. 70"
            " means that an average pod is using now 70% of its requested CPU."
        ),
    )
    currentReplicas: int = Field(
        ...,
        description=(
            "currentReplicas is the current number of replicas of pods managed by this"
            " autoscaler."
        ),
    )
    desiredReplicas: int = Field(
        ...,
        description=(
            "desiredReplicas is the  desired number of replicas of pods managed by this"
            " autoscaler."
        ),
    )
    lastScaleTime: Optional[v1.Time] = Field(
        None,
        description=(
            "lastScaleTime is the last time the HorizontalPodAutoscaler scaled the"
            " number of pods; used by the autoscaler to control how often the number of"
            " pods is changed."
        ),
    )
    observedGeneration: Optional[int] = Field(
        None,
        description=(
            "observedGeneration is the most recent generation observed by this"
            " autoscaler."
        ),
    )


class Scale(BaseModel):
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
            "Standard object metadata; More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata."
        ),
    )
    spec: Optional[ScaleSpec] = Field(
        None,
        description=(
            "spec defines the behavior of the scale. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status."
        ),
    )
    status: Optional[ScaleStatus] = Field(
        None,
        description=(
            "status is the current status of the scale. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status."
            " Read-only."
        ),
    )


class HorizontalPodAutoscaler(BaseModel):
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
            "Standard object metadata. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata"
        ),
    )
    spec: Optional[HorizontalPodAutoscalerSpec] = Field(
        None,
        description=(
            "spec defines the behaviour of autoscaler. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status."
        ),
    )
    status: Optional[HorizontalPodAutoscalerStatus] = Field(
        None, description="status is the current information about the autoscaler."
    )


class HorizontalPodAutoscalerList(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description=(
            "APIVersion defines the versioned schema of this representation of an"
            " object. Servers should convert recognized schemas to the latest internal"
            " value, and may reject unrecognized values. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources"
        ),
    )
    items: List[HorizontalPodAutoscaler] = Field(
        ..., description="items is the list of horizontal pod autoscaler objects."
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
    metadata: Optional[v1.ListMeta] = Field(None, description="Standard list metadata.")
