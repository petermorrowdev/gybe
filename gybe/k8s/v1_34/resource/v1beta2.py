"""Models generated from Kubernetes OpenAPI Spec."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Literal, Optional

import gybe.k8s.v1_34.api.resource
import gybe.k8s.v1_34.core.v1
import gybe.k8s.v1_34.meta.v1
from gybe.k8s.types import JSONDict, JSONObj, K8sResource, K8sSpec


@dataclass
class AllocatedDeviceStatus(K8sSpec):
    """AllocatedDeviceStatus contains the status of an allocated device, if the driver chooses to report it.
    This may include driver-specific information.  The combination of Driver, Pool, Device, and ShareID
    must match the corresponding key in Status.Allocation.Devices.

    Attributes:
        conditions: Conditions contains the latest observation of the device's state. If the device has been
            configured according to the class and claim config references, the `Ready` condition should be
            True.  Must not contain more than 8 entries.
        data: Data contains arbitrary driver-specific data.  The length of the raw data must be smaller or
            equal to 10 Ki.
        device: Device references one device instance via its name in the driver's resource pool. It must be a
            DNS label.
        driver: Driver specifies the name of the DRA driver whose kubelet plugin should be invoked to process
            the allocation once the claim is needed on a node.  Must be a DNS subdomain and should end with a
            DNS domain owned by the vendor of the driver.
        networkData: NetworkData contains network-related information specific to the device.
        pool: This name together with the driver name and the device name field identify which device was
            allocated (`<driver name>/<pool name>/<device name>`).  Must not be longer than 253 characters and
            may contain one or more DNS sub-domains separated by slashes.
        shareID: ShareID uniquely identifies an individual allocation share of the device.

    """

    driver: str
    pool: str
    device: str
    conditions: Optional[List[gybe.k8s.v1_34.meta.v1.Condition]] = None
    data: Optional[JSONObj] = None
    networkData: Optional[NetworkDeviceData] = None
    shareID: Optional[str] = None


@dataclass
class AllocationResult(K8sSpec):
    """AllocationResult contains attributes of an allocated resource.

    Attributes:
        allocationTimestamp: AllocationTimestamp stores the time when the resources were allocated. This field
            is not guaranteed to be set, in which case that time is unknown.  This is an alpha field and
            requires enabling the DRADeviceBindingConditions and DRAResourceClaimDeviceStatus feature gate.
        devices: Devices is the result of allocating devices.
        nodeSelector: NodeSelector defines where the allocated resources are available. If unset, they are
            available everywhere.

    """

    allocationTimestamp: Optional[str] = None
    devices: Optional[DeviceAllocationResult] = None
    nodeSelector: Optional[gybe.k8s.v1_34.core.v1.NodeSelector] = None


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
            device's capacities, grouped by prefix.  - allowMultipleAllocations (bool): the
            allowMultipleAllocations property of the device    (v1.34+ with the DRAConsumableCapacity feature
            enabled).  Example: Consider a device with driver='dra.example.com', which exposes two attributes
            named 'model' and 'ext.example.com/family' and which exposes one capacity named 'modules'. This
            input to this expression would have the following fields:      device.driver
            device.attributes['dra.example.com'].model     device.attributes['ext.example.com'].family
            device.capacity['dra.example.com'].modules  The device.driver field can be used to check for a
            specific driver, either as a high-level precondition (i.e. you only want to consider devices from
            this driver) or as part of a multi-clause expression that is meant to consider devices from
            different drivers.  The value type of each attribute is defined by the device definition, and
            users who write these expressions must consult the documentation for their specific drivers. The
            value type of each capacity is Quantity.  If an unknown prefix is used as a lookup in either
            device.attributes or device.capacity, an empty map will be returned. Any reference to an unknown
            field will cause an evaluation error and allocation to abort.  A robust expression should check
            for the existence of attributes before referencing them.  For ease of use, the cel.bind() function
            is enabled, and can be used to simplify expressions that access multiple attributes with the same
            domain. For example:      cel.bind(dra, device.attributes['dra.example.com'], dra.someBool &&
            dra.anotherBool)  The length of the expression must be smaller or equal to 10 Ki. The cost of
            evaluating it is also limited based on the estimated number of logical steps.

    """

    expression: str


