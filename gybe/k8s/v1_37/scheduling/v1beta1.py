"""Models generated from Kubernetes OpenAPI Spec."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Literal, Optional

import gybe.k8s.v1_37.meta.v1 as _meta_v1
from gybe.k8s.types import JSONObj, K8sResource, K8sSpec


@dataclass
class AllCompositeDisruptionMode(K8sSpec):
    """AllCompositeDisruptionMode means that children of a CompositePodGroup can only be disrupted or
    preempted together.
    """


@dataclass
class AllDisruptionMode(K8sSpec):
    """AllDisruptionMode specifies that children can only be disrupted together."""


@dataclass
class CompositeDisruptionMode(K8sSpec):
    """CompositeDisruptionMode defines how individual entities within a composite pod group can be disrupted.
    Exactly one mode must be set.

    Attributes:
        all: all specifies that all children groups can only be disrupted together.
        single: single specifies that children groups can be disrupted independently from each other.

    """

    all: Optional[AllCompositeDisruptionMode] = None
    single: Optional[SingleCompositeDisruptionMode] = None


@dataclass
class CompositeGangSchedulingPolicy(K8sSpec):
    """CompositeGangSchedulingPolicy indicates that the groups belonging to the composite group should be
    scheduled using all-or-nothing semantics.

    Attributes:
        minGroupCount: minGroupCount is the minimum number of child groups that must be schedulable or
            scheduled at the same time for the scheduler to admit the entire group. It must be a positive
            integer.

    """

    minGroupCount: int


@dataclass
class CompositePodGroupSchedulingConstraints(K8sSpec):
    """CompositePodGroupSchedulingConstraints defines scheduling constraints (e.g. topology) for a
    CompositePodGroup.

    Attributes:
        topology: topology defines the topology constraints for the composite pod group. Currently only a
            single topology constraint can be specified. This may change in the future.

    """

    topology: Optional[List[TopologyConstraint]] = None


@dataclass
class CompositePodGroupSchedulingPolicy(K8sSpec):
    """CompositePodGroupSchedulingPolicy defines the scheduling configuration for a CompositePodGroup.
    Exactly one policy must be set.

    Attributes:
        basic: basic specifies that the groups of this composite group should be scheduled independently. This
            field is immutable.
        gang: gang specifies that the groups of this composite group should be scheduled using all-or-nothing
            semantics.

    """

    basic: Optional[JSONObj] = None
    gang: Optional[CompositeGangSchedulingPolicy] = None


@dataclass
class CompositePodGroupTemplate(K8sSpec):
    """CompositePodGroupTemplate represents a template for a CompositePodGroup with a scheduling policy.

    Attributes:
        compositePodGroupTemplates: compositePodGroupTemplates is the list of templates for children
            CompositePodGroups. The maximum number of templates is 8. At least one entry in
            CompositePodGroupTemplates or PodGroupTemplates must be set.
        disruptionMode: disruptionMode defines the mode in which a given CompositePodGroup can be disrupted.
            One of Single, All. This field is immutable.
        name: name is a unique identifier for the CompositePodGroupTemplate within the Workload. It must be a
            DNS label. This field is required.
        podGroupTemplates: podGroupTemplates is the list of templates for children PodGroups. The maximum
            number of templates is 8. At least one entry in CompositePodGroupTemplates or PodGroupTemplates
            must be set.
        preemptionPolicy: preemptionPolicy is the Policy for preempting pods/podgroups with lower priority.
            One of Never, PreemptLowerPriority. This field is immutable. This field is available only when the
            PodGroupPreemptionPolicy feature gate is enabled.
        priority: priority is the value of priority of composite pod groups created from this template.
            Various system components use this field to find the priority of the composite pod group. When
            Priority Admission Controller is enabled, it prevents users from setting this field. The admission
            controller populates this field from PriorityClassName. The higher the value, the higher the
            priority. This field is immutable.
        priorityClassName: priorityClassName indicates the priority that should be considered when scheduling
            a composite pod group created from this template. If no priority class is specified, admission
            control can set this to the global default priority class if it exists. Otherwise, composite pod
            groups created from this template will have the priority set to zero. This field is immutable.
        schedulingConstraints: schedulingConstraints defines optional scheduling constraints (e.g. topology)
            for this CompositePodGroupTemplate. This field is immutable.
        schedulingPolicy: schedulingPolicy defines the scheduling policy for this template.

    """

    name: str
    schedulingPolicy: CompositePodGroupSchedulingPolicy
    compositePodGroupTemplates: Optional[List[CompositePodGroupTemplate]] = None
    disruptionMode: Optional[CompositeDisruptionMode] = None
    podGroupTemplates: Optional[List[PodGroupTemplate]] = None
    preemptionPolicy: Optional[str] = None
    priority: Optional[int] = None
    priorityClassName: Optional[str] = None
    schedulingConstraints: Optional[CompositePodGroupSchedulingConstraints] = None


@dataclass
class DisruptionMode(K8sSpec):
    """DisruptionMode defines how individual entities within a group can be disrupted. Exactly one mode can
    be set.

    Attributes:
        all: all specifies that all children can only be disrupted together.
        single: single specifies that children can be disrupted independently from each other.

    """

    all: Optional[AllDisruptionMode] = None
    single: Optional[SingleDisruptionMode] = None


@dataclass
class GangSchedulingPolicy(K8sSpec):
    """GangSchedulingPolicy defines the parameters for gang scheduling.

    Attributes:
        minCount: minCount is the minimum number of pods that must be schedulable or scheduled at the same
            time for the scheduler to admit the entire group. It must be a positive integer. This field is
            mutable to support workload scaling.  Note that the scheduler operates on an eventually consistent
            model. Updates to minCount may not be immediately reflected in scheduling decisions due to
            propagation delays. If minCount is updated while a scheduling cycle is in progress for that group,
            the new value may not take effect until the next cycle. Moreover, minCount is only enforced during
            scheduling, meaning that modifications to this field do not affect already-scheduled pods,
            applying only to those evaluated in future cycles.

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
        metadata: metadata is the standard object metadata.
        spec: spec defines the desired state of the PodGroup.
        status: status represents the current observed state of the PodGroup.

    """

    spec: PodGroupSpec
    apiVersion: Literal['scheduling.k8s.io/v1beta1'] = 'scheduling.k8s.io/v1beta1'
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
        name: name uniquely identifies this resource claim inside the PodGroup. This must be a DNS_LABEL.
        resourceClaimName: resourceClaimName is the name of a ResourceClaim object in the same namespace as
            this PodGroup. The ResourceClaim will be reserved for the PodGroup instead of its individual pods.
            Exactly one of ResourceClaimName and ResourceClaimTemplateName must be set.
        resourceClaimTemplateName: resourceClaimTemplateName is the name of a ResourceClaimTemplate object in
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
        name: name uniquely identifies this resource claim inside the PodGroup. This must match the name of an
            entry in podgroup.spec.resourceClaims, which implies that the string must be a DNS_LABEL.
        resourceClaimName: resourceClaimName is the name of the ResourceClaim that was generated for the
            PodGroup in the namespace of the PodGroup. If this is unset, then generating a ResourceClaim was
            not necessary. The podgroup.spec.resourceClaims entry can be ignored in this case.

    """

    name: str
    resourceClaimName: Optional[str] = None


