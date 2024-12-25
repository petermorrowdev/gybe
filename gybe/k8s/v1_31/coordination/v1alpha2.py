"""Models generated from Kubernetes OpenAPI Spec."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

import gybe.k8s.v1_31.meta.v1
from gybe.k8s.types import JSONObj, K8sSpec


@dataclass
class LeaseCandidate(K8sSpec):
    """LeaseCandidate defines a candidate for a Lease object. Candidates are created such that coordinated
    leader election will pick the best leader from the list of candidates.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata:
        spec: spec contains the specification of the Lease.

    """

    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[gybe.k8s.v1_31.meta.v1.ObjectMeta] = None
    spec: Optional[LeaseCandidateSpec] = None


@dataclass
class LeaseCandidateList(K8sSpec):
    """LeaseCandidateList is a list of Lease objects.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        items: items is a list of schema objects.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard list metadata.

    """

    items: List[LeaseCandidate]
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[JSONObj] = None


@dataclass
class LeaseCandidateSpec(K8sSpec):
    """LeaseCandidateSpec is a specification of a Lease.

    Attributes:
        binaryVersion: BinaryVersion is the binary version. It must be in a semver format without leading `v`.
            This field is required.
        emulationVersion: EmulationVersion is the emulation version. It must be in a semver format without
            leading `v`. EmulationVersion must be less than or equal to BinaryVersion. This field is required
            when strategy is 'OldestEmulationVersion'
        leaseName: LeaseName is the name of the lease for which this candidate is contending. This field is
            immutable.
        pingTime: PingTime is the last time that the server has requested the LeaseCandidate to renew. It is
            only done during leader election to check if any LeaseCandidates have become ineligible. When
            PingTime is updated, the LeaseCandidate will respond by updating RenewTime.
        renewTime: RenewTime is the time that the LeaseCandidate was last updated. Any time a Lease needs to
            do leader election, the PingTime field is updated to signal to the LeaseCandidate that they should
            update the RenewTime. Old LeaseCandidate objects are also garbage collected if it has been hours
            since the last renew. The PingTime field is updated regularly to prevent garbage collection for
            still active LeaseCandidates.
        strategy: Strategy is the strategy that coordinated leader election will use for picking the leader.
            If multiple candidates for the same Lease return different strategies, the strategy provided by
            the candidate with the latest BinaryVersion will be used. If there is still conflict, this is a
            user error and coordinated leader election will not operate the Lease until resolved. (Alpha)
            Using this field requires the CoordinatedLeaderElection feature gate to be enabled.

    """

    leaseName: str
    binaryVersion: str
    strategy: str
    emulationVersion: Optional[str] = None
    pingTime: Optional[str] = None
    renewTime: Optional[str] = None
