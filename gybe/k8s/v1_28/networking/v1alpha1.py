"""Models generated from Kubernetes OpenAPI Spec."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

import gybe.k8s.v1_28.core.v1
import gybe.k8s.v1_28.meta.v1
from gybe.k8s.types import JSONObj, K8sSpec


@dataclass
class ClusterCIDR(K8sSpec):
    """ClusterCIDR represents a single configuration for per-Node Pod CIDR allocations when the
    MultiCIDRRangeAllocator is enabled (see the config for kube-controller-manager).  A cluster may have
    any number of ClusterCIDR resources, all of which will be considered when allocating a CIDR for a
    Node.  A ClusterCIDR is eligible to be used for a given Node when the node selector matches the node
    in question and has free CIDRs to allocate.  In case of multiple matching ClusterCIDR resources, the
    allocator will attempt to break ties using internal heuristics, but any ClusterCIDR whose node
    selector matches the Node may be used.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object's metadata.
        spec: spec is the desired state of the ClusterCIDR.

    """

    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[gybe.k8s.v1_28.meta.v1.ObjectMeta] = None
    spec: Optional[ClusterCIDRSpec] = None


@dataclass
class ClusterCIDRList(K8sSpec):
    """ClusterCIDRList contains a list of ClusterCIDR.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        items: items is the list of ClusterCIDRs.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object's metadata.

    """

    items: List[ClusterCIDR]
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[JSONObj] = None


@dataclass
class ClusterCIDRSpec(K8sSpec):
    """ClusterCIDRSpec defines the desired state of ClusterCIDR.

    Attributes:
        ipv4: ipv4 defines an IPv4 IP block in CIDR notation(e.g. '10.0.0.0/8'). At least one of ipv4 and ipv6
            must be specified. This field is immutable.
        ipv6: ipv6 defines an IPv6 IP block in CIDR notation(e.g. '2001:db8::/64'). At least one of ipv4 and
            ipv6 must be specified. This field is immutable.
        nodeSelector: nodeSelector defines which nodes the config is applicable to. An empty or nil
            nodeSelector selects all nodes. This field is immutable.
        perNodeHostBits: perNodeHostBits defines the number of host bits to be configured per node. A subnet
            mask determines how much of the address is used for network bits and host bits. For example an
            IPv4 address of 192.168.0.0/24, splits the address into 24 bits for the network portion and 8 bits
            for the host portion. To allocate 256 IPs, set this field to 8 (a /24 mask for IPv4 or a /120 for
            IPv6). Minimum value is 4 (16 IPs). This field is immutable.

    """

    perNodeHostBits: int
    ipv4: Optional[str] = None
    ipv6: Optional[str] = None
    nodeSelector: Optional[gybe.k8s.v1_28.core.v1.NodeSelector] = None


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
    metadata: Optional[gybe.k8s.v1_28.meta.v1.ObjectMeta] = None
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

    parentRef: Optional[ParentReference] = None


@dataclass
class ParentReference(K8sSpec):
    """ParentReference describes a reference to a parent object.

    Attributes:
        group: Group is the group of the object being referenced.
        name: Name is the name of the object being referenced.
        namespace: Namespace is the namespace of the object being referenced.
        resource: Resource is the resource of the object being referenced.
        uid: UID is the uid of the object being referenced.

    """

    group: Optional[str] = None
    name: Optional[str] = None
    namespace: Optional[str] = None
    resource: Optional[str] = None
    uid: Optional[str] = None
