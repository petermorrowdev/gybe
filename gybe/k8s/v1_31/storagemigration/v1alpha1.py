"""Models generated from Kubernetes OpenAPI Spec."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Literal, Optional

import gybe.k8s.v1_31.meta.v1
from gybe.k8s.types import JSONObj, K8sResource, K8sSpec


@dataclass
class GroupVersionResource(K8sSpec):
    """The names of the group, the version, and the resource.

    Attributes:
        group: The name of the group.
        resource: The name of the resource.
        version: The name of the version.

    """

    group: Optional[str] = None
    resource: Optional[str] = None
    version: Optional[str] = None


@dataclass
class MigrationCondition(K8sSpec):
    """Describes the state of a migration at a certain point.

    Attributes:
        lastUpdateTime: The last time this condition was updated.
        message: A human readable message indicating details about the transition.
        reason: The reason for the condition's last transition.
        status: Status of the condition, one of True, False, Unknown.
        type: Type of the condition.

    """

    type: str
    status: str
    lastUpdateTime: Optional[str] = None
    message: Optional[str] = None
    reason: Optional[str] = None


@dataclass
class StorageVersionMigration(K8sResource):
    """StorageVersionMigration represents a migration of stored data to the latest storage version.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object metadata.
        spec: Specification of the migration.
        status: Status of the migration.

    """

    apiVersion: Literal['storage.k8s.io/v1alpha1'] = 'storage.k8s.io/v1alpha1'
    kind: Literal['StorageVersionMigration'] = 'StorageVersionMigration'
    metadata: Optional[gybe.k8s.v1_31.meta.v1.ObjectMeta] = None
    spec: Optional[StorageVersionMigrationSpec] = None
    status: Optional[StorageVersionMigrationStatus] = None


@dataclass
class StorageVersionMigrationList(K8sSpec):
    """StorageVersionMigrationList is a collection of storage version migrations.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        items: Items is the list of StorageVersionMigration
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard list metadata

    """

    items: List[StorageVersionMigration]
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[JSONObj] = None


@dataclass
class StorageVersionMigrationSpec(K8sSpec):
    """Spec of the storage version migration.

    Attributes:
        continueToken: The token used in the list options to get the next chunk of objects to migrate. When
            the .status.conditions indicates the migration is 'Running', users can use this token to check the
            progress of the migration.
        resource: The resource that is being migrated. The migrator sends requests to the endpoint serving the
            resource. Immutable.

    """

    resource: GroupVersionResource
    continueToken: Optional[str] = None


@dataclass
class StorageVersionMigrationStatus(K8sSpec):
    """Status of the storage version migration.

    Attributes:
        conditions: The latest available observations of the migration's current state.
        resourceVersion: ResourceVersion to compare with the GC cache for performing the migration. This is
            the current resource version of given group, version and resource when kube-controller-manager
            first observes this StorageVersionMigration resource.

    """

    conditions: Optional[List[MigrationCondition]] = None
    resourceVersion: Optional[str] = None
