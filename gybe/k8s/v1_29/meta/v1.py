"""Models generated from Kubernetes OpenAPI Spec."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from gybe.k8s.types import JSONDict, JSONObj, K8sSpec


@dataclass
class APIGroup(K8sSpec):
    """APIGroup contains the name, the supported versions, and the preferred version of a group.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        name: name is the name of the group.
        preferredVersion: preferredVersion is the version preferred by the API server, which probably is the
            storage version.
        serverAddressByClientCIDRs: a map of client CIDR to server address that is serving this group. This is
            to help clients reach servers in the most network-efficient way possible. Clients can use the
            appropriate server address as per the CIDR that they match. In case of multiple matches, clients
            should use the longest matching CIDR. The server returns only those CIDRs that it thinks that the
            client can match. For example: the master will return an internal IP CIDR only, if the client
            reaches the server using an internal IP. Server looks at X-Forwarded-For header or X-Real-Ip
            header or request.RemoteAddr (in that order) to get the client IP.
        versions: versions are the versions supported in this group.

    """

    name: str
    versions: List[GroupVersionForDiscovery]
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    preferredVersion: Optional[GroupVersionForDiscovery] = None
    serverAddressByClientCIDRs: Optional[List[ServerAddressByClientCIDR]] = None


@dataclass
class GroupVersionForDiscovery(K8sSpec):
    """GroupVersion contains the 'group/version' and 'version' string of a version. It is made a struct to
    keep extensibility.

    Attributes:
        groupVersion: groupVersion specifies the API group and version in the form 'group/version'
        version: version specifies the version in the form of 'version'. This is to save the clients the
            trouble of splitting the GroupVersion.

    """

    groupVersion: str
    version: str


@dataclass
class ServerAddressByClientCIDR(K8sSpec):
    """ServerAddressByClientCIDR helps the client to determine the server address that they should use,
    depending on the clientCIDR that they match.

    Attributes:
        clientCIDR: The CIDR with which clients can match their IP to figure out the server address that they
            should use.
        serverAddress: Address of this server, suitable for a client that matches the above CIDR. This can be
            a hostname, hostname:port, IP or IP:port.

    """

    clientCIDR: str
    serverAddress: str


@dataclass
class APIResource(K8sSpec):
    """APIResource specifies the name of a resource and whether it is namespaced.

    Attributes:
        categories: categories is a list of the grouped resources this resource belongs to (e.g. 'all')
        group: group is the preferred group of the resource.  Empty implies the group of the containing
            resource list. For subresources, this may have a different value, for example: Scale'.
        kind: kind is the kind for the resource (e.g. 'Foo' is the kind for a resource 'foo')
        name: name is the plural name of the resource.
        namespaced: namespaced indicates if a resource is namespaced or not.
        shortNames: shortNames is a list of suggested short names of the resource.
        singularName: singularName is the singular name of the resource.  This allows clients to handle plural
            and singular opaquely. The singularName is more correct for reporting status on a single item and
            both singular and plural are allowed from the kubectl CLI interface.
        storageVersionHash: The hash value of the storage version, the version this resource is converted to
            when written to the data store. Value must be treated as opaque by clients. Only equality
            comparison on the value is valid. This is an alpha feature and may change or be removed in the
            future. The field is populated by the apiserver only if the StorageVersionHash feature gate is
            enabled. This field will remain optional even if it graduates.
        verbs: verbs is a list of supported kube verbs (this includes get, list, watch, create, update, patch,
            delete, deletecollection, and proxy)
        version: version is the preferred version of the resource.  Empty implies the version of the
            containing resource list For subresources, this may have a different value, for example: v1 (while
            inside a v1beta1 version of the core resource's group)'.

    """

    name: str
    singularName: str
    namespaced: bool
    kind: str
    verbs: List[str]
    categories: Optional[List[str]] = None
    group: Optional[str] = None
    shortNames: Optional[List[str]] = None
    storageVersionHash: Optional[str] = None
    version: Optional[str] = None


@dataclass
class APIResourceList(K8sSpec):
    """APIResourceList is a list of APIResource, it is used to expose the name of the resources supported in
    a specific group and version, and if the resource is namespaced.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        groupVersion: groupVersion is the group and version this APIResourceList is for.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        resources: resources contains the name of the resources and if they are namespaced.

    """

    groupVersion: str
    resources: List[APIResource]
    apiVersion: Optional[str] = None
    kind: Optional[str] = None


@dataclass
class DeleteOptions(K8sSpec):
    """DeleteOptions may be provided when deleting an API object.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        dryRun: When present, indicates that modifications should not be persisted. An invalid or unrecognized
            dryRun directive will result in an error response and no further processing of the request. Valid
            values are: - All: all dry run stages will be processed
        gracePeriodSeconds: The duration in seconds before the object should be deleted. Value must be non-
            negative integer. The value zero indicates delete immediately. If this value is nil, the default
            grace period for the specified type will be used. Defaults to a per object value if not specified.
            zero means delete immediately.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        orphanDependents: Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7.
            Should the dependent objects be orphaned. If true/false, the 'orphan' finalizer will be added
            to/removed from the object's finalizers list. Either this field or PropagationPolicy may be set,
            but not both.
        preconditions: Must be fulfilled before a deletion is carried out. If not possible, a 409 Conflict
            status will be returned.
        propagationPolicy: Whether and how garbage collection will be performed. Either this field or
            OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer
            set in the metadata.finalizers and the resource-specific default policy. Acceptable values are:
            'Orphan' - orphan the dependents; 'Background' - allow the garbage collector to delete the
            dependents in the background; 'Foreground' - a cascading policy that deletes all dependents in the
            foreground.

    """

    apiVersion: Optional[str] = None
    dryRun: Optional[List[str]] = None
    gracePeriodSeconds: Optional[int] = None
    kind: Optional[str] = None
    orphanDependents: Optional[bool] = None
    preconditions: Optional[Preconditions] = None
    propagationPolicy: Optional[str] = None


@dataclass
class ManagedFieldsEntry(K8sSpec):
    """ManagedFieldsEntry is a workflow-id, a FieldSet and the group version of the resource that the
    fieldset applies to.

    Attributes:
        apiVersion: APIVersion defines the version of this resource that this field set applies to. The format
            is 'group/version' just like the top-level APIVersion field. It is necessary to track the version
            of a field set because it cannot be automatically converted.
        fieldsType: FieldsType is the discriminator for the different fields format and version. There is
            currently only one possible value: 'FieldsV1'
        fieldsV1: FieldsV1 holds the first JSON version format as described in the 'FieldsV1' type.
        manager: Manager is an identifier of the workflow managing these fields.
        operation: Operation is the type of operation which lead to this ManagedFieldsEntry being created. The
            only valid values for this field are 'Apply' and 'Update'.
        subresource: Subresource is the name of the subresource used to update that object, or empty string if
            the object was updated through the main resource. The value of this field is used to distinguish
            between managers, even if they share the same name. For example, a status update will be distinct
            from a regular update using the same manager name. Note that the APIVersion field is not related
            to the Subresource field and it always corresponds to the version of the main resource.
        time: Time is the timestamp of when the ManagedFields entry was added. The timestamp will also be
            updated if a field is added, the manager changes any of the owned fields value or removes a field.
            The timestamp does not update when a field is removed from the entry because another manager took
            it over.

    """

    apiVersion: Optional[str] = None
    fieldsType: Optional[str] = None
    fieldsV1: Optional[JSONObj] = None
    manager: Optional[str] = None
    operation: Optional[str] = None
    subresource: Optional[str] = None
    time: Optional[str] = None


@dataclass
class ObjectMeta(K8sSpec):
    """ObjectMeta is metadata that all persisted resources must have, which includes all objects users must
    create.

    Attributes:
        annotations: Annotations is an unstructured key value map stored with a resource that may be set by
            external tools to store and retrieve arbitrary metadata. They are not queryable and should be
            preserved when modifying objects.
        creationTimestamp: CreationTimestamp is a timestamp representing the server time when this object was
            created. It is not guaranteed to be set in happens-before order across separate operations.
            Clients may not set this value. It is represented in RFC3339 form and is in UTC.  Populated by the
            system. Read-only. Null for lists.
        deletionGracePeriodSeconds: Number of seconds allowed for this object to gracefully terminate before
            it will be removed from the system. Only set when deletionTimestamp is also set. May only be
            shortened. Read-only.
        deletionTimestamp: DeletionTimestamp is RFC 3339 date and time at which this resource will be deleted.
            This field is set by the server when a graceful deletion is requested by the user, and is not
            directly settable by a client. The resource is expected to be deleted (no longer visible from
            resource lists, and not reachable by name) after the time in this field, once the finalizers list
            is empty. As long as the finalizers list contains items, deletion is blocked. Once the
            deletionTimestamp is set, this value may not be unset or be set further into the future, although
            it may be shortened or the resource may be deleted prior to this time. For example, a user may
            request that a pod is deleted in 30 seconds. The Kubelet will react by sending a graceful
            termination signal to the containers in the pod. After that 30 seconds, the Kubelet will send a
            hard termination signal (SIGKILL) to the container and after cleanup, remove the pod from the API.
            In the presence of network partitions, this object may still exist after this timestamp, until an
            administrator or automated process can determine the resource is fully terminated. If not set,
            graceful deletion of the object has not been requested.  Populated by the system when a graceful
            deletion is requested. Read-only.
        finalizers: Must be empty before the object is deleted from the registry. Each entry is an identifier
            for the responsible component that will remove the entry from the list. If the deletionTimestamp
            of the object is non-nil, entries in this list can only be removed. Finalizers may be processed
            and removed in any order.  Order is NOT enforced because it introduces significant risk of stuck
            finalizers. finalizers is a shared field, any actor with permission can reorder it. If the
            finalizer list is processed in order, then this can lead to a situation in which the component
            responsible for the first finalizer in the list is waiting for a signal (field value, external
            system, or other) produced by a component responsible for a finalizer later in the list, resulting
            in a deadlock. Without enforced ordering finalizers are free to order amongst themselves and are
            not vulnerable to ordering changes in the list.
        generateName: GenerateName is an optional prefix, used by the server, to generate a unique name ONLY
            IF the Name field has not been provided. If this field is used, the name returned to the client
            will be different than the name passed. This value will also be combined with a unique suffix. The
            provided value has the same validation rules as the Name field, and may be truncated by the length
            of the suffix required to make the value unique on the server.  If this field is specified and the
            generated name exists, the server will return a 409.  Applied only if Name is not specified.
        generation: A sequence number representing a specific generation of the desired state. Populated by
            the system. Read-only.
        labels: Map of string keys and values that can be used to organize and categorize (scope and select)
            objects. May match selectors of replication controllers and services.
        managedFields: ManagedFields maps workflow-id and version to the set of fields that are managed by
            that workflow. This is mostly for internal housekeeping, and users typically shouldn't need to set
            or understand this field. A workflow can be the user's name, a controller's name, or the name of a
            specific apply path like 'ci-cd'. The set of fields is always in the version that the workflow
            used when modifying the object.
        name: Name must be unique within a namespace. Is required when creating resources, although some
            resources may allow a client to request the generation of an appropriate name automatically. Name
            is primarily intended for creation idempotence and configuration definition. Cannot be updated.
        namespace: Namespace defines the space within which each name must be unique. An empty namespace is
            equivalent to the 'default' namespace, but 'default' is the canonical representation. Not all
            objects are required to be scoped to a namespace - the value of this field for those objects will
            be empty.  Must be a DNS_LABEL. Cannot be updated.
        ownerReferences: List of objects depended by this object. If ALL objects in the list have been
            deleted, this object will be garbage collected. If this object is managed by a controller, then an
            entry in this list will point to this controller, with the controller field set to true. There
            cannot be more than one managing controller.
        resourceVersion: An opaque value that represents the internal version of this object that can be used
            by clients to determine when objects have changed. May be used for optimistic concurrency, change
            detection, and the watch operation on a resource or set of resources. Clients must treat these
            values as opaque and passed unmodified back to the server. They may only be valid for a particular
            resource or set of resources.  Populated by the system. Read-only. Value must be treated as opaque
            by clients and .
        selfLink: Deprecated: selfLink is a legacy read-only field that is no longer populated by the system.
        uid: UID is the unique in time and space value for this object. It is typically generated by the
            server on successful creation of a resource and is not allowed to change on PUT operations.
            Populated by the system. Read-only.

    """

    annotations: Optional[JSONDict] = None
    creationTimestamp: Optional[str] = None
    deletionGracePeriodSeconds: Optional[int] = None
    deletionTimestamp: Optional[str] = None
    finalizers: Optional[List[str]] = None
    generateName: Optional[str] = None
    generation: Optional[int] = None
    labels: Optional[JSONDict] = None
    managedFields: Optional[List[ManagedFieldsEntry]] = None
    name: Optional[str] = None
    namespace: Optional[str] = None
    ownerReferences: Optional[List[OwnerReference]] = None
    resourceVersion: Optional[str] = None
    selfLink: Optional[str] = None
    uid: Optional[str] = None


@dataclass
class OwnerReference(K8sSpec):
    """OwnerReference contains enough information to let you identify an owning object. An owning object must
    be in the same namespace as the dependent, or be cluster-scoped, so there is no namespace field.

    Attributes:
        apiVersion: API version of the referent.
        blockOwnerDeletion: If true, AND if the owner has the 'foregroundDeletion' finalizer, then the owner
            cannot be deleted from the key-value store until this reference is removed. See
            https://kubernetes.io/docs/concepts/architecture/garbage-collection/#foreground-deletion for how
            the garbage collector interacts with this field and enforces the foreground deletion. Defaults to
            false. To set this field, a user needs 'delete' permission of the owner, otherwise 422
            (Unprocessable Entity) will be returned.
        controller: If true, this reference points to the managing controller.
        kind: Kind of the referent.
        name: Name of the referent.
        uid: UID of the referent.

    """

    apiVersion: str
    kind: str
    name: str
    uid: str
    blockOwnerDeletion: Optional[bool] = None
    controller: Optional[bool] = None


@dataclass
class Preconditions(K8sSpec):
    """Preconditions must be fulfilled before an operation (update, delete, etc.) is carried out.

    Attributes:
        resourceVersion: Specifies the target ResourceVersion
        uid: Specifies the target UID.

    """

    resourceVersion: Optional[str] = None
    uid: Optional[str] = None


@dataclass
class Status(K8sSpec):
    """Status is a return value for calls that don't return other objects.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        code: Suggested HTTP return code for this status, 0 if not set.
        details: Extended data associated with the reason.  Each reason may define its own extended details.
            This field is optional and the data returned is not guaranteed to conform to any schema except
            that defined by the reason type.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        message: A human-readable description of the status of this operation.
        metadata: Standard list metadata.
        reason: A machine-readable description of why this operation is in the 'Failure' status. If this value
            is empty there is no information available. A Reason clarifies an HTTP status code but does not
            override it.
        status: Status of the operation. One of: 'Success' or 'Failure'.

    """

    apiVersion: Optional[str] = None
    code: Optional[int] = None
    details: Optional[StatusDetails] = None
    kind: Optional[str] = None
    message: Optional[str] = None
    metadata: Optional[JSONObj] = None
    reason: Optional[str] = None
    status: Optional[str] = None


@dataclass
class StatusCause(K8sSpec):
    """StatusCause provides more information about an api.Status failure, including cases when multiple
    errors are encountered.

    Attributes:
        field: The field of the resource that has caused this error, as named by its JSON serialization. May
            include dot and postfix notation for nested attributes. Arrays are zero-indexed.  Fields may
            appear more than once in an array of causes due to fields having multiple errors. Optional.
            Examples:   'name' - the field 'name' on the current resource   'items[0].name' - the field 'name'
            on the first array entry in 'items'
        message: A human-readable description of the cause of the error.  This field may be presented as-is to
            a reader.
        reason: A machine-readable description of the cause of the error. If this value is empty there is no
            information available.

    """

    field: Optional[str] = None
    message: Optional[str] = None
    reason: Optional[str] = None


@dataclass
class StatusDetails(K8sSpec):
    """StatusDetails is a set of additional properties that MAY be set by the server to provide additional
    information about a response. The Reason field of a Status object defines what attributes will be set.
    Clients must ignore fields that do not match the defined type of each attribute, and should assume
    that any attribute may be empty, invalid, or under defined.

    Attributes:
        causes: The Causes array includes more details associated with the StatusReason failure. Not all
            StatusReasons may provide detailed causes.
        group: The group attribute of the resource associated with the status StatusReason.
        kind: The kind attribute of the resource associated with the status StatusReason. On some operations
            may differ from the requested resource Kind.
        name: The name attribute of the resource associated with the status StatusReason (when there is a
            single name which can be described).
        retryAfterSeconds: If specified, the time in seconds before the operation should be retried. Some
            errors may indicate the client must take an alternate action - for those errors this field may
            indicate how long to wait before taking the alternate action.
        uid: UID of the resource. (when there is a single resource which can be described).

    """

    causes: Optional[List[StatusCause]] = None
    group: Optional[str] = None
    kind: Optional[str] = None
    name: Optional[str] = None
    retryAfterSeconds: Optional[int] = None
    uid: Optional[str] = None


@dataclass
class WatchEvent(K8sSpec):
    """Event represents a single event to a watched resource.

    Attributes:
        object: Object is:  * If Type is Added or Modified: the new state of the object.  * If Type is
            Deleted: the state of the object immediately before deletion.  * If Type is Error: *Status is
            recommended; other types may make sense    depending on context.
        type: ...

    """

    type: str
    object: JSONObj


@dataclass
class LabelSelector(K8sSpec):
    """A label selector is a label query over a set of resources. The result of matchLabels and
    matchExpressions are ANDed. An empty label selector matches all objects. A null label selector matches
    no objects.

    Attributes:
        matchExpressions: matchExpressions is a list of label selector requirements. The requirements are
            ANDed.
        matchLabels: matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is
            equivalent to an element of matchExpressions, whose key field is 'key', the operator is 'In', and
            the values array contains only 'value'. The requirements are ANDed.

    """

    matchExpressions: Optional[List[LabelSelectorRequirement]] = None
    matchLabels: Optional[JSONDict] = None


@dataclass
class LabelSelectorRequirement(K8sSpec):
    """A label selector requirement is a selector that contains values, a key, and an operator that relates
    the key and values.

    Attributes:
        key: key is the label key that the selector applies to.
        operator: operator represents a key's relationship to a set of values. Valid operators are In, NotIn,
            Exists and DoesNotExist.
        values: values is an array of string values. If the operator is In or NotIn, the values array must be
            non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array
            is replaced during a strategic merge patch.

    """

    key: str
    operator: str
    values: Optional[List[str]] = None


@dataclass
class APIGroupList(K8sSpec):
    """APIGroupList is a list of APIGroup, to allow clients to discover the API at /apis.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        groups: groups is a list of APIGroup.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.

    """

    groups: List[APIGroup]
    apiVersion: Optional[str] = None
    kind: Optional[str] = None


@dataclass
class Condition(K8sSpec):
    """Condition contains details for one aspect of the current state of this API Resource.

    Attributes:
        lastTransitionTime: lastTransitionTime is the last time the condition transitioned from one status to
            another. This should be when the underlying condition changed.  If that is not known, then using
            the time when the API field changed is acceptable.
        message: message is a human readable message indicating details about the transition. This may be an
            empty string.
        observedGeneration: observedGeneration represents the .metadata.generation that the condition was set
            based upon. For instance, if .metadata.generation is currently 12, but the
            .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the
            current state of the instance.
        reason: reason contains a programmatic identifier indicating the reason for the condition's last
            transition. Producers of specific condition types may define expected values and meanings for this
            field, and whether the values are considered a guaranteed API. The value should be a CamelCase
            string. This field may not be empty.
        status: status of the condition, one of True, False, Unknown.
        type: type of condition in CamelCase or in foo.example.com/CamelCase.

    """

    type: str
    status: str
    lastTransitionTime: str
    reason: str
    message: str
    observedGeneration: Optional[int] = None


@dataclass
class APIVersions(K8sSpec):
    """APIVersions lists the versions that are available, to allow clients to discover the API at /api, which
    is the root path of the legacy v1 API.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        serverAddressByClientCIDRs: a map of client CIDR to server address that is serving this group. This is
            to help clients reach servers in the most network-efficient way possible. Clients can use the
            appropriate server address as per the CIDR that they match. In case of multiple matches, clients
            should use the longest matching CIDR. The server returns only those CIDRs that it thinks that the
            client can match. For example: the master will return an internal IP CIDR only, if the client
            reaches the server using an internal IP. Server looks at X-Forwarded-For header or X-Real-Ip
            header or request.RemoteAddr (in that order) to get the client IP.
        versions: versions are the api versions that are available.

    """

    versions: List[str]
    serverAddressByClientCIDRs: List[ServerAddressByClientCIDR]
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
