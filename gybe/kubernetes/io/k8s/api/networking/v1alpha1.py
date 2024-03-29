from __future__ import annotations
from typing import List, Optional
from pydantic import BaseModel, Field
from ...apimachinery.pkg.apis.meta import v1 as v1_1
from ..core import v1


class ParentReference(BaseModel):
    group: Optional[str] = Field(
        None, description="Group is the group of the object being referenced."
    )
    name: Optional[str] = Field(
        None, description="Name is the name of the object being referenced."
    )
    namespace: Optional[str] = Field(
        None, description="Namespace is the namespace of the object being referenced."
    )
    resource: Optional[str] = Field(
        None, description="Resource is the resource of the object being referenced."
    )
    uid: Optional[str] = Field(
        None, description="UID is the uid of the object being referenced."
    )


class ClusterCIDRSpec(BaseModel):
    ipv4: Optional[str] = Field(
        "",
        description=(
            'ipv4 defines an IPv4 IP block in CIDR notation(e.g. "10.0.0.0/8"). At'
            " least one of ipv4 and ipv6 must be specified. This field is immutable."
        ),
    )
    ipv6: Optional[str] = Field(
        "",
        description=(
            'ipv6 defines an IPv6 IP block in CIDR notation(e.g. "2001:db8::/64"). At'
            " least one of ipv4 and ipv6 must be specified. This field is immutable."
        ),
    )
    nodeSelector: Optional[v1.NodeSelector] = Field(
        None,
        description=(
            "nodeSelector defines which nodes the config is applicable to. An empty or"
            " nil nodeSelector selects all nodes. This field is immutable."
        ),
    )
    perNodeHostBits: int = Field(
        ...,
        description=(
            "perNodeHostBits defines the number of host bits to be configured per node."
            " A subnet mask determines how much of the address is used for network bits"
            " and host bits. For example an IPv4 address of 192.168.0.0/24, splits the"
            " address into 24 bits for the network portion and 8 bits for the host"
            " portion. To allocate 256 IPs, set this field to 8 (a /24 mask for IPv4 or"
            " a /120 for IPv6). Minimum value is 4 (16 IPs). This field is immutable."
        ),
    )


class IPAddressSpec(BaseModel):
    parentRef: Optional[ParentReference] = Field(
        None,
        description=(
            "ParentRef references the resource that an IPAddress is attached to. An"
            " IPAddress must reference a parent object."
        ),
    )


class ClusterCIDR(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description=(
            "APIVersion defines the versioned schema of this representation of an"
            " object. Servers should convert recognized schemas to the latest internal"
            " value, and may reject unrecognized values. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources"
        ),
    )
    kind: Optional[str] = Field(
        None,
        description=(
            "Kind is a string value representing the REST resource this object"
            " represents. Servers may infer this from the endpoint the client submits"
            " requests to. Cannot be updated. In CamelCase. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"
        ),
    )
    metadata: Optional[v1_1.ObjectMeta] = Field(
        None,
        description=(
            "Standard object's metadata. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata"
        ),
    )
    spec: Optional[ClusterCIDRSpec] = Field(
        None,
        description=(
            "spec is the desired state of the ClusterCIDR. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status"
        ),
    )


class ClusterCIDRList(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description=(
            "APIVersion defines the versioned schema of this representation of an"
            " object. Servers should convert recognized schemas to the latest internal"
            " value, and may reject unrecognized values. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources"
        ),
    )
    items: List[ClusterCIDR] = Field(
        ..., description="items is the list of ClusterCIDRs."
    )
    kind: Optional[str] = Field(
        None,
        description=(
            "Kind is a string value representing the REST resource this object"
            " represents. Servers may infer this from the endpoint the client submits"
            " requests to. Cannot be updated. In CamelCase. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"
        ),
    )
    metadata: Optional[v1_1.ListMeta] = Field(
        None,
        description=(
            "Standard object's metadata. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata"
        ),
    )


class IPAddress(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description=(
            "APIVersion defines the versioned schema of this representation of an"
            " object. Servers should convert recognized schemas to the latest internal"
            " value, and may reject unrecognized values. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources"
        ),
    )
    kind: Optional[str] = Field(
        None,
        description=(
            "Kind is a string value representing the REST resource this object"
            " represents. Servers may infer this from the endpoint the client submits"
            " requests to. Cannot be updated. In CamelCase. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"
        ),
    )
    metadata: Optional[v1_1.ObjectMeta] = Field(
        None,
        description=(
            "Standard object's metadata. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata"
        ),
    )
    spec: Optional[IPAddressSpec] = Field(
        None,
        description=(
            "spec is the desired state of the IPAddress. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status"
        ),
    )


class IPAddressList(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description=(
            "APIVersion defines the versioned schema of this representation of an"
            " object. Servers should convert recognized schemas to the latest internal"
            " value, and may reject unrecognized values. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources"
        ),
    )
    items: List[IPAddress] = Field(..., description="items is the list of IPAddresses.")
    kind: Optional[str] = Field(
        None,
        description=(
            "Kind is a string value representing the REST resource this object"
            " represents. Servers may infer this from the endpoint the client submits"
            " requests to. Cannot be updated. In CamelCase. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"
        ),
    )
    metadata: Optional[v1_1.ListMeta] = Field(
        None,
        description=(
            "Standard object's metadata. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata"
        ),
    )