@dataclass
class CapacityRequestPolicy(K8sSpec):
    """CapacityRequestPolicy defines how requests consume device capacity.  Must not set more than one
    ValidRequestValues.

    Attributes:
        default: Default specifies how much of this capacity is consumed by a request that does not contain an
            entry for it in DeviceRequest's Capacity.
        validRange: ValidRange defines an acceptable quantity value range in consuming requests.  If this
            field is set, Default must be defined and it must fall within the defined ValidRange.  If the
            requested amount does not fall within the defined range, the request violates the policy, and this
            device cannot be allocated.  If the request doesn't contain this capacity entry, Default value is
            used.
        validValues: ValidValues defines a set of acceptable quantity values in consuming requests.  Must not
            contain more than 10 entries. Must be sorted in ascending order.  If this field is set, Default
            must be defined and it must be included in ValidValues list.  If the requested amount does not
            match any valid value but smaller than some valid values, the scheduler calculates the smallest
            valid value that is greater than or equal to the request. That is: min(ceil(requestedValue) ∈
            validValues), where requestedValue ≤ max(validValues).  If the requested amount exceeds all valid
            values, the request violates the policy, and this device cannot be allocated.

    """

    default: Optional[gybe.k8s.v1_34.api.resource.Quantity] = None
    validRange: Optional[CapacityRequestPolicyRange] = None
    validValues: Optional[List[gybe.k8s.v1_34.api.resource.Quantity]] = None


@dataclass
class CapacityRequestPolicyRange(K8sSpec):
    """CapacityRequestPolicyRange defines a valid range for consumable capacity values.    - If the requested
    amount is less than Min, it is rounded up to the Min value.   - If Step is set and the requested
    amount is between Min and Max but not aligned with Step,     it will be rounded up to the next value
    equal to Min + (n * Step).   - If Step is not set, the requested amount is used as-is if it falls
    within the range Min to Max (if set).   - If the requested or rounded amount exceeds Max (if set), the
    request does not satisfy the policy,     and the device cannot be allocated.

    Attributes:
        max: Max defines the upper limit for capacity that can be requested.  Max must be less than or equal
            to the capacity value. Min and requestPolicy.default must be less than or equal to the maximum.
        min: Min specifies the minimum capacity allowed for a consumption request.  Min must be greater than
            or equal to zero, and less than or equal to the capacity value. requestPolicy.default must be more
            than or equal to the minimum.
        step: Step defines the step size between valid capacity amounts within the range.  Max (if set) and
            requestPolicy.default must be a multiple of Step. Min + Step must be less than or equal to the
            capacity value.

    """

    min: gybe.k8s.v1_34.api.resource.Quantity
    max: Optional[gybe.k8s.v1_34.api.resource.Quantity] = None
    step: Optional[gybe.k8s.v1_34.api.resource.Quantity] = None


@dataclass
class CapacityRequirements(K8sSpec):
    """CapacityRequirements defines the capacity requirements for a specific device request.

    Attributes:
        requests: Requests represent individual device resource requests for distinct resources, all of which
            must be provided by the device.  This value is used as an additional filtering condition against
            the available capacity on the device. This is semantically equivalent to a CEL selector with
            `device.capacity[<domain>].<name>.compareTo(quantity(<request quantity>)) >= 0`. For example,
            device.capacity['test-driver.cdi.k8s.io'].counters.compareTo(quantity('2')) >= 0.  When a
            requestPolicy is defined, the requested amount is adjusted upward to the nearest valid value based
            on the policy. If the requested amount cannot be adjusted to a valid value—because it exceeds what
            the requestPolicy allows— the device is considered ineligible for allocation.  For any capacity
            that is not explicitly requested: - If no requestPolicy is set, the default consumed capacity is
            equal to the full device capacity   (i.e., the whole device is claimed). - If a requestPolicy is
            set, the default consumed capacity is determined according to that policy.  If the device allows
            multiple allocation, the aggregated amount across all requests must not exceed the capacity value.
            The consumed capacity, which may be adjusted based on the requestPolicy if defined, is recorded in
            the resource claim’s status.devices[*].consumedCapacity field.

    """

    requests: Optional[JSONDict] = None


@dataclass
class Counter(K8sSpec):
    """Counter describes a quantity associated with a device.

    Attributes:
        value: Value defines how much of a certain device counter is available.

    """

    value: gybe.k8s.v1_34.api.resource.Quantity


@dataclass
class CounterSet(K8sSpec):
    """CounterSet defines a named set of counters that are available to be used by devices defined in the
    ResourceSlice.  The counters are not allocatable by themselves, but can be referenced by devices. When
    a device is allocated, the portion of counters it uses will no longer be available for use by other
    devices.

    Attributes:
        counters: Counters defines the set of counters for this CounterSet The name of each counter must be
            unique in that set and must be a DNS label.  The maximum number of counters in all sets is 32.
        name: Name defines the name of the counter set. It must be a DNS label.

    """

    name: str
    counters: JSONDict


