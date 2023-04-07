from __future__ import annotations
from typing import List, Optional
from pydantic import BaseModel, Field
from ...apimachinery.pkg.apis.meta import v1 as v1_1
from ..core import v1


class PodSchedulingContextSpec(BaseModel):
    potentialNodes: Optional[List[str]] = Field(
        None,
        description=(
            "PotentialNodes lists nodes where the Pod might be able to run.\n\nThe size"
            " of this field is limited to 128. This is large enough for many clusters."
            " Larger clusters may need more attempts to find a node that suits all"
            " pending resources. This may get increased in the future, but not reduced."
        ),
    )
    selectedNode: Optional[str] = Field(
        None,
        description=(
            "SelectedNode is the node for which allocation of ResourceClaims that are"
            ' referenced by the Pod and that use "WaitForFirstConsumer" allocation is'
            " to be attempted."
        ),
    )


class ResourceClaimConsumerReference(BaseModel):
    apiGroup: Optional[str] = Field(
        None,
        description=(
            "APIGroup is the group for the resource being referenced. It is empty for"
            " the core API. This matches the group in the APIVersion that is used when"
            " creating the resources."
        ),
    )
    name: str = Field(..., description="Name is the name of resource being referenced.")
    resource: str = Field(
        ...,
        description=(
            'Resource is the type of resource being referenced, for example "pods".'
        ),
    )
    uid: str = Field(
        ..., description="UID identifies exactly one incarnation of the resource."
    )


class ResourceClaimParametersReference(BaseModel):
    apiGroup: Optional[str] = Field(
        None,
        description=(
            "APIGroup is the group for the resource being referenced. It is empty for"
            " the core API. This matches the group in the APIVersion that is used when"
            " creating the resources."
        ),
    )
    kind: str = Field(
        ...,
        description=(
            "Kind is the type of resource being referenced. This is the same value as"
            ' in the parameter object\'s metadata, for example "ConfigMap".'
        ),
    )
    name: str = Field(..., description="Name is the name of resource being referenced.")


class ResourceClaimSchedulingStatus(BaseModel):
    name: Optional[str] = Field(
        None, description="Name matches the pod.spec.resourceClaims[*].Name field."
    )
    unsuitableNodes: Optional[List[str]] = Field(
        None,
        description=(
            "UnsuitableNodes lists nodes that the ResourceClaim cannot be allocated"
            " for.\n\nThe size of this field is limited to 128, the same as for"
            " PodSchedulingSpec.PotentialNodes. This may get increased in the future,"
            " but not reduced."
        ),
    )


class ResourceClaimSpec(BaseModel):
    allocationMode: Optional[str] = Field(
        None,
        description=(
            "Allocation can start immediately or when a Pod wants to use the resource."
            ' "WaitForFirstConsumer" is the default.'
        ),
    )
    parametersRef: Optional[ResourceClaimParametersReference] = Field(
        None,
        description=(
            "ParametersRef references a separate object with arbitrary parameters that"
            " will be used by the driver when allocating a resource for the"
            " claim.\n\nThe object must be in the same namespace as the ResourceClaim."
        ),
    )
    resourceClassName: str = Field(
        ...,
        description=(
            "ResourceClassName references the driver and additional parameters via the"
            " name of a ResourceClass that was created as part of the driver"
            " deployment."
        ),
    )


class ResourceClassParametersReference(BaseModel):
    apiGroup: Optional[str] = Field(
        None,
        description=(
            "APIGroup is the group for the resource being referenced. It is empty for"
            " the core API. This matches the group in the APIVersion that is used when"
            " creating the resources."
        ),
    )
    kind: str = Field(
        ...,
        description=(
            "Kind is the type of resource being referenced. This is the same value as"
            " in the parameter object's metadata."
        ),
    )
    name: str = Field(..., description="Name is the name of resource being referenced.")
    namespace: Optional[str] = Field(
        None,
        description=(
            "Namespace that contains the referenced resource. Must be empty for"
            " cluster-scoped resources and non-empty for namespaced resources."
        ),
    )


