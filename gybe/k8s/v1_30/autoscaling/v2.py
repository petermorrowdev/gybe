"""Models generated from Kubernetes OpenAPI Spec."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Literal, Optional

import gybe.k8s.v1_30.api.resource
import gybe.k8s.v1_30.meta.v1
from gybe.k8s.types import JSONObj, K8sResource, K8sSpec


@dataclass
class ContainerResourceMetricSource(K8sSpec):
    """ContainerResourceMetricSource indicates how to scale on a resource metric known to Kubernetes, as
    specified in requests and limits, describing each pod in the current scale target (e.g. CPU or
    memory).  The values will be averaged together before being compared to the target.  Such metrics are
    built in to Kubernetes, and have special scaling options on top of those available to normal per-pod
    metrics using the 'pods' source.  Only one 'target' type should be set.

    Attributes:
        container: container is the name of the container in the pods of the scaling target
        name: name is the name of the resource in question.
        target: target specifies the target value for the given metric

    """

    name: str
    target: MetricTarget
    container: str


@dataclass
class ContainerResourceMetricStatus(K8sSpec):
    """ContainerResourceMetricStatus indicates the current value of a resource metric known to Kubernetes, as
    specified in requests and limits, describing a single container in each pod in the current scale
    target (e.g. CPU or memory).  Such metrics are built in to Kubernetes, and have special scaling
    options on top of those available to normal per-pod metrics using the 'pods' source.

    Attributes:
        container: container is the name of the container in the pods of the scaling target
        current: current contains the current value for the given metric
        name: name is the name of the resource in question.

    """

    name: str
    current: MetricValueStatus
    container: str


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
class ExternalMetricSource(K8sSpec):
    """ExternalMetricSource indicates how to scale on a metric not associated with any Kubernetes object (for
    example length of queue in cloud messaging service, or QPS from loadbalancer running outside of
    cluster).

    Attributes:
        metric: metric identifies the target metric by name and selector
        target: target specifies the target value for the given metric

    """

    metric: MetricIdentifier
    target: MetricTarget


@dataclass
class ExternalMetricStatus(K8sSpec):
    """ExternalMetricStatus indicates the current value of a global metric not associated with any Kubernetes
    object.

    Attributes:
        current: current contains the current value for the given metric
        metric: metric identifies the target metric by name and selector

    """

    metric: MetricIdentifier
    current: MetricValueStatus


@dataclass
class HPAScalingPolicy(K8sSpec):
    """HPAScalingPolicy is a single policy which must hold true for a specified past interval.

    Attributes:
        periodSeconds: periodSeconds specifies the window of time for which the policy should hold true.
            PeriodSeconds must be greater than zero and less than or equal to 1800 (30 min).
        type: type is used to specify the scaling policy.
        value: value contains the amount of change which is permitted by the policy. It must be greater than
            zero

    """

    type: str
    value: int
    periodSeconds: int


@dataclass
class HPAScalingRules(K8sSpec):
    """HPAScalingRules configures the scaling behavior for one direction. These Rules are applied after
    calculating DesiredReplicas from metrics for the HPA. They can limit the scaling velocity by
    specifying scaling policies. They can prevent flapping by specifying the stabilization window, so that
    the number of replicas is not set instantly, instead, the safest value from the stabilization window
    is chosen.

    Attributes:
        policies: policies is a list of potential scaling polices which can be used during scaling. At least
            one policy must be specified, otherwise the HPAScalingRules will be discarded as invalid
        selectPolicy: selectPolicy is used to specify which policy should be used. If not set, the default
            value Max is used.
        stabilizationWindowSeconds: stabilizationWindowSeconds is the number of seconds for which past
            recommendations should be considered while scaling up or scaling down. StabilizationWindowSeconds
            must be greater than or equal to zero and less than or equal to 3600 (one hour). If not set, use
            the default values: - For scale up: 0 (i.e. no stabilization is done). - For scale down: 300 (i.e.
            the stabilization window is 300 seconds long).

    """

    policies: Optional[List[HPAScalingPolicy]] = None
    selectPolicy: Optional[str] = None
    stabilizationWindowSeconds: Optional[int] = None


@dataclass
class HorizontalPodAutoscaler(K8sResource):
    """HorizontalPodAutoscaler is the configuration for a horizontal pod autoscaler, which automatically
    manages the replica count of any resource implementing the scale subresource based on the metrics
    specified.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: metadata is the standard object metadata.
        spec: spec is the specification for the behaviour of the autoscaler.
        status: status is the current information about the autoscaler.

    """

    apiVersion: Literal['autoscaling/v2'] = 'autoscaling/v2'
    kind: Literal['HorizontalPodAutoscaler'] = 'HorizontalPodAutoscaler'
    metadata: Optional[gybe.k8s.v1_30.meta.v1.ObjectMeta] = None
    spec: Optional[HorizontalPodAutoscalerSpec] = None
    status: Optional[HorizontalPodAutoscalerStatus] = None


@dataclass
class HorizontalPodAutoscalerBehavior(K8sSpec):
    """HorizontalPodAutoscalerBehavior configures the scaling behavior of the target in both Up and Down
    directions (scaleUp and scaleDown fields respectively).

    Attributes:
        scaleDown: scaleDown is scaling policy for scaling Down. If not set, the default value is to allow to
            scale down to minReplicas pods, with a 300 second stabilization window (i.e., the highest
            recommendation for the last 300sec is used).
        scaleUp: scaleUp is scaling policy for scaling Up. If not set, the default value is the higher of:   *
            increase no more than 4 pods per 60 seconds   * double the number of pods per 60 seconds No
            stabilization is used.

    """

    scaleDown: Optional[HPAScalingRules] = None
    scaleUp: Optional[HPAScalingRules] = None


@dataclass
class HorizontalPodAutoscalerCondition(K8sSpec):
    """HorizontalPodAutoscalerCondition describes the state of a HorizontalPodAutoscaler at a certain point.

    Attributes:
        lastTransitionTime: lastTransitionTime is the last time the condition transitioned from one status to
            another
        message: message is a human-readable explanation containing details about the transition
        reason: reason is the reason for the condition's last transition.
        status: status is the status of the condition (True, False, Unknown)
        type: type describes the current condition

    """

    type: str
    status: str
    lastTransitionTime: Optional[str] = None
    message: Optional[str] = None
    reason: Optional[str] = None


@dataclass
class HorizontalPodAutoscalerList(K8sSpec):
    """HorizontalPodAutoscalerList is a list of horizontal pod autoscaler objects.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        items: items is the list of horizontal pod autoscaler objects.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: metadata is the standard list metadata.

    """

    items: List[HorizontalPodAutoscaler]
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[JSONObj] = None


@dataclass
class HorizontalPodAutoscalerSpec(K8sSpec):
    """HorizontalPodAutoscalerSpec describes the desired functionality of the HorizontalPodAutoscaler.

    Attributes:
        behavior: behavior configures the scaling behavior of the target in both Up and Down directions
            (scaleUp and scaleDown fields respectively). If not set, the default HPAScalingRules for scale up
            and scale down are used.
        maxReplicas: maxReplicas is the upper limit for the number of replicas to which the autoscaler can
            scale up. It cannot be less that minReplicas.
        metrics: metrics contains the specifications for which to use to calculate the desired replica count
            (the maximum replica count across all metrics will be used).  The desired replica count is
            calculated multiplying the ratio between the target value and the current value by the current
            number of pods.  Ergo, metrics used must decrease as the pod count is increased, and vice-versa.
            See the individual metric source types for more information about how each type of metric must
            respond. If not set, the default metric will be set to 80% average CPU utilization.
        minReplicas: minReplicas is the lower limit for the number of replicas to which the autoscaler can
            scale down.  It defaults to 1 pod.  minReplicas is allowed to be 0 if the alpha feature gate
            HPAScaleToZero is enabled and at least one Object or External metric is configured.  Scaling is
            active as long as at least one metric value is available.
        scaleTargetRef: scaleTargetRef points to the target resource to scale, and is used to the pods for
            which metrics should be collected, as well as to actually change the replica count.

    """

    scaleTargetRef: CrossVersionObjectReference
    maxReplicas: int
    behavior: Optional[HorizontalPodAutoscalerBehavior] = None
    metrics: Optional[List[MetricSpec]] = None
    minReplicas: Optional[int] = None


@dataclass
class HorizontalPodAutoscalerStatus(K8sSpec):
    """HorizontalPodAutoscalerStatus describes the current status of a horizontal pod autoscaler.

    Attributes:
        conditions: conditions is the set of conditions required for this autoscaler to scale its target, and
            indicates whether or not those conditions are met.
        currentMetrics: currentMetrics is the last read state of the metrics used by this autoscaler.
        currentReplicas: currentReplicas is current number of replicas of pods managed by this autoscaler, as
            last seen by the autoscaler.
        desiredReplicas: desiredReplicas is the desired number of replicas of pods managed by this autoscaler,
            as last calculated by the autoscaler.
        lastScaleTime: lastScaleTime is the last time the HorizontalPodAutoscaler scaled the number of pods,
            used by the autoscaler to control how often the number of pods is changed.
        observedGeneration: observedGeneration is the most recent generation observed by this autoscaler.

    """

    desiredReplicas: int
    conditions: Optional[List[HorizontalPodAutoscalerCondition]] = None
    currentMetrics: Optional[List[MetricStatus]] = None
    currentReplicas: Optional[int] = None
    lastScaleTime: Optional[str] = None
    observedGeneration: Optional[int] = None


@dataclass
class MetricIdentifier(K8sSpec):
    """MetricIdentifier defines the name and optionally selector for a metric
    Attributes:
        name: name is the name of the given metric
        selector: selector is the string-encoded form of a standard kubernetes label selector for the given
            metric When set, it is passed as an additional parameter to the metrics server for more specific
            metrics scoping. When unset, just the metricName will be used to gather metrics.

    """

    name: str
    selector: Optional[gybe.k8s.v1_30.meta.v1.LabelSelector] = None


@dataclass
class MetricSpec(K8sSpec):
    """MetricSpec specifies how to scale based on a single metric (only `type` and one other matching field
    should be set at once).

    Attributes:
        containerResource: containerResource refers to a resource metric (such as those specified in requests
            and limits) known to Kubernetes describing a single container in each pod of the current scale
            target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling
            options on top of those available to normal per-pod metrics using the 'pods' source. This is an
            alpha feature and can be enabled by the HPAContainerMetrics feature flag.
        external: external refers to a global metric that is not associated with any Kubernetes object. It
            allows autoscaling based on information coming from components running outside of cluster (for
            example length of queue in cloud messaging service, or QPS from loadbalancer running outside of
            cluster).
        object: object refers to a metric describing a single kubernetes object (for example, hits-per-second
            on an Ingress object).
        pods: pods refers to a metric describing each pod in the current scale target (for example,
            transactions-processed-per-second).  The values will be averaged together before being compared to
            the target value.
        resource: resource refers to a resource metric (such as those specified in requests and limits) known
            to Kubernetes describing each pod in the current scale target (e.g. CPU or memory). Such metrics
            are built in to Kubernetes, and have special scaling options on top of those available to normal
            per-pod metrics using the 'pods' source.
        type: type is the type of metric source.  It should be one of 'ContainerResource', 'External',
            'Object', 'Pods' or 'Resource', each mapping to a matching field in the object. Note:
            'ContainerResource' type is available on when the feature-gate HPAContainerMetrics is enabled

    """

    type: str
    containerResource: Optional[ContainerResourceMetricSource] = None
    external: Optional[ExternalMetricSource] = None
    object: Optional[ObjectMetricSource] = None
    pods: Optional[PodsMetricSource] = None
    resource: Optional[ResourceMetricSource] = None


@dataclass
class MetricStatus(K8sSpec):
    """MetricStatus describes the last-read state of a single metric.

    Attributes:
        containerResource: container resource refers to a resource metric (such as those specified in requests
            and limits) known to Kubernetes describing a single container in each pod in the current scale
            target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling
            options on top of those available to normal per-pod metrics using the 'pods' source.
        external: external refers to a global metric that is not associated with any Kubernetes object. It
            allows autoscaling based on information coming from components running outside of cluster (for
            example length of queue in cloud messaging service, or QPS from loadbalancer running outside of
            cluster).
        object: object refers to a metric describing a single kubernetes object (for example, hits-per-second
            on an Ingress object).
        pods: pods refers to a metric describing each pod in the current scale target (for example,
            transactions-processed-per-second).  The values will be averaged together before being compared to
            the target value.
        resource: resource refers to a resource metric (such as those specified in requests and limits) known
            to Kubernetes describing each pod in the current scale target (e.g. CPU or memory). Such metrics
            are built in to Kubernetes, and have special scaling options on top of those available to normal
            per-pod metrics using the 'pods' source.
        type: type is the type of metric source.  It will be one of 'ContainerResource', 'External', 'Object',
            'Pods' or 'Resource', each corresponds to a matching field in the object. Note:
            'ContainerResource' type is available on when the feature-gate HPAContainerMetrics is enabled

    """

    type: str
    containerResource: Optional[ContainerResourceMetricStatus] = None
    external: Optional[ExternalMetricStatus] = None
    object: Optional[ObjectMetricStatus] = None
    pods: Optional[PodsMetricStatus] = None
    resource: Optional[ResourceMetricStatus] = None


@dataclass
class MetricTarget(K8sSpec):
    """MetricTarget defines the target value, average value, or average utilization of a specific metric
    Attributes:
        averageUtilization: averageUtilization is the target value of the average of the resource metric
            across all relevant pods, represented as a percentage of the requested value of the resource for
            the pods. Currently only valid for Resource metric source type
        averageValue: averageValue is the target value of the average of the metric across all relevant pods
            (as a quantity)
        type: type represents whether the metric type is Utilization, Value, or AverageValue
        value: value is the target value of the metric (as a quantity).

    """

    type: str
    averageUtilization: Optional[int] = None
    averageValue: Optional[gybe.k8s.v1_30.api.resource.Quantity] = None
    value: Optional[gybe.k8s.v1_30.api.resource.Quantity] = None


@dataclass
class MetricValueStatus(K8sSpec):
    """MetricValueStatus holds the current value for a metric
    Attributes:
        averageUtilization: currentAverageUtilization is the current value of the average of the resource
            metric across all relevant pods, represented as a percentage of the requested value of the
            resource for the pods.
        averageValue: averageValue is the current value of the average of the metric across all relevant pods
            (as a quantity)
        value: value is the current value of the metric (as a quantity).

    """

    averageUtilization: Optional[int] = None
    averageValue: Optional[gybe.k8s.v1_30.api.resource.Quantity] = None
    value: Optional[gybe.k8s.v1_30.api.resource.Quantity] = None


@dataclass
class ObjectMetricSource(K8sSpec):
    """ObjectMetricSource indicates how to scale on a metric describing a kubernetes object (for example,
    hits-per-second on an Ingress object).

    Attributes:
        describedObject: describedObject specifies the descriptions of a object,such as kind,name apiVersion
        metric: metric identifies the target metric by name and selector
        target: target specifies the target value for the given metric

    """

    describedObject: CrossVersionObjectReference
    target: MetricTarget
    metric: MetricIdentifier


@dataclass
class ObjectMetricStatus(K8sSpec):
    """ObjectMetricStatus indicates the current value of a metric describing a kubernetes object (for
    example, hits-per-second on an Ingress object).

    Attributes:
        current: current contains the current value for the given metric
        describedObject: DescribedObject specifies the descriptions of a object,such as kind,name apiVersion
        metric: metric identifies the target metric by name and selector

    """

    metric: MetricIdentifier
    current: MetricValueStatus
    describedObject: CrossVersionObjectReference


@dataclass
class PodsMetricSource(K8sSpec):
    """PodsMetricSource indicates how to scale on a metric describing each pod in the current scale target
    (for example, transactions-processed-per-second). The values will be averaged together before being
    compared to the target value.

    Attributes:
        metric: metric identifies the target metric by name and selector
        target: target specifies the target value for the given metric

    """

    metric: MetricIdentifier
    target: MetricTarget


@dataclass
class PodsMetricStatus(K8sSpec):
    """PodsMetricStatus indicates the current value of a metric describing each pod in the current scale
    target (for example, transactions-processed-per-second).

    Attributes:
        current: current contains the current value for the given metric
        metric: metric identifies the target metric by name and selector

    """

    metric: MetricIdentifier
    current: MetricValueStatus


@dataclass
class ResourceMetricSource(K8sSpec):
    """ResourceMetricSource indicates how to scale on a resource metric known to Kubernetes, as specified in
    requests and limits, describing each pod in the current scale target (e.g. CPU or memory).  The values
    will be averaged together before being compared to the target.  Such metrics are built in to
    Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using
    the 'pods' source.  Only one 'target' type should be set.

    Attributes:
        name: name is the name of the resource in question.
        target: target specifies the target value for the given metric

    """

    name: str
    target: MetricTarget


@dataclass
class ResourceMetricStatus(K8sSpec):
    """ResourceMetricStatus indicates the current value of a resource metric known to Kubernetes, as
    specified in requests and limits, describing each pod in the current scale target (e.g. CPU or
    memory).  Such metrics are built in to Kubernetes, and have special scaling options on top of those
    available to normal per-pod metrics using the 'pods' source.

    Attributes:
        current: current contains the current value for the given metric
        name: name is the name of the resource in question.

    """

    name: str
    current: MetricValueStatus