@dataclass
class Device(K8sSpec):
    """Device represents one individual hardware instance that can be selected based on its attributes.
    Besides the name, exactly one field must be set.

    Attributes:
        allNodes: AllNodes indicates that all nodes have access to the device.  Must only be set if
            Spec.PerDeviceNodeSelection is set to true. At most one of NodeName, NodeSelector and AllNodes can
            be set.
        allowMultipleAllocations: AllowMultipleAllocations marks whether the device is allowed to be allocated
            to multiple DeviceRequests.  If AllowMultipleAllocations is set to true, the device can be
            allocated more than once, and all of its capacity is consumable, regardless of whether the
            requestPolicy is defined or not.
        attributes: Attributes defines the set of attributes for this device. The name of each attribute must
            be unique in that set.  The maximum number of attributes and capacities combined is 32.
        bindingConditions: BindingConditions defines the conditions for proceeding with binding. All of these
            conditions must be set in the per-device status conditions with a value of True to proceed with
            binding the pod to the node while scheduling the pod.  The maximum number of binding conditions is
            4.  The conditions must be a valid condition type string.  This is an alpha field and requires
            enabling the DRADeviceBindingConditions and DRAResourceClaimDeviceStatus feature gates.
        bindingFailureConditions: BindingFailureConditions defines the conditions for binding failure. They
            may be set in the per-device status conditions. If any is set to 'True', a binding failure
            occurred.  The maximum number of binding failure conditions is 4.  The conditions must be a valid
            condition type string.  This is an alpha field and requires enabling the
            DRADeviceBindingConditions and DRAResourceClaimDeviceStatus feature gates.
        bindsToNode: BindsToNode indicates if the usage of an allocation involving this device has to be
            limited to exactly the node that was chosen when allocating the claim. If set to true, the
            scheduler will set the ResourceClaim.Status.Allocation.NodeSelector to match the node where the
            allocation was made.  This is an alpha field and requires enabling the DRADeviceBindingConditions
            and DRAResourceClaimDeviceStatus feature gates.
        capacity: Capacity defines the set of capacities for this device. The name of each capacity must be
            unique in that set.  The maximum number of attributes and capacities combined is 32.
        consumesCounters: ConsumesCounters defines a list of references to sharedCounters and the set of
            counters that the device will consume from those counter sets.  There can only be a single entry
            per counterSet.  The total number of device counter consumption entries must be <= 32. In
            addition, the total number in the entire ResourceSlice must be <= 1024 (for example, 64 devices
            with 16 counters each).
        name: Name is unique identifier among all devices managed by the driver in the pool. It must be a DNS
            label.
        nodeName: NodeName identifies the node where the device is available.  Must only be set if
            Spec.PerDeviceNodeSelection is set to true. At most one of NodeName, NodeSelector and AllNodes can
            be set.
        nodeSelector: NodeSelector defines the nodes where the device is available.  Must use exactly one
            term.  Must only be set if Spec.PerDeviceNodeSelection is set to true. At most one of NodeName,
            NodeSelector and AllNodes can be set.
        taints: If specified, these are the driver-defined taints.  The maximum number of taints is 4.  This
            is an alpha field and requires enabling the DRADeviceTaints feature gate.

    """

    name: str
    allNodes: Optional[bool] = None
    allowMultipleAllocations: Optional[bool] = None
    attributes: Optional[JSONDict] = None
    bindingConditions: Optional[List[str]] = None
    bindingFailureConditions: Optional[List[str]] = None
    bindsToNode: Optional[bool] = None
    capacity: Optional[JSONDict] = None
    consumesCounters: Optional[List[DeviceCounterConsumption]] = None
    nodeName: Optional[str] = None
    nodeSelector: Optional[gybe.k8s.v1_34.core.v1.NodeSelector] = None
    taints: Optional[List[DeviceTaint]] = None


