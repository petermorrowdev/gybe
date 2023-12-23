from __future__ import annotations
from datetime import datetime
from typing import Dict, List, Optional
from pydantic import BaseModel, Field
from ... import runtime


class GroupVersionForDiscovery(BaseModel):
    groupVersion: str = Field(
        ...,
        description=(
            "groupVersion specifies the API group and version in the form"
            ' "group/version"'
        ),
    )
    version: str = Field(
        ...,
        description=(
            'version specifies the version in the form of "version". This is to save'
            " the clients the trouble of splitting the GroupVersion."
        ),
    )


class ServerAddressByClientCIDR(BaseModel):
    clientCIDR: str = Field(
        ...,
        description=(
            "The CIDR with which clients can match their IP to figure out the server"
            " address that they should use."
        ),
    )
    serverAddress: str = Field(
        ...,
        description=(
            "Address of this server, suitable for a client that matches the above CIDR."
            " This can be a hostname, hostname:port, IP or IP:port."
        ),
    )


class APIResource(BaseModel):
    categories: Optional[List[str]] = Field(
        None,
        description=(
            "categories is a list of the grouped resources this resource belongs to"
            " (e.g. 'all')"
        ),
    )
    group: Optional[str] = Field(
        None,
        description=(
            "group is the preferred group of the resource.  Empty implies the group of"
            " the containing resource list. For subresources, this may have a different"
            ' value, for example: Scale".'
        ),
    )
    kind: str = Field(
        ...,
        description=(
            "kind is the kind for the resource (e.g. 'Foo' is the kind for a resource"
            " 'foo')"
        ),
    )
    name: str = Field(..., description="name is the plural name of the resource.")
    namespaced: bool = Field(
        ..., description="namespaced indicates if a resource is namespaced or not."
    )
    shortNames: Optional[List[str]] = Field(
        None,
        description="shortNames is a list of suggested short names of the resource.",
    )
    singularName: str = Field(
        ...,
        description=(
            "singularName is the singular name of the resource.  This allows clients to"
            " handle plural and singular opaquely. The singularName is more correct for"
            " reporting status on a single item and both singular and plural are"
            " allowed from the kubectl CLI interface."
        ),
    )
    storageVersionHash: Optional[str] = Field(
        None,
        description=(
            "The hash value of the storage version, the version this resource is"
            " converted to when written to the data store. Value must be treated as"
            " opaque by clients. Only equality comparison on the value is valid. This"
            " is an alpha feature and may change or be removed in the future. The field"
            " is populated by the apiserver only if the StorageVersionHash feature gate"
            " is enabled. This field will remain optional even if it graduates."
        ),
    )
    verbs: List[str] = Field(
        ...,
        description=(
            "verbs is a list of supported kube verbs (this includes get, list, watch,"
            " create, update, patch, delete, deletecollection, and proxy)"
        ),
    )
    version: Optional[str] = Field(
        None,
        description=(
            "version is the preferred version of the resource.  Empty implies the"
            " version of the containing resource list For subresources, this may have a"
            " different value, for example: v1 (while inside a v1beta1 version of the"
            " core resource's group)\"."
        ),
    )


