from __future__ import annotations
from typing import Dict, List, Optional
from pydantic import BaseModel, Field
from ...apimachinery.pkg.api import resource
from ...apimachinery.pkg.apis.meta import v1 as v1_1
from ..core import v1


class Scheduling(BaseModel):
    nodeSelector: Optional[Dict[str, str]] = Field(
        None,
        description=(
            "nodeSelector lists labels that must be present on nodes that support this"
            " RuntimeClass. Pods using this RuntimeClass can only be scheduled to a"
            " node matched by this selector. The RuntimeClass nodeSelector is merged"
            " with a pod's existing nodeSelector. Any conflicts will cause the pod to"
            " be rejected in admission."
        ),
    )
    tolerations: Optional[List[v1.Toleration]] = Field(
        None,
        description=(
            "tolerations are appended (excluding duplicates) to pods running with this"
            " RuntimeClass during admission, effectively unioning the set of nodes"
            " tolerated by the pod and the RuntimeClass."
        ),
    )


class Overhead(BaseModel):
    podFixed: Optional[Dict[str, resource.Quantity]] = Field(
        None,
        description=(
            "PodFixed represents the fixed resource overhead associated with running a"
            " pod."
        ),
    )


class RuntimeClass(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description=(
            "APIVersion defines the versioned schema of this representation of an"
            " object. Servers should convert recognized schemas to the latest internal"
            " value, and may reject unrecognized values. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources"
        ),
    )
    handler: str = Field(
        ...,
        description=(
            "Handler specifies the underlying runtime and configuration that the CRI"
            " implementation will use to handle pods of this class. The possible values"
            " are specific to the node & CRI configuration.  It is assumed that all"
            " handlers are available on every node, and handlers of the same name are"
            ' equivalent on every node. For example, a handler called "runc" might'
            " specify that the runc OCI runtime (using native Linux containers) will be"
            " used to run the containers in a pod. The Handler must be lowercase,"
            " conform to the DNS Label (RFC 1123) requirements, and is immutable."
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
            "More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata"
        ),
    )
    overhead: Optional[Overhead] = Field(
        None,
        description=(
            "Overhead represents the resource overhead associated with running a pod"
            " for a given RuntimeClass. For more details, see\n"
            " https://kubernetes.io/docs/concepts/scheduling-eviction/pod-overhead/"
        ),
    )
    scheduling: Optional[Scheduling] = Field(
        None,
        description=(
            "Scheduling holds the scheduling constraints to ensure that pods running"
            " with this RuntimeClass are scheduled to nodes that support it. If"
            " scheduling is nil, this RuntimeClass is assumed to be supported by all"
            " nodes."
        ),
    )


class RuntimeClassList(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description=(
            "APIVersion defines the versioned schema of this representation of an"
            " object. Servers should convert recognized schemas to the latest internal"
            " value, and may reject unrecognized values. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources"
        ),
    )
    items: List[RuntimeClass] = Field(
        ..., description="Items is a list of schema objects."
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
            "Standard list metadata. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata"
        ),
    )
