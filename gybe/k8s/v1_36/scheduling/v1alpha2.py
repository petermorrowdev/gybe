"""Models generated from Kubernetes OpenAPI Spec."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Literal, Optional

import gybe.k8s.v1_36.meta.v1 as _meta_v1
from gybe.k8s.types import JSONObj, K8sResource, K8sSpec


@dataclass
class GangSchedulingPolicy(K8sSpec):
    """GangSchedulingPolicy defines the parameters for gang scheduling.

    Attributes:
        minCount: MinCount is the minimum number of pods that must be schedulable or scheduled at the same
            time for the scheduler to admit the entire group. It must be a positive integer.

    """

    minCount: int


@dataclass
class PodGroup(K8sResource):
    """PodGroup represents a runtime instance of pods grouped together. PodGroups are created by workload
    controllers (Job, LWS, JobSet, etc...) from Workload.podGroupTemplates. PodGroup API enablement is
    toggled by the GenericWorkload feature gate.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object's metadata.
        spec: Spec defines the desired state of the PodGroup.
        status: Status represents the current observed state of the PodGroup.

    """

    spec: PodGroupSpec
    apiVersion: Literal['scheduling.k8s.io/v1alpha2'] = 'scheduling.k8s.io/v1alpha2'
    kind: Literal['PodGroup'] = 'PodGroup'
    metadata: Optional[_meta_v1.ObjectMeta] = None
    status: Optional[PodGroupStatus] = None


@dataclass
class PodGroupResourceClaim(K8sSpec):
    """PodGroupResourceClaim references exactly one ResourceClaim, either directly or by naming a
    ResourceClaimTemplate which is then turned into a ResourceClaim for the PodGroup.  It adds a name to
    it that uniquely identifies the ResourceClaim inside the PodGroup. Pods that need access to the
    ResourceClaim define a matching reference in its own Spec.ResourceClaims. The Pod's claim must match
    all fields of the PodGroup's claim exactly.

    Attributes:
        name: Name uniquely identifies this resource claim inside the PodGroup. This must be a DNS_LABEL.
        resourceClaimName: ResourceClaimName is the name of a ResourceClaim object in the same namespace as
            this PodGroup. The ResourceClaim will be reserved for the PodGroup instead of its individual pods.
            Exactly one of ResourceClaimName and ResourceClaimTemplateName must be set.
        resourceClaimTemplateName: ResourceClaimTemplateName is the name of a ResourceClaimTemplate object in
            the same namespace as this PodGroup.  The template will be used to create a new ResourceClaim,
            which will be bound to this PodGroup. When this PodGroup is deleted, the ResourceClaim will also
            be deleted. The PodGroup name and resource name, along with a generated component, will be used to
            form a unique name for the ResourceClaim, which will be recorded in
            podgroup.status.resourceClaimStatuses.  This field is immutable and no changes will be made to the
            corresponding ResourceClaim by the control plane after creating the ResourceClaim.  Exactly one of
            ResourceClaimName and ResourceClaimTemplateName must be set.

    """

    name: str
    resourceClaimName: Optional[str] = None
    resourceClaimTemplateName: Optional[str] = None


@dataclass
class PodGroupResourceClaimStatus(K8sSpec):
    """PodGroupResourceClaimStatus is stored in the PodGroupStatus for each PodGroupResourceClaim which
    references a ResourceClaimTemplate. It stores the generated name for the corresponding ResourceClaim.

    Attributes:
        name: Name uniquely identifies this resource claim inside the PodGroup. This must match the name of an
            entry in podgroup.spec.resourceClaims, which implies that the string must be a DNS_LABEL.
        resourceClaimName: ResourceClaimName is the name of the ResourceClaim that was generated for the
            PodGroup in the namespace of the PodGroup. If this is unset, then generating a ResourceClaim was
            not necessary. The podgroup.spec.resourceClaims entry can be ignored in this case.

    """

    name: str
    resourceClaimName: Optional[str] = None


@dataclass
class PodGroupSchedulingConstraints(K8sSpec):
    """PodGroupSchedulingConstraints defines scheduling constraints (e.g. topology) for a PodGroup.

    Attributes:
        topology: Topology defines the topology constraints for the pod group. Currently only a single
            topology constraint can be specified. This may change in the future.

    """

    topology: Optional[List[TopologyConstraint]] = None


@dataclass
class PodGroupSchedulingPolicy(K8sSpec):
    """PodGroupSchedulingPolicy defines the scheduling configuration for a PodGroup. Exactly one policy must
    be set.

    Attributes:
        basic: Basic specifies that the pods in this group should be scheduled using standard Kubernetes
            scheduling behavior.
        gang: Gang specifies that the pods in this group should be scheduled using all-or-nothing semantics.

    """

    basic: Optional[JSONObj] = None
    gang: Optional[GangSchedulingPolicy] = None


@dataclass
class PodGroupSpec(K8sSpec):
    """PodGroupSpec defines the desired state of a PodGroup.

    Attributes:
        disruptionMode: DisruptionMode defines the mode in which a given PodGroup can be disrupted.
            Controllers are expected to fill this field by copying it from a PodGroupTemplate. One of Pod,
            PodGroup. Defaults to Pod if unset. This field is immutable. This field is available only when the
            WorkloadAwarePreemption feature gate is enabled.
        podGroupTemplateRef: PodGroupTemplateRef references an optional PodGroup template within other object
            (e.g. Workload) that was used to create the PodGroup. This field is immutable.
        priority: Priority is the value of priority of this pod group. Various system components use this
            field to find the priority of the pod group. When Priority Admission Controller is enabled, it
            prevents users from setting this field. The admission controller populates this field from
            PriorityClassName. The higher the value, the higher the priority. This field is immutable. This
            field is available only when the WorkloadAwarePreemption feature gate is enabled.
        priorityClassName: PriorityClassName defines the priority that should be considered when scheduling
            this pod group. Controllers are expected to fill this field by copying it from a PodGroupTemplate.
            Otherwise, it is validated and resolved similarly to the PriorityClassName on PodGroupTemplate
            (i.e. if no priority class is specified, admission control can set this to the global default
            priority class if it exists. Otherwise, the pod group's priority will be zero). This field is
            immutable. This field is available only when the WorkloadAwarePreemption feature gate is enabled.
        resourceClaims: ResourceClaims defines which ResourceClaims may be shared among Pods in the group.
            Pods consume the devices allocated to a PodGroup's claim by defining a claim in its own
            Spec.ResourceClaims that matches the PodGroup's claim exactly. The claim must have the same name
            and refer to the same ResourceClaim or ResourceClaimTemplate.  This is an alpha-level field and
            requires that the DRAWorkloadResourceClaims feature gate is enabled.  This field is immutable.
        schedulingConstraints: SchedulingConstraints defines optional scheduling constraints (e.g. topology)
            for this PodGroup. Controllers are expected to fill this field by copying it from a
            PodGroupTemplate. This field is immutable. This field is only available when the
            TopologyAwareWorkloadScheduling feature gate is enabled.
        schedulingPolicy: SchedulingPolicy defines the scheduling policy for this instance of the PodGroup.
            Controllers are expected to fill this field by copying it from a PodGroupTemplate. This field is
            immutable.

    """

    schedulingPolicy: PodGroupSchedulingPolicy
    disruptionMode: Optional[str] = None
    podGroupTemplateRef: Optional[PodGroupTemplateReference] = None
    priority: Optional[int] = None
    priorityClassName: Optional[str] = None
    resourceClaims: Optional[List[PodGroupResourceClaim]] = None
    schedulingConstraints: Optional[PodGroupSchedulingConstraints] = None


@dataclass
class PodGroupStatus(K8sSpec):
    """PodGroupStatus represents information about the status of a pod group.

    Attributes:
        conditions: Conditions represent the latest observations of the PodGroup's state.  Known condition
            types: - 'PodGroupScheduled': Indicates whether the scheduling requirement has been satisfied. -
            'DisruptionTarget': Indicates whether the PodGroup is about to be terminated   due to disruption
            such as preemption.  Known reasons for the PodGroupScheduled condition: - 'Unschedulable': The
            PodGroup cannot be scheduled due to resource constraints,   affinity/anti-affinity rules, or
            insufficient capacity for the gang. - 'SchedulerError': The PodGroup cannot be scheduled due to
            some internal error   that happened during scheduling, for example due to nodeAffinity parsing
            errors.  Known reasons for the DisruptionTarget condition: - 'PreemptionByScheduler': The PodGroup
            was preempted by the scheduler to make room for   higher-priority PodGroups or Pods.
        resourceClaimStatuses: Status of resource claims.

    """

    conditions: Optional[List[_meta_v1.Condition]] = None
    resourceClaimStatuses: Optional[List[PodGroupResourceClaimStatus]] = None


@dataclass
class PodGroupTemplate(K8sSpec):
    """PodGroupTemplate represents a template for a set of pods with a scheduling policy.

    Attributes:
        disruptionMode: DisruptionMode defines the mode in which a given PodGroup can be disrupted. One of
            Pod, PodGroup. This field is available only when the WorkloadAwarePreemption feature gate is
            enabled.
        name: Name is a unique identifier for the PodGroupTemplate within the Workload. It must be a DNS
            label. This field is immutable.
        priority: Priority is the value of priority of pod groups created from this template. Various system
            components use this field to find the priority of the pod group. When Priority Admission
            Controller is enabled, it prevents users from setting this field. The admission controller
            populates this field from PriorityClassName. The higher the value, the higher the priority. This
            field is available only when the WorkloadAwarePreemption feature gate is enabled.
        priorityClassName: PriorityClassName indicates the priority that should be considered when scheduling
            a pod group created from this template. If no priority class is specified, admission control can
            set this to the global default priority class if it exists. Otherwise, pod groups created from
            this template will have the priority set to zero. This field is available only when the
            WorkloadAwarePreemption feature gate is enabled.
        resourceClaims: ResourceClaims defines which ResourceClaims may be shared among Pods in the group.
            Pods consume the devices allocated to a PodGroup's claim by defining a claim in its own
            Spec.ResourceClaims that matches the PodGroup's claim exactly. The claim must have the same name
            and refer to the same ResourceClaim or ResourceClaimTemplate.  This is an alpha-level field and
            requires that the DRAWorkloadResourceClaims feature gate is enabled.  This field is immutable.
        schedulingConstraints: SchedulingConstraints defines optional scheduling constraints (e.g. topology)
            for this PodGroupTemplate. This field is only available when the TopologyAwareWorkloadScheduling
            feature gate is enabled.
        schedulingPolicy: SchedulingPolicy defines the scheduling policy for this PodGroupTemplate.

    """

    name: str
    schedulingPolicy: PodGroupSchedulingPolicy
    disruptionMode: Optional[str] = None
    priority: Optional[int] = None
    priorityClassName: Optional[str] = None
    resourceClaims: Optional[List[PodGroupResourceClaim]] = None
    schedulingConstraints: Optional[PodGroupSchedulingConstraints] = None


@dataclass
class PodGroupTemplateReference(K8sSpec):
    """PodGroupTemplateReference references a PodGroup template defined in some object (e.g. Workload).
    Exactly one reference must be set.

    Attributes:
        workload: Workload references the PodGroupTemplate within the Workload object that was used to create
            the PodGroup.

    """

    workload: Optional[WorkloadPodGroupTemplateReference] = None


@dataclass
class TopologyConstraint(K8sSpec):
    """TopologyConstraint defines a topology constraint for a PodGroup.

    Attributes:
        key: Key specifies the key of the node label representing the topology domain. All pods within the
            PodGroup must be colocated within the same domain instance. Different PodGroups can land on
            different domain instances even if they derive from the same PodGroupTemplate. Examples:
            'topology.kubernetes.io/rack'

    """

    key: str


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
    """Workload allows for expressing scheduling constraints that should be used when managing the lifecycle
    of workloads from the scheduling perspective, including scheduling, preemption, eviction and other
    phases. Workload API enablement is toggled by the GenericWorkload feature gate.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object's metadata.
        spec: Spec defines the desired behavior of a Workload.

    """

    spec: WorkloadSpec
    apiVersion: Literal['scheduling.k8s.io/v1alpha2'] = 'scheduling.k8s.io/v1alpha2'
    kind: Literal['Workload'] = 'Workload'
    metadata: Optional[_meta_v1.ObjectMeta] = None


@dataclass
class WorkloadPodGroupTemplateReference(K8sSpec):
    """WorkloadPodGroupTemplateReference references the PodGroupTemplate within the Workload object.

    Attributes:
        podGroupTemplateName: PodGroupTemplateName defines the PodGroupTemplate name within the Workload
            object.
        workloadName: WorkloadName defines the name of the Workload object.

    """

    workloadName: str
    podGroupTemplateName: str


@dataclass
class WorkloadSpec(K8sSpec):
    """WorkloadSpec defines the desired state of a Workload.

    Attributes:
        controllerRef: ControllerRef is an optional reference to the controlling object, such as a Deployment
            or Job. This field is intended for use by tools like CLIs to provide a link back to the original
            workload definition. This field is immutable.
        podGroupTemplates: PodGroupTemplates is the list of templates that make up the Workload. The maximum
            number of templates is 8. This field is immutable.

    """

    podGroupTemplates: List[PodGroupTemplate]
    controllerRef: Optional[TypedLocalObjectReference] = None
