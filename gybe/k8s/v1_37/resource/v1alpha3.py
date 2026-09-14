"""Models generated from Kubernetes OpenAPI Spec."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Literal, Optional

import gybe.k8s.v1_37.api.resource as _api_resource
import gybe.k8s.v1_37.meta.v1 as _meta_v1
from gybe.k8s.types import K8sResource, K8sSpec


@dataclass
class DeviceTaint(K8sSpec):
    """The device this taint is attached to has the 'effect' on any claim which does not tolerate the taint
    and, through the claim, to pods using the claim.

    Attributes:
        effect: The effect of the taint on claims that do not tolerate the taint and through such claims on
            the pods using them.  Valid effects are None, NoSchedule and NoExecute. PreferNoSchedule as used
            for nodes is not valid here. More effects may get added in the future. Consumers must treat
            unknown effects like None.
        key: The taint key to be applied to a device. Must be a label name.
        timeAdded: TimeAdded represents the time at which the taint was added or (only in a DeviceTaintRule)
            the effect was modified. Added automatically during create or update if not set.  In addition, in
            a DeviceTaintRule a value provided during an update gets replaced with the current time if the
            provided value is the same as the old one and the new effect is different. Changing the key and/or
            value while keeping the effect unchanged is possible and does not update the time stamp because
            the eviction which uses it is either already started (NoExecute) or not started yet (NoEffect,
            NoSchedule).
        value: The taint value corresponding to the taint key. Must be a label value.

    """

    key: str
    effect: str
    timeAdded: Optional[str] = None
    value: Optional[str] = None


@dataclass
class DeviceTaintRule(K8sResource):
    """DeviceTaintRule adds one taint to all devices which match the selector. This has the same effect as if
    the taint was specified directly in the ResourceSlice by the DRA driver.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object metadata
        spec: Spec specifies the selector and one taint.  Changing the spec automatically increments the
            metadata.generation number.
        status: Status provides information about what was requested in the spec.

    """

    spec: DeviceTaintRuleSpec
    apiVersion: Literal['resource.k8s.io/v1alpha3'] = 'resource.k8s.io/v1alpha3'
    kind: Literal['DeviceTaintRule'] = 'DeviceTaintRule'
    metadata: Optional[_meta_v1.ObjectMeta] = None
    status: Optional[DeviceTaintRuleStatus] = None


@dataclass
class DeviceTaintRuleSpec(K8sSpec):
    """DeviceTaintRuleSpec specifies the selector and one taint.

    Attributes:
        deviceSelector: DeviceSelector defines which device(s) the taint is applied to. All selector criteria
            must be satisfied for a device to match. The empty selector matches all devices. Without a
            selector, no devices are matches.
        taint: The taint that gets applied to matching devices.

    """

    taint: DeviceTaint
    deviceSelector: Optional[DeviceTaintSelector] = None


@dataclass
class DeviceTaintRuleStatus(K8sSpec):
    """DeviceTaintRuleStatus provides information about an on-going pod eviction.

    Attributes:
        conditions: Conditions provide information about the state of the DeviceTaintRule and the cluster at
            some point in time, in a machine-readable and human-readable format.  The following condition is
            currently defined as part of this API, more may get added: - Type: EvictionInProgress - Status:
            True if there are currently pods which need to be evicted, False otherwise   (includes the effects
            which don't cause eviction). - Reason: not specified, may change - Message: includes information
            about number of pending pods and already evicted pods   in a human-readable format, updated
            periodically, may change  For `effect: None`, the condition above gets set once for each change to
            the spec, with the message containing information about what would happen if the effect was
            `NoExecute`. This feedback can be used to decide whether changing the effect to `NoExecute` will
            work as intended. It only gets set once to avoid having to constantly update the status.  Must
            have 8 or fewer entries.

    """

    conditions: Optional[List[_meta_v1.Condition]] = None


@dataclass
class DeviceTaintSelector(K8sSpec):
    """DeviceTaintSelector defines which device(s) a DeviceTaintRule applies to. The empty selector matches
    all devices. Without a selector, no devices are matched.

    Attributes:
        device: If device is set, only devices with that name are selected. This field corresponds to
            slice.spec.devices[].name.  Setting also driver and pool may be required to avoid ambiguity, but
            is not required.
        driver: If driver is set, only devices from that driver are selected. This fields corresponds to
            slice.spec.driver.
        pool: If pool is set, only devices in that pool are selected.  Also setting the driver name may be
            useful to avoid ambiguity when different drivers use the same pool name, but this is not required
            because selecting pools from different drivers may also be useful, for example when drivers with
            node-local devices use the node name as their pool name.

    """

    device: Optional[str] = None
    driver: Optional[str] = None
    pool: Optional[str] = None


@dataclass
class PartitionTypeStatus(K8sSpec):
    """PartitionTypeStatus reports allocatability for a single partition type, identified by the value of a
    grouping attribute.

    Attributes:
        allocatable: Allocatable is the number of additional devices of this partition type that could still
            be allocated given current shared-counter consumption.
        attribute: Attribute is the fully qualified name of the device attribute whose value groups this
            entry. It is the PartitionTypeAttribute declared by the devices' own slice, or the default named
            in the request when their slice declares none.
        total: Total is the number of devices of this partition type in the pool.
        type: Type is the partition type value (e.g. 'Full' or 'Half').

    """

    attribute: str
    type: str
    total: int
    allocatable: int


@dataclass
class PoolStatus(K8sSpec):
    """PoolStatus contains status information for a single resource pool.

    Attributes:
        allocatedDevices: AllocatedDevices is the number of devices currently allocated to claims. A value of
            0 means no devices are allocated. May be unset when validationError is set.
        availableDevices: AvailableDevices is the number of devices available for allocation. This equals
            TotalDevices - AllocatedDevices - UnavailableDevices. A value of 0 means no devices are currently
            available. May be unset when validationError is set.
        driver: Driver is the DRA driver name for this pool. Must be a DNS subdomain (e.g.,
            'gpu.example.com').
        generation: Generation is the pool generation observed across all ResourceSlices in this pool. Only
            the latest generation is reported. During a generation rollout, if not all slices at the latest
            generation have been published, the pool is included with a validationError and device counts
            unset.
        nodeName: NodeName is the node this pool is associated with. When omitted, the pool is not associated
            with a specific node. Must be a valid DNS subdomain name (RFC1123).
        partitionSummary: PartitionSummary reports allocatability per (attribute, partition type) for a
            partitionable pool that publishes SharedCounters. Each entry names the grouping attribute it was
            resolved from: the PartitionTypeAttribute declared by a device's own slice, or for devices whose
            slice declares none, the default named in the request. A pool that mixes partitions declared under
            different attributes reports each independently. When no slice declares an attribute and the
            request names no default, the pool reports no partition summary.
        poolName: PoolName is the name of the pool. Must be a valid resource pool name (DNS subdomains
            separated by '/').
        resourceSliceCount: ResourceSliceCount is the number of ResourceSlices that make up this pool. May be
            unset when validationError is set.
        shareableSummary: ShareableSummary reports aggregate capacity for a pool that contains devices with
            AllowMultipleAllocations. It is populated only when at least one device in the pool is shareable.
        totalDevices: TotalDevices is the total number of devices in the pool across all slices. A value of 0
            means the pool has no devices. May be unset when validationError is set.
        unavailableDevices: UnavailableDevices is the number of devices that are not available due to taints
            or other conditions, but are not allocated. A value of 0 means all unallocated devices are
            available. May be unset when validationError is set.
        validationError: ValidationError is set when the pool's data could not be fully validated (e.g.,
            incomplete slice publication). When set, device count fields and ResourceSliceCount may be unset.

    """

    driver: str
    poolName: str
    generation: int
    allocatedDevices: Optional[int] = None
    availableDevices: Optional[int] = None
    nodeName: Optional[str] = None
    partitionSummary: Optional[List[PartitionTypeStatus]] = None
    resourceSliceCount: Optional[int] = None
    shareableSummary: Optional[ShareableSummaryStatus] = None
    totalDevices: Optional[int] = None
    unavailableDevices: Optional[int] = None
    validationError: Optional[str] = None


@dataclass
class ResourcePoolStatusRequest(K8sResource):
    """ResourcePoolStatusRequest triggers a one-time calculation of resource pool status based on the
    provided filters. Once status is set, the request is considered complete and will not be reprocessed.
    Users should delete and recreate requests to get updated information.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object metadata
        spec: Spec defines the filters for which pools to include in the status. The spec is immutable once
            created.
        status: Status is populated by the controller with the calculated pool status. When status is non-nil,
            the request is considered complete and the entire object becomes immutable.

    """

    metadata: _meta_v1.ObjectMeta
    spec: ResourcePoolStatusRequestSpec
    apiVersion: Literal['resource.k8s.io/v1alpha3'] = 'resource.k8s.io/v1alpha3'
    kind: Literal['ResourcePoolStatusRequest'] = 'ResourcePoolStatusRequest'
    status: Optional[ResourcePoolStatusRequestStatus] = None


@dataclass
class ResourcePoolStatusRequestSpec(K8sSpec):
    """ResourcePoolStatusRequestSpec defines the filters for the pool status request.

    Attributes:
        defaultPartitionTypeAttribute: DefaultPartitionTypeAttribute optionally names a device attribute (by
            its fully qualified name, e.g. 'gpu.example.com/profile') to use as the default grouping attribute
            for partitionable devices whose slice has not declared one themselves.  A slice's own
            PartitionTypeAttribute always takes precedence. This default applies only to devices whose slice
            does not declare one, so that a request can still get an accurate partitionSummary from a driver
            that has not been updated to declare it. When neither the slice nor this default names an
            attribute, a partitionable pool reports no partitionSummary.  Must include the domain qualifier.
        driver: Driver specifies the DRA driver name to filter pools. Only pools from ResourceSlices with this
            driver will be included. Must be a DNS subdomain (e.g., 'gpu.example.com').
        limit: Limit optionally specifies the maximum number of pools to return in the status. If more pools
            match the filter criteria, the response will be truncated (i.e., len(status.pools) <
            status.poolCount).  Default: 100 Minimum: 1 Maximum: 1000
        poolName: PoolName optionally filters to a specific pool name. If not specified, all pools from the
            specified driver are included. When specified, must be a non-empty valid resource pool name (DNS
            subdomains separated by '/').

    """

    driver: str
    defaultPartitionTypeAttribute: Optional[str] = None
    limit: Optional[int] = None
    poolName: Optional[str] = None


@dataclass
class ResourcePoolStatusRequestStatus(K8sSpec):
    """ResourcePoolStatusRequestStatus contains the calculated pool status information.

    Attributes:
        conditions: Conditions provide information about the state of the request. A condition with
            type=Complete or type=Failed will always be set when the status is populated.  Known condition
            types: - 'Complete': True when the request has been processed successfully - 'Failed': True when
            the request could not be processed
        poolCount: PoolCount is the total number of pools that matched the filter criteria, regardless of
            truncation. This helps users understand how many pools exist even when the response is truncated.
            A value of 0 means no pools matched the filter criteria.
        pools: Pools contains the first `spec.limit` matching pools, sorted by driver then pool name. If
            `len(pools) < poolCount`, the list was truncated. When omitted, no pools matched the request
            filters.

    """

    poolCount: int
    conditions: Optional[List[_meta_v1.Condition]] = None
    pools: Optional[List[PoolStatus]] = None


@dataclass
class ShareableCapacityStatus(K8sSpec):
    """ShareableCapacityStatus reports aggregate amounts for a single shareable capacity key.

    Attributes:
        available: Available is Total minus Consumed, never negative.
        consumed: Consumed is the amount drawn by current allocations.
        name: Name is the capacity name.
        total: Total is the sum of this capacity across shareable devices in the pool.

    """

    name: str
    total: _api_resource.Quantity
    consumed: _api_resource.Quantity
    available: _api_resource.Quantity


@dataclass
class ShareableSummaryStatus(K8sSpec):
    """ShareableSummaryStatus reports aggregate capacity for a pool that contains devices with
    AllowMultipleAllocations.

    Attributes:
        capacity: Capacity reports aggregate total, consumed, and available amounts per shareable capacity key
            across the pool.
        fullyAvailableDevices: FullyAvailableDevices is the number of shareable devices with no capacity
            consumed.
        partiallyAvailableDevices: PartiallyAvailableDevices is the number of shareable devices with some but
            not all capacity consumed.

    """

    fullyAvailableDevices: int
    partiallyAvailableDevices: int
    capacity: Optional[List[ShareableCapacityStatus]] = None
