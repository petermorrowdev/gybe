"""Models generated from Kubernetes OpenAPI Spec."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Literal, Optional

import gybe.k8s.v1_35.meta.v1 as _meta_v1
from gybe.k8s.types import K8sResource, K8sSpec


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

    apiVersion: Literal['storagemigration.k8s.io/v1beta1'] = 'storagemigration.k8s.io/v1beta1'
    kind: Literal['StorageVersionMigration'] = 'StorageVersionMigration'
    metadata: Optional[_meta_v1.ObjectMeta] = None
    spec: Optional[StorageVersionMigrationSpec] = None
    status: Optional[StorageVersionMigrationStatus] = None


@dataclass
class StorageVersionMigrationSpec(K8sSpec):
    """Spec of the storage version migration.

    Attributes:
        resource: The resource that is being migrated. The migrator sends requests to the endpoint serving the
            resource. Immutable.

    """

    resource: _meta_v1.GroupResource


@dataclass
class StorageVersionMigrationStatus(K8sSpec):
    """Status of the storage version migration.

    Attributes:
        conditions: The latest available observations of the migration's current state.
        resourceVersion: ResourceVersion to compare with the GC cache for performing the migration. This is
            the current resource version of given group, version and resource when kube-controller-manager
            first observes this StorageVersionMigration resource.

    """

    conditions: Optional[List[_meta_v1.Condition]] = None
    resourceVersion: Optional[str] = None