class APIResourceList(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description=(
            "APIVersion defines the versioned schema of this representation of an"
            " object. Servers should convert recognized schemas to the latest internal"
            " value, and may reject unrecognized values. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources"
        ),
    )
    groupVersion: str = Field(
        ...,
        description=(
            "groupVersion is the group and version this APIResourceList is for."
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
    resources: List[APIResource] = Field(
        ...,
        description=(
            "resources contains the name of the resources and if they are namespaced."
        ),
    )


class FieldsV1(BaseModel):
    pass


class ListMeta(BaseModel):
    continue_: Optional[str] = Field(
        None,
        alias="continue",
        description=(
            "continue may be set if the user set a limit on the number of items"
            " returned, and indicates that the server has more data available. The"
            " value is opaque and may be used to issue another request to the endpoint"
            " that served this list to retrieve the next set of available objects."
            " Continuing a consistent list may not be possible if the server"
            " configuration has changed or more than a few minutes have passed. The"
            " resourceVersion field returned when using this continue value will be"
            " identical to the value in the first response, unless you have received"
            " this token from an error message."
        ),
    )
    remainingItemCount: Optional[int] = Field(
        None,
        description=(
            "remainingItemCount is the number of subsequent items in the list which are"
            " not included in this list response. If the list request contained label"
            " or field selectors, then the number of remaining items is unknown and the"
            " field will be left unset and omitted during serialization. If the list is"
            " complete (either because it is not chunking or because this is the last"
            " chunk), then there are no more remaining items and this field will be"
            " left unset and omitted during serialization. Servers older than v1.15 do"
            " not set this field. The intended use of the remainingItemCount is"
            " *estimating* the size of a collection. Clients should not rely on the"
            " remainingItemCount to be set or to be exact."
        ),
    )
    resourceVersion: Optional[str] = Field(
        None,
        description=(
            "String that identifies the server's internal version of this object that"
            " can be used by clients to determine when objects have changed. Value must"
            " be treated as opaque by clients and passed unmodified back to the server."
            " Populated by the system. Read-only. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency"
        ),
    )
    selfLink: Optional[str] = Field(
        None,
        description=(
            "Deprecated: selfLink is a legacy read-only field that is no longer"
            " populated by the system."
        ),
    )


class MicroTime(BaseModel):
    __root__: datetime = Field(
        ...,
        description="MicroTime is version of Time with microsecond level precision.",
    )


class OwnerReference(BaseModel):
    apiVersion: str = Field(..., description="API version of the referent.")
    blockOwnerDeletion: Optional[bool] = Field(
        None,
        description=(
            'If true, AND if the owner has the "foregroundDeletion" finalizer, then the'
            " owner cannot be deleted from the key-value store until this reference is"
            " removed. See"
            " https://kubernetes.io/docs/concepts/architecture/garbage-collection/#foreground-deletion"
            " for how the garbage collector interacts with this field and enforces the"
            " foreground deletion. Defaults to false. To set this field, a user needs"
            ' "delete" permission of the owner, otherwise 422 (Unprocessable Entity)'
            " will be returned."
        ),
    )
    controller: Optional[bool] = Field(
        None, description="If true, this reference points to the managing controller."
    )
    kind: str = Field(
        ...,
        description=(
            "Kind of the referent. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"
        ),
    )
    name: str = Field(
        ...,
        description=(
            "Name of the referent. More info:"
            " https://kubernetes.io/docs/concepts/overview/working-with-objects/names#names"
        ),
    )
    uid: str = Field(
        ...,
        description=(
            "UID of the referent. More info:"
            " https://kubernetes.io/docs/concepts/overview/working-with-objects/names#uids"
        ),
    )


class Patch(BaseModel):
    pass


class Preconditions(BaseModel):
    resourceVersion: Optional[str] = Field(
        None, description="Specifies the target ResourceVersion"
    )
    uid: Optional[str] = Field(None, description="Specifies the target UID.")


class StatusCause(BaseModel):
    field: Optional[str] = Field(
        None,
        description=(
            "The field of the resource that has caused this error, as named by its JSON"
            " serialization. May include dot and postfix notation for nested"
            " attributes. Arrays are zero-indexed.  Fields may appear more than once in"
            " an array of causes due to fields having multiple errors."
            ' Optional.\n\nExamples:\n  "name" - the field "name" on the current'
            ' resource\n  "items[0].name" - the field "name" on the first array entry'
            ' in "items"'
        ),
    )
    message: Optional[str] = Field(
        None,
        description=(
            "A human-readable description of the cause of the error.  This field may be"
            " presented as-is to a reader."
        ),
    )
    reason: Optional[str] = Field(
        None,
        description=(
            "A machine-readable description of the cause of the error. If this value is"
            " empty there is no information available."
        ),
    )


class StatusDetails(BaseModel):
    causes: Optional[List[StatusCause]] = Field(
        None,
        description=(
            "The Causes array includes more details associated with the StatusReason"
            " failure. Not all StatusReasons may provide detailed causes."
        ),
    )
    group: Optional[str] = Field(
        None,
        description=(
            "The group attribute of the resource associated with the status"
            " StatusReason."
        ),
    )
    kind: Optional[str] = Field(
        None,
        description=(
            "The kind attribute of the resource associated with the status"
            " StatusReason. On some operations may differ from the requested resource"
            " Kind. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"
        ),
    )
    name: Optional[str] = Field(
        None,
        description=(
            "The name attribute of the resource associated with the status StatusReason"
            " (when there is a single name which can be described)."
        ),
    )
    retryAfterSeconds: Optional[int] = Field(
        None,
        description=(
            "If specified, the time in seconds before the operation should be retried."
            " Some errors may indicate the client must take an alternate action - for"
            " those errors this field may indicate how long to wait before taking the"
            " alternate action."
        ),
    )
    uid: Optional[str] = Field(
        None,
        description=(
            "UID of the resource. (when there is a single resource which can be"
            " described). More info:"
            " https://kubernetes.io/docs/concepts/overview/working-with-objects/names#uids"
        ),
    )


class Time(BaseModel):
    __root__: datetime = Field(
        ...,
        description=(
            "Time is a wrapper around time.Time which supports correct marshaling to"
            " YAML and JSON.  Wrappers are provided for many of the factory methods"
            " that the time package offers."
        ),
    )


class LabelSelectorRequirement(BaseModel):
    key: str = Field(
        ..., description="key is the label key that the selector applies to."
    )
    operator: str = Field(
        ...,
        description=(
            "operator represents a key's relationship to a set of values. Valid"
            " operators are In, NotIn, Exists and DoesNotExist."
        ),
    )
    values: Optional[List[str]] = Field(
        None,
        description=(
            "values is an array of string values. If the operator is In or NotIn, the"
            " values array must be non-empty. If the operator is Exists or"
            " DoesNotExist, the values array must be empty. This array is replaced"
            " during a strategic merge patch."
        ),
    )


class APIGroup(BaseModel):
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
    name: str = Field(..., description="name is the name of the group.")
    preferredVersion: Optional[GroupVersionForDiscovery] = Field(
        None,
        description=(
            "preferredVersion is the version preferred by the API server, which"
            " probably is the storage version."
        ),
    )
    serverAddressByClientCIDRs: Optional[List[ServerAddressByClientCIDR]] = Field(
        None,
        description=(
            "a map of client CIDR to server address that is serving this group. This is"
            " to help clients reach servers in the most network-efficient way possible."
            " Clients can use the appropriate server address as per the CIDR that they"
            " match. In case of multiple matches, clients should use the longest"
            " matching CIDR. The server returns only those CIDRs that it thinks that"
            " the client can match. For example: the master will return an internal IP"
            " CIDR only, if the client reaches the server using an internal IP. Server"
            " looks at X-Forwarded-For header or X-Real-Ip header or request.RemoteAddr"
            " (in that order) to get the client IP."
        ),
    )
    versions: List[GroupVersionForDiscovery] = Field(
        ..., description="versions are the versions supported in this group."
    )


class DeleteOptions(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description=(
            "APIVersion defines the versioned schema of this representation of an"
            " object. Servers should convert recognized schemas to the latest internal"
            " value, and may reject unrecognized values. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources"
        ),
    )
    dryRun: Optional[List[str]] = Field(
        None,
        description=(
            "When present, indicates that modifications should not be persisted. An"
            " invalid or unrecognized dryRun directive will result in an error response"
            " and no further processing of the request. Valid values are: - All: all"
            " dry run stages will be processed"
        ),
    )
    gracePeriodSeconds: Optional[int] = Field(
        None,
        description=(
            "The duration in seconds before the object should be deleted. Value must be"
            " non-negative integer. The value zero indicates delete immediately. If"
            " this value is nil, the default grace period for the specified type will"
            " be used. Defaults to a per object value if not specified. zero means"
            " delete immediately."
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
    orphanDependents: Optional[bool] = Field(
        None,
        description=(
            "Deprecated: please use the PropagationPolicy, this field will be"
            " deprecated in 1.7. Should the dependent objects be orphaned. If"
            ' true/false, the "orphan" finalizer will be added to/removed from the'
            " object's finalizers list. Either this field or PropagationPolicy may be"
            " set, but not both."
        ),
    )
    preconditions: Optional[Preconditions] = Field(
        None,
        description=(
            "Must be fulfilled before a deletion is carried out. If not possible, a 409"
            " Conflict status will be returned."
        ),
    )
    propagationPolicy: Optional[str] = Field(
        None,
        description=(
            "Whether and how garbage collection will be performed. Either this field or"
            " OrphanDependents may be set, but not both. The default policy is decided"
            " by the existing finalizer set in the metadata.finalizers and the"
            " resource-specific default policy. Acceptable values are: 'Orphan' -"
            " orphan the dependents; 'Background' - allow the garbage collector to"
            " delete the dependents in the background; 'Foreground' - a cascading"
            " policy that deletes all dependents in the foreground."
        ),
    )


class ManagedFieldsEntry(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description=(
            "APIVersion defines the version of this resource that this field set"
            ' applies to. The format is "group/version" just like the top-level'
            " APIVersion field. It is necessary to track the version of a field set"
            " because it cannot be automatically converted."
        ),
    )
    fieldsType: Optional[str] = Field(
        None,
        description=(
            "FieldsType is the discriminator for the different fields format and"
            ' version. There is currently only one possible value: "FieldsV1"'
        ),
    )
    fieldsV1: Optional[FieldsV1] = Field(
        None,
        description=(
            "FieldsV1 holds the first JSON version format as described in the"
            ' "FieldsV1" type.'
        ),
    )
    manager: Optional[str] = Field(
        None,
        description="Manager is an identifier of the workflow managing these fields.",
    )
    operation: Optional[str] = Field(
        None,
        description=(
            "Operation is the type of operation which lead to this ManagedFieldsEntry"
            " being created. The only valid values for this field are 'Apply' and"
            " 'Update'."
        ),
    )
    subresource: Optional[str] = Field(
        None,
        description=(
            "Subresource is the name of the subresource used to update that object, or"
            " empty string if the object was updated through the main resource. The"
            " value of this field is used to distinguish between managers, even if they"
            " share the same name. For example, a status update will be distinct from a"
            " regular update using the same manager name. Note that the APIVersion"
            " field is not related to the Subresource field and it always corresponds"
            " to the version of the main resource."
        ),
    )
    time: Optional[Time] = Field(
        None,
        description=(
            "Time is the timestamp of when the ManagedFields entry was added. The"
            " timestamp will also be updated if a field is added, the manager changes"
            " any of the owned fields value or removes a field. The timestamp does not"
            " update when a field is removed from the entry because another manager"
            " took it over."
        ),
    )


class ObjectMeta(BaseModel):
    annotations: Optional[Dict[str, str]] = Field(
        None,
        description=(
            "Annotations is an unstructured key value map stored with a resource that"
            " may be set by external tools to store and retrieve arbitrary metadata."
            " They are not queryable and should be preserved when modifying objects."
            " More info:"
            " https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations"
        ),
    )
    creationTimestamp: Optional[Time] = Field(
        None,
        description=(
            "CreationTimestamp is a timestamp representing the server time when this"
            " object was created. It is not guaranteed to be set in happens-before"
            " order across separate operations. Clients may not set this value. It is"
            " represented in RFC3339 form and is in UTC.\n\nPopulated by the system."
            " Read-only. Null for lists. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata"
        ),
    )
    deletionGracePeriodSeconds: Optional[int] = Field(
        None,
        description=(
            "Number of seconds allowed for this object to gracefully terminate before"
            " it will be removed from the system. Only set when deletionTimestamp is"
            " also set. May only be shortened. Read-only."
        ),
    )
    deletionTimestamp: Optional[Time] = Field(
        None,
        description=(
            "DeletionTimestamp is RFC 3339 date and time at which this resource will be"
            " deleted. This field is set by the server when a graceful deletion is"
            " requested by the user, and is not directly settable by a client. The"
            " resource is expected to be deleted (no longer visible from resource"
            " lists, and not reachable by name) after the time in this field, once the"
            " finalizers list is empty. As long as the finalizers list contains items,"
            " deletion is blocked. Once the deletionTimestamp is set, this value may"
            " not be unset or be set further into the future, although it may be"
            " shortened or the resource may be deleted prior to this time. For example,"
            " a user may request that a pod is deleted in 30 seconds. The Kubelet will"
            " react by sending a graceful termination signal to the containers in the"
            " pod. After that 30 seconds, the Kubelet will send a hard termination"
            " signal (SIGKILL) to the container and after cleanup, remove the pod from"
            " the API. In the presence of network partitions, this object may still"
            " exist after this timestamp, until an administrator or automated process"
            " can determine the resource is fully terminated. If not set, graceful"
            " deletion of the object has not been requested.\n\nPopulated by the system"
            " when a graceful deletion is requested. Read-only. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata"
        ),
    )
    finalizers: Optional[List[str]] = Field(
        None,
        description=(
            "Must be empty before the object is deleted from the registry. Each entry"
            " is an identifier for the responsible component that will remove the entry"
            " from the list. If the deletionTimestamp of the object is non-nil, entries"
            " in this list can only be removed. Finalizers may be processed and removed"
            " in any order.  Order is NOT enforced because it introduces significant"
            " risk of stuck finalizers. finalizers is a shared field, any actor with"
            " permission can reorder it. If the finalizer list is processed in order,"
            " then this can lead to a situation in which the component responsible for"
            " the first finalizer in the list is waiting for a signal (field value,"
            " external system, or other) produced by a component responsible for a"
            " finalizer later in the list, resulting in a deadlock. Without enforced"
            " ordering finalizers are free to order amongst themselves and are not"
            " vulnerable to ordering changes in the list."
        ),
    )
    generateName: Optional[str] = Field(
        None,
        description=(
            "GenerateName is an optional prefix, used by the server, to generate a"
            " unique name ONLY IF the Name field has not been provided. If this field"
            " is used, the name returned to the client will be different than the name"
            " passed. This value will also be combined with a unique suffix. The"
            " provided value has the same validation rules as the Name field, and may"
            " be truncated by the length of the suffix required to make the value"
            " unique on the server.\n\nIf this field is specified and the generated"
            " name exists, the server will return a 409.\n\nApplied only if Name is not"
            " specified. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#idempotency"
        ),
    )
    generation: Optional[int] = Field(
        None,
        description=(
            "A sequence number representing a specific generation of the desired state."
            " Populated by the system. Read-only."
        ),
    )
    labels: Optional[Dict[str, str]] = Field(
        None,
        description=(
            "Map of string keys and values that can be used to organize and categorize"
            " (scope and select) objects. May match selectors of replication"
            " controllers and services. More info:"
            " https://kubernetes.io/docs/concepts/overview/working-with-objects/labels"
        ),
    )
    managedFields: Optional[List[ManagedFieldsEntry]] = Field(
        None,
        description=(
            "ManagedFields maps workflow-id and version to the set of fields that are"
            " managed by that workflow. This is mostly for internal housekeeping, and"
            " users typically shouldn't need to set or understand this field. A"
            " workflow can be the user's name, a controller's name, or the name of a"
            ' specific apply path like "ci-cd". The set of fields is always in the'
            " version that the workflow used when modifying the object."
        ),
    )
    name: Optional[str] = Field(
        None,
        description=(
            "Name must be unique within a namespace. Is required when creating"
            " resources, although some resources may allow a client to request the"
            " generation of an appropriate name automatically. Name is primarily"
            " intended for creation idempotence and configuration definition. Cannot be"
            " updated. More info:"
            " https://kubernetes.io/docs/concepts/overview/working-with-objects/names#names"
        ),
    )
    namespace: Optional[str] = Field(
        None,
        description=(
            "Namespace defines the space within which each name must be unique. An"
            ' empty namespace is equivalent to the "default" namespace, but "default"'
            " is the canonical representation. Not all objects are required to be"
            " scoped to a namespace - the value of this field for those objects will be"
            " empty.\n\nMust be a DNS_LABEL. Cannot be updated. More info:"
            " https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces"
        ),
    )
    ownerReferences: Optional[List[OwnerReference]] = Field(
        None,
        description=(
            "List of objects depended by this object. If ALL objects in the list have"
            " been deleted, this object will be garbage collected. If this object is"
            " managed by a controller, then an entry in this list will point to this"
            " controller, with the controller field set to true. There cannot be more"
            " than one managing controller."
        ),
    )
    resourceVersion: Optional[str] = Field(
        None,
        description=(
            "An opaque value that represents the internal version of this object that"
            " can be used by clients to determine when objects have changed. May be"
            " used for optimistic concurrency, change detection, and the watch"
            " operation on a resource or set of resources. Clients must treat these"
            " values as opaque and passed unmodified back to the server. They may only"
            " be valid for a particular resource or set of resources.\n\nPopulated by"
            " the system. Read-only. Value must be treated as opaque by clients and ."
            " More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency"
        ),
    )
    selfLink: Optional[str] = Field(
        None,
        description=(
            "Deprecated: selfLink is a legacy read-only field that is no longer"
            " populated by the system."
        ),
    )
    uid: Optional[str] = Field(
        None,
        description=(
            "UID is the unique in time and space value for this object. It is typically"
            " generated by the server on successful creation of a resource and is not"
            " allowed to change on PUT operations.\n\nPopulated by the system."
            " Read-only. More info:"
            " https://kubernetes.io/docs/concepts/overview/working-with-objects/names#uids"
        ),
    )


class Status(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description=(
            "APIVersion defines the versioned schema of this representation of an"
            " object. Servers should convert recognized schemas to the latest internal"
            " value, and may reject unrecognized values. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources"
        ),
    )
    code: Optional[int] = Field(
        None, description="Suggested HTTP return code for this status, 0 if not set."
    )
    details: Optional[StatusDetails] = Field(
        None,
        description=(
            "Extended data associated with the reason.  Each reason may define its own"
            " extended details. This field is optional and the data returned is not"
            " guaranteed to conform to any schema except that defined by the reason"
            " type."
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
    message: Optional[str] = Field(
        None,
        description="A human-readable description of the status of this operation.",
    )
    metadata: Optional[ListMeta] = Field(
        None,
        description=(
            "Standard list metadata. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"
        ),
    )
    reason: Optional[str] = Field(
        None,
        description=(
            'A machine-readable description of why this operation is in the "Failure"'
            " status. If this value is empty there is no information available. A"
            " Reason clarifies an HTTP status code but does not override it."
        ),
    )
    status: Optional[str] = Field(
        None,
        description=(
            'Status of the operation. One of: "Success" or "Failure". More info:'
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status"
        ),
    )


class WatchEvent(BaseModel):
    object: runtime.RawExtension = Field(
        ...,
        description=(
            "Object is:\n * If Type is Added or Modified: the new state of the"
            " object.\n * If Type is Deleted: the state of the object immediately"
            " before deletion.\n * If Type is Error: *Status is recommended; other"
            " types may make sense\n   depending on context."
        ),
    )
    type: str


class LabelSelector(BaseModel):
    matchExpressions: Optional[List[LabelSelectorRequirement]] = Field(
        None,
        description=(
            "matchExpressions is a list of label selector requirements. The"
            " requirements are ANDed."
        ),
    )
    matchLabels: Optional[Dict[str, str]] = Field(
        None,
        description=(
            "matchLabels is a map of {key,value} pairs. A single {key,value} in the"
            " matchLabels map is equivalent to an element of matchExpressions, whose"
            ' key field is "key", the operator is "In", and the values array contains'
            ' only "value". The requirements are ANDed.'
        ),
    )


class APIGroupList(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description=(
            "APIVersion defines the versioned schema of this representation of an"
            " object. Servers should convert recognized schemas to the latest internal"
            " value, and may reject unrecognized values. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources"
        ),
    )
    groups: List[APIGroup] = Field(..., description="groups is a list of APIGroup.")
    kind: Optional[str] = Field(
        None,
        description=(
            "Kind is a string value representing the REST resource this object"
            " represents. Servers may infer this from the endpoint the client submits"
            " requests to. Cannot be updated. In CamelCase. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"
        ),
    )


class Condition(BaseModel):
    lastTransitionTime: Time = Field(
        ...,
        description=(
            "lastTransitionTime is the last time the condition transitioned from one"
            " status to another. This should be when the underlying condition changed. "
            " If that is not known, then using the time when the API field changed is"
            " acceptable."
        ),
    )
    message: str = Field(
        ...,
        description=(
            "message is a human readable message indicating details about the"
            " transition. This may be an empty string."
        ),
    )
    observedGeneration: Optional[int] = Field(
        None,
        description=(
            "observedGeneration represents the .metadata.generation that the condition"
            " was set based upon. For instance, if .metadata.generation is currently"
            " 12, but the .status.conditions[x].observedGeneration is 9, the condition"
            " is out of date with respect to the current state of the instance."
        ),
    )
    reason: str = Field(
        ...,
        description=(
            "reason contains a programmatic identifier indicating the reason for the"
            " condition's last transition. Producers of specific condition types may"
            " define expected values and meanings for this field, and whether the"
            " values are considered a guaranteed API. The value should be a CamelCase"
            " string. This field may not be empty."
        ),
    )
    status: str = Field(
        ..., description="status of the condition, one of True, False, Unknown."
    )
    type: str = Field(
        ...,
        description="type of condition in CamelCase or in foo.example.com/CamelCase.",
    )


class APIVersions(BaseModel):
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
    serverAddressByClientCIDRs: List[ServerAddressByClientCIDR] = Field(
        ...,
        description=(
            "a map of client CIDR to server address that is serving this group. This is"
            " to help clients reach servers in the most network-efficient way possible."
            " Clients can use the appropriate server address as per the CIDR that they"
            " match. In case of multiple matches, clients should use the longest"
            " matching CIDR. The server returns only those CIDRs that it thinks that"
            " the client can match. For example: the master will return an internal IP"
            " CIDR only, if the client reaches the server using an internal IP. Server"
            " looks at X-Forwarded-For header or X-Real-Ip header or request.RemoteAddr"
            " (in that order) to get the client IP."
        ),
    )
    versions: List[str] = Field(
        ..., description="versions are the api versions that are available."
    )
