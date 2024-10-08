"""Models generated from Kubernetes OpenAPI Spec."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Literal, Optional

import gybe.k8s.v1_30.api.resource
import gybe.k8s.v1_30.core.v1
import gybe.k8s.v1_30.meta.v1
from gybe.k8s.types import JSONObj, K8sResource, K8sSpec


@dataclass
class AllocationResult(K8sSpec):
    """AllocationResult contains attributes of an allocated resource.

    Attributes:
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

    availableOnNodes: Optional[gybe.k8s.v1_30.core.v1.NodeSelector] = None
    resourceHandles: Optional[List[ResourceHandle]] = None
    shareable: Optional[bool] = None


@dataclass
class DriverAllocationResult(K8sSpec):
    """DriverAllocationResult contains vendor parameters and the allocation result for one request.

    Attributes:
        namedResources: NamedResources describes the allocation result when using the named resources model.
        vendorRequestParameters: VendorRequestParameters are the per-request configuration parameters from the
            time that the claim was allocated.

    """

    namedResources: Optional[NamedResourcesAllocationResult] = None
    vendorRequestParameters: Optional[JSONObj] = None


@dataclass
class DriverRequests(K8sSpec):
    """DriverRequests describes all resources that are needed from one particular driver.

    Attributes:
        driverName: DriverName is the name used by the DRA driver kubelet plugin.
        requests: Requests describes all resources that are needed from the driver.
        vendorParameters: VendorParameters are arbitrary setup parameters for all requests of the claim. They
            are ignored while allocating the claim.

    """

    driverName: Optional[str] = None
    requests: Optional[List[ResourceRequest]] = None
    vendorParameters: Optional[JSONObj] = None


@dataclass
class NamedResourcesAllocationResult(K8sSpec):
    """NamedResourcesAllocationResult is used in AllocationResultModel.

    Attributes:
        name: Name is the name of the selected resource instance.

    """

    name: str


@dataclass
class NamedResourcesAttribute(K8sSpec):
    """NamedResourcesAttribute is a combination of an attribute name and its value.

    Attributes:
        bool: BoolValue is a true/false value.
        int: IntValue is a 64-bit integer.
        intSlice: IntSliceValue is an array of 64-bit integers.
        name: Name is unique identifier among all resource instances managed by the driver on the node. It
            must be a DNS subdomain.
        quantity: QuantityValue is a quantity.
        string: StringValue is a string.
        stringSlice: StringSliceValue is an array of strings.
        version: VersionValue is a semantic version according to semver.org spec 2.0.0.

    """

    name: str
    bool: Optional[bool] = None
    int: Optional[int] = None
    intSlice: Optional[NamedResourcesIntSlice] = None
    quantity: Optional[gybe.k8s.v1_30.api.resource.Quantity] = None
    string: Optional[str] = None
    stringSlice: Optional[NamedResourcesStringSlice] = None
    version: Optional[str] = None


@dataclass
class NamedResourcesFilter(K8sSpec):
    """NamedResourcesFilter is used in ResourceFilterModel.

    Attributes:
        selector: Selector is a CEL expression which must evaluate to true if a resource instance is suitable.
            The language is as defined in https://kubernetes.io/docs/reference/using-api/cel/  In addition,
            for each type NamedResourcesin AttributeValue there is a map that resolves to the corresponding
            value of the instance under evaluation. For example:
            attributes.quantity['a'].isGreaterThan(quantity('0')) &&    attributes.stringslice['b'].isSorted()

    """

    selector: str


@dataclass
class NamedResourcesInstance(K8sSpec):
    """NamedResourcesInstance represents one individual hardware instance that can be selected based on its
    attributes.

    Attributes:
        attributes: Attributes defines the attributes of this resource instance. The name of each attribute
            must be unique.
        name: Name is unique identifier among all resource instances managed by the driver on the node. It
            must be a DNS subdomain.

    """

    name: str
    attributes: Optional[List[NamedResourcesAttribute]] = None


@dataclass
class NamedResourcesIntSlice(K8sSpec):
    """NamedResourcesIntSlice contains a slice of 64-bit integers.

    Attributes:
        ints: Ints is the slice of 64-bit integers.

    """

    ints: List[int]


