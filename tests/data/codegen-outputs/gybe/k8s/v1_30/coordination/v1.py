"""Models generated from Kubernetes OpenAPI Spec."""
from __future__ import annotations
from typing import List, Optional, Literal
from dataclasses import dataclass
from gybe.k8s.types import JSONObj, JSONDict, K8sSpec, K8sResource
import gybe.k8s.v1_30.meta.v1

@dataclass
class Lease(K8sResource):
    """
    Lease defines a lease concept.
    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata:
        spec: spec contains the specification of the Lease.

"""
    apiVersion: Literal['coordination.k8s.io/v1'] = 'coordination.k8s.io/v1'
    kind: Literal['Lease'] = 'Lease'
    metadata: Optional[gybe.k8s.v1_30.meta.v1.ObjectMeta] = None
    spec: Optional[LeaseSpec] = None

@dataclass
class LeaseSpec(K8sSpec):
    """
    LeaseSpec is a specification of a Lease.
    Attributes:
        acquireTime: acquireTime is a time when the current lease was acquired.
        holderIdentity: holderIdentity contains the identity of the holder of a current lease.
        leaseDurationSeconds: leaseDurationSeconds is a duration that candidates for a lease need to wait to
            force acquire it. This is measure against time of last observed renewTime.
        leaseTransitions: leaseTransitions is the number of transitions of a lease between holders.
        renewTime: renewTime is a time when the current holder of a lease has last updated the lease.

"""
    acquireTime: Optional[str] = None
    holderIdentity: Optional[str] = None
    leaseDurationSeconds: Optional[int] = None
    leaseTransitions: Optional[int] = None
    renewTime: Optional[str] = None