@dataclass
class DeviceAllocationConfiguration(K8sSpec):
    """DeviceAllocationConfiguration gets embedded in an AllocationResult.

    Attributes:
        opaque: Opaque provides driver-specific configuration parameters.
        requests: Requests lists the names of requests where the configuration applies. If empty, its applies
            to all requests.  References to subrequests must include the name of the main request and may
            include the subrequest using the format <main request>[/<subrequest>]. If just the main request is
            given, the configuration applies to all subrequests.
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
class DeviceCapacity(K8sSpec):
    """DeviceCapacity describes a quantity associated with a device.

    Attributes:
        requestPolicy: RequestPolicy defines how this DeviceCapacity must be consumed when the device is
            allowed to be shared by multiple allocations.  The Device must have allowMultipleAllocations set
            to true in order to set a requestPolicy.  If unset, capacity requests are unconstrained: requests
            can consume any amount of capacity, as long as the total consumed across all allocations does not
            exceed the device's defined capacity. If request is also unset, default is the full capacity
            value.
        value: Value defines how much of a certain capacity that device has.  This field reflects the fixed
            total capacity and does not change. The consumed amount is tracked separately by scheduler and
            does not affect this value.

    """

    value: gybe.k8s.v1_34.api.resource.Quantity
    requestPolicy: Optional[CapacityRequestPolicy] = None


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
            to all requests.  References to subrequests must include the name of the main request and may
            include the subrequest using the format <main request>[/<subrequest>]. If just the main request is
            given, the configuration applies to all subrequests.

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
    apiVersion: Literal['resource.k8s.io/v1beta2'] = 'resource.k8s.io/v1beta2'
    kind: Literal['DeviceClass'] = 'DeviceClass'
    metadata: Optional[gybe.k8s.v1_34.meta.v1.ObjectMeta] = None


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
        extendedResourceName: ExtendedResourceName is the extended resource name for the devices of this
            class. The devices of this class can be used to satisfy a pod's extended resource requests. It has
            the same format as the name of a pod's extended resource. It should be unique among all the device
            classes in a cluster. If two device classes have the same name, then the class created later is
            picked to satisfy a pod's extended resource requests. If two classes are created at the same time,
            then the name of the class lexicographically sorted first is picked.  This is an alpha field.
        selectors: Each selector must be satisfied by a device which is claimed via this class.

    """

    config: Optional[List[DeviceClassConfiguration]] = None
    extendedResourceName: Optional[str] = None
    selectors: Optional[List[DeviceSelector]] = None


@dataclass
class DeviceConstraint(K8sSpec):
    """DeviceConstraint must have exactly one field set besides Requests.

    Attributes:
        distinctAttribute: DistinctAttribute requires that all devices in question have this attribute and
            that its type and value are unique across those devices.  This acts as the inverse of
            MatchAttribute.  This constraint is used to avoid allocating multiple requests to the same device
            by ensuring attribute-level differentiation.  This is useful for scenarios where resource requests
            must be fulfilled by separate physical devices. For example, a container requests two network
            interfaces that must be allocated from two different physical NICs.
        matchAttribute: MatchAttribute requires that all devices in question have this attribute and that its
            type and value are the same across those devices.  For example, if you specified
            'dra.example.com/numa' (a hypothetical example!), then only devices in the same NUMA node will be
            chosen. A device which does not have that attribute will not be chosen. All devices should use a
            value of the same type for this attribute because that is part of its specification, but if one
            device doesn't, then it also will not be chosen.  Must include the domain qualifier.
        requests: Requests is a list of the one or more requests in this claim which must co-satisfy this
            constraint. If a request is fulfilled by multiple devices, then all of the devices must satisfy
            the constraint. If this is not specified, this constraint applies to all requests in this claim.
            References to subrequests must include the name of the main request and may include the subrequest
            using the format <main request>[/<subrequest>]. If just the main request is given, the constraint
            applies to all subrequests.

    """

    distinctAttribute: Optional[str] = None
    matchAttribute: Optional[str] = None
    requests: Optional[List[str]] = None


@dataclass
class DeviceCounterConsumption(K8sSpec):
    """DeviceCounterConsumption defines a set of counters that a device will consume from a CounterSet.

    Attributes:
        counterSet: CounterSet is the name of the set from which the counters defined will be consumed.
        counters: Counters defines the counters that will be consumed by the device.  The maximum number
            counters in a device is 32. In addition, the maximum number of all counters in all devices is 1024
            (for example, 64 devices with 16 counters each).

    """

    counterSet: str
    counters: JSONDict


@dataclass
class DeviceRequest(K8sSpec):
    """DeviceRequest is a request for devices required for a claim. This is typically a request for a single
    resource like a device, but can also ask for several identical devices. With FirstAvailable it is also
    possible to provide a prioritized list of requests.

    Attributes:
        exactly: Exactly specifies the details for a single request that must be met exactly for the request
            to be satisfied.  One of Exactly or FirstAvailable must be set.
        firstAvailable: FirstAvailable contains subrequests, of which exactly one will be selected by the
            scheduler. It tries to satisfy them in the order in which they are listed here. So if there are
            two entries in the list, the scheduler will only check the second one if it determines that the
            first one can not be used.  DRA does not yet implement scoring, so the scheduler will select the
            first set of devices that satisfies all the requests in the claim. And if the requirements can be
            satisfied on more than one node, other scheduling features will determine which node is chosen.
            This means that the set of devices allocated to a claim might not be the optimal set available to
            the cluster. Scoring will be implemented later.
        name: Name can be used to reference this request in a pod.spec.containers[].resources.claims entry and
            in a constraint of the claim.  References using the name in the DeviceRequest will uniquely
            identify a request when the Exactly field is set. When the FirstAvailable field is set, a
            reference to the name of the DeviceRequest will match whatever subrequest is chosen by the
            scheduler.  Must be a DNS label.

    """

    name: str
    exactly: Optional[ExactDeviceRequest] = None
    firstAvailable: Optional[List[DeviceSubRequest]] = None


