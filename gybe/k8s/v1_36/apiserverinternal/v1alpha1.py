"""Models generated from Kubernetes OpenAPI Spec."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Literal, Optional

import gybe.k8s.v1_36.meta.v1 as _meta_v1
from gybe.k8s.types import JSONObj, K8sResource, K8sSpec


@dataclass
class ServerStorageVersion(K8sSpec):
    """An API server instance reports the version it can decode and the version it encodes objects to when
    persisting objects in the backend.

    Attributes:
        apiServerID: apiServerID is the ID of the reporting API server.
        decodableVersions: decodableVersions are the encoding versions the API server can handle to decode.
            The API server can decode objects encoded in these versions. The encodingVersion must be included
            in the decodableVersions.
        encodingVersion: encodingVersion the API server encodes the object to when persisting it in the
            backend (e.g., etcd).
        servedVersions: servedVersions lists all versions the API server can serve. DecodableVersions must
            include all ServedVersions.

    """

    apiServerID: str
    encodingVersion: str
    decodableVersions: List[str]
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
        metadata: metadata is the standard object metadata. The name is <group>.<resource>.
        spec: spec is an empty spec. It is here to comply with Kubernetes API style.
        status: status on the version the API server instance can decode from and encode objects to when
            persisting objects in the backend.

    """

    metadata: _meta_v1.ObjectMeta
    apiVersion: Literal['internal.apiserver.k8s.io/v1alpha1'] = 'internal.apiserver.k8s.io/v1alpha1'
    kind: Literal['StorageVersion'] = 'StorageVersion'
    spec: Optional[JSONObj] = None
    status: Optional[StorageVersionStatus] = None


@dataclass
class StorageVersionCondition(K8sSpec):
    """Describes the state of the storageVersion at a certain point.

    Attributes:
        lastTransitionTime: lastTransitionTime is the last time the condition transitioned from one status to
            another.
        message: message is a human readable string indicating details about the transition.
        observedGeneration: observedGeneration represents the .metadata.generation that the condition was set
            based upon, if field is set.
        reason: reason for the condition's last transition.
        status: status of the condition, one of True, False, Unknown.
        type: type of the condition.

    """

    type: str
    status: str
    reason: str
    message: str
    lastTransitionTime: Optional[str] = None
    observedGeneration: Optional[int] = None


@dataclass
class StorageVersionStatus(K8sSpec):
    """API server instances report the versions they can decode and the version they encode objects to when
    persisting objects in the backend.

    Attributes:
        commonEncodingVersion: commonEncodingVersion is set to an encoding storage version if all API server
            instances share that same version. If they don't share one storage version, this field is left
            empty. API servers should finish updating its storageVersionStatus entry before serving write
            operations, so that this field will be in sync with the reality.
        conditions: conditions lists the latest available observations of the storageVersion's state.
        storageVersions: storageVersions lists the reported versions per API server instance.

    """

    commonEncodingVersion: Optional[str] = None
    conditions: Optional[List[StorageVersionCondition]] = None
    storageVersions: Optional[List[ServerStorageVersion]] = None