@dataclass
class PodGroupSchedulingConstraints(K8sSpec):
    """PodGroupSchedulingConstraints defines scheduling constraints (e.g. topology) for a PodGroup.

    Attributes:
        topology: topology defines the topology constraints for the pod group. Currently only a single
            topology constraint can be specified. This may change in the future.

    """

    topology: Optional[List[TopologyConstraint]] = None


@dataclass
class PodGroupSchedulingPolicy(K8sSpec):
    """PodGroupSchedulingPolicy defines the scheduling configuration for a PodGroup. Exactly one policy must
    be set. The policy is chosen at creation time by setting either the Basic or Gang field. The PodGroup
    may not change policy after creation. Fields within chosen policy may be updated after creation when
    their individual fields allow it.

    Attributes:
        basic: basic specifies that the pods in this group should be scheduled using standard Kubernetes
            scheduling behavior. Setting this field at group creation time opts this group to basic
            scheduling; this field cannot be changed afterward.
        gang: gang specifies that the pods in this group should be scheduled using all-or-nothing semantics.
            Setting this field at group creation time opts this group to gang scheduling; this field cannot be
            set or unset afterward. The minCount field within Gang scheduling policy remains mutable after
            group creation.

    """

    basic: Optional[JSONObj] = None
    gang: Optional[GangSchedulingPolicy] = None