@dataclass
class NamedResourcesRequest(K8sSpec):
    """NamedResourcesRequest is used in ResourceRequestModel.

    Attributes:
        selector: Selector is a CEL expression which must evaluate to true if a resource instance is suitable.
            The language is as defined in https://kubernetes.io/docs/reference/using-api/cel/  In addition,
            for each type NamedResourcesin AttributeValue there is a map that resolves to the corresponding
            value of the instance under evaluation. For example:
            attributes.quantity['a'].isGreaterThan(quantity('0')) &&    attributes.stringslice['b'].isSorted()

    """

    selector: str


@dataclass
class NamedResourcesResources(K8sSpec):
    """NamedResourcesResources is used in ResourceModel.

    Attributes:
        instances: The list of all individual resources instances currently available.

    """

    instances: List[NamedResourcesInstance]


@dataclass
class NamedResourcesStringSlice(K8sSpec):
    """NamedResourcesStringSlice contains a slice of strings.

    Attributes:
        strings: Strings is the slice of strings.

    """

    strings: List[str]


@dataclass
class PodSchedulingContext(K8sResource):
    """PodSchedulingContext objects hold information that is needed to schedule a Pod with ResourceClaims
    that use 'WaitForFirstConsumer' allocation mode.  This is an alpha type and requires enabling the
    DynamicResourceAllocation feature gate.

    Attributes:
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
    apiVersion: Literal['policy/v1alpha2'] = 'policy/v1alpha2'
    kind: Literal['PodSchedulingContext'] = 'PodSchedulingContext'
    metadata: Optional[gybe.k8s.v1_30.meta.v1.ObjectMeta] = None
    status: Optional[PodSchedulingContextStatus] = None


@dataclass
class PodSchedulingContextList(K8sSpec):
    """PodSchedulingContextList is a collection of Pod scheduling objects.

    Attributes:
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
class PodSchedulingContextSpec(K8sSpec):
    """PodSchedulingContextSpec describes where resources for the Pod are needed.

    Attributes:
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
class PodSchedulingContextStatus(K8sSpec):
    """PodSchedulingContextStatus describes where resources for the Pod can be allocated.

    Attributes:
        resourceClaims: ResourceClaims describes resource availability for each pod.spec.resourceClaim entry
            where the corresponding ResourceClaim uses 'WaitForFirstConsumer' allocation mode.

    """

    resourceClaims: Optional[List[ResourceClaimSchedulingStatus]] = None


@dataclass
class ResourceClaim(K8sResource):
    """ResourceClaim describes which resources are needed by a resource consumer. Its status tracks whether
    the resource has been allocated and what the resulting attributes are.  This is an alpha type and
    requires enabling the DynamicResourceAllocation feature gate.

    Attributes:
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
    apiVersion: Literal['policy/v1alpha2'] = 'policy/v1alpha2'
    kind: Literal['ResourceClaim'] = 'ResourceClaim'
    metadata: Optional[gybe.k8s.v1_30.meta.v1.ObjectMeta] = None
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
class ResourceClaimList(K8sSpec):
    """ResourceClaimList is a collection of claims.

    Attributes:
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
class ResourceClaimParameters(K8sSpec):
    """ResourceClaimParameters defines resource requests for a ResourceClaim in an in-tree format understood
    by Kubernetes.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        driverRequests: DriverRequests describes all resources that are needed for the allocated claim. A
            single claim may use resources coming from different drivers. For each driver, this array has at
            most one entry which then may have one or more per-driver requests.  May be empty, in which case
            the claim can always be allocated.
        generatedFrom: If this object was created from some other resource, then this links back to that
            resource. This field is used to find the in-tree representation of the claim parameters when the
            parameter reference of the claim refers to some unknown type.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object metadata
        shareable: Shareable indicates whether the allocated claim is meant to be shareable by multiple
            consumers at the same time.

    """

    apiVersion: Optional[str] = None
    driverRequests: Optional[List[DriverRequests]] = None
    generatedFrom: Optional[ResourceClaimParametersReference] = None
    kind: Optional[str] = None
    metadata: Optional[gybe.k8s.v1_30.meta.v1.ObjectMeta] = None
    shareable: Optional[bool] = None


@dataclass
class ResourceClaimParametersList(K8sSpec):
    """ResourceClaimParametersList is a collection of ResourceClaimParameters.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        items: Items is the list of node resource capacity objects.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard list metadata

    """

    items: List[ResourceClaimParameters]
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[JSONObj] = None


@dataclass
class ResourceClaimParametersReference(K8sSpec):
    """ResourceClaimParametersReference contains enough information to let you locate the parameters for a
    ResourceClaim. The object must be in the same namespace as the ResourceClaim.

    Attributes:
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
class ResourceClaimSchedulingStatus(K8sSpec):
    """ResourceClaimSchedulingStatus contains information about one particular ResourceClaim with
    'WaitForFirstConsumer' allocation mode.

    Attributes:
        name: Name matches the pod.spec.resourceClaims[*].Name field.
        unsuitableNodes: UnsuitableNodes lists nodes that the ResourceClaim cannot be allocated for.  The size
            of this field is limited to 128, the same as for PodSchedulingSpec.PotentialNodes. This may get
            increased in the future, but not reduced.

    """

    name: Optional[str] = None
    unsuitableNodes: Optional[List[str]] = None


