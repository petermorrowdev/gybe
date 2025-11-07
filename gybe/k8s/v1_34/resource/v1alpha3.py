"""Models generated from Kubernetes OpenAPI Spec."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Literal, Optional

import gybe.k8s.v1_34.meta.v1
from gybe.k8s.types import K8sResource, K8sSpec


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
            cel.bind(dra, device.attributes['dra.example.com'], dra.someBool && dra.anotherBool)  The length
            of the expression must be smaller or equal to 10 Ki. The cost of evaluating it is also limited
            based on the estimated number of logical steps.

    """

    expression: str


@dataclass
class DeviceSelector(K8sSpec):
    """DeviceSelector must have exactly one field set.

    Attributes:
        cel: CEL contains a CEL expression for selecting a device.

    """

    cel: Optional[CELDeviceSelector] = None


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

    """

    spec: DeviceTaintRuleSpec
    apiVersion: Literal['resource.k8s.io/v1alpha3'] = 'resource.k8s.io/v1alpha3'
    kind: Literal['DeviceTaintRule'] = 'DeviceTaintRule'
    metadata: Optional[gybe.k8s.v1_34.meta.v1.ObjectMeta] = None


@dataclass
class DeviceTaintRuleSpec(K8sSpec):
    """DeviceTaintRuleSpec specifies the selector and one taint.

    Attributes:
        deviceSelector: DeviceSelector defines which device(s) the taint is applied to. All selector criteria
            must be satified for a device to match. The empty selector matches all devices. Without a
            selector, no devices are matches.
        taint: The taint that gets applied to matching devices.

    """

    taint: DeviceTaint
    deviceSelector: Optional[DeviceTaintSelector] = None


@dataclass
class DeviceTaintSelector(K8sSpec):
    """DeviceTaintSelector defines which device(s) a DeviceTaintRule applies to. The empty selector matches
    all devices. Without a selector, no devices are matched.

    Attributes:
        device: If device is set, only devices with that name are selected. This field corresponds to
            slice.spec.devices[].name.  Setting also driver and pool may be required to avoid ambiguity, but
            is not required.
        deviceClassName: If DeviceClassName is set, the selectors defined there must be satisfied by a device
            to be selected. This field corresponds to class.metadata.name.
        driver: If driver is set, only devices from that driver are selected. This fields corresponds to
            slice.spec.driver.
        pool: If pool is set, only devices in that pool are selected.  Also setting the driver name may be
            useful to avoid ambiguity when different drivers use the same pool name, but this is not required
            because selecting pools from different drivers may also be useful, for example when drivers with
            node-local devices use the node name as their pool name.
        selectors: Selectors contains the same selection criteria as a ResourceClaim. Currently, CEL
            expressions are supported. All of these selectors must be satisfied.

    """

    device: Optional[str] = None
    deviceClassName: Optional[str] = None
    driver: Optional[str] = None
    pool: Optional[str] = None
    selectors: Optional[List[DeviceSelector]] = None
