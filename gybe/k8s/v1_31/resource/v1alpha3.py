"""Models generated from Kubernetes OpenAPI Spec."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Literal, Optional

import gybe.k8s.v1_31.core.v1
import gybe.k8s.v1_31.meta.v1
from gybe.k8s.types import JSONDict, JSONObj, K8sResource, K8sSpec


@dataclass
class AllocationResult(K8sSpec):
    """AllocationResult contains attributes of an allocated resource.

    Attributes:
        controller: Controller is the name of the DRA driver which handled the allocation. That driver is also
            responsible for deallocating the claim. It is empty when the claim can be deallocated without
            involving a driver.  A driver may allocate devices provided by other drivers, so this driver name
            here can be different from the driver names listed for the results.  This is an alpha field and
            requires enabling the DRAControlPlaneController feature gate.
        devices: Devices is the result of allocating devices.
        nodeSelector: NodeSelector defines where the allocated resources are available. If unset, they are
            available everywhere.

    """

    controller: Optional[str] = None
    devices: Optional[DeviceAllocationResult] = None
    nodeSelector: Optional[gybe.k8s.v1_31.core.v1.NodeSelector] = None


@dataclass
class BasicDevice(K8sSpec):
    """BasicDevice defines one device instance.

    Attributes:
        attributes: Attributes defines the set of attributes for this device. The name of each attribute must
            be unique in that set.  The maximum number of attributes and capacities combined is 32.
        capacity: Capacity defines the set of capacities for this device. The name of each capacity must be
            unique in that set.  The maximum number of attributes and capacities combined is 32.

    """

    attributes: Optional[JSONDict] = None
    capacity: Optional[JSONDict] = None


@dataclass
class CELDeviceSelector(K8sSpec):
    """CELDeviceSelector contains a CEL expression for selecting a device.

    Attributes:
        expression: Expression is a CEL expression which evaluates a single device. It must evaluate to true
            when the device under consideration satisfies the desired criteria, and false when it does not.
            Any other result is an error and causes allocation of devices to abort.  The expression's input is
            an object named 'device', which carries the following properties:  - driver (string): the name of
            the driver which defines this device.  - attributes (map[string]object): the device's attributes,
            grouped by prefix    (e.g. device.attributes['dra.example.com'] evaluates to an object with all
            of the attributes which were prefixed by 'dra.example.com'.  - capacity (map[string]object): the
            device's capacities, grouped by prefix.  Example: Consider a device with driver='dra.example.com',
            which exposes two attributes named 'model' and 'ext.example.com/family' and which exposes one
            capacity named 'modules'. This input to this expression would have the following fields:
            device.driver     device.attributes['dra.example.com'].model
            device.attributes['ext.example.com'].family     device.capacity['dra.example.com'].modules  The
            device.driver field can be used to check for a specific driver, either as a high-level
            precondition (i.e. you only want to consider devices from this driver) or as part of a multi-
            clause expression that is meant to consider devices from different drivers.  The value type of
            each attribute is defined by the device definition, and users who write these expressions must
            consult the documentation for their specific drivers. The value type of each capacity is Quantity.
            If an unknown prefix is used as a lookup in either device.attributes or device.capacity, an empty
            map will be returned. Any reference to an unknown field will cause an evaluation error and
            allocation to abort.  A robust expression should check for the existence of attributes before
            referencing them.  For ease of use, the cel.bind() function is enabled, and can be used to
            simplify expressions that access multiple attributes with the same domain. For example:
            cel.bind(dra, device.attributes['dra.example.com'], dra.someBool && dra.anotherBool)

    """

    expression: str


@dataclass
class Device(K8sSpec):
    """Device represents one individual hardware instance that can be selected based on its attributes.
    Besides the name, exactly one field must be set.

    Attributes:
        basic: Basic defines one device instance.
        name: Name is unique identifier among all devices managed by the driver in the pool. It must be a DNS
            label.

    """

    name: str
    basic: Optional[BasicDevice] = None


@dataclass
class DeviceAllocationConfiguration(K8sSpec):
    """DeviceAllocationConfiguration gets embedded in an AllocationResult.

    Attributes:
        opaque: Opaque provides driver-specific configuration parameters.
        requests: Requests lists the names of requests where the configuration applies. If empty, its applies
            to all requests.
        source: Source records whether the configuration comes from a class and thus is not something that a
            normal user would have been able to set or from a claim.

    """

    source: str
    opaque: Optional[OpaqueDeviceConfiguration] = None
    requests: Optional[List[str]] = None


@dataclass
class DeviceAllocationResult(K8sSpec):
    """DeviceAllocationResult is the result of allocating devices.

    Attributes:
        config: This field is a combination of all the claim and class configuration parameters. Drivers can
            distinguish between those based on a flag.  This includes configuration parameters for drivers
            which have no allocated devices in the result because it is up to the drivers which configuration
            parameters they support. They can silently ignore unknown configuration parameters.
        results: Results lists all allocated devices.

    """

    config: Optional[List[DeviceAllocationConfiguration]] = None
    results: Optional[List[DeviceRequestAllocationResult]] = None


@dataclass
class DeviceAttribute(K8sSpec):
    """DeviceAttribute must have exactly one field set.

    Attributes:
        bool: BoolValue is a true/false value.
        int: IntValue is a number.
        string: StringValue is a string. Must not be longer than 64 characters.
        version: VersionValue is a semantic version according to semver.org spec 2.0.0. Must not be longer
            than 64 characters.

    """

    bool: Optional[bool] = None
    int: Optional[int] = None
    string: Optional[str] = None
    version: Optional[str] = None


@dataclass
class DeviceClaim(K8sSpec):
    """DeviceClaim defines how to request devices with a ResourceClaim.

    Attributes:
        config: This field holds configuration for multiple potential drivers which could satisfy requests in
            this claim. It is ignored while allocating the claim.
        constraints: These constraints must be satisfied by the set of devices that get allocated for the
            claim.
        requests: Requests represent individual requests for distinct devices which must all be satisfied. If
            empty, nothing needs to be allocated.

    """

    config: Optional[List[DeviceClaimConfiguration]] = None
    constraints: Optional[List[DeviceConstraint]] = None
    requests: Optional[List[DeviceRequest]] = None


@dataclass
class DeviceClaimConfiguration(K8sSpec):
    """DeviceClaimConfiguration is used for configuration parameters in DeviceClaim.

    Attributes:
        opaque: Opaque provides driver-specific configuration parameters.
        requests: Requests lists the names of requests where the configuration applies. If empty, it applies
            to all requests.

    """

    opaque: Optional[OpaqueDeviceConfiguration] = None
    requests: Optional[List[str]] = None


@dataclass
class DeviceClass(K8sResource):
    """DeviceClass is a vendor- or admin-provided resource that contains device configuration and selectors.
    It can be referenced in the device requests of a claim to apply these presets. Cluster scoped.  This
    is an alpha type and requires enabling the DynamicResourceAllocation feature gate.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object metadata
        spec: Spec defines what can be allocated and how to configure it.  This is mutable. Consumers have to
            be prepared for classes changing at any time, either because they get updated or replaced. Claim
            allocations are done once based on whatever was set in classes at the time of allocation.
            Changing the spec automatically increments the metadata.generation number.

    """

    spec: DeviceClassSpec
    apiVersion: Literal['resource.k8s.io/v1alpha3'] = 'resource.k8s.io/v1alpha3'
    kind: Literal['DeviceClass'] = 'DeviceClass'
    metadata: Optional[gybe.k8s.v1_31.meta.v1.ObjectMeta] = None


@dataclass
class DeviceClassConfiguration(K8sSpec):
    """DeviceClassConfiguration is used in DeviceClass.

    Attributes:
        opaque: Opaque provides driver-specific configuration parameters.

    """

    opaque: Optional[OpaqueDeviceConfiguration] = None


@dataclass
class DeviceClassSpec(K8sSpec):
    """DeviceClassSpec is used in a [DeviceClass] to define what can be allocated and how to configure it.

    Attributes:
        config: Config defines configuration parameters that apply to each device that is claimed via this
            class. Some classses may potentially be satisfied by multiple drivers, so each instance of a
            vendor configuration applies to exactly one driver.  They are passed to the driver, but are not
            considered while allocating the claim.
        selectors: Each selector must be satisfied by a device which is claimed via this class.
        suitableNodes: Only nodes matching the selector will be considered by the scheduler when trying to
            find a Node that fits a Pod when that Pod uses a claim that has not been allocated yet *and* that
            claim gets allocated through a control plane controller. It is ignored when the claim does not use
            a control plane controller for allocation.  Setting this field is optional. If unset, all Nodes
            are candidates.  This is an alpha field and requires enabling the DRAControlPlaneController
            feature gate.

    """

    config: Optional[List[DeviceClassConfiguration]] = None
    selectors: Optional[List[DeviceSelector]] = None
    suitableNodes: Optional[gybe.k8s.v1_31.core.v1.NodeSelector] = None


@dataclass
class DeviceConstraint(K8sSpec):
    """DeviceConstraint must have exactly one field set besides Requests.

    Attributes:
        matchAttribute: MatchAttribute requires that all devices in question have this attribute and that its
            type and value are the same across those devices.  For example, if you specified
            'dra.example.com/numa' (a hypothetical example!), then only devices in the same NUMA node will be
            chosen. A device which does not have that attribute will not be chosen. All devices should use a
            value of the same type for this attribute because that is part of its specification, but if one
            device doesn't, then it also will not be chosen.  Must include the domain qualifier.
        requests: Requests is a list of the one or more requests in this claim which must co-satisfy this
            constraint. If a request is fulfilled by multiple devices, then all of the devices must satisfy
            the constraint. If this is not specified, this constraint applies to all requests in this claim.

    """

    matchAttribute: Optional[str] = None
    requests: Optional[List[str]] = None


@dataclass
class DeviceRequest(K8sSpec):
    """DeviceRequest is a request for devices required for a claim. This is typically a request for a single
    resource like a device, but can also ask for several identical devices.  A DeviceClassName is
    currently required. Clients must check that it is indeed set. It's absence indicates that something
    changed in a way that is not supported by the client yet, in which case it must refuse to handle the
    request.

    Attributes:
        adminAccess: AdminAccess indicates that this is a claim for administrative access to the device(s).
            Claims with AdminAccess are expected to be used for monitoring or other management services for a
            device.  They ignore all ordinary claims to the device with respect to access modes and any
            resource allocations.
        allocationMode: AllocationMode and its related fields define how devices are allocated to satisfy this
            request. Supported values are:  - ExactCount: This request is for a specific number of devices.
            This is the default. The exact number is provided in the   count field.  - All: This request is
            for all of the matching devices in a pool.   Allocation will fail if some devices are already
            allocated,   unless adminAccess is requested.  If AlloctionMode is not specified, the default mode
            is ExactCount. If the mode is ExactCount and count is not specified, the default count is one. Any
            other requests must specify this field.  More modes may get added in the future. Clients must
            refuse to handle requests with unknown modes.
        count: Count is used only when the count mode is 'ExactCount'. Must be greater than zero. If
            AllocationMode is ExactCount and this field is not specified, the default is one.
        deviceClassName: DeviceClassName references a specific DeviceClass, which can define additional
            configuration and selectors to be inherited by this request.  A class is required. Which classes
            are available depends on the cluster.  Administrators may use this to restrict which devices may
            get requested by only installing classes with selectors for permitted devices. If users are free
            to request anything without restrictions, then administrators can create an empty DeviceClass for
            users to reference.
        name: Name can be used to reference this request in a pod.spec.containers[].resources.claims entry and
            in a constraint of the claim.  Must be a DNS label.
        selectors: Selectors define criteria which must be satisfied by a specific device in order for that
            device to be considered for this request. All selectors must be satisfied for a device to be
            considered.

    """

    name: str
    deviceClassName: str
    adminAccess: Optional[bool] = None
    allocationMode: Optional[str] = None
    count: Optional[int] = None
    selectors: Optional[List[DeviceSelector]] = None


@dataclass
class DeviceRequestAllocationResult(K8sSpec):
    """DeviceRequestAllocationResult contains the allocation result for one request.

    Attributes:
        device: Device references one device instance via its name in the driver's resource pool. It must be a
            DNS label.
        driver: Driver specifies the name of the DRA driver whose kubelet plugin should be invoked to process
            the allocation once the claim is needed on a node.  Must be a DNS subdomain and should end with a
            DNS domain owned by the vendor of the driver.
        pool: This name together with the driver name and the device name field identify which device was
            allocated (`<driver name>/<pool name>/<device name>`).  Must not be longer than 253 characters and
            may contain one or more DNS sub-domains separated by slashes.
        request: Request is the name of the request in the claim which caused this device to be allocated.
            Multiple devices may have been allocated per request.

    """

    request: str
    driver: str
    pool: str
    device: str


@dataclass
class DeviceSelector(K8sSpec):
    """DeviceSelector must have exactly one field set.

    Attributes:
        cel: CEL contains a CEL expression for selecting a device.

    """

    cel: Optional[CELDeviceSelector] = None


@dataclass
class OpaqueDeviceConfiguration(K8sSpec):
    """OpaqueDeviceConfiguration contains configuration parameters for a driver in a format defined by the
    driver vendor.

    Attributes:
        driver: Driver is used to determine which kubelet plugin needs to be passed these configuration
            parameters.  An admission policy provided by the driver developer could use this to decide whether
            it needs to validate them.  Must be a DNS subdomain and should end with a DNS domain owned by the
            vendor of the driver.
        parameters: Parameters can contain arbitrary data. It is the responsibility of the driver developer to
            handle validation and versioning. Typically this includes self-identification and a version
            ('kind' + 'apiVersion' for Kubernetes types), with conversion between different versions.

    """

    driver: str
    parameters: JSONObj


@dataclass
class PodSchedulingContext(K8sResource):
    """PodSchedulingContext objects hold information that is needed to schedule a Pod with ResourceClaims
    that use 'WaitForFirstConsumer' allocation mode.  This is an alpha type and requires enabling the
    DRAControlPlaneController feature gate.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object metadata
        spec: Spec describes where resources for the Pod are needed.
        status: Status describes where resources for the Pod can be allocated.

    """

    spec: PodSchedulingContextSpec
    apiVersion: Literal['resource.k8s.io/v1alpha3'] = 'resource.k8s.io/v1alpha3'
    kind: Literal['PodSchedulingContext'] = 'PodSchedulingContext'
    metadata: Optional[gybe.k8s.v1_31.meta.v1.ObjectMeta] = None
    status: Optional[PodSchedulingContextStatus] = None


@dataclass
class PodSchedulingContextSpec(K8sSpec):
    """PodSchedulingContextSpec describes where resources for the Pod are needed.

    Attributes:
        potentialNodes: PotentialNodes lists nodes where the Pod might be able to run.  The size of this field
            is limited to 128. This is large enough for many clusters. Larger clusters may need more attempts
            to find a node that suits all pending resources. This may get increased in the future, but not
            reduced.
        selectedNode: SelectedNode is the node for which allocation of ResourceClaims that are referenced by
            the Pod and that use 'WaitForFirstConsumer' allocation is to be attempted.

    """

    potentialNodes: Optional[List[str]] = None
    selectedNode: Optional[str] = None


@dataclass
class PodSchedulingContextStatus(K8sSpec):
    """PodSchedulingContextStatus describes where resources for the Pod can be allocated.

    Attributes:
        resourceClaims: ResourceClaims describes resource availability for each pod.spec.resourceClaim entry
            where the corresponding ResourceClaim uses 'WaitForFirstConsumer' allocation mode.

    """

    resourceClaims: Optional[List[ResourceClaimSchedulingStatus]] = None


@dataclass
class ResourceClaim(K8sResource):
    """ResourceClaim describes a request for access to resources in the cluster, for use by workloads. For
    example, if a workload needs an accelerator device with specific properties, this is how that request
    is expressed. The status stanza tracks whether this claim has been satisfied and what specific
    resources have been allocated.  This is an alpha type and requires enabling the
    DynamicResourceAllocation feature gate.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object metadata
        spec: Spec describes what is being requested and how to configure it. The spec is immutable.
        status: Status describes whether the claim is ready to use and what has been allocated.

    """

    spec: ResourceClaimSpec
    apiVersion: Literal['resource.k8s.io/v1alpha3'] = 'resource.k8s.io/v1alpha3'
    kind: Literal['ResourceClaim'] = 'ResourceClaim'
    metadata: Optional[gybe.k8s.v1_31.meta.v1.ObjectMeta] = None
    status: Optional[ResourceClaimStatus] = None


@dataclass
class ResourceClaimConsumerReference(K8sSpec):
    """ResourceClaimConsumerReference contains enough information to let you locate the consumer of a
    ResourceClaim. The user must be a resource in the same namespace as the ResourceClaim.

    Attributes:
        apiGroup: APIGroup is the group for the resource being referenced. It is empty for the core API. This
            matches the group in the APIVersion that is used when creating the resources.
        name: Name is the name of resource being referenced.
        resource: Resource is the type of resource being referenced, for example 'pods'.
        uid: UID identifies exactly one incarnation of the resource.

    """

    resource: str
    name: str
    uid: str
    apiGroup: Optional[str] = None


@dataclass
class ResourceClaimSchedulingStatus(K8sSpec):
    """ResourceClaimSchedulingStatus contains information about one particular ResourceClaim with
    'WaitForFirstConsumer' allocation mode.

    Attributes:
        name: Name matches the pod.spec.resourceClaims[*].Name field.
        unsuitableNodes: UnsuitableNodes lists nodes that the ResourceClaim cannot be allocated for.  The size
            of this field is limited to 128, the same as for PodSchedulingSpec.PotentialNodes. This may get
            increased in the future, but not reduced.

    """

    name: str
    unsuitableNodes: Optional[List[str]] = None


@dataclass
class ResourceClaimSpec(K8sSpec):
    """ResourceClaimSpec defines what is being requested in a ResourceClaim and how to configure it.

    Attributes:
        controller: Controller is the name of the DRA driver that is meant to handle allocation of this claim.
            If empty, allocation is handled by the scheduler while scheduling a pod.  Must be a DNS subdomain
            and should end with a DNS domain owned by the vendor of the driver.  This is an alpha field and
            requires enabling the DRAControlPlaneController feature gate.
        devices: Devices defines how to request devices.

    """

    controller: Optional[str] = None
    devices: Optional[DeviceClaim] = None


@dataclass
class ResourceClaimStatus(K8sSpec):
    """ResourceClaimStatus tracks whether the resource has been allocated and what the result of that was.

    Attributes:
        allocation: Allocation is set once the claim has been allocated successfully.
        deallocationRequested: Indicates that a claim is to be deallocated. While this is set, no new
            consumers may be added to ReservedFor.  This is only used if the claim needs to be deallocated by
            a DRA driver. That driver then must deallocate this claim and reset the field together with
            clearing the Allocation field.  This is an alpha field and requires enabling the
            DRAControlPlaneController feature gate.
        reservedFor: ReservedFor indicates which entities are currently allowed to use the claim. A Pod which
            references a ResourceClaim which is not reserved for that Pod will not be started. A claim that is
            in use or might be in use because it has been reserved must not get deallocated.  In a cluster
            with multiple scheduler instances, two pods might get scheduled concurrently by different
            schedulers. When they reference the same ResourceClaim which already has reached its maximum
            number of consumers, only one pod can be scheduled.  Both schedulers try to add their pod to the
            claim.status.reservedFor field, but only the update that reaches the API server first gets stored.
            The other one fails with an error and the scheduler which issued it knows that it must put the pod
            back into the queue, waiting for the ResourceClaim to become usable again.  There can be at most
            32 such reservations. This may get increased in the future, but not reduced.

    """

    allocation: Optional[AllocationResult] = None
    deallocationRequested: Optional[bool] = None
    reservedFor: Optional[List[ResourceClaimConsumerReference]] = None


@dataclass
class ResourceClaimTemplate(K8sResource):
    """ResourceClaimTemplate is used to produce ResourceClaim objects.  This is an alpha type and requires
    enabling the DynamicResourceAllocation feature gate.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object metadata
        spec: Describes the ResourceClaim that is to be generated.  This field is immutable. A ResourceClaim
            will get created by the control plane for a Pod when needed and then not get updated anymore.

    """

    spec: ResourceClaimTemplateSpec
    apiVersion: Literal['resource.k8s.io/v1alpha3'] = 'resource.k8s.io/v1alpha3'
    kind: Literal['ResourceClaimTemplate'] = 'ResourceClaimTemplate'
    metadata: Optional[gybe.k8s.v1_31.meta.v1.ObjectMeta] = None


@dataclass
class ResourceClaimTemplateSpec(K8sSpec):
    """ResourceClaimTemplateSpec contains the metadata and fields for a ResourceClaim.

    Attributes:
        metadata: ObjectMeta may contain labels and annotations that will be copied into the PVC when creating
            it. No other fields are allowed and will be rejected during validation.
        spec: Spec for the ResourceClaim. The entire content is copied unchanged into the ResourceClaim that
            gets created from this template. The same fields as in a ResourceClaim are also valid here.

    """

    spec: ResourceClaimSpec
    metadata: Optional[gybe.k8s.v1_31.meta.v1.ObjectMeta] = None


@dataclass
class ResourcePool(K8sSpec):
    """ResourcePool describes the pool that ResourceSlices belong to.

    Attributes:
        generation: Generation tracks the change in a pool over time. Whenever a driver changes something
            about one or more of the resources in a pool, it must change the generation in all ResourceSlices
            which are part of that pool. Consumers of ResourceSlices should only consider resources from the
            pool with the highest generation number. The generation may be reset by drivers, which should be
            fine for consumers, assuming that all ResourceSlices in a pool are updated to match or deleted.
            Combined with ResourceSliceCount, this mechanism enables consumers to detect pools which are
            comprised of multiple ResourceSlices and are in an incomplete state.
        name: Name is used to identify the pool. For node-local devices, this is often the node name, but this
            is not required.  It must not be longer than 253 characters and must consist of one or more DNS
            sub-domains separated by slashes. This field is immutable.
        resourceSliceCount: ResourceSliceCount is the total number of ResourceSlices in the pool at this
            generation number. Must be greater than zero.  Consumers can use this to check whether they have
            seen all ResourceSlices belonging to the same pool.

    """

    name: str
    generation: int
    resourceSliceCount: int


@dataclass
class ResourceSlice(K8sResource):
    """ResourceSlice represents one or more resources in a pool of similar resources, managed by a common
    driver. A pool may span more than one ResourceSlice, and exactly how many ResourceSlices comprise a
    pool is determined by the driver.  At the moment, the only supported resources are devices with
    attributes and capacities. Each device in a given pool, regardless of how many ResourceSlices, must
    have a unique name. The ResourceSlice in which a device gets published may change over time. The
    unique identifier for a device is the tuple <driver name>, <pool name>, <device name>.  Whenever a
    driver needs to update a pool, it increments the pool.Spec.Pool.Generation number and updates all
    ResourceSlices with that new number and new resource definitions. A consumer must only use
    ResourceSlices with the highest generation number and ignore all others.  When allocating all
    resources in a pool matching certain criteria or when looking for the best solution among several
    different alternatives, a consumer should check the number of ResourceSlices in a pool (included in
    each ResourceSlice) to determine whether its view of a pool is complete and if not, should wait until
    the driver has completed updating the pool.  For resources that are not local to a node, the node name
    is not set. Instead, the driver may use a node selector to specify where the devices are available.
    This is an alpha type and requires enabling the DynamicResourceAllocation feature gate.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object metadata
        spec: Contains the information published by the driver.  Changing the spec automatically increments
            the metadata.generation number.

    """

    spec: ResourceSliceSpec
    apiVersion: Literal['resource.k8s.io/v1alpha3'] = 'resource.k8s.io/v1alpha3'
    kind: Literal['ResourceSlice'] = 'ResourceSlice'
    metadata: Optional[gybe.k8s.v1_31.meta.v1.ObjectMeta] = None


@dataclass
class ResourceSliceSpec(K8sSpec):
    """ResourceSliceSpec contains the information published by the driver in one ResourceSlice.

    Attributes:
        allNodes: AllNodes indicates that all nodes have access to the resources in the pool.  Exactly one of
            NodeName, NodeSelector and AllNodes must be set.
        devices: Devices lists some or all of the devices in this pool.  Must not have more than 128 entries.
        driver: Driver identifies the DRA driver providing the capacity information. A field selector can be
            used to list only ResourceSlice objects with a certain driver name.  Must be a DNS subdomain and
            should end with a DNS domain owned by the vendor of the driver. This field is immutable.
        nodeName: NodeName identifies the node which provides the resources in this pool. A field selector can
            be used to list only ResourceSlice objects belonging to a certain node.  This field can be used to
            limit access from nodes to ResourceSlices with the same node name. It also indicates to
            autoscalers that adding new nodes of the same type as some old node might also make new resources
            available.  Exactly one of NodeName, NodeSelector and AllNodes must be set. This field is
            immutable.
        nodeSelector: NodeSelector defines which nodes have access to the resources in the pool, when that
            pool is not limited to a single node.  Must use exactly one term.  Exactly one of NodeName,
            NodeSelector and AllNodes must be set.
        pool: Pool describes the pool that this ResourceSlice belongs to.

    """

    driver: str
    pool: ResourcePool
    allNodes: Optional[bool] = None
    devices: Optional[List[Device]] = None
    nodeName: Optional[str] = None
    nodeSelector: Optional[gybe.k8s.v1_31.core.v1.NodeSelector] = None
