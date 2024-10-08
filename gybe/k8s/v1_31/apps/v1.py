"""Models generated from Kubernetes OpenAPI Spec."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Literal, Optional

import gybe.k8s.v1_31.core.v1
import gybe.k8s.v1_31.meta.v1
from gybe.k8s.types import JSONObj, K8sResource, K8sSpec


@dataclass
class ControllerRevision(K8sSpec):
    """ControllerRevision implements an immutable snapshot of state data. Clients are responsible for
    serializing and deserializing the objects that contain their internal state. Once a ControllerRevision
    has been successfully created, it can not be updated. The API Server will fail validation of all
    requests that attempt to mutate the Data field. ControllerRevisions may, however, be deleted. Note
    that, due to its use by both the DaemonSet and StatefulSet controllers for update and rollback, this
    object is beta. However, it may be subject to name and representation changes in future releases, and
    clients should not depend on its stability. It is primarily for internal use by controllers.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        data: Data is the serialized representation of the state.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object's metadata.
        revision: Revision indicates the revision of the state represented by Data.

    """

    revision: int
    apiVersion: Optional[str] = None
    data: Optional[JSONObj] = None
    kind: Optional[str] = None
    metadata: Optional[gybe.k8s.v1_31.meta.v1.ObjectMeta] = None


@dataclass
class ControllerRevisionList(K8sSpec):
    """ControllerRevisionList is a resource containing a list of ControllerRevision objects.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        items: Items is the list of ControllerRevisions
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata:

    """

    items: List[ControllerRevision]
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[JSONObj] = None


@dataclass
class DaemonSet(K8sResource):
    """DaemonSet represents the configuration of a daemon set.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object's metadata.
        spec: The desired behavior of this daemon set.
        status: The current status of this daemon set. This data may be out of date by some window of time.
            Populated by the system. Read-only.

    """

    apiVersion: Literal['apps/v1'] = 'apps/v1'
    kind: Literal['DaemonSet'] = 'DaemonSet'
    metadata: Optional[gybe.k8s.v1_31.meta.v1.ObjectMeta] = None
    spec: Optional[DaemonSetSpec] = None
    status: Optional[DaemonSetStatus] = None


@dataclass
class DaemonSetCondition(K8sSpec):
    """DaemonSetCondition describes the state of a DaemonSet at a certain point.

    Attributes:
        lastTransitionTime: Last time the condition transitioned from one status to another.
        message: A human readable message indicating details about the transition.
        reason: The reason for the condition's last transition.
        status: Status of the condition, one of True, False, Unknown.
        type: Type of DaemonSet condition.

    """

    type: str
    status: str
    lastTransitionTime: Optional[str] = None
    message: Optional[str] = None
    reason: Optional[str] = None


@dataclass
class DaemonSetList(K8sSpec):
    """DaemonSetList is a collection of daemon sets.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        items: A list of daemon sets.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard list metadata.

    """

    items: List[DaemonSet]
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[JSONObj] = None


@dataclass
class DaemonSetSpec(K8sSpec):
    """DaemonSetSpec is the specification of a daemon set.

    Attributes:
        minReadySeconds: The minimum number of seconds for which a newly created DaemonSet pod should be ready
            without any of its container crashing, for it to be considered available. Defaults to 0 (pod will
            be considered available as soon as it is ready).
        revisionHistoryLimit: The number of old history to retain to allow rollback. This is a pointer to
            distinguish between explicit zero and not specified. Defaults to 10.
        selector: A label query over pods that are managed by the daemon set. Must match in order to be
            controlled. It must match the pod template's labels.
        template: An object that describes the pod that will be created. The DaemonSet will create exactly one
            copy of this pod on every node that matches the template's node selector (or on every node if no
            node selector is specified). The only allowed template.spec.restartPolicy value is 'Always'.
        updateStrategy: An update strategy to replace existing DaemonSet pods with new pods.

    """

    selector: gybe.k8s.v1_31.meta.v1.LabelSelector
    template: gybe.k8s.v1_31.core.v1.PodTemplateSpec
    minReadySeconds: Optional[int] = None
    revisionHistoryLimit: Optional[int] = None
    updateStrategy: Optional[DaemonSetUpdateStrategy] = None


@dataclass
class DaemonSetStatus(K8sSpec):
    """DaemonSetStatus represents the current status of a daemon set.

    Attributes:
        collisionCount: Count of hash collisions for the DaemonSet. The DaemonSet controller uses this field
            as a collision avoidance mechanism when it needs to create the name for the newest
            ControllerRevision.
        conditions: Represents the latest available observations of a DaemonSet's current state.
        currentNumberScheduled: The number of nodes that are running at least 1 daemon pod and are supposed to
            run the daemon pod.
        desiredNumberScheduled: The total number of nodes that should be running the daemon pod (including
            nodes correctly running the daemon pod).
        numberAvailable: The number of nodes that should be running the daemon pod and have one or more of the
            daemon pod running and available (ready for at least spec.minReadySeconds)
        numberMisscheduled: The number of nodes that are running the daemon pod, but are not supposed to run
            the daemon pod.
        numberReady: numberReady is the number of nodes that should be running the daemon pod and have one or
            more of the daemon pod running with a Ready Condition.
        numberUnavailable: The number of nodes that should be running the daemon pod and have none of the
            daemon pod running and available (ready for at least spec.minReadySeconds)
        observedGeneration: The most recent generation observed by the daemon set controller.
        updatedNumberScheduled: The total number of nodes that are running updated daemon pod

    """

    currentNumberScheduled: int
    numberMisscheduled: int
    desiredNumberScheduled: int
    numberReady: int
    collisionCount: Optional[int] = None
    conditions: Optional[List[DaemonSetCondition]] = None
    numberAvailable: Optional[int] = None
    numberUnavailable: Optional[int] = None
    observedGeneration: Optional[int] = None
    updatedNumberScheduled: Optional[int] = None


@dataclass
class DaemonSetUpdateStrategy(K8sSpec):
    """DaemonSetUpdateStrategy is a struct used to control the update strategy for a DaemonSet.

    Attributes:
        rollingUpdate: Rolling update config params. Present only if type = 'RollingUpdate'.
        type: Type of daemon set update. Can be 'RollingUpdate' or 'OnDelete'. Default is RollingUpdate.

    """

    rollingUpdate: Optional[RollingUpdateDaemonSet] = None
    type: Optional[str] = None


@dataclass
class Deployment(K8sResource):
    """Deployment enables declarative updates for Pods and ReplicaSets.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object's metadata.
        spec: Specification of the desired behavior of the Deployment.
        status: Most recently observed status of the Deployment.

    """

    apiVersion: Literal['apps/v1'] = 'apps/v1'
    kind: Literal['Deployment'] = 'Deployment'
    metadata: Optional[gybe.k8s.v1_31.meta.v1.ObjectMeta] = None
    spec: Optional[DeploymentSpec] = None
    status: Optional[DeploymentStatus] = None


@dataclass
class DeploymentCondition(K8sSpec):
    """DeploymentCondition describes the state of a deployment at a certain point.

    Attributes:
        lastTransitionTime: Last time the condition transitioned from one status to another.
        lastUpdateTime: The last time this condition was updated.
        message: A human readable message indicating details about the transition.
        reason: The reason for the condition's last transition.
        status: Status of the condition, one of True, False, Unknown.
        type: Type of deployment condition.

    """

    type: str
    status: str
    lastTransitionTime: Optional[str] = None
    lastUpdateTime: Optional[str] = None
    message: Optional[str] = None
    reason: Optional[str] = None


@dataclass
class DeploymentList(K8sSpec):
    """DeploymentList is a list of Deployments.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        items: Items is the list of Deployments.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard list metadata.

    """

    items: List[Deployment]
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[JSONObj] = None


@dataclass
class DeploymentSpec(K8sSpec):
    """DeploymentSpec is the specification of the desired behavior of the Deployment.

    Attributes:
        minReadySeconds: Minimum number of seconds for which a newly created pod should be ready without any
            of its container crashing, for it to be considered available. Defaults to 0 (pod will be
            considered available as soon as it is ready)
        paused: Indicates that the deployment is paused.
        progressDeadlineSeconds: The maximum time in seconds for a deployment to make progress before it is
            considered to be failed. The deployment controller will continue to process failed deployments and
            a condition with a ProgressDeadlineExceeded reason will be surfaced in the deployment status. Note
            that progress will not be estimated during the time a deployment is paused. Defaults to 600s.
        replicas: Number of desired pods. This is a pointer to distinguish between explicit zero and not
            specified. Defaults to 1.
        revisionHistoryLimit: The number of old ReplicaSets to retain to allow rollback. This is a pointer to
            distinguish between explicit zero and not specified. Defaults to 10.
        selector: Label selector for pods. Existing ReplicaSets whose pods are selected by this will be the
            ones affected by this deployment. It must match the pod template's labels.
        strategy: The deployment strategy to use to replace existing pods with new ones.
        template: Template describes the pods that will be created. The only allowed
            template.spec.restartPolicy value is 'Always'.

    """

    selector: gybe.k8s.v1_31.meta.v1.LabelSelector
    template: gybe.k8s.v1_31.core.v1.PodTemplateSpec
    minReadySeconds: Optional[int] = None
    paused: Optional[bool] = None
    progressDeadlineSeconds: Optional[int] = None
    replicas: Optional[int] = None
    revisionHistoryLimit: Optional[int] = None
    strategy: Optional[DeploymentStrategy] = None


@dataclass
class DeploymentStatus(K8sSpec):
    """DeploymentStatus is the most recently observed status of the Deployment.

    Attributes:
        availableReplicas: Total number of available pods (ready for at least minReadySeconds) targeted by
            this deployment.
        collisionCount: Count of hash collisions for the Deployment. The Deployment controller uses this field
            as a collision avoidance mechanism when it needs to create the name for the newest ReplicaSet.
        conditions: Represents the latest available observations of a deployment's current state.
        observedGeneration: The generation observed by the deployment controller.
        readyReplicas: readyReplicas is the number of pods targeted by this Deployment with a Ready Condition.
        replicas: Total number of non-terminated pods targeted by this deployment (their labels match the
            selector).
        unavailableReplicas: Total number of unavailable pods targeted by this deployment. This is the total
            number of pods that are still required for the deployment to have 100% available capacity. They
            may either be pods that are running but not yet available or pods that still have not been
            created.
        updatedReplicas: Total number of non-terminated pods targeted by this deployment that have the desired
            template spec.

    """

    availableReplicas: Optional[int] = None
    collisionCount: Optional[int] = None
    conditions: Optional[List[DeploymentCondition]] = None
    observedGeneration: Optional[int] = None
    readyReplicas: Optional[int] = None
    replicas: Optional[int] = None
    unavailableReplicas: Optional[int] = None
    updatedReplicas: Optional[int] = None


@dataclass
class DeploymentStrategy(K8sSpec):
    """DeploymentStrategy describes how to replace existing pods with new ones.

    Attributes:
        rollingUpdate: Rolling update config params. Present only if DeploymentStrategyType = RollingUpdate.
        type: Type of deployment. Can be 'Recreate' or 'RollingUpdate'. Default is RollingUpdate.

    """

    rollingUpdate: Optional[RollingUpdateDeployment] = None
    type: Optional[str] = None


@dataclass
class ReplicaSet(K8sResource):
    """ReplicaSet ensures that a specified number of pod replicas are running at any given time.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: If the Labels of a ReplicaSet are empty, they are defaulted to be the same as the Pod(s)
            that the ReplicaSet manages. Standard object's metadata.
        spec: Spec defines the specification of the desired behavior of the ReplicaSet.
        status: Status is the most recently observed status of the ReplicaSet. This data may be out of date by
            some window of time. Populated by the system. Read-only.

    """

    apiVersion: Literal['apps/v1'] = 'apps/v1'
    kind: Literal['ReplicaSet'] = 'ReplicaSet'
    metadata: Optional[gybe.k8s.v1_31.meta.v1.ObjectMeta] = None
    spec: Optional[ReplicaSetSpec] = None
    status: Optional[ReplicaSetStatus] = None


@dataclass
class ReplicaSetCondition(K8sSpec):
    """ReplicaSetCondition describes the state of a replica set at a certain point.

    Attributes:
        lastTransitionTime: The last time the condition transitioned from one status to another.
        message: A human readable message indicating details about the transition.
        reason: The reason for the condition's last transition.
        status: Status of the condition, one of True, False, Unknown.
        type: Type of replica set condition.

    """

    type: str
    status: str
    lastTransitionTime: Optional[str] = None
    message: Optional[str] = None
    reason: Optional[str] = None


@dataclass
class ReplicaSetList(K8sSpec):
    """ReplicaSetList is a collection of ReplicaSets.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        items: List of ReplicaSets.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard list metadata.

    """

    items: List[ReplicaSet]
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[JSONObj] = None


@dataclass
class ReplicaSetSpec(K8sSpec):
    """ReplicaSetSpec is the specification of a ReplicaSet.

    Attributes:
        minReadySeconds: Minimum number of seconds for which a newly created pod should be ready without any
            of its container crashing, for it to be considered available. Defaults to 0 (pod will be
            considered available as soon as it is ready)
        replicas: Replicas is the number of desired replicas. This is a pointer to distinguish between
            explicit zero and unspecified. Defaults to 1.
        selector: Selector is a label query over pods that should match the replica count. Label keys and
            values that must match in order to be controlled by this replica set. It must match the pod
            template's labels.
        template: Template is the object that describes the pod that will be created if insufficient replicas
            are detected.

    """

    selector: gybe.k8s.v1_31.meta.v1.LabelSelector
    minReadySeconds: Optional[int] = None
    replicas: Optional[int] = None
    template: Optional[gybe.k8s.v1_31.core.v1.PodTemplateSpec] = None


@dataclass
class ReplicaSetStatus(K8sSpec):
    """ReplicaSetStatus represents the current status of a ReplicaSet.

    Attributes:
        availableReplicas: The number of available replicas (ready for at least minReadySeconds) for this
            replica set.
        conditions: Represents the latest available observations of a replica set's current state.
        fullyLabeledReplicas: The number of pods that have labels matching the labels of the pod template of
            the replicaset.
        observedGeneration: ObservedGeneration reflects the generation of the most recently observed
            ReplicaSet.
        readyReplicas: readyReplicas is the number of pods targeted by this ReplicaSet with a Ready Condition.
        replicas: Replicas is the most recently observed number of replicas.

    """

    replicas: int
    availableReplicas: Optional[int] = None
    conditions: Optional[List[ReplicaSetCondition]] = None
    fullyLabeledReplicas: Optional[int] = None
    observedGeneration: Optional[int] = None
    readyReplicas: Optional[int] = None


@dataclass
class RollingUpdateDaemonSet(K8sSpec):
    """Spec to control the desired behavior of daemon set rolling update.

    Attributes:
        maxSurge: The maximum number of nodes with an existing available DaemonSet pod that can have an
            updated DaemonSet pod during during an update. Value can be an absolute number (ex: 5) or a
            percentage of desired pods (ex: 10%). This can not be 0 if MaxUnavailable is 0. Absolute number is
            calculated from percentage by rounding up to a minimum of 1. Default value is 0. Example: when
            this is set to 30%, at most 30% of the total number of nodes that should be running the daemon pod
            (i.e. status.desiredNumberScheduled) can have their a new pod created before the old pod is marked
            as deleted. The update starts by launching new pods on 30% of nodes. Once an updated pod is
            available (Ready for at least minReadySeconds) the old DaemonSet pod on that node is marked
            deleted. If the old pod becomes unavailable for any reason (Ready transitions to false, is
            evicted, or is drained) an updated pod is immediatedly created on that node without considering
            surge limits. Allowing surge implies the possibility that the resources consumed by the daemonset
            on any given node can double if the readiness check fails, and so resource intensive daemonsets
            should take into account that they may cause evictions during disruption.
        maxUnavailable: The maximum number of DaemonSet pods that can be unavailable during the update. Value
            can be an absolute number (ex: 5) or a percentage of total number of DaemonSet pods at the start
            of the update (ex: 10%). Absolute number is calculated from percentage by rounding up. This cannot
            be 0 if MaxSurge is 0 Default value is 1. Example: when this is set to 30%, at most 30% of the
            total number of nodes that should be running the daemon pod (i.e. status.desiredNumberScheduled)
            can have their pods stopped for an update at any given time. The update starts by stopping at most
            30% of those DaemonSet pods and then brings up new DaemonSet pods in their place. Once the new
            pods are available, it then proceeds onto other DaemonSet pods, thus ensuring that at least 70% of
            original number of DaemonSet pods are available at all times during the update.

    """

    maxSurge: Optional[str] = None
    maxUnavailable: Optional[str] = None


@dataclass
class RollingUpdateDeployment(K8sSpec):
    """Spec to control the desired behavior of rolling update.

    Attributes:
        maxSurge: The maximum number of pods that can be scheduled above the desired number of pods. Value can
            be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%). This can not be 0 if
            MaxUnavailable is 0. Absolute number is calculated from percentage by rounding up. Defaults to
            25%. Example: when this is set to 30%, the new ReplicaSet can be scaled up immediately when the
            rolling update starts, such that the total number of old and new pods do not exceed 130% of
            desired pods. Once old pods have been killed, new ReplicaSet can be scaled up further, ensuring
            that total number of pods running at any time during the update is at most 130% of desired pods.
        maxUnavailable: The maximum number of pods that can be unavailable during the update. Value can be an
            absolute number (ex: 5) or a percentage of desired pods (ex: 10%). Absolute number is calculated
            from percentage by rounding down. This can not be 0 if MaxSurge is 0. Defaults to 25%. Example:
            when this is set to 30%, the old ReplicaSet can be scaled down to 70% of desired pods immediately
            when the rolling update starts. Once new pods are ready, old ReplicaSet can be scaled down
            further, followed by scaling up the new ReplicaSet, ensuring that the total number of pods
            available at all times during the update is at least 70% of desired pods.

    """

    maxSurge: Optional[str] = None
    maxUnavailable: Optional[str] = None


@dataclass
class RollingUpdateStatefulSetStrategy(K8sSpec):
    """RollingUpdateStatefulSetStrategy is used to communicate parameter for
    RollingUpdateStatefulSetStrategyType.

    Attributes:
        maxUnavailable: The maximum number of pods that can be unavailable during the update. Value can be an
            absolute number (ex: 5) or a percentage of desired pods (ex: 10%). Absolute number is calculated
            from percentage by rounding up. This can not be 0. Defaults to 1. This field is alpha-level and is
            only honored by servers that enable the MaxUnavailableStatefulSet feature. The field applies to
            all pods in the range 0 to Replicas-1. That means if there is any unavailable pod in the range 0
            to Replicas-1, it will be counted towards MaxUnavailable.
        partition: Partition indicates the ordinal at which the StatefulSet should be partitioned for updates.
            During a rolling update, all pods from ordinal Replicas-1 to Partition are updated. All pods from
            ordinal Partition-1 to 0 remain untouched. This is helpful in being able to do a canary based
            deployment. The default value is 0.

    """

    maxUnavailable: Optional[str] = None
    partition: Optional[int] = None


@dataclass
class StatefulSet(K8sResource):
    """StatefulSet represents a set of pods with consistent identities. Identities are defined as:   -
    Network: A single stable DNS and hostname.   - Storage: As many VolumeClaims as requested.  The
    StatefulSet guarantees that a given network identity will always map to the same storage identity.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object's metadata.
        spec: Spec defines the desired identities of pods in this set.
        status: Status is the current status of Pods in this StatefulSet. This data may be out of date by some
            window of time.

    """

    apiVersion: Literal['apps/v1'] = 'apps/v1'
    kind: Literal['StatefulSet'] = 'StatefulSet'
    metadata: Optional[gybe.k8s.v1_31.meta.v1.ObjectMeta] = None
    spec: Optional[StatefulSetSpec] = None
    status: Optional[StatefulSetStatus] = None


@dataclass
class StatefulSetCondition(K8sSpec):
    """StatefulSetCondition describes the state of a statefulset at a certain point.

    Attributes:
        lastTransitionTime: Last time the condition transitioned from one status to another.
        message: A human readable message indicating details about the transition.
        reason: The reason for the condition's last transition.
        status: Status of the condition, one of True, False, Unknown.
        type: Type of statefulset condition.

    """

    type: str
    status: str
    lastTransitionTime: Optional[str] = None
    message: Optional[str] = None
    reason: Optional[str] = None


@dataclass
class StatefulSetList(K8sSpec):
    """StatefulSetList is a collection of StatefulSets.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        items: Items is the list of stateful sets.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard list's metadata.

    """

    items: List[StatefulSet]
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[JSONObj] = None


@dataclass
class StatefulSetOrdinals(K8sSpec):
    """StatefulSetOrdinals describes the policy used for replica ordinal assignment in this StatefulSet.

    Attributes:
        start: start is the number representing the first replica's index. It may be used to number replicas
            from an alternate index (eg: 1-indexed) over the default 0-indexed names, or to orchestrate
            progressive movement of replicas from one StatefulSet to another. If set, replica indices will be
            in the range:   [.spec.ordinals.start, .spec.ordinals.start + .spec.replicas). If unset, defaults
            to 0. Replica indices will be in the range:   [0, .spec.replicas).

    """

    start: Optional[int] = None


@dataclass
class StatefulSetPersistentVolumeClaimRetentionPolicy(K8sSpec):
    """StatefulSetPersistentVolumeClaimRetentionPolicy describes the policy used for PVCs created from the
    StatefulSet VolumeClaimTemplates.

    Attributes:
        whenDeleted: WhenDeleted specifies what happens to PVCs created from StatefulSet VolumeClaimTemplates
            when the StatefulSet is deleted. The default policy of `Retain` causes PVCs to not be affected by
            StatefulSet deletion. The `Delete` policy causes those PVCs to be deleted.
        whenScaled: WhenScaled specifies what happens to PVCs created from StatefulSet VolumeClaimTemplates
            when the StatefulSet is scaled down. The default policy of `Retain` causes PVCs to not be affected
            by a scaledown. The `Delete` policy causes the associated PVCs for any excess pods above the
            replica count to be deleted.

    """

    whenDeleted: Optional[str] = None
    whenScaled: Optional[str] = None


@dataclass
class StatefulSetSpec(K8sSpec):
    """A StatefulSetSpec is the specification of a StatefulSet.

    Attributes:
        minReadySeconds: Minimum number of seconds for which a newly created pod should be ready without any
            of its container crashing for it to be considered available. Defaults to 0 (pod will be considered
            available as soon as it is ready)
        ordinals: ordinals controls the numbering of replica indices in a StatefulSet. The default ordinals
            behavior assigns a '0' index to the first replica and increments the index by one for each
            additional replica requested.
        persistentVolumeClaimRetentionPolicy: persistentVolumeClaimRetentionPolicy describes the lifecycle of
            persistent volume claims created from volumeClaimTemplates. By default, all persistent volume
            claims are created as needed and retained until manually deleted. This policy allows the lifecycle
            to be altered, for example by deleting persistent volume claims when their stateful set is
            deleted, or when their pod is scaled down. This requires the StatefulSetAutoDeletePVC feature gate
            to be enabled, which is beta.
        podManagementPolicy: podManagementPolicy controls how pods are created during initial scale up, when
            replacing pods on nodes, or when scaling down. The default policy is `OrderedReady`, where pods
            are created in increasing order (pod-0, then pod-1, etc) and the controller will wait until each
            pod is ready before continuing. When scaling down, the pods are removed in the opposite order. The
            alternative policy is `Parallel` which will create pods in parallel to match the desired scale
            without waiting, and on scale down will delete all pods at once.
        replicas: replicas is the desired number of replicas of the given Template. These are replicas in the
            sense that they are instantiations of the same Template, but individual replicas also have a
            consistent identity. If unspecified, defaults to 1.
        revisionHistoryLimit: revisionHistoryLimit is the maximum number of revisions that will be maintained
            in the StatefulSet's revision history. The revision history consists of all revisions not
            represented by a currently applied StatefulSetSpec version. The default value is 10.
        selector: selector is a label query over pods that should match the replica count. It must match the
            pod template's labels.
        serviceName: serviceName is the name of the service that governs this StatefulSet. This service must
            exist before the StatefulSet, and is responsible for the network identity of the set. Pods get
            DNS/hostnames that follow the pattern: pod-specific-string.serviceName.default.svc.cluster.local
            where 'pod-specific-string' is managed by the StatefulSet controller.
        template: template is the object that describes the pod that will be created if insufficient replicas
            are detected. Each pod stamped out by the StatefulSet will fulfill this Template, but have a
            unique identity from the rest of the StatefulSet. Each pod will be named with the format
            <statefulsetname>-<podindex>. For example, a pod in a StatefulSet named 'web' with index number
            '3' would be named 'web-3'. The only allowed template.spec.restartPolicy value is 'Always'.
        updateStrategy: updateStrategy indicates the StatefulSetUpdateStrategy that will be employed to update
            Pods in the StatefulSet when a revision is made to Template.
        volumeClaimTemplates: volumeClaimTemplates is a list of claims that pods are allowed to reference. The
            StatefulSet controller is responsible for mapping network identities to claims in a way that
            maintains the identity of a pod. Every claim in this list must have at least one matching (by
            name) volumeMount in one container in the template. A claim in this list takes precedence over any
            volumes in the template, with the same name.

    """

    selector: gybe.k8s.v1_31.meta.v1.LabelSelector
    template: gybe.k8s.v1_31.core.v1.PodTemplateSpec
    serviceName: str
    minReadySeconds: Optional[int] = None
    ordinals: Optional[StatefulSetOrdinals] = None
    persistentVolumeClaimRetentionPolicy: Optional[StatefulSetPersistentVolumeClaimRetentionPolicy] = None
    podManagementPolicy: Optional[str] = None
    replicas: Optional[int] = None
    revisionHistoryLimit: Optional[int] = None
    updateStrategy: Optional[StatefulSetUpdateStrategy] = None
    volumeClaimTemplates: Optional[List[gybe.k8s.v1_31.core.v1.PersistentVolumeClaim]] = None


@dataclass
class StatefulSetStatus(K8sSpec):
    """StatefulSetStatus represents the current state of a StatefulSet.

    Attributes:
        availableReplicas: Total number of available pods (ready for at least minReadySeconds) targeted by
            this statefulset.
        collisionCount: collisionCount is the count of hash collisions for the StatefulSet. The StatefulSet
            controller uses this field as a collision avoidance mechanism when it needs to create the name for
            the newest ControllerRevision.
        conditions: Represents the latest available observations of a statefulset's current state.
        currentReplicas: currentReplicas is the number of Pods created by the StatefulSet controller from the
            StatefulSet version indicated by currentRevision.
        currentRevision: currentRevision, if not empty, indicates the version of the StatefulSet used to
            generate Pods in the sequence [0,currentReplicas).
        observedGeneration: observedGeneration is the most recent generation observed for this StatefulSet. It
            corresponds to the StatefulSet's generation, which is updated on mutation by the API Server.
        readyReplicas: readyReplicas is the number of pods created for this StatefulSet with a Ready
            Condition.
        replicas: replicas is the number of Pods created by the StatefulSet controller.
        updateRevision: updateRevision, if not empty, indicates the version of the StatefulSet used to
            generate Pods in the sequence [replicas-updatedReplicas,replicas)
        updatedReplicas: updatedReplicas is the number of Pods created by the StatefulSet controller from the
            StatefulSet version indicated by updateRevision.

    """

    replicas: int
    availableReplicas: Optional[int] = None
    collisionCount: Optional[int] = None
    conditions: Optional[List[StatefulSetCondition]] = None
    currentReplicas: Optional[int] = None
    currentRevision: Optional[str] = None
    observedGeneration: Optional[int] = None
    readyReplicas: Optional[int] = None
    updateRevision: Optional[str] = None
    updatedReplicas: Optional[int] = None


@dataclass
class StatefulSetUpdateStrategy(K8sSpec):
    """StatefulSetUpdateStrategy indicates the strategy that the StatefulSet controller will use to perform
    updates. It includes any additional parameters necessary to perform the update for the indicated
    strategy.

    Attributes:
        rollingUpdate: RollingUpdate is used to communicate parameters when Type is
            RollingUpdateStatefulSetStrategyType.
        type: Type indicates the type of the StatefulSetUpdateStrategy. Default is RollingUpdate.

    """

    rollingUpdate: Optional[RollingUpdateStatefulSetStrategy] = None
    type: Optional[str] = None
