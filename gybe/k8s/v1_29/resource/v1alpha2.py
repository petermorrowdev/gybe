"""Models generated from Kubernetes OpenAPI Spec."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

import gybe.k8s.v1_29.core.v1
import gybe.k8s.v1_29.meta.v1
from gybe.k8s.types import JSONObj


@dataclass
class AllocationResult:
    """AllocationResult contains attributes of an allocated resource.

    Attributes
    ----------
        availableOnNodes: This field will get set by the resource driver after it has allocated the resource
            to inform the scheduler where it can schedule Pods using the ResourceClaim.  Setting this field is
            optional. If null, the resource is available everywhere.
        resourceHandles: ResourceHandles contain the state associated with an allocation that should be
            maintained throughout the lifetime of a claim. Each ResourceHandle contains data that should be
            passed to a specific kubelet plugin once it lands on a node. This data is returned by the driver
            after a successful allocation and is opaque to Kubernetes. Driver documentation may explain to
            users how to interpret this data if needed.  Setting this field is optional. It has a maximum size
            of 32 entries. If null (or empty), it is assumed this allocation will be processed by a single
            kubelet plugin with no ResourceHandle data attached. The name of the kubelet plugin invoked will
            match the DriverName set in the ResourceClaimStatus this AllocationResult is embedded in.
        shareable: Shareable determines whether the resource supports more than one consumer at a time.

    """

    availableOnNodes: Optional[gybe.k8s.v1_29.core.v1.NodeSelector] = None
    resourceHandles: Optional[List[ResourceHandle]] = None
    shareable: Optional[bool] = None


@dataclass
class PodSchedulingContext:
    """PodSchedulingContext objects hold information that is needed to schedule a Pod with ResourceClaims
    that use 'WaitForFirstConsumer' allocation mode.  This is an alpha type and requires enabling the
    DynamicResourceAllocation feature gate.

    Attributes
    ----------
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
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[gybe.k8s.v1_29.meta.v1.ObjectMeta] = None
    status: Optional[PodSchedulingContextStatus] = None


@dataclass
class PodSchedulingContextList:
    """PodSchedulingContextList is a collection of Pod scheduling objects.

    Attributes
    ----------
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        items: Items is the list of PodSchedulingContext objects.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard list metadata

    """

    items: List[PodSchedulingContext]
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[JSONObj] = None


@dataclass
class PodSchedulingContextSpec:
    """PodSchedulingContextSpec describes where resources for the Pod are needed.

    Attributes
    ----------
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
class PodSchedulingContextStatus:
    """PodSchedulingContextStatus describes where resources for the Pod can be allocated.

    Attributes
    ----------
        resourceClaims: ResourceClaims describes resource availability for each pod.spec.resourceClaim entry
            where the corresponding ResourceClaim uses 'WaitForFirstConsumer' allocation mode.

    """

    resourceClaims: Optional[List[ResourceClaimSchedulingStatus]] = None


@dataclass
class ResourceClaim:
    """ResourceClaim describes which resources are needed by a resource consumer. Its status tracks whether
    the resource has been allocated and what the resulting attributes are.  This is an alpha type and
    requires enabling the DynamicResourceAllocation feature gate.

    Attributes
    ----------
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object metadata
        spec: Spec describes the desired attributes of a resource that then needs to be allocated. It can only
            be set once when creating the ResourceClaim.
        status: Status describes whether the resource is available and with which attributes.

    """

    spec: ResourceClaimSpec
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[gybe.k8s.v1_29.meta.v1.ObjectMeta] = None
    status: Optional[ResourceClaimStatus] = None


@dataclass
class ResourceClaimConsumerReference:
    """ResourceClaimConsumerReference contains enough information to let you locate the consumer of a
    ResourceClaim. The user must be a resource in the same namespace as the ResourceClaim.

    Attributes
    ----------
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
class ResourceClaimList:
    """ResourceClaimList is a collection of claims.

    Attributes
    ----------
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        items: Items is the list of resource claims.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard list metadata

    """

    items: List[ResourceClaim]
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[JSONObj] = None


@dataclass
class ResourceClaimParametersReference:
    """ResourceClaimParametersReference contains enough information to let you locate the parameters for a
    ResourceClaim. The object must be in the same namespace as the ResourceClaim.

    Attributes
    ----------
        apiGroup: APIGroup is the group for the resource being referenced. It is empty for the core API. This
            matches the group in the APIVersion that is used when creating the resources.
        kind: Kind is the type of resource being referenced. This is the same value as in the parameter
            object's metadata, for example 'ConfigMap'.
        name: Name is the name of resource being referenced.

    """

    kind: str
    name: str
    apiGroup: Optional[str] = None


@dataclass
class ResourceClaimSchedulingStatus:
    """ResourceClaimSchedulingStatus contains information about one particular ResourceClaim with
    'WaitForFirstConsumer' allocation mode.

    Attributes
    ----------
        name: Name matches the pod.spec.resourceClaims[*].Name field.
        unsuitableNodes: UnsuitableNodes lists nodes that the ResourceClaim cannot be allocated for.  The size
            of this field is limited to 128, the same as for PodSchedulingSpec.PotentialNodes. This may get
            increased in the future, but not reduced.

    """

    name: Optional[str] = None
    unsuitableNodes: Optional[List[str]] = None


