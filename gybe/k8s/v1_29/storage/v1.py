"""Models generated from Kubernetes OpenAPI Spec."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

import gybe.k8s.v1_29.api.resource
import gybe.k8s.v1_29.core.v1
import gybe.k8s.v1_29.meta.v1
from gybe.k8s.types import JSONDict, JSONObj


@dataclass
class CSIDriver:
    """CSIDriver captures information about a Container Storage Interface (CSI) volume driver deployed on the
    cluster. Kubernetes attach detach controller uses this object to determine whether attach is required.
    Kubelet uses this object to determine whether pod information needs to be passed on mount. CSIDriver
    objects are non-namespaced.

    Attributes
    ----------
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object metadata. metadata.Name indicates the name of the CSI driver that this
            object refers to; it MUST be the same name returned by the CSI GetPluginName() call for that
            driver. The driver name must be 63 characters or less, beginning and ending with an alphanumeric
            character ([a-z0-9A-Z]) with dashes (-), dots (.), and alphanumerics between.
        spec: spec represents the specification of the CSI Driver.

    """

    spec: CSIDriverSpec
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[gybe.k8s.v1_29.meta.v1.ObjectMeta] = None


@dataclass
class CSIDriverList:
    """CSIDriverList is a collection of CSIDriver objects.

    Attributes
    ----------
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        items: items is the list of CSIDriver
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard list metadata

    """

    items: List[CSIDriver]
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[JSONObj] = None


@dataclass
class CSIDriverSpec:
    """CSIDriverSpec is the specification of a CSIDriver.

    Attributes
    ----------
        attachRequired: attachRequired indicates this CSI volume driver requires an attach operation (because
            it implements the CSI ControllerPublishVolume() method), and that the Kubernetes attach detach
            controller should call the attach volume interface which checks the volumeattachment status and
            waits until the volume is attached before proceeding to mounting. The CSI external-attacher
            coordinates with CSI volume driver and updates the volumeattachment status when the attach
            operation is complete. If the CSIDriverRegistry feature gate is enabled and the value is specified
            to false, the attach operation will be skipped. Otherwise the attach operation will be called.
            This field is immutable.
        fsGroupPolicy: fsGroupPolicy defines if the underlying volume supports changing ownership and
            permission of the volume before being mounted. Refer to the specific FSGroupPolicy values for
            additional details.  This field is immutable.  Defaults to ReadWriteOnceWithFSType, which will
            examine each volume to determine if Kubernetes should modify ownership and permissions of the
            volume. With the default policy the defined fsGroup will only be applied if a fstype is defined
            and the volume's access mode contains ReadWriteOnce.
        podInfoOnMount: podInfoOnMount indicates this CSI volume driver requires additional pod information
            (like podName, podUID, etc.) during mount operations, if set to true. If set to false, pod
            information will not be passed on mount. Default is false.  The CSI driver specifies
            podInfoOnMount as part of driver deployment. If true, Kubelet will pass pod information as
            VolumeContext in the CSI NodePublishVolume() calls. The CSI driver is responsible for parsing and
            validating the information passed in as VolumeContext.  The following VolumeContext will be passed
            if podInfoOnMount is set to true. This list might grow, but the prefix will be used.
            'csi.storage.k8s.io/pod.name': pod.Name 'csi.storage.k8s.io/pod.namespace': pod.Namespace
            'csi.storage.k8s.io/pod.uid': string(pod.UID) 'csi.storage.k8s.io/ephemeral': 'true' if the volume
            is an ephemeral inline volume                                 defined by a CSIVolumeSource,
            otherwise 'false'  'csi.storage.k8s.io/ephemeral' is a new feature in Kubernetes 1.16. It is only
            required for drivers which support both the 'Persistent' and 'Ephemeral' VolumeLifecycleMode.
            Other drivers can leave pod info disabled and/or ignore this field. As Kubernetes 1.15 doesn't
            support this field, drivers can only support one mode when deployed on such a cluster and the
            deployment determines which mode that is, for example via a command line parameter of the driver.
            This field is immutable.
        requiresRepublish: requiresRepublish indicates the CSI driver wants `NodePublishVolume` being
            periodically called to reflect any possible change in the mounted volume. This field defaults to
            false.  Note: After a successful initial NodePublishVolume call, subsequent calls to
            NodePublishVolume should only update the contents of the volume. New mount points will not be seen
            by a running container.
        seLinuxMount: seLinuxMount specifies if the CSI driver supports '-o context' mount option.  When
            'true', the CSI driver must ensure that all volumes provided by this CSI driver can be mounted
            separately with different `-o context` options. This is typical for storage backends that provide
            volumes as filesystems on block devices or as independent shared volumes. Kubernetes will call
            NodeStage / NodePublish with '-o context=xyz' mount option when mounting a ReadWriteOncePod volume
            used in Pod that has explicitly set SELinux context. In the future, it may be expanded to other
            volume AccessModes. In any case, Kubernetes will ensure that the volume is mounted only with a
            single SELinux context.  When 'false', Kubernetes won't pass any special SELinux mount options to
            the driver. This is typical for volumes that represent subdirectories of a bigger shared
            filesystem.  Default is 'false'.
        storageCapacity: storageCapacity indicates that the CSI volume driver wants pod scheduling to consider
            the storage capacity that the driver deployment will report by creating CSIStorageCapacity objects
            with capacity information, if set to true.  The check can be enabled immediately when deploying a
            driver. In that case, provisioning new volumes with late binding will pause until the driver
            deployment has published some suitable CSIStorageCapacity object.  Alternatively, the driver can
            be deployed with the field unset or false and it can be flipped later when storage capacity
            information has been published.  This field was immutable in Kubernetes <= 1.22 and now is
            mutable.
        tokenRequests: tokenRequests indicates the CSI driver needs pods' service account tokens it is
            mounting volume for to do necessary authentication. Kubelet will pass the tokens in VolumeContext
            in the CSI NodePublishVolume calls. The CSI driver should parse and validate the following
            VolumeContext: 'csi.storage.k8s.io/serviceAccount.tokens': {   '<audience>': {     'token':
            <token>,     'expirationTimestamp': <expiration timestamp in RFC3339>,   },   ... }  Note:
            Audience in each TokenRequest should be different and at most one token is empty string. To
            receive a new token after expiry, RequiresRepublish can be used to trigger NodePublishVolume
            periodically.
        volumeLifecycleModes: volumeLifecycleModes defines what kind of volumes this CSI volume driver
            supports. The default if the list is empty is 'Persistent', which is the usage defined by the CSI
            specification and implemented in Kubernetes via the usual PV/PVC mechanism.  The other mode is
            'Ephemeral'. In this mode, volumes are defined inline inside the pod spec with CSIVolumeSource and
            their lifecycle is tied to the lifecycle of that pod. A driver has to be aware of this because it
            is only going to get a NodePublishVolume call for such a volume.  For more information about
            implementing this mode, see https://kubernetes-csi.github.io/docs/ephemeral-local-volumes.html A
            driver can support one or more of these modes and more modes may be added in the future.  This
            field is beta. This field is immutable.

    """

    attachRequired: Optional[bool] = None
    fsGroupPolicy: Optional[str] = None
    podInfoOnMount: Optional[bool] = None
    requiresRepublish: Optional[bool] = None
    seLinuxMount: Optional[bool] = None
    storageCapacity: Optional[bool] = None
    tokenRequests: Optional[List[TokenRequest]] = None
    volumeLifecycleModes: Optional[List[str]] = None


@dataclass
class CSINode:
    """CSINode holds information about all CSI drivers installed on a node. CSI drivers do not need to create
    the CSINode object directly. As long as they use the node-driver-registrar sidecar container, the
    kubelet will automatically populate the CSINode object for the CSI driver as part of kubelet plugin
    registration. CSINode has the same name as a node. If the object is missing, it means either there are
    no CSI Drivers available on the node, or the Kubelet version is low enough that it doesn't create this
    object. CSINode has an OwnerReference that points to the corresponding node object.

    Attributes
    ----------
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object's metadata. metadata.name must be the Kubernetes node name.
        spec: spec is the specification of CSINode

    """

    spec: CSINodeSpec
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[gybe.k8s.v1_29.meta.v1.ObjectMeta] = None


@dataclass
class CSINodeDriver:
    """CSINodeDriver holds information about the specification of one CSI driver installed on a node
    Attributes:
        allocatable: allocatable represents the volume resources of a node that are available for scheduling.
            This field is beta.
        name: name represents the name of the CSI driver that this object refers to. This MUST be the same
            name returned by the CSI GetPluginName() call for that driver.
        nodeID: nodeID of the node from the driver point of view. This field enables Kubernetes to communicate
            with storage systems that do not share the same nomenclature for nodes. For example, Kubernetes
            may refer to a given node as 'node1', but the storage system may refer to the same node as
            'nodeA'. When Kubernetes issues a command to the storage system to attach a volume to a specific
            node, it can use this field to refer to the node name using the ID that the storage system will
            understand, e.g. 'nodeA' instead of 'node1'. This field is required.
        topologyKeys: topologyKeys is the list of keys supported by the driver. When a driver is initialized
            on a cluster, it provides a set of topology keys that it understands (e.g. 'company.com/zone',
            'company.com/region'). When a driver is initialized on a node, it provides the same topology keys
            along with values. Kubelet will expose these topology keys as labels on its own node object. When
            Kubernetes does topology aware provisioning, it can use this list to determine which labels it
            should retrieve from the node object and pass back to the driver. It is possible for different
            nodes to use different topology keys. This can be empty if driver does not support topology.

    """

    name: str
    nodeID: str
    allocatable: Optional[VolumeNodeResources] = None
    topologyKeys: Optional[List[str]] = None


@dataclass
class CSINodeList:
    """CSINodeList is a collection of CSINode objects.

    Attributes
    ----------
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        items: items is the list of CSINode
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard list metadata

    """

    items: List[CSINode]
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[JSONObj] = None


@dataclass
class CSINodeSpec:
    """CSINodeSpec holds information about the specification of all CSI drivers installed on a node
    Attributes:
        drivers: drivers is a list of information of all CSI Drivers existing on a node. If all drivers in the
            list are uninstalled, this can become empty.

    """

    drivers: List[CSINodeDriver]


@dataclass
class CSIStorageCapacity:
    """CSIStorageCapacity stores the result of one CSI GetCapacity call. For a given StorageClass, this
    describes the available capacity in a particular topology segment.  This can be used when considering
    where to instantiate new PersistentVolumes.  For example this can express things like: - StorageClass
    'standard' has '1234 GiB' available in 'topology.kubernetes.io/zone=us-east1' - StorageClass
    'localssd' has '10 GiB' available in 'kubernetes.io/hostname=knode-abc123'  The following three cases
    all imply that no capacity is available for a certain combination: - no object exists with suitable
    topology and storage class name - such an object exists, but the capacity is unset - such an object
    exists, but the capacity is zero  The producer of these objects can decide which approach is more
    suitable.  They are consumed by the kube-scheduler when a CSI driver opts into capacity-aware
    scheduling with CSIDriverSpec.StorageCapacity. The scheduler compares the MaximumVolumeSize against
    the requested size of pending volumes to filter out unsuitable nodes. If MaximumVolumeSize is unset,
    it falls back to a comparison against the less precise Capacity. If that is also unset, the scheduler
    assumes that capacity is insufficient and tries some other node.

    Attributes
    ----------
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        capacity: capacity is the value reported by the CSI driver in its GetCapacityResponse for a
            GetCapacityRequest with topology and parameters that match the previous fields.  The semantic is
            currently (CSI spec 1.2) defined as: The available capacity, in bytes, of the storage that can be
            used to provision volumes. If not set, that information is currently unavailable.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        maximumVolumeSize: maximumVolumeSize is the value reported by the CSI driver in its
            GetCapacityResponse for a GetCapacityRequest with topology and parameters that match the previous
            fields.  This is defined since CSI spec 1.4.0 as the largest size that may be used in a
            CreateVolumeRequest.capacity_range.required_bytes field to create a volume with the same
            parameters as those in GetCapacityRequest. The corresponding value in the Kubernetes API is
            ResourceRequirements.Requests in a volume claim.
        metadata: Standard object's metadata. The name has no particular meaning. It must be a DNS subdomain
            (dots allowed, 253 characters). To ensure that there are no conflicts with other CSI drivers on
            the cluster, the recommendation is to use csisc-<uuid>, a generated name, or a reverse-domain name
            which ends with the unique CSI driver name.  Objects are namespaced.
        nodeTopology: nodeTopology defines which nodes have access to the storage for which capacity was
            reported. If not set, the storage is not accessible from any node in the cluster. If empty, the
            storage is accessible from all nodes. This field is immutable.
        storageClassName: storageClassName represents the name of the StorageClass that the reported capacity
            applies to. It must meet the same requirements as the name of a StorageClass object (non-empty,
            DNS subdomain). If that object no longer exists, the CSIStorageCapacity object is obsolete and
            should be removed by its creator. This field is immutable.

    """

    storageClassName: str
    apiVersion: Optional[str] = None
    capacity: Optional[gybe.k8s.v1_29.api.resource.Quantity] = None
    kind: Optional[str] = None
    maximumVolumeSize: Optional[gybe.k8s.v1_29.api.resource.Quantity] = None
    metadata: Optional[gybe.k8s.v1_29.meta.v1.ObjectMeta] = None
    nodeTopology: Optional[gybe.k8s.v1_29.meta.v1.LabelSelector] = None


@dataclass
class CSIStorageCapacityList:
    """CSIStorageCapacityList is a collection of CSIStorageCapacity objects.

    Attributes
    ----------
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        items: items is the list of CSIStorageCapacity objects.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard list metadata

    """

    items: List[CSIStorageCapacity]
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[JSONObj] = None


@dataclass
class StorageClass:
    """StorageClass describes the parameters for a class of storage for which PersistentVolumes can be
    dynamically provisioned.  StorageClasses are non-namespaced; the name of the storage class according
    to etcd is in ObjectMeta.Name.

    Attributes
    ----------
        allowVolumeExpansion: allowVolumeExpansion shows whether the storage class allow volume expand.
        allowedTopologies: allowedTopologies restrict the node topologies where volumes can be dynamically
            provisioned. Each volume plugin defines its own supported topology specifications. An empty
            TopologySelectorTerm list means there is no topology restriction. This field is only honored by
            servers that enable the VolumeScheduling feature.
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object's metadata.
        mountOptions: mountOptions controls the mountOptions for dynamically provisioned PersistentVolumes of
            this storage class. e.g. ['ro', 'soft']. Not validated - mount of the PVs will simply fail if one
            is invalid.
        parameters: parameters holds the parameters for the provisioner that should create volumes of this
            storage class.
        provisioner: provisioner indicates the type of the provisioner.
        reclaimPolicy: reclaimPolicy controls the reclaimPolicy for dynamically provisioned PersistentVolumes
            of this storage class. Defaults to Delete.
        volumeBindingMode: volumeBindingMode indicates how PersistentVolumeClaims should be provisioned and
            bound.  When unset, VolumeBindingImmediate is used. This field is only honored by servers that
            enable the VolumeScheduling feature.

    """

    provisioner: str
    allowVolumeExpansion: Optional[bool] = None
    allowedTopologies: Optional[List[gybe.k8s.v1_29.core.v1.TopologySelectorTerm]] = None
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[gybe.k8s.v1_29.meta.v1.ObjectMeta] = None
    mountOptions: Optional[List[str]] = None
    parameters: Optional[JSONDict] = None
    reclaimPolicy: Optional[str] = None
    volumeBindingMode: Optional[str] = None


@dataclass
class StorageClassList:
    """StorageClassList is a collection of storage classes.

    Attributes
    ----------
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        items: items is the list of StorageClasses
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard list metadata

    """

    items: List[StorageClass]
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[JSONObj] = None


@dataclass
class TokenRequest:
    """TokenRequest contains parameters of a service account token.

    Attributes
    ----------
        audience: audience is the intended audience of the token in 'TokenRequestSpec'. It will default to the
            audiences of kube apiserver.
        expirationSeconds: expirationSeconds is the duration of validity of the token in 'TokenRequestSpec'.
            It has the same default value of 'ExpirationSeconds' in 'TokenRequestSpec'.

    """

    audience: str
    expirationSeconds: Optional[int] = None


@dataclass
class VolumeAttachment:
    """VolumeAttachment captures the intent to attach or detach the specified volume to/from the specified
    node.  VolumeAttachment objects are non-namespaced.

    Attributes
    ----------
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object metadata.
        spec: spec represents specification of the desired attach/detach volume behavior. Populated by the
            Kubernetes system.
        status: status represents status of the VolumeAttachment request. Populated by the entity completing
            the attach or detach operation, i.e. the external-attacher.

    """

    spec: VolumeAttachmentSpec
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[gybe.k8s.v1_29.meta.v1.ObjectMeta] = None
    status: Optional[VolumeAttachmentStatus] = None


@dataclass
class VolumeAttachmentList:
    """VolumeAttachmentList is a collection of VolumeAttachment objects.

    Attributes
    ----------
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        items: items is the list of VolumeAttachments
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard list metadata

    """

    items: List[VolumeAttachment]
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[JSONObj] = None


@dataclass
class VolumeAttachmentSource:
    """VolumeAttachmentSource represents a volume that should be attached. Right now only PersistenVolumes
    can be attached via external attacher, in future we may allow also inline volumes in pods. Exactly one
    member can be set.

    Attributes
    ----------
        inlineVolumeSpec: inlineVolumeSpec contains all the information necessary to attach a persistent
            volume defined by a pod's inline VolumeSource. This field is populated only for the CSIMigration
            feature. It contains translated fields from a pod's inline VolumeSource to a PersistentVolumeSpec.
            This field is beta-level and is only honored by servers that enabled the CSIMigration feature.
        persistentVolumeName: persistentVolumeName represents the name of the persistent volume to attach.

    """

    inlineVolumeSpec: Optional[gybe.k8s.v1_29.core.v1.PersistentVolumeSpec] = None
    persistentVolumeName: Optional[str] = None


@dataclass
class VolumeAttachmentSpec:
    """VolumeAttachmentSpec is the specification of a VolumeAttachment request.

    Attributes
    ----------
        attacher: attacher indicates the name of the volume driver that MUST handle this request. This is the
            name returned by GetPluginName().
        nodeName: nodeName represents the node that the volume should be attached to.
        source: source represents the volume that should be attached.

    """

    attacher: str
    source: VolumeAttachmentSource
    nodeName: str


@dataclass
class VolumeAttachmentStatus:
    """VolumeAttachmentStatus is the status of a VolumeAttachment request.

    Attributes
    ----------
        attachError: attachError represents the last error encountered during attach operation, if any. This
            field must only be set by the entity completing the attach operation, i.e. the external-attacher.
        attached: attached indicates the volume is successfully attached. This field must only be set by the
            entity completing the attach operation, i.e. the external-attacher.
        attachmentMetadata: attachmentMetadata is populated with any information returned by the attach
            operation, upon successful attach, that must be passed into subsequent WaitForAttach or Mount
            calls. This field must only be set by the entity completing the attach operation, i.e. the
            external-attacher.
        detachError: detachError represents the last error encountered during detach operation, if any. This
            field must only be set by the entity completing the detach operation, i.e. the external-attacher.

    """

    attached: bool
    attachError: Optional[VolumeError] = None
    attachmentMetadata: Optional[JSONDict] = None
    detachError: Optional[VolumeError] = None


@dataclass
class VolumeError:
    """VolumeError captures an error encountered during a volume operation.

    Attributes
    ----------
        message: message represents the error encountered during Attach or Detach operation. This string may
            be logged, so it should not contain sensitive information.
        time: time represents the time the error was encountered.

    """

    message: Optional[str] = None
    time: Optional[str] = None


@dataclass
class VolumeNodeResources:
    """VolumeNodeResources is a set of resource limits for scheduling of volumes.

    Attributes
    ----------
        count: count indicates the maximum number of unique volumes managed by the CSI driver that can be used
            on a node. A volume that is both attached and mounted on a node is considered to be used once, not
            twice. The same rule applies for a unique volume that is shared among multiple pods on the same
            node. If this field is not specified, then the supported number of volumes on this node is
            unbounded.

    """

    count: Optional[int] = None