class ResourceHandle(BaseModel):
    data: Optional[str] = Field(
        None,
        description=(
            "Data contains the opaque data associated with this ResourceHandle. It is"
            " set by the controller component of the resource driver whose name matches"
            " the DriverName set in the ResourceClaimStatus this ResourceHandle is"
            " embedded in. It is set at allocation time and is intended for processing"
            " by the kubelet plugin whose name matches the DriverName set in this"
            " ResourceHandle.\n\nThe maximum size of this field is 16KiB. This may get"
            " increased in the future, but not reduced."
        ),
    )
    driverName: Optional[str] = Field(
        None,
        description=(
            "DriverName specifies the name of the resource driver whose kubelet plugin"
            " should be invoked to process this ResourceHandle's data once it lands on"
            " a node. This may differ from the DriverName set in ResourceClaimStatus"
            " this ResourceHandle is embedded in."
        ),
    )


class AllocationResult(BaseModel):
    availableOnNodes: Optional[v1.NodeSelector] = Field(
        None,
        description=(
            "This field will get set by the resource driver after it has allocated the"
            " resource to inform the scheduler where it can schedule Pods using the"
            " ResourceClaim.\n\nSetting this field is optional. If null, the resource"
            " is available everywhere."
        ),
    )
    resourceHandles: Optional[List[ResourceHandle]] = Field(
        None,
        description=(
            "ResourceHandles contain the state associated with an allocation that"
            " should be maintained throughout the lifetime of a claim. Each"
            " ResourceHandle contains data that should be passed to a specific kubelet"
            " plugin once it lands on a node. This data is returned by the driver after"
            " a successful allocation and is opaque to Kubernetes. Driver documentation"
            " may explain to users how to interpret this data if needed.\n\nSetting"
            " this field is optional. It has a maximum size of 32 entries. If null (or"
            " empty), it is assumed this allocation will be processed by a single"
            " kubelet plugin with no ResourceHandle data attached. The name of the"
            " kubelet plugin invoked will match the DriverName set in the"
            " ResourceClaimStatus this AllocationResult is embedded in."
        ),
    )
    shareable: Optional[bool] = Field(
        None,
        description=(
            "Shareable determines whether the resource supports more than one consumer"
            " at a time."
        ),
    )


class PodSchedulingContextStatus(BaseModel):
    resourceClaims: Optional[List[ResourceClaimSchedulingStatus]] = Field(
        None,
        description=(
            "ResourceClaims describes resource availability for each"
            " pod.spec.resourceClaim entry where the corresponding ResourceClaim uses"
            ' "WaitForFirstConsumer" allocation mode.'
        ),
    )


class ResourceClaimStatus(BaseModel):
    allocation: Optional[AllocationResult] = Field(
        None,
        description=(
            "Allocation is set by the resource driver once a resource or set of"
            " resources has been allocated successfully. If this is not specified, the"
            " resources have not been allocated yet."
        ),
    )
    deallocationRequested: Optional[bool] = Field(
        None,
        description=(
            "DeallocationRequested indicates that a ResourceClaim is to be"
            " deallocated.\n\nThe driver then must deallocate this claim and reset the"
            " field together with clearing the Allocation field.\n\nWhile"
            " DeallocationRequested is set, no new consumers may be added to"
            " ReservedFor."
        ),
    )
    driverName: Optional[str] = Field(
        None,
        description=(
            "DriverName is a copy of the driver name from the ResourceClass at the time"
            " when allocation started."
        ),
    )
    reservedFor: Optional[List[ResourceClaimConsumerReference]] = Field(
        None,
        description=(
            "ReservedFor indicates which entities are currently allowed to use the"
            " claim. A Pod which references a ResourceClaim which is not reserved for"
            " that Pod will not be started.\n\nThere can be at most 32 such"
            " reservations. This may get increased in the future, but not reduced."
        ),
    )


class PodSchedulingContext(BaseModel):
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
        None, description="Standard object metadata"
    )
    spec: PodSchedulingContextSpec = Field(
        ..., description="Spec describes where resources for the Pod are needed."
    )
    status: Optional[PodSchedulingContextStatus] = Field(
        None,
        description="Status describes where resources for the Pod can be allocated.",
    )


