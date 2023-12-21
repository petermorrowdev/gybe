from __future__ import annotations
from typing import Dict, List, Optional
from pydantic import BaseModel, Field
from ...apimachinery.pkg.api import resource
from ...apimachinery.pkg.apis.meta import v1
from ..core import v1 as v1_1


class TokenRequest(BaseModel):
    audience: str = Field(
        ...,
        description=(
            'audience is the intended audience of the token in "TokenRequestSpec". It'
            " will default to the audiences of kube apiserver."
        ),
    )
    expirationSeconds: Optional[int] = Field(
        None,
        description=(
            "expirationSeconds is the duration of validity of the token in"
            ' "TokenRequestSpec". It has the same default value of "ExpirationSeconds"'
            ' in "TokenRequestSpec".'
        ),
    )


class VolumeNodeResources(BaseModel):
    count: Optional[int] = Field(
        None,
        description=(
            "count indicates the maximum number of unique volumes managed by the CSI"
            " driver that can be used on a node. A volume that is both attached and"
            " mounted on a node is considered to be used once, not twice. The same rule"
            " applies for a unique volume that is shared among multiple pods on the"
            " same node. If this field is not specified, then the supported number of"
            " volumes on this node is unbounded."
        ),
    )


class CSIDriverSpec(BaseModel):
    attachRequired: Optional[bool] = Field(
        None,
        description=(
            "attachRequired indicates this CSI volume driver requires an attach"
            " operation (because it implements the CSI ControllerPublishVolume()"
            " method), and that the Kubernetes attach detach controller should call the"
            " attach volume interface which checks the volumeattachment status and"
            " waits until the volume is attached before proceeding to mounting. The CSI"
            " external-attacher coordinates with CSI volume driver and updates the"
            " volumeattachment status when the attach operation is complete. If the"
            " CSIDriverRegistry feature gate is enabled and the value is specified to"
            " false, the attach operation will be skipped. Otherwise the attach"
            " operation will be called.\n\nThis field is immutable."
        ),
    )
    fsGroupPolicy: Optional[str] = Field(
        None,
        description=(
            "fsGroupPolicy defines if the underlying volume supports changing ownership"
            " and permission of the volume before being mounted. Refer to the specific"
            " FSGroupPolicy values for additional details.\n\nThis field is"
            " immutable.\n\nDefaults to ReadWriteOnceWithFSType, which will examine"
            " each volume to determine if Kubernetes should modify ownership and"
            " permissions of the volume. With the default policy the defined fsGroup"
            " will only be applied if a fstype is defined and the volume's access mode"
            " contains ReadWriteOnce."
        ),
    )
    podInfoOnMount: Optional[bool] = Field(
        None,
        description=(
            "podInfoOnMount indicates this CSI volume driver requires additional pod"
            " information (like podName, podUID, etc.) during mount operations, if set"
            " to true. If set to false, pod information will not be passed on mount."
            " Default is false.\n\nThe CSI driver specifies podInfoOnMount as part of"
            " driver deployment. If true, Kubelet will pass pod information as"
            " VolumeContext in the CSI NodePublishVolume() calls. The CSI driver is"
            " responsible for parsing and validating the information passed in as"
            " VolumeContext.\n\nThe following VolumeConext will be passed if"
            " podInfoOnMount is set to true. This list might grow, but the prefix will"
            ' be used. "csi.storage.k8s.io/pod.name": pod.Name'
            ' "csi.storage.k8s.io/pod.namespace": pod.Namespace'
            ' "csi.storage.k8s.io/pod.uid": string(pod.UID)'
            ' "csi.storage.k8s.io/ephemeral": "true" if the volume is an ephemeral'
            " inline volume\n                                defined by a"
            ' CSIVolumeSource, otherwise "false"\n\n"csi.storage.k8s.io/ephemeral" is a'
            " new feature in Kubernetes 1.16. It is only required for drivers which"
            ' support both the "Persistent" and "Ephemeral" VolumeLifecycleMode. Other'
            " drivers can leave pod info disabled and/or ignore this field. As"
            " Kubernetes 1.15 doesn't support this field, drivers can only support one"
            " mode when deployed on such a cluster and the deployment determines which"
            " mode that is, for example via a command line parameter of the"
            " driver.\n\nThis field is immutable."
        ),
    )
    requiresRepublish: Optional[bool] = Field(
        None,
        description=(
            "requiresRepublish indicates the CSI driver wants `NodePublishVolume` being"
            " periodically called to reflect any possible change in the mounted volume."
            " This field defaults to false.\n\nNote: After a successful initial"
            " NodePublishVolume call, subsequent calls to NodePublishVolume should only"
            " update the contents of the volume. New mount points will not be seen by a"
            " running container."
        ),
    )
    seLinuxMount: Optional[bool] = Field(
        None,
        description=(
            'seLinuxMount specifies if the CSI driver supports "-o context" mount'
            ' option.\n\nWhen "true", the CSI driver must ensure that all volumes'
            " provided by this CSI driver can be mounted separately with different `-o"
            " context` options. This is typical for storage backends that provide"
            " volumes as filesystems on block devices or as independent shared volumes."
            ' Kubernetes will call NodeStage / NodePublish with "-o context=xyz" mount'
            " option when mounting a ReadWriteOncePod volume used in Pod that has"
            " explicitly set SELinux context. In the future, it may be expanded to"
            " other volume AccessModes. In any case, Kubernetes will ensure that the"
            ' volume is mounted only with a single SELinux context.\n\nWhen "false",'
            " Kubernetes won't pass any special SELinux mount options to the driver."
            " This is typical for volumes that represent subdirectories of a bigger"
            ' shared filesystem.\n\nDefault is "false".'
        ),
    )
    storageCapacity: Optional[bool] = Field(
        None,
        description=(
            "storageCapacity indicates that the CSI volume driver wants pod scheduling"
            " to consider the storage capacity that the driver deployment will report"
            " by creating CSIStorageCapacity objects with capacity information, if set"
            " to true.\n\nThe check can be enabled immediately when deploying a driver."
            " In that case, provisioning new volumes with late binding will pause until"
            " the driver deployment has published some suitable CSIStorageCapacity"
            " object.\n\nAlternatively, the driver can be deployed with the field unset"
            " or false and it can be flipped later when storage capacity information"
            " has been published.\n\nThis field was immutable in Kubernetes <= 1.22 and"
            " now is mutable."
        ),
    )
    tokenRequests: Optional[List[TokenRequest]] = Field(
        None,
        description=(
            "tokenRequests indicates the CSI driver needs pods' service account tokens"
            " it is mounting volume for to do necessary authentication. Kubelet will"
            " pass the tokens in VolumeContext in the CSI NodePublishVolume calls. The"
            " CSI driver should parse and validate the following VolumeContext:"
            ' "csi.storage.k8s.io/serviceAccount.tokens": {\n  "<audience>": {\n   '
            ' "token": <token>,\n    "expirationTimestamp": <expiration timestamp in'
            " RFC3339>,\n  },\n  ...\n}\n\nNote: Audience in each TokenRequest should"
            " be different and at most one token is empty string. To receive a new"
            " token after expiry, RequiresRepublish can be used to trigger"
            " NodePublishVolume periodically."
        ),
    )
    volumeLifecycleModes: Optional[List[str]] = Field(
        None,
        description=(
            "volumeLifecycleModes defines what kind of volumes this CSI volume driver"
            ' supports. The default if the list is empty is "Persistent", which is the'
            " usage defined by the CSI specification and implemented in Kubernetes via"
            ' the usual PV/PVC mechanism.\n\nThe other mode is "Ephemeral". In this'
            " mode, volumes are defined inline inside the pod spec with CSIVolumeSource"
            " and their lifecycle is tied to the lifecycle of that pod. A driver has to"
            " be aware of this because it is only going to get a NodePublishVolume call"
            " for such a volume.\n\nFor more information about implementing this mode,"
            " see https://kubernetes-csi.github.io/docs/ephemeral-local-volumes.html A"
            " driver can support one or more of these modes and more modes may be added"
            " in the future.\n\nThis field is beta. This field is immutable."
        ),
    )