@dataclass
class ResourceClaimSpec:
    """ResourceClaimSpec defines how a resource is to be allocated.

    Attributes
    ----------
        allocationMode: Allocation can start immediately or when a Pod wants to use the resource.
            'WaitForFirstConsumer' is the default.
        parametersRef: ParametersRef references a separate object with arbitrary parameters that will be used
            by the driver when allocating a resource for the claim.  The object must be in the same namespace
            as the ResourceClaim.
        resourceClassName: ResourceClassName references the driver and additional parameters via the name of a
            ResourceClass that was created as part of the driver deployment.

    """

    resourceClassName: str
    allocationMode: Optional[str] = None
    parametersRef: Optional[ResourceClaimParametersReference] = None


@dataclass
class ResourceClaimStatus:
    """ResourceClaimStatus tracks whether the resource has been allocated and what the resulting attributes
    are.

    Attributes
    ----------
        allocation: Allocation is set by the resource driver once a resource or set of resources has been
            allocated successfully. If this is not specified, the resources have not been allocated yet.
        deallocationRequested: DeallocationRequested indicates that a ResourceClaim is to be deallocated.  The
            driver then must deallocate this claim and reset the field together with clearing the Allocation
            field.  While DeallocationRequested is set, no new consumers may be added to ReservedFor.
        driverName: DriverName is a copy of the driver name from the ResourceClass at the time when allocation
            started.
        reservedFor: ReservedFor indicates which entities are currently allowed to use the claim. A Pod which
            references a ResourceClaim which is not reserved for that Pod will not be started.  There can be
            at most 32 such reservations. This may get increased in the future, but not reduced.

    """

    allocation: Optional[AllocationResult] = None
    deallocationRequested: Optional[bool] = None
    driverName: Optional[str] = None
    reservedFor: Optional[List[ResourceClaimConsumerReference]] = None


@dataclass
class ResourceClaimTemplate:
    """ResourceClaimTemplate is used to produce ResourceClaim objects.

    Attributes
    ----------
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
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[gybe.k8s.v1_29.meta.v1.ObjectMeta] = None


@dataclass
class ResourceClaimTemplateList:
    """ResourceClaimTemplateList is a collection of claim templates.

    Attributes
    ----------
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        items: Items is the list of resource claim templates.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard list metadata

    """

    items: List[ResourceClaimTemplate]
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[JSONObj] = None


@dataclass
class ResourceClaimTemplateSpec:
    """ResourceClaimTemplateSpec contains the metadata and fields for a ResourceClaim.

    Attributes
    ----------
        metadata: ObjectMeta may contain labels and annotations that will be copied into the PVC when creating
            it. No other fields are allowed and will be rejected during validation.
        spec: Spec for the ResourceClaim. The entire content is copied unchanged into the ResourceClaim that
            gets created from this template. The same fields as in a ResourceClaim are also valid here.

    """

    spec: ResourceClaimSpec
    metadata: Optional[gybe.k8s.v1_29.meta.v1.ObjectMeta] = None


@dataclass
class ResourceClass:
    """ResourceClass is used by administrators to influence how resources are allocated.  This is an alpha
    type and requires enabling the DynamicResourceAllocation feature gate.

    Attributes
    ----------
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        driverName: DriverName defines the name of the dynamic resource driver that is used for allocation of
            a ResourceClaim that uses this class.  Resource drivers have a unique name in forward domain order
            (acme.example.com).
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object metadata
        parametersRef: ParametersRef references an arbitrary separate object that may hold parameters that
            will be used by the driver when allocating a resource that uses this class. A dynamic resource
            driver can distinguish between parameters stored here and and those stored in ResourceClaimSpec.
        suitableNodes: Only nodes matching the selector will be considered by the scheduler when trying to
            find a Node that fits a Pod when that Pod uses a ResourceClaim that has not been allocated yet.
            Setting this field is optional. If null, all nodes are candidates.

    """

    driverName: str
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[gybe.k8s.v1_29.meta.v1.ObjectMeta] = None
    parametersRef: Optional[ResourceClassParametersReference] = None
    suitableNodes: Optional[gybe.k8s.v1_29.core.v1.NodeSelector] = None


@dataclass
class ResourceClassList:
    """ResourceClassList is a collection of classes.

    Attributes
    ----------
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        items: Items is the list of resource classes.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard list metadata

    """

    items: List[ResourceClass]
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[JSONObj] = None


@dataclass
class ResourceClassParametersReference:
    """ResourceClassParametersReference contains enough information to let you locate the parameters for a
    ResourceClass.

    Attributes
    ----------
        apiGroup: APIGroup is the group for the resource being referenced. It is empty for the core API. This
            matches the group in the APIVersion that is used when creating the resources.
        kind: Kind is the type of resource being referenced. This is the same value as in the parameter
            object's metadata.
        name: Name is the name of resource being referenced.
        namespace: Namespace that contains the referenced resource. Must be empty for cluster-scoped resources
            and non-empty for namespaced resources.

    """

    kind: str
    name: str
    apiGroup: Optional[str] = None
    namespace: Optional[str] = None


@dataclass
class ResourceHandle:
    """ResourceHandle holds opaque resource data for processing by a specific kubelet plugin.

    Attributes
    ----------
        data: Data contains the opaque data associated with this ResourceHandle. It is set by the controller
            component of the resource driver whose name matches the DriverName set in the ResourceClaimStatus
            this ResourceHandle is embedded in. It is set at allocation time and is intended for processing by
            the kubelet plugin whose name matches the DriverName set in this ResourceHandle.  The maximum size
            of this field is 16KiB. This may get increased in the future, but not reduced.
        driverName: DriverName specifies the name of the resource driver whose kubelet plugin should be
            invoked to process this ResourceHandle's data once it lands on a node. This may differ from the
            DriverName set in ResourceClaimStatus this ResourceHandle is embedded in.

    """

    data: Optional[str] = None
    driverName: Optional[str] = None