@dataclass
class ResourceClaimSpec(K8sSpec):
    """ResourceClaimSpec defines how a resource is to be allocated.

    Attributes:
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
class ResourceClaimStatus(K8sSpec):
    """ResourceClaimStatus tracks whether the resource has been allocated and what the resulting attributes
    are.

    Attributes:
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
class ResourceClaimTemplate(K8sSpec):
    """ResourceClaimTemplate is used to produce ResourceClaim objects.

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
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[gybe.k8s.v1_30.meta.v1.ObjectMeta] = None


@dataclass
class ResourceClaimTemplateList(K8sSpec):
    """ResourceClaimTemplateList is a collection of claim templates.

    Attributes:
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
class ResourceClaimTemplateSpec(K8sSpec):
    """ResourceClaimTemplateSpec contains the metadata and fields for a ResourceClaim.

    Attributes:
        metadata: ObjectMeta may contain labels and annotations that will be copied into the PVC when creating
            it. No other fields are allowed and will be rejected during validation.
        spec: Spec for the ResourceClaim. The entire content is copied unchanged into the ResourceClaim that
            gets created from this template. The same fields as in a ResourceClaim are also valid here.

    """

    spec: ResourceClaimSpec
    metadata: Optional[gybe.k8s.v1_30.meta.v1.ObjectMeta] = None


@dataclass
class ResourceClass(K8sSpec):
    """ResourceClass is used by administrators to influence how resources are allocated.  This is an alpha
    type and requires enabling the DynamicResourceAllocation feature gate.

    Attributes:
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
        structuredParameters: If and only if allocation of claims using this class is handled via structured
            parameters, then StructuredParameters must be set to true.
        suitableNodes: Only nodes matching the selector will be considered by the scheduler when trying to
            find a Node that fits a Pod when that Pod uses a ResourceClaim that has not been allocated yet.
            Setting this field is optional. If null, all nodes are candidates.

    """

    driverName: str
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[gybe.k8s.v1_30.meta.v1.ObjectMeta] = None
    parametersRef: Optional[ResourceClassParametersReference] = None
    structuredParameters: Optional[bool] = None
    suitableNodes: Optional[gybe.k8s.v1_30.core.v1.NodeSelector] = None


@dataclass
class ResourceClassList(K8sSpec):
    """ResourceClassList is a collection of classes.

    Attributes:
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
class ResourceClassParameters(K8sSpec):
    """ResourceClassParameters defines resource requests for a ResourceClass in an in-tree format understood
    by Kubernetes.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        filters: Filters describes additional contraints that must be met when using the class.
        generatedFrom: If this object was created from some other resource, then this links back to that
            resource. This field is used to find the in-tree representation of the class parameters when the
            parameter reference of the class refers to some unknown type.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object metadata
        vendorParameters: VendorParameters are arbitrary setup parameters for all claims using this class.
            They are ignored while allocating the claim. There must not be more than one entry per driver.

    """

    apiVersion: Optional[str] = None
    filters: Optional[List[ResourceFilter]] = None
    generatedFrom: Optional[ResourceClassParametersReference] = None
    kind: Optional[str] = None
    metadata: Optional[gybe.k8s.v1_30.meta.v1.ObjectMeta] = None
    vendorParameters: Optional[List[VendorParameters]] = None


@dataclass
class ResourceClassParametersList(K8sSpec):
    """ResourceClassParametersList is a collection of ResourceClassParameters.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        items: Items is the list of node resource capacity objects.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard list metadata

    """

    items: List[ResourceClassParameters]
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[JSONObj] = None


@dataclass
class ResourceClassParametersReference(K8sSpec):
    """ResourceClassParametersReference contains enough information to let you locate the parameters for a
    ResourceClass.

    Attributes:
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
class ResourceFilter(K8sSpec):
    """ResourceFilter is a filter for resources from one particular driver.

    Attributes:
        driverName: DriverName is the name used by the DRA driver kubelet plugin.
        namedResources: NamedResources describes a resource filter using the named resources model.

    """

    driverName: Optional[str] = None
    namedResources: Optional[NamedResourcesFilter] = None