class CSINodeDriver(BaseModel):
    allocatable: Optional[VolumeNodeResources] = Field(
        None,
        description=(
            "allocatable represents the volume resources of a node that are available"
            " for scheduling. This field is beta."
        ),
    )
    name: str = Field(
        ...,
        description=(
            "name represents the name of the CSI driver that this object refers to."
            " This MUST be the same name returned by the CSI GetPluginName() call for"
            " that driver."
        ),
    )
    nodeID: str = Field(
        ...,
        description=(
            "nodeID of the node from the driver point of view. This field enables"
            " Kubernetes to communicate with storage systems that do not share the same"
            " nomenclature for nodes. For example, Kubernetes may refer to a given node"
            ' as "node1", but the storage system may refer to the same node as "nodeA".'
            " When Kubernetes issues a command to the storage system to attach a volume"
            " to a specific node, it can use this field to refer to the node name using"
            ' the ID that the storage system will understand, e.g. "nodeA" instead of'
            ' "node1". This field is required.'
        ),
    )
    topologyKeys: Optional[List[str]] = Field(
        None,
        description=(
            "topologyKeys is the list of keys supported by the driver. When a driver is"
            " initialized on a cluster, it provides a set of topology keys that it"
            ' understands (e.g. "company.com/zone", "company.com/region"). When a'
            " driver is initialized on a node, it provides the same topology keys along"
            " with values. Kubelet will expose these topology keys as labels on its own"
            " node object. When Kubernetes does topology aware provisioning, it can use"
            " this list to determine which labels it should retrieve from the node"
            " object and pass back to the driver. It is possible for different nodes to"
            " use different topology keys. This can be empty if driver does not support"
            " topology."
        ),
    )