@dataclass
class DeviceRequestAllocationResult(K8sSpec):
    """DeviceRequestAllocationResult contains the allocation result for one request.

    Attributes:
        adminAccess: AdminAccess indicates that this device was allocated for administrative access. See the
            corresponding request field for a definition of mode.  This is an alpha field and requires
            enabling the DRAAdminAccess feature gate. Admin access is disabled if this field is unset or set
            to false, otherwise it is enabled.
        bindingConditions: BindingConditions contains a copy of the BindingConditions from the corresponding
            ResourceSlice at the time of allocation.  This is an alpha field and requires enabling the
            DRADeviceBindingConditions and DRAResourceClaimDeviceStatus feature gates.
        bindingFailureConditions: BindingFailureConditions contains a copy of the BindingFailureConditions
            from the corresponding ResourceSlice at the time of allocation.  This is an alpha field and
            requires enabling the DRADeviceBindingConditions and DRAResourceClaimDeviceStatus feature gates.
        consumedCapacity: ConsumedCapacity tracks the amount of capacity consumed per device as part of the
            claim request. The consumed amount may differ from the requested amount: it is rounded up to the
            nearest valid value based on the device’s requestPolicy if applicable (i.e., may not be less than
            the requested amount).  The total consumed capacity for each device must not exceed the
            DeviceCapacity's Value.  This field is populated only for devices that allow multiple allocations.
            All capacity entries are included, even if the consumed amount is zero.
        device: Device references one device instance via its name in the driver's resource pool. It must be a
            DNS label.
        driver: Driver specifies the name of the DRA driver whose kubelet plugin should be invoked to process
            the allocation once the claim is needed on a node.  Must be a DNS subdomain and should end with a
            DNS domain owned by the vendor of the driver.
        pool: This name together with the driver name and the device name field identify which device was
            allocated (`<driver name>/<pool name>/<device name>`).  Must not be longer than 253 characters and
            may contain one or more DNS sub-domains separated by slashes.
        request: Request is the name of the request in the claim which caused this device to be allocated. If
            it references a subrequest in the firstAvailable list on a DeviceRequest, this field must include
            both the name of the main request and the subrequest using the format <main request>/<subrequest>.
            Multiple devices may have been allocated per request.
        shareID: ShareID uniquely identifies an individual allocation share of the device, used when the
            device supports multiple simultaneous allocations. It serves as an additional map key to
            differentiate concurrent shares of the same device.
        tolerations: A copy of all tolerations specified in the request at the time when the device got
            allocated.  The maximum number of tolerations is 16.  This is an alpha field and requires enabling
            the DRADeviceTaints feature gate.

    """

    request: str
    driver: str
    pool: str
    device: str
    adminAccess: Optional[bool] = None
    bindingConditions: Optional[List[str]] = None
    bindingFailureConditions: Optional[List[str]] = None
    consumedCapacity: Optional[JSONDict] = None
    shareID: Optional[str] = None
    tolerations: Optional[List[DeviceToleration]] = None


@dataclass
class DeviceSelector(K8sSpec):
    """DeviceSelector must have exactly one field set.

    Attributes:
        cel: CEL contains a CEL expression for selecting a device.

    """

    cel: Optional[CELDeviceSelector] = None