class PodSchedulingContextList(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description=(
            "APIVersion defines the versioned schema of this representation of an"
            " object. Servers should convert recognized schemas to the latest internal"
            " value, and may reject unrecognized values. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources"
        ),
    )
    items: List[PodSchedulingContext] = Field(
        ..., description="Items is the list of PodSchedulingContext objects."
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
        None, description="Standard list metadata"
    )


class ResourceClaim(BaseModel):
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
        None, description="Standard object metadata"
    )
    spec: ResourceClaimSpec = Field(
        ...,
        description=(
            "Spec describes the desired attributes of a resource that then needs to be"
            " allocated. It can only be set once when creating the ResourceClaim."
        ),
    )
    status: Optional[ResourceClaimStatus] = Field(
        None,
        description=(
            "Status describes whether the resource is available and with which"
            " attributes."
        ),
    )


class ResourceClaimList(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description=(
            "APIVersion defines the versioned schema of this representation of an"
            " object. Servers should convert recognized schemas to the latest internal"
            " value, and may reject unrecognized values. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources"
        ),
    )
    items: List[ResourceClaim] = Field(
        ..., description="Items is the list of resource claims."
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
        None, description="Standard list metadata"
    )


class ResourceClaimTemplateSpec(BaseModel):
    metadata: Optional[v1_1.ObjectMeta] = Field(
        None,
        description=(
            "ObjectMeta may contain labels and annotations that will be copied into the"
            " PVC when creating it. No other fields are allowed and will be rejected"
            " during validation."
        ),
    )
    spec: ResourceClaimSpec = Field(
        ...,
        description=(
            "Spec for the ResourceClaim. The entire content is copied unchanged into"
            " the ResourceClaim that gets created from this template. The same fields"
            " as in a ResourceClaim are also valid here."
        ),
    )


class ResourceClass(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description=(
            "APIVersion defines the versioned schema of this representation of an"
            " object. Servers should convert recognized schemas to the latest internal"
            " value, and may reject unrecognized values. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources"
        ),
    )
    driverName: str = Field(
        ...,
        description=(
            "DriverName defines the name of the dynamic resource driver that is used"
            " for allocation of a ResourceClaim that uses this class.\n\nResource"
            " drivers have a unique name in forward domain order (acme.example.com)."
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
        None, description="Standard object metadata"
    )
    parametersRef: Optional[ResourceClassParametersReference] = Field(
        None,
        description=(
            "ParametersRef references an arbitrary separate object that may hold"
            " parameters that will be used by the driver when allocating a resource"
            " that uses this class. A dynamic resource driver can distinguish between"
            " parameters stored here and and those stored in ResourceClaimSpec."
        ),
    )
    suitableNodes: Optional[v1.NodeSelector] = Field(
        None,
        description=(
            "Only nodes matching the selector will be considered by the scheduler when"
            " trying to find a Node that fits a Pod when that Pod uses a ResourceClaim"
            " that has not been allocated yet.\n\nSetting this field is optional. If"
            " null, all nodes are candidates."
        ),
    )


class ResourceClassList(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description=(
            "APIVersion defines the versioned schema of this representation of an"
            " object. Servers should convert recognized schemas to the latest internal"
            " value, and may reject unrecognized values. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources"
        ),
    )
    items: List[ResourceClass] = Field(
        ..., description="Items is the list of resource classes."
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
        None, description="Standard list metadata"
    )


class ResourceClaimTemplate(BaseModel):
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
        None, description="Standard object metadata"
    )
    spec: ResourceClaimTemplateSpec = Field(
        ...,
        description=(
            "Describes the ResourceClaim that is to be generated.\n\nThis field is"
            " immutable. A ResourceClaim will get created by the control plane for a"
            " Pod when needed and then not get updated anymore."
        ),
    )


class ResourceClaimTemplateList(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description=(
            "APIVersion defines the versioned schema of this representation of an"
            " object. Servers should convert recognized schemas to the latest internal"
            " value, and may reject unrecognized values. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources"
        ),
    )
    items: List[ResourceClaimTemplate] = Field(
        ..., description="Items is the list of resource claim templates."
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
        None, description="Standard list metadata"
    )