@dataclass
class PodGroupSpec(K8sSpec):
    """PodGroupSpec defines the desired state of a PodGroup.

    Attributes:
        disruptionMode: disruptionMode defines the mode in which a given PodGroup can be disrupted.
            Controllers are expected to fill this field by copying it from a PodGroupTemplate. One of Single,
            All. Defaults to Single if unset. This field is immutable.
        parentCompositePodGroupName: parentCompositePodGroupName contains the name of the parent composite pod
            group within the same namespace as this pod group. If it's nil, then this pod group is a root of a
            workload's hierarchy. This field is used only when the CompositePodGroup feature gate is enabled.
            This field is immutable.
        preemptionPolicy: preemptionPolicy is the Policy for preempting pods/podgroups with lower priority.
            One of Never, PreemptLowerPriority. Defaults to PreemptLowerPriority if unset. When Priority
            Admission Controller is enabled, it populates this field from PriorityClassName, and defaults to
            PreemptLowerPriority if value is unset in PriorityClass. This field is immutable. This field is
            available only when the PodGroupPreemptionPolicy feature gate is enabled.
        priority: priority is the value of priority of this pod group. Various system components use this
            field to find the priority of the pod group. When Priority Admission Controller is enabled, it
            prevents users from setting this field. The admission controller populates this field from
            PriorityClassName. The higher the value, the higher the priority. This field is immutable.
        priorityClassName: priorityClassName defines the priority that should be considered when scheduling
            this pod group. Controllers are expected to fill this field by copying it from a PodGroupTemplate.
            Otherwise, it is validated and resolved similarly to the PriorityClassName on PodGroupTemplate
            (i.e. if no priority class is specified, admission control can set this to the global default
            priority class if it exists. Otherwise, the pod group's priority will be zero). This field is
            immutable.
        resourceClaims: resourceClaims defines which ResourceClaims may be shared among Pods in the group.
            Pods consume the devices allocated to a PodGroup's claim by defining a claim in its own
            Spec.ResourceClaims that matches the PodGroup's claim exactly. The claim must have the same name
            and refer to the same ResourceClaim or ResourceClaimTemplate.  This is a beta-level field and
            requires that the DRAWorkloadResourceClaims feature gate is enabled.  This field is immutable.
        schedulingConstraints: schedulingConstraints defines optional scheduling constraints (e.g. topology)
            for this PodGroup. Controllers are expected to fill this field by copying it from a
            PodGroupTemplate. This field is immutable. This field is only available when the
            TopologyAwareWorkloadScheduling feature gate is enabled.
        schedulingPolicy: schedulingPolicy defines the scheduling policy for this instance of the PodGroup.
            Controllers are expected to fill this field by copying it from a PodGroupTemplate.
        workloadRef: workloadRef references an optional PodGroup template within the Workload object that was
            used to create the PodGroup. This field is immutable.

    """

    schedulingPolicy: PodGroupSchedulingPolicy
    disruptionMode: Optional[DisruptionMode] = None
    parentCompositePodGroupName: Optional[str] = None
    preemptionPolicy: Optional[str] = None
    priority: Optional[int] = None
    priorityClassName: Optional[str] = None
    resourceClaims: Optional[List[PodGroupResourceClaim]] = None
    schedulingConstraints: Optional[PodGroupSchedulingConstraints] = None
    workloadRef: Optional[WorkloadReference] = None


@dataclass
class PodGroupStatus(K8sSpec):
    """PodGroupStatus represents information about the status of a pod group.

    Attributes:
        conditions: conditions represent the latest observations of the PodGroup's state.  Known condition
            types: - 'PodGroupInitiallyScheduled': Indicates whether the scheduling requirement has been
            satisfied. Once this condition transitions to True, it serves as a terminal state and will never
            revert to False, even if pods are subsequently evicted and group constraints are no longer met. -
            'DisruptionTarget': Indicates whether the PodGroup is about to be terminated   due to disruption
            such as preemption.  Known reasons for the PodGroupInitiallyScheduled condition: -
            'Unschedulable': The PodGroup cannot be scheduled due to resource constraints,   affinity/anti-
            affinity rules, or insufficient capacity for the gang. - 'SchedulerError': The PodGroup cannot be
            scheduled due to some internal error   that happened during scheduling, for example due to
            nodeAffinity parsing errors.  Known reasons for the DisruptionTarget condition: -
            'PreemptionByScheduler': The PodGroup was preempted by the scheduler to make room for   higher-
            priority PodGroups or Pods.
        resourceClaimStatuses: resourceClaimStatuses is status of resource claims.

    """

    conditions: Optional[List[_meta_v1.Condition]] = None
    resourceClaimStatuses: Optional[List[PodGroupResourceClaimStatus]] = None


