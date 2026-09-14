"""Models generated from Kubernetes OpenAPI Spec."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Literal, Optional

import gybe.k8s.v1_35.meta.v1 as _meta_v1
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