@dataclass
class DeviceSubRequest(K8sSpec):
    """DeviceSubRequest describes a request for device provided in the
    claim.spec.devices.requests[].firstAvailable array. Each is typically a request for a single resource
    like a device, but can also ask for several identical devices.  DeviceSubRequest is similar to
    ExactDeviceRequest, but doesn't expose the AdminAccess field as that one is only supported when
    requesting a specific device.

    Attributes:
        allocationMode: AllocationMode and its related fields define how devices are allocated to satisfy this
            subrequest. Supported values are:  - ExactCount: This request is for a specific number of devices.
            This is the default. The exact number is provided in the   count field.  - All: This subrequest is
            for all of the matching devices in a pool.   Allocation will fail if some devices are already
            allocated,   unless adminAccess is requested.  If AllocationMode is not specified, the default
            mode is ExactCount. If the mode is ExactCount and count is not specified, the default count is
            one. Any other subrequests must specify this field.  More modes may get added in the future.
            Clients must refuse to handle requests with unknown modes.
        capacity: Capacity define resource requirements against each capacity.  If this field is unset and the
            device supports multiple allocations, the default value will be applied to each capacity according
            to requestPolicy. For the capacity that has no requestPolicy, default is the full capacity value.
            Applies to each device allocation. If Count > 1, the request fails if there aren't enough devices
            that meet the requirements. If AllocationMode is set to All, the request fails if there are
            devices that otherwise match the request, and have this capacity, with a value >= the requested
            amount, but which cannot be allocated to this request.
        count: Count is used only when the count mode is 'ExactCount'. Must be greater than zero. If
            AllocationMode is ExactCount and this field is not specified, the default is one.
        deviceClassName: DeviceClassName references a specific DeviceClass, which can define additional
            configuration and selectors to be inherited by this subrequest.  A class is required. Which
            classes are available depends on the cluster.  Administrators may use this to restrict which
            devices may get requested by only installing classes with selectors for permitted devices. If
            users are free to request anything without restrictions, then administrators can create an empty
            DeviceClass for users to reference.
        name: Name can be used to reference this subrequest in the list of constraints or the list of
            configurations for the claim. References must use the format <main request>/<subrequest>.  Must be
            a DNS label.
        selectors: Selectors define criteria which must be satisfied by a specific device in order for that
            device to be considered for this subrequest. All selectors must be satisfied for a device to be
            considered.
        tolerations: If specified, the request's tolerations.  Tolerations for NoSchedule are required to
            allocate a device which has a taint with that effect. The same applies to NoExecute.  In addition,
            should any of the allocated devices get tainted with NoExecute after allocation and that effect is
            not tolerated, then all pods consuming the ResourceClaim get deleted to evict them. The scheduler
            will not let new pods reserve the claim while it has these tainted devices. Once all pods are
            evicted, the claim will get deallocated.  The maximum number of tolerations is 16.  This is an
            alpha field and requires enabling the DRADeviceTaints feature gate.

    """

    name: str
    deviceClassName: str
    allocationMode: Optional[str] = None
    capacity: Optional[CapacityRequirements] = None
    count: Optional[int] = None
    selectors: Optional[List[DeviceSelector]] = None
    tolerations: Optional[List[DeviceToleration]] = None


@dataclass
class DeviceTaint(K8sSpec):
    """The device this taint is attached to has the 'effect' on any claim which does not tolerate the taint
    and, through the claim, to pods using the claim.

    Attributes:
        effect: The effect of the taint on claims that do not tolerate the taint and through such claims on
            the pods using them. Valid effects are NoSchedule and NoExecute. PreferNoSchedule as used for
            nodes is not valid here.
        key: The taint key to be applied to a device. Must be a label name.
        timeAdded: TimeAdded represents the time at which the taint was added. Added automatically during
            create or update if not set.
        value: The taint value corresponding to the taint key. Must be a label value.

    """

    key: str
    effect: str
    timeAdded: Optional[str] = None
    value: Optional[str] = None


@dataclass
class DeviceToleration(K8sSpec):
    """The ResourceClaim this DeviceToleration is attached to tolerates any taint that matches the triple
    <key,value,effect> using the matching operator <operator>.

    Attributes:
        effect: Effect indicates the taint effect to match. Empty means match all taint effects. When
            specified, allowed values are NoSchedule and NoExecute.
        key: Key is the taint key that the toleration applies to. Empty means match all taint keys. If the key
            is empty, operator must be Exists; this combination means to match all values and all keys. Must
            be a label name.
        operator: Operator represents a key's relationship to the value. Valid operators are Exists and Equal.
            Defaults to Equal. Exists is equivalent to wildcard for value, so that a ResourceClaim can
            tolerate all taints of a particular category.
        tolerationSeconds: TolerationSeconds represents the period of time the toleration (which must be of
            effect NoExecute, otherwise this field is ignored) tolerates the taint. By default, it is not set,
            which means tolerate the taint forever (do not evict). Zero and negative values will be treated as
            0 (evict immediately) by the system. If larger than zero, the time when the pod needs to be
            evicted is calculated as <time when taint was adedd> + <toleration seconds>.
        value: Value is the taint value the toleration matches to. If the operator is Exists, the value must
            be empty, otherwise just a regular string. Must be a label value.

    """

    effect: Optional[str] = None
    key: Optional[str] = None
    operator: Optional[str] = None
    tolerationSeconds: Optional[int] = None
    value: Optional[str] = None


