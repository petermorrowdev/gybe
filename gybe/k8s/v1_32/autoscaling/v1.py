"""Models generated from Kubernetes OpenAPI Spec."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Literal, Optional

import gybe.k8s.v1_32.meta.v1
from gybe.k8s.types import JSONObj, K8sResource, K8sSpec


@dataclass
class Scale(K8sResource):
    """Scale represents a scaling request for a resource.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object metadata;
        spec: spec defines the behavior of the scale.
        status: status is the current status of the scale.

    """

    apiVersion: Literal['autoscaling/v1'] = 'autoscaling/v1'
    kind: Literal['Scale'] = 'Scale'
    metadata: Optional[gybe.k8s.v1_32.meta.v1.ObjectMeta] = None
    spec: Optional[ScaleSpec] = None
    status: Optional[ScaleStatus] = None


@dataclass
class ScaleSpec(K8sSpec):
    """ScaleSpec describes the attributes of a scale subresource.

    Attributes:
        replicas: replicas is the desired number of instances for the scaled object.

    """

    replicas: Optional[int] = None


@dataclass
class ScaleStatus(K8sSpec):
    """ScaleStatus represents the current status of a scale subresource.

    Attributes:
        replicas: replicas is the actual number of observed instances of the scaled object.
        selector: selector is the label query over pods that should match the replicas count. This is same as
            the label selector but in the string format to avoid introspection by clients. The string will be
            in the same format as the query-param syntax. More info about label selectors:
            https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/

    """

    replicas: int
    selector: Optional[str] = None


@dataclass
class CrossVersionObjectReference(K8sSpec):
    """CrossVersionObjectReference contains enough information to let you identify the referred resource.

    Attributes:
        apiVersion: apiVersion is the API version of the referent
        kind: kind is the kind of the referent;
        name: name is the name of the referent;

    """

    kind: str
    name: str
    apiVersion: Optional[str] = None


@dataclass
class HorizontalPodAutoscaler(K8sResource):
    """configuration of a horizontal pod autoscaler.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object metadata.
        spec: spec defines the behaviour of autoscaler.
        status: status is the current information about the autoscaler.

    """

    apiVersion: Literal['autoscaling/v1'] = 'autoscaling/v1'
    kind: Literal['HorizontalPodAutoscaler'] = 'HorizontalPodAutoscaler'
    metadata: Optional[gybe.k8s.v1_32.meta.v1.ObjectMeta] = None
    spec: Optional[HorizontalPodAutoscalerSpec] = None
    status: Optional[HorizontalPodAutoscalerStatus] = None


@dataclass
class HorizontalPodAutoscalerList(K8sSpec):
    """list of horizontal pod autoscaler objects.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        items: items is the list of horizontal pod autoscaler objects.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard list metadata.

    """

    items: List[HorizontalPodAutoscaler]
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[JSONObj] = None


@dataclass
class HorizontalPodAutoscalerSpec(K8sSpec):
    """specification of a horizontal pod autoscaler.

    Attributes:
        maxReplicas: maxReplicas is the upper limit for the number of pods that can be set by the autoscaler;
            cannot be smaller than MinReplicas.
        minReplicas: minReplicas is the lower limit for the number of replicas to which the autoscaler can
            scale down.  It defaults to 1 pod.  minReplicas is allowed to be 0 if the alpha feature gate
            HPAScaleToZero is enabled and at least one Object or External metric is configured.  Scaling is
            active as long as at least one metric value is available.
        scaleTargetRef: reference to scaled resource; horizontal pod autoscaler will learn the current
            resource consumption and will set the desired number of pods by using its Scale subresource.
        targetCPUUtilizationPercentage: targetCPUUtilizationPercentage is the target average CPU utilization
            (represented as a percentage of requested CPU) over all the pods; if not specified the default
            autoscaling policy will be used.

    """

    scaleTargetRef: CrossVersionObjectReference
    maxReplicas: int
    minReplicas: Optional[int] = None
    targetCPUUtilizationPercentage: Optional[int] = None


@dataclass
class HorizontalPodAutoscalerStatus(K8sSpec):
    """current status of a horizontal pod autoscaler
    Attributes:
        currentCPUUtilizationPercentage: currentCPUUtilizationPercentage is the current average CPU
            utilization over all pods, represented as a percentage of requested CPU, e.g. 70 means that an
            average pod is using now 70% of its requested CPU.
        currentReplicas: currentReplicas is the current number of replicas of pods managed by this autoscaler.
        desiredReplicas: desiredReplicas is the  desired number of replicas of pods managed by this
            autoscaler.
        lastScaleTime: lastScaleTime is the last time the HorizontalPodAutoscaler scaled the number of pods;
            used by the autoscaler to control how often the number of pods is changed.
        observedGeneration: observedGeneration is the most recent generation observed by this autoscaler.

    """

    currentReplicas: int
    desiredReplicas: int
    currentCPUUtilizationPercentage: Optional[int] = None
    lastScaleTime: Optional[str] = None
    observedGeneration: Optional[int] = None
