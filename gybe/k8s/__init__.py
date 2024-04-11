"""Kubernetes models as dataclasses copied from k8s' OpenAPI V3 Spec."""

from gybe.k8s.v1_29.apps.v1 import (
    DaemonSet,
    DaemonSetSpec,
    Deployment,
    DeploymentSpec,
    StatefulSet,
    StatefulSetSpec,
)
from gybe.k8s.v1_29.batch.v1 import Job, JobSpec
from gybe.k8s.v1_29.core.v1 import (
    Container,
    EnvVar,
    HTTPGetAction,
    PersistentVolume,
    PersistentVolumeClaim,
    PersistentVolumeSpec,
    Pod,
    PodSpec,
    Probe,
    ResourceRequirements,
    Secret,
    SecurityContext,
    Service,
    ServiceSpec,
)
from gybe.k8s.v1_29.meta.v1 import ObjectMeta

__all__ = [
    'Deployment',
    'DeploymentSpec',
    'StatefulSet',
    'StatefulSetSpec',
    'Job',
    'JobSpec',
    'DaemonSet',
    'DaemonSetSpec',
    'Pod',
    'PodSpec',
    'Container',
    'Secret',
    'ResourceRequirements',
    'EnvVar',
    'SecurityContext',
    'Probe',
    'HTTPGetAction',
    'Service',
    'ServiceSpec',
    'ObjectMeta',
    'PersistentVolume',
    'PersistentVolumeSpec',
    'PersistentVolumeClaim',
    'PersistentVolumeClaimSpec',
]
