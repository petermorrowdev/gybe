from __future__ import annotations
from typing import List, Optional
from pydantic import BaseModel, Field
from ...apimachinery.pkg.apis.meta import v1


class ServerStorageVersion(BaseModel):
    apiServerID: Optional[str] = Field(
        None, description="The ID of the reporting API server."
    )
    decodableVersions: Optional[List[str]] = Field(
        None,
        description=(
            "The API server can decode objects encoded in these versions. The"
            " encodingVersion must be included in the decodableVersions."
        ),
    )
    encodingVersion: Optional[str] = Field(
        None,
        description=(
            "The API server encodes the object to this version when persisting it in"
            " the backend (e.g., etcd)."
        ),
    )


class StorageVersionSpec(BaseModel):
    pass


class StorageVersionCondition(BaseModel):
    lastTransitionTime: Optional[v1.Time] = Field(
        None,
        description="Last time the condition transitioned from one status to another.",
    )
    message: Optional[str] = Field(
        None,
        description="A human readable message indicating details about the transition.",
    )
    observedGeneration: Optional[int] = Field(
        None,
        description=(
            "If set, this represents the .metadata.generation that the condition was"
            " set based upon."
        ),
    )
    reason: str = Field(
        ..., description="The reason for the condition's last transition."
    )
    status: str = Field(
        ..., description="Status of the condition, one of True, False, Unknown."
    )
    type: str = Field(..., description="Type of the condition.")


class StorageVersionStatus(BaseModel):
    commonEncodingVersion: Optional[str] = Field(
        None,
        description=(
            "If all API server instances agree on the same encoding storage version,"
            " then this field is set to that version. Otherwise this field is left"
            " empty. API servers should finish updating its storageVersionStatus entry"
            " before serving write operations, so that this field will be in sync with"
            " the reality."
        ),
    )
    conditions: Optional[List[StorageVersionCondition]] = Field(
        None,
        description="The latest available observations of the storageVersion's state.",
    )
    storageVersions: Optional[List[ServerStorageVersion]] = Field(
        None, description="The reported versions per API server instance."
    )


class StorageVersion(BaseModel):
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
    metadata: Optional[v1.ObjectMeta] = Field(
        None, description="The name is <group>.<resource>."
    )
    spec: StorageVersionSpec = Field(
        ...,
        description=(
            "Spec is an empty spec. It is here to comply with Kubernetes API style."
        ),
    )
    status: StorageVersionStatus = Field(
        ...,
        description=(
            "API server instances report the version they can decode and the version"
            " they encode objects to when persisting objects in the backend."
        ),
    )


class StorageVersionList(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description=(
            "APIVersion defines the versioned schema of this representation of an"
            " object. Servers should convert recognized schemas to the latest internal"
            " value, and may reject unrecognized values. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources"
        ),
    )
    items: List[StorageVersion] = Field(
        ..., description="Items holds a list of StorageVersion"
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
    metadata: Optional[v1.ListMeta] = Field(
        None,
        description=(
            "Standard list metadata. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata"
        ),
    )