class CSINodeSpec(BaseModel):
    drivers: List[CSINodeDriver] = Field(
        ...,
        description=(
            "drivers is a list of information of all CSI Drivers existing on a node. If"
            " all drivers in the list are uninstalled, this can become empty."
        ),
    )


class VolumeError(BaseModel):
    message: Optional[str] = Field(
        None,
        description=(
            "message represents the error encountered during Attach or Detach"
            " operation. This string may be logged, so it should not contain sensitive"
            " information."
        ),
    )
    time: Optional[v1.Time] = Field(
        None, description="time represents the time the error was encountered."
    )


class CSIDriver(BaseModel):
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
        None,
        description=(
            "Standard object metadata. metadata.Name indicates the name of the CSI"
            " driver that this object refers to; it MUST be the same name returned by"
            " the CSI GetPluginName() call for that driver. The driver name must be 63"
            " characters or less, beginning and ending with an alphanumeric character"
            " ([a-z0-9A-Z]) with dashes (-), dots (.), and alphanumerics between. More"
            " info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata"
        ),
    )
    spec: CSIDriverSpec = Field(
        ..., description="spec represents the specification of the CSI Driver."
    )


class CSIDriverList(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description=(
            "APIVersion defines the versioned schema of this representation of an"
            " object. Servers should convert recognized schemas to the latest internal"
            " value, and may reject unrecognized values. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources"
        ),
    )
    items: List[CSIDriver] = Field(..., description="items is the list of CSIDriver")
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
            "Standard list metadata More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata"
        ),
    )


class CSINode(BaseModel):
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
        None,
        description=(
            "Standard object's metadata. metadata.name must be the Kubernetes node"
            " name."
        ),
    )
    spec: CSINodeSpec = Field(..., description="spec is the specification of CSINode")


class CSINodeList(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description=(
            "APIVersion defines the versioned schema of this representation of an"
            " object. Servers should convert recognized schemas to the latest internal"
            " value, and may reject unrecognized values. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources"
        ),
    )
    items: List[CSINode] = Field(..., description="items is the list of CSINode")
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
            "Standard list metadata More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata"
        ),
    )


