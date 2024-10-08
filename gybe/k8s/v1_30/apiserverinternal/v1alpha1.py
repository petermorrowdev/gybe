"""Models generated from Kubernetes OpenAPI Spec."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Literal, Optional

import gybe.k8s.v1_30.meta.v1
from gybe.k8s.types import JSONObj, K8sResource, K8sSpec


@dataclass
class ServerStorageVersion(K8sSpec):
    """An API server instance reports the version it can decode and the version it encodes objects to when
    persisting objects in the backend.

    Attributes:
        apiServerID: The ID of the reporting API server.
        decodableVersions: The API server can decode objects encoded in these versions. The encodingVersion
            must be included in the decodableVersions.
        encodingVersion: The API server encodes the object to this version when persisting it in the backend
            (e.g., etcd).
        servedVersions: The API server can serve these versions. DecodableVersions must include all
            ServedVersions.

    """

    apiServerID: Optional[str] = None
    decodableVersions: Optional[List[str]] = None
    encodingVersion: Optional[str] = None
    servedVersions: Optional[List[str]] = None


@dataclass
class StorageVersion(K8sResource):
    """Storage version of a specific resource.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: The name is <group>.<resource>.
        spec: Spec is an empty spec. It is here to comply with Kubernetes API style.
        status: API server instances report the version they can decode and the version they encode objects to
            when persisting objects in the backend.

    """

    spec: JSONObj
    status: StorageVersionStatus
    apiVersion: Literal['admissionregistration.k8s.io/v1alpha1'] = 'admissionregistration.k8s.io/v1alpha1'
    kind: Literal['StorageVersion'] = 'StorageVersion'
    metadata: Optional[gybe.k8s.v1_30.meta.v1.ObjectMeta] = None


@dataclass
class StorageVersionCondition(K8sSpec):
    """Describes the state of the storageVersion at a certain point.

    Attributes:
        lastTransitionTime: Last time the condition transitioned from one status to another.
        message: A human readable message indicating details about the transition.
        observedGeneration: If set, this represents the .metadata.generation that the condition was set based
            upon.
        reason: The reason for the condition's last transition.
        status: Status of the condition, one of True, False, Unknown.
        type: Type of the condition.

    """

    type: str
    status: str
    reason: str
    message: str
    lastTransitionTime: Optional[str] = None
    observedGeneration: Optional[int] = None


@dataclass
class StorageVersionList(K8sSpec):
    """A list of StorageVersions.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        items: Items holds a list of StorageVersion
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard list metadata.

    """

    items: List[StorageVersion]
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[JSONObj] = None


@dataclass
class StorageVersionStatus(K8sSpec):
    """API server instances report the versions they can decode and the version they encode objects to when
    persisting objects in the backend.

    Attributes:
        commonEncodingVersion: If all API server instances agree on the same encoding storage version, then
            this field is set to that version. Otherwise this field is left empty. API servers should finish
            updating its storageVersionStatus entry before serving write operations, so that this field will
            be in sync with the reality.
        conditions: The latest available observations of the storageVersion's state.
        storageVersions: The reported versions per API server instance.

    """

    commonEncodingVersion: Optional[str] = None
    conditions: Optional[List[StorageVersionCondition]] = None
    storageVersions: Optional[List[ServerStorageVersion]] = None