@dataclass
class ExactDeviceRequest(K8sSpec):
    """ExactDeviceRequest is a request for one or more identical devices.

    Attributes:
        adminAccess: AdminAccess indicates that this is a claim for administrative access to the device(s).
            Claims with AdminAccess are expected to be used for monitoring or other management services for a
            device.  They ignore all ordinary claims to the device with respect to access modes and any
            resource allocations.  This is an alpha field and requires enabling the DRAAdminAccess feature
            gate. Admin access is disabled if this field is unset or set to false, otherwise it is enabled.
        allocationMode: AllocationMode and its related fields define how devices are allocated to satisfy this
            request. Supported values are:  - ExactCount: This request is for a specific number of devices.
            This is the default. The exact number is provided in the   count field.  - All: This request is
            for all of the matching devices in a pool.   At least one device must exist on the node for the
            allocation to succeed.   Allocation will fail if some devices are already allocated,   unless
            adminAccess is requested.  If AllocationMode is not specified, the default mode is ExactCount. If
            the mode is ExactCount and count is not specified, the default count is one. Any other requests
            must specify this field.  More modes may get added in the future. Clients must refuse to handle
            requests with unknown modes.
        capacity: Capacity define resource requirements against each capacity.  If this field is unset and the
            device supports multiple allocations, the default value will be applied to each capacity according
            to requestPolicy. For the capacity that has no requestPolicy, default is the full capacity value.
            Applies to each device allocation. If Count > 1, the request fails if there aren't enough devices
            that meet the requirements. If AllocationMode is set to All, the request fails if there are
            devices that otherwise match the request, and have this capacity, with a value >= the requested
            amount, but which cannot be allocated to this request.
        count: Count is used only when the count mode is 'ExactCount'. Must be greater than zero. If
            AllocationMode is ExactCount and this field is not specified, the default is one.
        deviceClassName: DeviceClassName references a specific DeviceClass, which can define additional
            configuration and selectors to be inherited by this request.  A DeviceClassName is required.
            Administrators may use this to restrict which devices may get requested by only installing classes
            with selectors for permitted devices. If users are free to request anything without restrictions,
            then administrators can create an empty DeviceClass for users to reference.
        selectors: Selectors define criteria which must be satisfied by a specific device in order for that
            device to be considered for this request. All selectors must be satisfied for a device to be
            considered.
        tolerations: If specified, the request's tolerations.  Tolerations for NoSchedule are required to
            allocate a device which has a taint with that effect. The same applies to NoExecute.  In addition,
            should any of the allocated devices get tainted with NoExecute after allocation and that effect is
            not tolerated, then all pods consuming the ResourceClaim get deleted to evict them. The scheduler
            will not let new pods reserve the claim while it has these tainted devices. Once all pods are
            evicted, the claim will get deallocated.  The maximum number of tolerations is 16.  This is an
            alpha field and requires enabling the DRADeviceTaints feature gate.

    """

    deviceClassName: str
    adminAccess: Optional[bool] = None
    allocationMode: Optional[str] = None
    capacity: Optional[CapacityRequirements] = None
    count: Optional[int] = None
    selectors: Optional[List[DeviceSelector]] = None
    tolerations: Optional[List[DeviceToleration]] = None