class CSIStorageCapacity(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description=(
            "APIVersion defines the versioned schema of this representation of an"
            " object. Servers should convert recognized schemas to the latest internal"
            " value, and may reject unrecognized values. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources"
        ),
    )
    capacity: Optional[resource.Quantity] = Field(
        None,
        description=(
            "capacity is the value reported by the CSI driver in its"
            " GetCapacityResponse for a GetCapacityRequest with topology and parameters"
            " that match the previous fields.\n\nThe semantic is currently (CSI spec"
            " 1.2) defined as: The available capacity, in bytes, of the storage that"
            " can be used to provision volumes. If not set, that information is"
            " currently unavailable."
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
    maximumVolumeSize: Optional[resource.Quantity] = Field(
        None,
        description=(
            "maximumVolumeSize is the value reported by the CSI driver in its"
            " GetCapacityResponse for a GetCapacityRequest with topology and parameters"
            " that match the previous fields.\n\nThis is defined since CSI spec 1.4.0"
            " as the largest size that may be used in a"
            " CreateVolumeRequest.capacity_range.required_bytes field to create a"
            " volume with the same parameters as those in GetCapacityRequest. The"
            " corresponding value in the Kubernetes API is"
            " ResourceRequirements.Requests in a volume claim."
        ),
    )
    metadata: Optional[v1.ObjectMeta] = Field(
        None,
        description=(
            "Standard object's metadata. The name has no particular meaning. It must be"
            " a DNS subdomain (dots allowed, 253 characters). To ensure that there are"
            " no conflicts with other CSI drivers on the cluster, the recommendation is"
            " to use csisc-<uuid>, a generated name, or a reverse-domain name which"
            " ends with the unique CSI driver name.\n\nObjects are namespaced.\n\nMore"
            " info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata"
        ),
    )
    nodeTopology: Optional[v1.LabelSelector] = Field(
        None,
        description=(
            "nodeTopology defines which nodes have access to the storage for which"
            " capacity was reported. If not set, the storage is not accessible from any"
            " node in the cluster. If empty, the storage is accessible from all nodes."
            " This field is immutable."
        ),
    )
    storageClassName: str = Field(
        ...,
        description=(
            "storageClassName represents the name of the StorageClass that the reported"
            " capacity applies to. It must meet the same requirements as the name of a"
            " StorageClass object (non-empty, DNS subdomain). If that object no longer"
            " exists, the CSIStorageCapacity object is obsolete and should be removed"
            " by its creator. This field is immutable."
        ),
    )


class CSIStorageCapacityList(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description=(
            "APIVersion defines the versioned schema of this representation of an"
            " object. Servers should convert recognized schemas to the latest internal"
            " value, and may reject unrecognized values. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources"
        ),
    )
    items: List[CSIStorageCapacity] = Field(
        ..., description="items is the list of CSIStorageCapacity objects."
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
            "Standard list metadata More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata"
        ),
    )


class StorageClass(BaseModel):
    allowVolumeExpansion: Optional[bool] = Field(
        None,
        description=(
            "allowVolumeExpansion shows whether the storage class allow volume expand."
        ),
    )
    allowedTopologies: Optional[List[v1_1.TopologySelectorTerm]] = Field(
        None,
        description=(
            "allowedTopologies restrict the node topologies where volumes can be"
            " dynamically provisioned. Each volume plugin defines its own supported"
            " topology specifications. An empty TopologySelectorTerm list means there"
            " is no topology restriction. This field is only honored by servers that"
            " enable the VolumeScheduling feature."
        ),
    )
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
        None,
        description=(
            "Standard object's metadata. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata"
        ),
    )
    mountOptions: Optional[List[str]] = Field(
        None,
        description=(
            "mountOptions controls the mountOptions for dynamically provisioned"
            ' PersistentVolumes of this storage class. e.g. ["ro", "soft"]. Not'
            " validated - mount of the PVs will simply fail if one is invalid."
        ),
    )
    parameters: Optional[Dict[str, str]] = Field(
        None,
        description=(
            "parameters holds the parameters for the provisioner that should create"
            " volumes of this storage class."
        ),
    )
    provisioner: str = Field(
        ..., description="provisioner indicates the type of the provisioner."
    )
    reclaimPolicy: Optional[str] = Field(
        None,
        description=(
            "reclaimPolicy controls the reclaimPolicy for dynamically provisioned"
            " PersistentVolumes of this storage class. Defaults to Delete."
        ),
    )
    volumeBindingMode: Optional[str] = Field(
        None,
        description=(
            "volumeBindingMode indicates how PersistentVolumeClaims should be"
            " provisioned and bound.  When unset, VolumeBindingImmediate is used. This"
            " field is only honored by servers that enable the VolumeScheduling"
            " feature."
        ),
    )