@dataclass
class PodGroupTemplate(K8sSpec):
    """PodGroupTemplate represents a template for a set of pods with a scheduling policy.

    Attributes:
        disruptionMode: disruptionMode defines the mode in which a given PodGroup can be disrupted. One of
            Single, All. This field is immutable.
        name: name is a unique identifier for the PodGroupTemplate within the Workload. It must be a DNS
            label. This field is immutable.
        preemptionPolicy: preemptionPolicy is the Policy for preempting pods/podgroups with lower priority.
            One of Never, PreemptLowerPriority. This field is immutable. This field is available only when the
            PodGroupPreemptionPolicy feature gate is enabled.
        priority: priority is the value of priority of pod groups created from this template. Various system
            components use this field to find the priority of the pod group. The higher the value, the higher
            the priority. This field is immutable.
        priorityClassName: priorityClassName indicates the priority that should be considered when scheduling
            a pod group created from this template. This field is immutable.
        resourceClaims: resourceClaims defines which ResourceClaims may be shared among Pods in the group.
            Pods consume the devices allocated to a PodGroup's claim by defining a claim in its own
            Spec.ResourceClaims that matches the PodGroup's claim exactly. The claim must have the same name
            and refer to the same ResourceClaim or ResourceClaimTemplate.  This is a beta-level field and
            requires that the DRAWorkloadResourceClaims feature gate is enabled.  This field is immutable.
        schedulingConstraints: schedulingConstraints defines optional scheduling constraints (e.g. topology)
            for this PodGroupTemplate. This field is only available when the TopologyAwareWorkloadScheduling
            feature gate is enabled. This field is immutable.
        schedulingPolicy: schedulingPolicy defines the scheduling policy for this PodGroupTemplate.

    """

    name: str
    schedulingPolicy: PodGroupSchedulingPolicy
    disruptionMode: Optional[DisruptionMode] = None
    preemptionPolicy: Optional[str] = None
    priority: Optional[int] = None
    priorityClassName: Optional[str] = None
    resourceClaims: Optional[List[PodGroupResourceClaim]] = None
    schedulingConstraints: Optional[PodGroupSchedulingConstraints] = None


@dataclass
class SingleCompositeDisruptionMode(K8sSpec):
    """SingleCompositeDisruptionMode means that individual children of a CompositePodGroup can be disrupted
    or preempted independently.
    """


@dataclass
class SingleDisruptionMode(K8sSpec):
    """SingleDisruptionMode specifies that children can be disrupted independently."""


@dataclass
class TopologyConstraint(K8sSpec):
    """TopologyConstraint defines a topology constraint for a PodGroup.

    Attributes:
        key: key specifies the key of the node label representing the topology domain. All pods within the
            PodGroup must be colocated within the same domain instance. Different PodGroups can land on
            different domain instances even if they derive from the same PodGroupTemplate. Examples:
            'topology.kubernetes.io/rack'

    """

    key: str


@dataclass
class TypedLocalObjectReference(K8sSpec):
    """TypedLocalObjectReference allows to reference typed object inside the same namespace.

    Attributes:
        apiGroup: apiGroup is the group for the resource being referenced. If apiGroup is empty, the specified
            Kind must be in the core API group. For any other third-party types, setting apiGroup is required.
            It must be a DNS subdomain.
        kind: kind is the type of resource being referenced. It must be a path segment name.
        name: name is the name of resource being referenced. It must be a path segment name.

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
        metadata: metadata is the standard object metadata.
        spec: spec defines the desired behavior of a Workload.

    """

    spec: WorkloadSpec
    apiVersion: Literal['scheduling.k8s.io/v1beta1'] = 'scheduling.k8s.io/v1beta1'
    kind: Literal['Workload'] = 'Workload'
    metadata: Optional[_meta_v1.ObjectMeta] = None


@dataclass
class WorkloadReference(K8sSpec):
    """WorkloadReference references the Workload object together with the template that was used to create a
    particular PodGroup.

    Attributes:
        templateName: templateName is the name of a template within the Workload object that was used to
            create a pod group. It must be a DNS label. This field is required.
        workloadName: workloadName is the name of the Workload object that contains a template that was used
            when creating a pod group. It must be a DNS name. This field is required.

    """

    workloadName: str
    templateName: str


@dataclass
class WorkloadSpec(K8sSpec):
    """WorkloadSpec defines the desired state of a Workload.

    Attributes:
        compositePodGroupTemplates: compositePodGroupTemplates is the list of CompositePodGroup templates that
            make up the Workload. The maximum number of templates is 8. This field is immutable. Exactly one
            of CompositePodGroupTemplates and PodGroupTemplates must be set.  This field is used only when the
            CompositePodGroup feature gate is enabled.
        controllerRef: controllerRef is an optional reference to the controlling object, such as a Deployment
            or Job. This field is intended for use by tools like CLIs to provide a link back to the original
            workload definition. This field is immutable.
        podGroupTemplates: podGroupTemplates is the list of templates that make up the Workload. The maximum
            number of templates is 8. Templates cannot be added or removed after the workload is created.
            Existing templates may still be updated where their individual fields allow it. Exactly one of
            CompositePodGroupTemplates and PodGroupTemplates must be set.

    """

    compositePodGroupTemplates: Optional[List[CompositePodGroupTemplate]] = None
    controllerRef: Optional[TypedLocalObjectReference] = None
    podGroupTemplates: Optional[List[PodGroupTemplate]] = None