@dataclass
class ResourceHandle(K8sSpec):
    """ResourceHandle holds opaque resource data for processing by a specific kubelet plugin.

    Attributes:
        data: Data contains the opaque data associated with this ResourceHandle. It is set by the controller
            component of the resource driver whose name matches the DriverName set in the ResourceClaimStatus
            this ResourceHandle is embedded in. It is set at allocation time and is intended for processing by
            the kubelet plugin whose name matches the DriverName set in this ResourceHandle.  The maximum size
            of this field is 16KiB. This may get increased in the future, but not reduced.
        driverName: DriverName specifies the name of the resource driver whose kubelet plugin should be
            invoked to process this ResourceHandle's data once it lands on a node. This may differ from the
            DriverName set in ResourceClaimStatus this ResourceHandle is embedded in.
        structuredData: If StructuredData is set, then it needs to be used instead of Data.

    """

    data: Optional[str] = None
    driverName: Optional[str] = None
    structuredData: Optional[StructuredResourceHandle] = None


@dataclass
class ResourceRequest(K8sSpec):
    """ResourceRequest is a request for resources from one particular driver.

    Attributes:
        namedResources: NamedResources describes a request for resources with the named resources model.
        vendorParameters: VendorParameters are arbitrary setup parameters for the requested resource. They are
            ignored while allocating a claim.

    """

    namedResources: Optional[NamedResourcesRequest] = None
    vendorParameters: Optional[JSONObj] = None


@dataclass
class ResourceSlice(K8sSpec):
    """ResourceSlice provides information about available resources on individual nodes.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        driverName: DriverName identifies the DRA driver providing the capacity information. A field selector
            can be used to list only ResourceSlice objects with a certain driver name.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object metadata
        namedResources: NamedResources describes available resources using the named resources model.
        nodeName: NodeName identifies the node which provides the resources if they are local to a node.  A
            field selector can be used to list only ResourceSlice objects with a certain node name.

    """

    driverName: str
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[gybe.k8s.v1_30.meta.v1.ObjectMeta] = None
    namedResources: Optional[NamedResourcesResources] = None
    nodeName: Optional[str] = None


@dataclass
class ResourceSliceList(K8sSpec):
    """ResourceSliceList is a collection of ResourceSlices.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        items: Items is the list of node resource capacity objects.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard list metadata

    """

    items: List[ResourceSlice]
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[JSONObj] = None


@dataclass
class StructuredResourceHandle(K8sSpec):
    """StructuredResourceHandle is the in-tree representation of the allocation result.

    Attributes:
        nodeName: NodeName is the name of the node providing the necessary resources if the resources are
            local to a node.
        results: Results lists all allocated driver resources.
        vendorClaimParameters: VendorClaimParameters are the per-claim configuration parameters from the
            resource claim parameters at the time that the claim was allocated.
        vendorClassParameters: VendorClassParameters are the per-claim configuration parameters from the
            resource class at the time that the claim was allocated.

    """

    results: List[DriverAllocationResult]
    nodeName: Optional[str] = None
    vendorClaimParameters: Optional[JSONObj] = None
    vendorClassParameters: Optional[JSONObj] = None


@dataclass
class VendorParameters(K8sSpec):
    """VendorParameters are opaque parameters for one particular driver.

    Attributes:
        driverName: DriverName is the name used by the DRA driver kubelet plugin.
        parameters: Parameters can be arbitrary setup parameters. They are ignored while allocating a claim.

    """

    driverName: Optional[str] = None
    parameters: Optional[JSONObj] = None