@dataclass
class NetworkDeviceData(K8sSpec):
    """NetworkDeviceData provides network-related details for the allocated device. This information may be
    filled by drivers or other components to configure or identify the device within a network context.

    Attributes:
        hardwareAddress: HardwareAddress represents the hardware address (e.g. MAC Address) of the device's
            network interface.  Must not be longer than 128 characters.
        interfaceName: InterfaceName specifies the name of the network interface associated with the allocated
            device. This might be the name of a physical or virtual network interface being configured in the
            pod.  Must not be longer than 256 characters.
        ips: IPs lists the network addresses assigned to the device's network interface. This can include both
            IPv4 and IPv6 addresses. The IPs are in the CIDR notation, which includes both the address and the
            associated subnet mask. e.g.: '192.0.2.5/24' for IPv4 and '2001:db8::5/64' for IPv6.

    """

    hardwareAddress: Optional[str] = None
    interfaceName: Optional[str] = None
    ips: Optional[List[str]] = None


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
            ('kind' + 'apiVersion' for Kubernetes types), with conversion between different versions.  The
            length of the raw data must be smaller or equal to 10 Ki.

    """

    driver: str
    parameters: JSONObj


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
    apiVersion: Literal['resource.k8s.io/v1beta2'] = 'resource.k8s.io/v1beta2'
    kind: Literal['ResourceClaim'] = 'ResourceClaim'
    metadata: Optional[gybe.k8s.v1_34.meta.v1.ObjectMeta] = None
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
class ResourceClaimSpec(K8sSpec):
    """ResourceClaimSpec defines what is being requested in a ResourceClaim and how to configure it.

    Attributes:
        devices: Devices defines how to request devices.

    """

    devices: Optional[DeviceClaim] = None


@dataclass
class ResourceClaimStatus(K8sSpec):
    """ResourceClaimStatus tracks whether the resource has been allocated and what the result of that was.

    Attributes:
        allocation: Allocation is set once the claim has been allocated successfully.
        devices: Devices contains the status of each device allocated for this claim, as reported by the
            driver. This can include driver-specific information. Entries are owned by their respective
            drivers.
        reservedFor: ReservedFor indicates which entities are currently allowed to use the claim. A Pod which
            references a ResourceClaim which is not reserved for that Pod will not be started. A claim that is
            in use or might be in use because it has been reserved must not get deallocated.  In a cluster
            with multiple scheduler instances, two pods might get scheduled concurrently by different
            schedulers. When they reference the same ResourceClaim which already has reached its maximum
            number of consumers, only one pod can be scheduled.  Both schedulers try to add their pod to the
            claim.status.reservedFor field, but only the update that reaches the API server first gets stored.
            The other one fails with an error and the scheduler which issued it knows that it must put the pod
            back into the queue, waiting for the ResourceClaim to become usable again.  There can be at most
            256 such reservations. This may get increased in the future, but not reduced.

    """

    allocation: Optional[AllocationResult] = None
    devices: Optional[List[AllocatedDeviceStatus]] = None
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
    apiVersion: Literal['resource.k8s.io/v1beta2'] = 'resource.k8s.io/v1beta2'
    kind: Literal['ResourceClaimTemplate'] = 'ResourceClaimTemplate'
    metadata: Optional[gybe.k8s.v1_34.meta.v1.ObjectMeta] = None


@dataclass
class ResourceClaimTemplateSpec(K8sSpec):
    """ResourceClaimTemplateSpec contains the metadata and fields for a ResourceClaim.

    Attributes:
        metadata: ObjectMeta may contain labels and annotations that will be copied into the ResourceClaim
            when creating it. No other fields are allowed and will be rejected during validation.
        spec: Spec for the ResourceClaim. The entire content is copied unchanged into the ResourceClaim that
            gets created from this template. The same fields as in a ResourceClaim are also valid here.

    """

    spec: ResourceClaimSpec
    metadata: Optional[gybe.k8s.v1_34.meta.v1.ObjectMeta] = None


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
    apiVersion: Literal['resource.k8s.io/v1beta2'] = 'resource.k8s.io/v1beta2'
    kind: Literal['ResourceSlice'] = 'ResourceSlice'
    metadata: Optional[gybe.k8s.v1_34.meta.v1.ObjectMeta] = None


@dataclass
class ResourceSliceSpec(K8sSpec):
    """ResourceSliceSpec contains the information published by the driver in one ResourceSlice.

    Attributes:
        allNodes: AllNodes indicates that all nodes have access to the resources in the pool.  Exactly one of
            NodeName, NodeSelector, AllNodes, and PerDeviceNodeSelection must be set.
        devices: Devices lists some or all of the devices in this pool.  Must not have more than 128 entries.
        driver: Driver identifies the DRA driver providing the capacity information. A field selector can be
            used to list only ResourceSlice objects with a certain driver name.  Must be a DNS subdomain and
            should end with a DNS domain owned by the vendor of the driver. This field is immutable.
        nodeName: NodeName identifies the node which provides the resources in this pool. A field selector can
            be used to list only ResourceSlice objects belonging to a certain node.  This field can be used to
            limit access from nodes to ResourceSlices with the same node name. It also indicates to
            autoscalers that adding new nodes of the same type as some old node might also make new resources
            available.  Exactly one of NodeName, NodeSelector, AllNodes, and PerDeviceNodeSelection must be
            set. This field is immutable.
        nodeSelector: NodeSelector defines which nodes have access to the resources in the pool, when that
            pool is not limited to a single node.  Must use exactly one term.  Exactly one of NodeName,
            NodeSelector, AllNodes, and PerDeviceNodeSelection must be set.
        perDeviceNodeSelection: PerDeviceNodeSelection defines whether the access from nodes to resources in
            the pool is set on the ResourceSlice level or on each device. If it is set to true, every device
            defined the ResourceSlice must specify this individually.  Exactly one of NodeName, NodeSelector,
            AllNodes, and PerDeviceNodeSelection must be set.
        pool: Pool describes the pool that this ResourceSlice belongs to.
        sharedCounters: SharedCounters defines a list of counter sets, each of which has a name and a list of
            counters available.  The names of the SharedCounters must be unique in the ResourceSlice.  The
            maximum number of counters in all sets is 32.

    """

    driver: str
    pool: ResourcePool
    allNodes: Optional[bool] = None
    devices: Optional[List[Device]] = None
    nodeName: Optional[str] = None
    nodeSelector: Optional[gybe.k8s.v1_34.core.v1.NodeSelector] = None
    perDeviceNodeSelection: Optional[bool] = None
    sharedCounters: Optional[List[CounterSet]] = None