class StorageClassList(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description=(
            "APIVersion defines the versioned schema of this representation of an"
            " object. Servers should convert recognized schemas to the latest internal"
            " value, and may reject unrecognized values. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources"
        ),
    )
    items: List[StorageClass] = Field(
        ..., description="items is the list of StorageClasses"
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
            "Standard list metadata More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata"
        ),
    )


class VolumeAttachmentSource(BaseModel):
    inlineVolumeSpec: Optional[v1_1.PersistentVolumeSpec] = Field(
        None,
        description=(
            "inlineVolumeSpec contains all the information necessary to attach a"
            " persistent volume defined by a pod's inline VolumeSource. This field is"
            " populated only for the CSIMigration feature. It contains translated"
            " fields from a pod's inline VolumeSource to a PersistentVolumeSpec. This"
            " field is beta-level and is only honored by servers that enabled the"
            " CSIMigration feature."
        ),
    )
    persistentVolumeName: Optional[str] = Field(
        None,
        description=(
            "persistentVolumeName represents the name of the persistent volume to"
            " attach."
        ),
    )


class VolumeAttachmentSpec(BaseModel):
    attacher: str = Field(
        ...,
        description=(
            "attacher indicates the name of the volume driver that MUST handle this"
            " request. This is the name returned by GetPluginName()."
        ),
    )
    nodeName: str = Field(
        ...,
        description=(
            "nodeName represents the node that the volume should be attached to."
        ),
    )
    source: VolumeAttachmentSource = Field(
        ..., description="source represents the volume that should be attached."
    )


class VolumeAttachmentStatus(BaseModel):
    attachError: Optional[VolumeError] = Field(
        None,
        description=(
            "attachError represents the last error encountered during attach operation,"
            " if any. This field must only be set by the entity completing the attach"
            " operation, i.e. the external-attacher."
        ),
    )
    attached: bool = Field(
        ...,
        description=(
            "attached indicates the volume is successfully attached. This field must"
            " only be set by the entity completing the attach operation, i.e. the"
            " external-attacher."
        ),
    )
    attachmentMetadata: Optional[Dict[str, str]] = Field(
        None,
        description=(
            "attachmentMetadata is populated with any information returned by the"
            " attach operation, upon successful attach, that must be passed into"
            " subsequent WaitForAttach or Mount calls. This field must only be set by"
            " the entity completing the attach operation, i.e. the external-attacher."
        ),
    )
    detachError: Optional[VolumeError] = Field(
        None,
        description=(
            "detachError represents the last error encountered during detach operation,"
            " if any. This field must only be set by the entity completing the detach"
            " operation, i.e. the external-attacher."
        ),
    )


class VolumeAttachment(BaseModel):
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
        None,
        description=(
            "Standard object metadata. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata"
        ),
    )
    spec: VolumeAttachmentSpec = Field(
        ...,
        description=(
            "spec represents specification of the desired attach/detach volume"
            " behavior. Populated by the Kubernetes system."
        ),
    )
    status: Optional[VolumeAttachmentStatus] = Field(
        None,
        description=(
            "status represents status of the VolumeAttachment request. Populated by the"
            " entity completing the attach or detach operation, i.e. the"
            " external-attacher."
        ),
    )


class VolumeAttachmentList(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description=(
            "APIVersion defines the versioned schema of this representation of an"
            " object. Servers should convert recognized schemas to the latest internal"
            " value, and may reject unrecognized values. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources"
        ),
    )
    items: List[VolumeAttachment] = Field(
        ..., description="items is the list of VolumeAttachments"
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
            "Standard list metadata More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata"
        ),
    )