"""Models generated from Kubernetes OpenAPI Spec."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Literal, Optional

import gybe.k8s.v1_30.meta.v1
from gybe.k8s.types import JSONObj, K8sResource, K8sSpec


@dataclass
class IPAddress(K8sSpec):
    """IPAddress represents a single IP of a single IP Family. The object is designed to be used by APIs that
    operate on IP addresses. The object is used by the Service core API for allocation of IP addresses. An
    IP address can be represented in different formats, to guarantee the uniqueness of the IP, the name of
    the object is the IP address in canonical format, four decimal digits separated by dots suppressing
    leading zeros for IPv4 and the representation defined by RFC 5952 for IPv6. Valid: 192.168.1.5 or
    2001:db8::1 or 2001:db8:aaaa:bbbb:cccc:dddd:eeee:1 Invalid: 10.01.2.3 or 2001:db8:0:0:0::1
    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object's metadata.
        spec: spec is the desired state of the IPAddress.

    """

    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[gybe.k8s.v1_30.meta.v1.ObjectMeta] = None
    spec: Optional[IPAddressSpec] = None


@dataclass
class IPAddressList(K8sSpec):
    """IPAddressList contains a list of IPAddress.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        items: items is the list of IPAddresses.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object's metadata.

    """

    items: List[IPAddress]
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[JSONObj] = None


@dataclass
class IPAddressSpec(K8sSpec):
    """IPAddressSpec describe the attributes in an IP Address.

    Attributes:
        parentRef: ParentRef references the resource that an IPAddress is attached to. An IPAddress must
            reference a parent object.

    """

    parentRef: ParentReference


@dataclass
class ParentReference(K8sSpec):
    """ParentReference describes a reference to a parent object.

    Attributes:
        group: Group is the group of the object being referenced.
        name: Name is the name of the object being referenced.
        namespace: Namespace is the namespace of the object being referenced.
        resource: Resource is the resource of the object being referenced.

    """

    resource: str
    name: str
    group: Optional[str] = None
    namespace: Optional[str] = None


@dataclass
class ServiceCIDR(K8sResource):
    """ServiceCIDR defines a range of IP addresses using CIDR format (e.g. 192.168.0.0/24 or 2001:db2::/64).
    This range is used to allocate ClusterIPs to Service objects.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object's metadata.
        spec: spec is the desired state of the ServiceCIDR.
        status: status represents the current state of the ServiceCIDR.

    """

    apiVersion: Literal['networking.k8s.io/v1alpha1'] = 'networking.k8s.io/v1alpha1'
    kind: Literal['ServiceCIDR'] = 'ServiceCIDR'
    metadata: Optional[gybe.k8s.v1_30.meta.v1.ObjectMeta] = None
    spec: Optional[ServiceCIDRSpec] = None
    status: Optional[ServiceCIDRStatus] = None


@dataclass
class ServiceCIDRList(K8sSpec):
    """ServiceCIDRList contains a list of ServiceCIDR objects.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        items: items is the list of ServiceCIDRs.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object's metadata.

    """

    items: List[ServiceCIDR]
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[JSONObj] = None


@dataclass
class ServiceCIDRSpec(K8sSpec):
    """ServiceCIDRSpec define the CIDRs the user wants to use for allocating ClusterIPs for Services.

    Attributes:
        cidrs: CIDRs defines the IP blocks in CIDR notation (e.g. '192.168.0.0/24' or '2001:db8::/64') from
            which to assign service cluster IPs. Max of two CIDRs is allowed, one of each IP family. This
            field is immutable.

    """

    cidrs: Optional[List[str]] = None


@dataclass
class ServiceCIDRStatus(K8sSpec):
    """ServiceCIDRStatus describes the current state of the ServiceCIDR.

    Attributes:
        conditions: conditions holds an array of metav1.Condition that describe the state of the ServiceCIDR.
            Current service state

    """

    conditions: Optional[List[gybe.k8s.v1_30.meta.v1.Condition]] = None
