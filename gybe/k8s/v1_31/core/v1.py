"""Models generated from Kubernetes OpenAPI Spec."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Literal, Optional

import gybe.k8s.v1_31.api.resource
import gybe.k8s.v1_31.meta.v1
from gybe.k8s.types import JSONDict, JSONObj, K8sResource, K8sSpec


@dataclass
class EventSource(K8sSpec):
    """EventSource contains information for an event.

    Attributes:
        component: Component from which the event is generated.
        host: Node name on which the event is generated.

    """

    component: Optional[str] = None
    host: Optional[str] = None


@dataclass
class ObjectReference(K8sSpec):
    """ObjectReference contains enough information to let you inspect or modify the referred object.

    Attributes:
        apiVersion: API version of the referent.
        fieldPath: If referring to a piece of an object instead of an entire object, this string should
            contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2]. For
            example, if the object reference is to a container within a pod, this would take on a value like:
            'spec.containers{name}' (where 'name' refers to the name of the container that triggered the
            event) or if no container name is specified 'spec.containers[2]' (container with index 2 in this
            pod). This syntax is chosen only to have some well-defined way of referencing a part of an object.
        kind: Kind of the referent.
        name: Name of the referent.
        namespace: Namespace of the referent.
        resourceVersion: Specific resourceVersion to which this reference is made, if any.
        uid: UID of the referent.

    """

    apiVersion: Optional[str] = None
    fieldPath: Optional[str] = None
    kind: Optional[str] = None
    name: Optional[str] = None
    namespace: Optional[str] = None
    resourceVersion: Optional[str] = None
    uid: Optional[str] = None


@dataclass
class NodeSelector(K8sSpec):
    """A node selector represents the union of the results of one or more label queries over a set of nodes;
    that is, it represents the OR of the selectors represented by the node selector terms.

    Attributes:
        nodeSelectorTerms: Required. A list of node selector terms. The terms are ORed.

    """

    nodeSelectorTerms: List[NodeSelectorTerm]


@dataclass
class NodeSelectorRequirement(K8sSpec):
    """A node selector requirement is a selector that contains values, a key, and an operator that relates
    the key and values.

    Attributes:
        key: The label key that the selector applies to.
        operator: Represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists,
            DoesNotExist. Gt, and Lt.
        values: An array of string values. If the operator is In or NotIn, the values array must be non-empty.
            If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt
            or Lt, the values array must have a single element, which will be interpreted as an integer. This
            array is replaced during a strategic merge patch.

    """

    key: str
    operator: str
    values: Optional[List[str]] = None


@dataclass
class NodeSelectorTerm(K8sSpec):
    """A null or empty node selector term matches no objects. The requirements of them are ANDed. The
    TopologySelectorTerm type implements a subset of the NodeSelectorTerm.

    Attributes:
        matchExpressions: A list of node selector requirements by node's labels.
        matchFields: A list of node selector requirements by node's fields.

    """

    matchExpressions: Optional[List[NodeSelectorRequirement]] = None
    matchFields: Optional[List[NodeSelectorRequirement]] = None


@dataclass
class AWSElasticBlockStoreVolumeSource(K8sSpec):
    """Represents a Persistent Disk resource in AWS.  An AWS EBS disk must exist before mounting to a
    container. The disk must also be in the same AWS zone as the kubelet. An AWS EBS disk can only be
    mounted as read/write once. AWS EBS volumes support ownership management and SELinux relabeling.

    Attributes:
        fsType: fsType is the filesystem type of the volume that you want to mount. Tip: Ensure that the
            filesystem type is supported by the host operating system. Examples: 'ext4', 'xfs', 'ntfs'.
            Implicitly inferred to be 'ext4' if unspecified.
        partition: partition is the partition in the volume that you want to mount. If omitted, the default is
            to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as '1'.
            Similarly, the volume partition for /dev/sda is '0' (or you can leave the property empty).
        readOnly: readOnly value true will force the readOnly setting in VolumeMounts.
        volumeID: volumeID is unique ID of the persistent disk resource in AWS (Amazon EBS volume).

    """

    volumeID: str
    fsType: Optional[str] = None
    partition: Optional[int] = None
    readOnly: Optional[bool] = None


@dataclass
class AzureDiskVolumeSource(K8sSpec):
    """AzureDisk represents an Azure Data Disk mount on the host and bind mount to the pod.

    Attributes:
        cachingMode: cachingMode is the Host Caching mode: None, Read Only, Read Write.
        diskName: diskName is the Name of the data disk in the blob storage
        diskURI: diskURI is the URI of data disk in the blob storage
        fsType: fsType is Filesystem type to mount. Must be a filesystem type supported by the host operating
            system. Ex. 'ext4', 'xfs', 'ntfs'. Implicitly inferred to be 'ext4' if unspecified.
        kind: kind expected values are Shared: multiple blob disks per storage account  Dedicated: single blob
            disk per storage account  Managed: azure managed data disk (only in managed availability set).
            defaults to shared
        readOnly: readOnly Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in
            VolumeMounts.

    """

    diskName: str
    diskURI: str
    cachingMode: Optional[str] = None
    fsType: Optional[str] = None
    kind: Optional[str] = None
    readOnly: Optional[bool] = None


@dataclass
class AzureFilePersistentVolumeSource(K8sSpec):
    """AzureFile represents an Azure File Service mount on the host and bind mount to the pod.

    Attributes:
        readOnly: readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in
            VolumeMounts.
        secretName: secretName is the name of secret that contains Azure Storage Account Name and Key
        secretNamespace: secretNamespace is the namespace of the secret that contains Azure Storage Account
            Name and Key default is the same as the Pod
        shareName: shareName is the azure Share Name

    """

    secretName: str
    shareName: str
    readOnly: Optional[bool] = None
    secretNamespace: Optional[str] = None


@dataclass
class CSIPersistentVolumeSource(K8sSpec):
    """Represents storage that is managed by an external CSI volume driver (Beta feature)

    Attributes:
        controllerExpandSecretRef: controllerExpandSecretRef is a reference to the secret object containing
            sensitive information to pass to the CSI driver to complete the CSI ControllerExpandVolume call.
            This field is optional, and may be empty if no secret is required. If the secret object contains
            more than one secret, all secrets are passed.
        controllerPublishSecretRef: controllerPublishSecretRef is a reference to the secret object containing
            sensitive information to pass to the CSI driver to complete the CSI ControllerPublishVolume and
            ControllerUnpublishVolume calls. This field is optional, and may be empty if no secret is
            required. If the secret object contains more than one secret, all secrets are passed.
        driver: driver is the name of the driver to use for this volume. Required.
        fsType: fsType to mount. Must be a filesystem type supported by the host operating system. Ex. 'ext4',
            'xfs', 'ntfs'.
        nodeExpandSecretRef: nodeExpandSecretRef is a reference to the secret object containing sensitive
            information to pass to the CSI driver to complete the CSI NodeExpandVolume call. This field is
            optional, may be omitted if no secret is required. If the secret object contains more than one
            secret, all secrets are passed.
        nodePublishSecretRef: nodePublishSecretRef is a reference to the secret object containing sensitive
            information to pass to the CSI driver to complete the CSI NodePublishVolume and
            NodeUnpublishVolume calls. This field is optional, and may be empty if no secret is required. If
            the secret object contains more than one secret, all secrets are passed.
        nodeStageSecretRef: nodeStageSecretRef is a reference to the secret object containing sensitive
            information to pass to the CSI driver to complete the CSI NodeStageVolume and NodeStageVolume and
            NodeUnstageVolume calls. This field is optional, and may be empty if no secret is required. If the
            secret object contains more than one secret, all secrets are passed.
        readOnly: readOnly value to pass to ControllerPublishVolumeRequest. Defaults to false (read/write).
        volumeAttributes: volumeAttributes of the volume to publish.
        volumeHandle: volumeHandle is the unique volume name returned by the CSI volume plugin’s CreateVolume
            to refer to the volume on all subsequent calls. Required.

    """

    driver: str
    volumeHandle: str
    controllerExpandSecretRef: Optional[SecretReference] = None
    controllerPublishSecretRef: Optional[SecretReference] = None
    fsType: Optional[str] = None
    nodeExpandSecretRef: Optional[SecretReference] = None
    nodePublishSecretRef: Optional[SecretReference] = None
    nodeStageSecretRef: Optional[SecretReference] = None
    readOnly: Optional[bool] = None
    volumeAttributes: Optional[JSONDict] = None


@dataclass
class CephFSPersistentVolumeSource(K8sSpec):
    """Represents a Ceph Filesystem mount that lasts the lifetime of a pod Cephfs volumes do not support
    ownership management or SELinux relabeling.

    Attributes:
        monitors: monitors is Required: Monitors is a collection of Ceph monitors
        path: path is Optional: Used as the mounted root, rather than the full Ceph tree, default is /
        readOnly: readOnly is Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly
            setting in VolumeMounts.
        secretFile: secretFile is Optional: SecretFile is the path to key ring for User, default is
            /etc/ceph/user.secret
        secretRef: secretRef is Optional: SecretRef is reference to the authentication secret for User,
            default is empty.
        user: user is Optional: User is the rados user name, default is admin

    """

    monitors: List[str]
    path: Optional[str] = None
    readOnly: Optional[bool] = None
    secretFile: Optional[str] = None
    secretRef: Optional[SecretReference] = None
    user: Optional[str] = None


@dataclass
class CinderPersistentVolumeSource(K8sSpec):
    """Represents a cinder volume resource in Openstack. A Cinder volume must exist before mounting to a
    container. The volume must also be in the same region as the kubelet. Cinder volumes support ownership
    management and SELinux relabeling.

    Attributes:
        fsType: fsType Filesystem type to mount. Must be a filesystem type supported by the host operating
            system. Examples: 'ext4', 'xfs', 'ntfs'. Implicitly inferred to be 'ext4' if unspecified.
        readOnly: readOnly is Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly
            setting in VolumeMounts.
        secretRef: secretRef is Optional: points to a secret object containing parameters used to connect to
            OpenStack.
        volumeID: volumeID used to identify the volume in cinder.

    """

    volumeID: str
    fsType: Optional[str] = None
    readOnly: Optional[bool] = None
    secretRef: Optional[SecretReference] = None


@dataclass
class FCVolumeSource(K8sSpec):
    """Represents a Fibre Channel volume. Fibre Channel volumes can only be mounted as read/write once. Fibre
    Channel volumes support ownership management and SELinux relabeling.

    Attributes:
        fsType: fsType is the filesystem type to mount. Must be a filesystem type supported by the host
            operating system. Ex. 'ext4', 'xfs', 'ntfs'. Implicitly inferred to be 'ext4' if unspecified.
        lun: lun is Optional: FC target lun number
        readOnly: readOnly is Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly
            setting in VolumeMounts.
        targetWWNs: targetWWNs is Optional: FC target worldwide names (WWNs)
        wwids: wwids Optional: FC volume world wide identifiers (wwids) Either wwids or combination of
            targetWWNs and lun must be set, but not both simultaneously.

    """

    fsType: Optional[str] = None
    lun: Optional[int] = None
    readOnly: Optional[bool] = None
    targetWWNs: Optional[List[str]] = None
    wwids: Optional[List[str]] = None


@dataclass
class FlexPersistentVolumeSource(K8sSpec):
    """FlexPersistentVolumeSource represents a generic persistent volume resource that is
    provisioned/attached using an exec based plugin.

    Attributes:
        driver: driver is the name of the driver to use for this volume.
        fsType: fsType is the Filesystem type to mount. Must be a filesystem type supported by the host
            operating system. Ex. 'ext4', 'xfs', 'ntfs'. The default filesystem depends on FlexVolume script.
        options: options is Optional: this field holds extra command options if any.
        readOnly: readOnly is Optional: defaults to false (read/write). ReadOnly here will force the ReadOnly
            setting in VolumeMounts.
        secretRef: secretRef is Optional: SecretRef is reference to the secret object containing sensitive
            information to pass to the plugin scripts. This may be empty if no secret object is specified. If
            the secret object contains more than one secret, all secrets are passed to the plugin scripts.

    """

    driver: str
    fsType: Optional[str] = None
    options: Optional[JSONDict] = None
    readOnly: Optional[bool] = None
    secretRef: Optional[SecretReference] = None


@dataclass
class FlockerVolumeSource(K8sSpec):
    """Represents a Flocker volume mounted by the Flocker agent. One and only one of datasetName and
    datasetUUID should be set. Flocker volumes do not support ownership management or SELinux relabeling.

    Attributes:
        datasetName: datasetName is Name of the dataset stored as metadata -> name on the dataset for Flocker
            should be considered as deprecated
        datasetUUID: datasetUUID is the UUID of the dataset. This is unique identifier of a Flocker dataset

    """

    datasetName: Optional[str] = None
    datasetUUID: Optional[str] = None


@dataclass
class GCEPersistentDiskVolumeSource(K8sSpec):
    """Represents a Persistent Disk resource in Google Compute Engine.  A GCE PD must exist before mounting
    to a container. The disk must also be in the same GCE project and zone as the kubelet. A GCE PD can
    only be mounted as read/write once or read-only many times. GCE PDs support ownership management and
    SELinux relabeling.

    Attributes:
        fsType: fsType is filesystem type of the volume that you want to mount. Tip: Ensure that the
            filesystem type is supported by the host operating system. Examples: 'ext4', 'xfs', 'ntfs'.
            Implicitly inferred to be 'ext4' if unspecified.
        partition: partition is the partition in the volume that you want to mount. If omitted, the default is
            to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as '1'.
            Similarly, the volume partition for /dev/sda is '0' (or you can leave the property empty).
        pdName: pdName is unique name of the PD resource in GCE. Used to identify the disk in GCE.
        readOnly: readOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false.

    """

    pdName: str
    fsType: Optional[str] = None
    partition: Optional[int] = None
    readOnly: Optional[bool] = None


@dataclass
class GlusterfsPersistentVolumeSource(K8sSpec):
    """Represents a Glusterfs mount that lasts the lifetime of a pod. Glusterfs volumes do not support
    ownership management or SELinux relabeling.

    Attributes:
        endpoints: endpoints is the endpoint name that details Glusterfs topology.
        endpointsNamespace: endpointsNamespace is the namespace that contains Glusterfs endpoint. If this
            field is empty, the EndpointNamespace defaults to the same namespace as the bound PVC.
        path: path is the Glusterfs volume path.
        readOnly: readOnly here will force the Glusterfs volume to be mounted with read-only permissions.
            Defaults to false.

    """

    endpoints: str
    path: str
    endpointsNamespace: Optional[str] = None
    readOnly: Optional[bool] = None


@dataclass
class HostPathVolumeSource(K8sSpec):
    """Represents a host path mapped into a pod. Host path volumes do not support ownership management or
    SELinux relabeling.

    Attributes:
        path: path of the directory on the host. If the path is a symlink, it will follow the link to the real
            path.
        type: type for HostPath Volume Defaults to ''

    """

    path: str
    type: Optional[str] = None


@dataclass
class ISCSIPersistentVolumeSource(K8sSpec):
    """ISCSIPersistentVolumeSource represents an ISCSI disk. ISCSI volumes can only be mounted as read/write
    once. ISCSI volumes support ownership management and SELinux relabeling.

    Attributes:
        chapAuthDiscovery: chapAuthDiscovery defines whether support iSCSI Discovery CHAP authentication
        chapAuthSession: chapAuthSession defines whether support iSCSI Session CHAP authentication
        fsType: fsType is the filesystem type of the volume that you want to mount. Tip: Ensure that the
            filesystem type is supported by the host operating system. Examples: 'ext4', 'xfs', 'ntfs'.
            Implicitly inferred to be 'ext4' if unspecified.
        initiatorName: initiatorName is the custom iSCSI Initiator Name. If initiatorName is specified with
            iscsiInterface simultaneously, new iSCSI interface <target portal>:<volume name> will be created
            for the connection.
        iqn: iqn is Target iSCSI Qualified Name.
        iscsiInterface: iscsiInterface is the interface Name that uses an iSCSI transport. Defaults to
            'default' (tcp).
        lun: lun is iSCSI Target Lun number.
        portals: portals is the iSCSI Target Portal List. The Portal is either an IP or ip_addr:port if the
            port is other than default (typically TCP ports 860 and 3260).
        readOnly: readOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false.
        secretRef: secretRef is the CHAP Secret for iSCSI target and initiator authentication
        targetPortal: targetPortal is iSCSI Target Portal. The Portal is either an IP or ip_addr:port if the
            port is other than default (typically TCP ports 860 and 3260).

    """

    targetPortal: str
    iqn: str
    lun: int
    chapAuthDiscovery: Optional[bool] = None
    chapAuthSession: Optional[bool] = None
    fsType: Optional[str] = None
    initiatorName: Optional[str] = None
    iscsiInterface: Optional[str] = None
    portals: Optional[List[str]] = None
    readOnly: Optional[bool] = None
    secretRef: Optional[SecretReference] = None


@dataclass
class LocalVolumeSource(K8sSpec):
    """Local represents directly-attached storage with node affinity (Beta feature)

    Attributes:
        fsType: fsType is the filesystem type to mount. It applies only when the Path is a block device. Must
            be a filesystem type supported by the host operating system. Ex. 'ext4', 'xfs', 'ntfs'. The
            default value is to auto-select a filesystem if unspecified.
        path: path of the full path to the volume on the node. It can be either a directory or block device
            (disk, partition, ...).

    """

    path: str
    fsType: Optional[str] = None


@dataclass
class NFSVolumeSource(K8sSpec):
    """Represents an NFS mount that lasts the lifetime of a pod. NFS volumes do not support ownership
    management or SELinux relabeling.

    Attributes:
        path: path that is exported by the NFS server.
        readOnly: readOnly here will force the NFS export to be mounted with read-only permissions. Defaults
            to false.
        server: server is the hostname or IP address of the NFS server.

    """

    server: str
    path: str
    readOnly: Optional[bool] = None


@dataclass
class PersistentVolumeSpec(K8sSpec):
    """PersistentVolumeSpec is the specification of a persistent volume.

    Attributes:
        accessModes: accessModes contains all ways the volume can be mounted.
        awsElasticBlockStore: awsElasticBlockStore represents an AWS Disk resource that is attached to a
            kubelet's host machine and then exposed to the pod.
        azureDisk: azureDisk represents an Azure Data Disk mount on the host and bind mount to the pod.
        azureFile: azureFile represents an Azure File Service mount on the host and bind mount to the pod.
        capacity: capacity is the description of the persistent volume's resources and capacity.
        cephfs: cephFS represents a Ceph FS mount on the host that shares a pod's lifetime
        cinder: cinder represents a cinder volume attached and mounted on kubelets host machine.
        claimRef: claimRef is part of a bi-directional binding between PersistentVolume and
            PersistentVolumeClaim. Expected to be non-nil when bound. claim.VolumeName is the authoritative
            bind between PV and PVC.
        csi: csi represents storage that is handled by an external CSI driver (Beta feature).
        fc: fc represents a Fibre Channel resource that is attached to a kubelet's host machine and then
            exposed to the pod.
        flexVolume: flexVolume represents a generic volume resource that is provisioned/attached using an exec
            based plugin.
        flocker: flocker represents a Flocker volume attached to a kubelet's host machine and exposed to the
            pod for its usage. This depends on the Flocker control service being running
        gcePersistentDisk: gcePersistentDisk represents a GCE Disk resource that is attached to a kubelet's
            host machine and then exposed to the pod. Provisioned by an admin.
        glusterfs: glusterfs represents a Glusterfs volume that is attached to a host and exposed to the pod.
            Provisioned by an admin.
        hostPath: hostPath represents a directory on the host. Provisioned by a developer or tester. This is
            useful for single-node development and testing only! On-host storage is not supported in any way
            and WILL NOT WORK in a multi-node cluster.
        iscsi: iscsi represents an ISCSI Disk resource that is attached to a kubelet's host machine and then
            exposed to the pod. Provisioned by an admin.
        local: local represents directly-attached storage with node affinity
        mountOptions: mountOptions is the list of mount options, e.g. ['ro', 'soft']. Not validated - mount
            will simply fail if one is invalid.
        nfs: nfs represents an NFS mount on the host. Provisioned by an admin.
        nodeAffinity: nodeAffinity defines constraints that limit what nodes this volume can be accessed from.
            This field influences the scheduling of pods that use this volume.
        persistentVolumeReclaimPolicy: persistentVolumeReclaimPolicy defines what happens to a persistent
            volume when released from its claim. Valid options are Retain (default for manually created
            PersistentVolumes), Delete (default for dynamically provisioned PersistentVolumes), and Recycle
            (deprecated). Recycle must be supported by the volume plugin underlying this PersistentVolume.
        photonPersistentDisk: photonPersistentDisk represents a PhotonController persistent disk attached and
            mounted on kubelets host machine
        portworxVolume: portworxVolume represents a portworx volume attached and mounted on kubelets host
            machine
        quobyte: quobyte represents a Quobyte mount on the host that shares a pod's lifetime
        rbd: rbd represents a Rados Block Device mount on the host that shares a pod's lifetime.
        scaleIO: scaleIO represents a ScaleIO persistent volume attached and mounted on Kubernetes nodes.
        storageClassName: storageClassName is the name of StorageClass to which this persistent volume
            belongs. Empty value means that this volume does not belong to any StorageClass.
        storageos: storageOS represents a StorageOS volume that is attached to the kubelet's host machine and
            mounted into the pod
        volumeAttributesClassName: Name of VolumeAttributesClass to which this persistent volume belongs.
            Empty value is not allowed. When this field is not set, it indicates that this volume does not
            belong to any VolumeAttributesClass. This field is mutable and can be changed by the CSI driver
            after a volume has been updated successfully to a new class. For an unbound PersistentVolume, the
            volumeAttributesClassName will be matched with unbound PersistentVolumeClaims during the binding
            process. This is a beta field and requires enabling VolumeAttributesClass feature (off by
            default).
        volumeMode: volumeMode defines if a volume is intended to be used with a formatted filesystem or to
            remain in raw block state. Value of Filesystem is implied when not included in spec.
        vsphereVolume: vsphereVolume represents a vSphere volume attached and mounted on kubelets host machine

    """

    accessModes: Optional[List[str]] = None
    awsElasticBlockStore: Optional[AWSElasticBlockStoreVolumeSource] = None
    azureDisk: Optional[AzureDiskVolumeSource] = None
    azureFile: Optional[AzureFilePersistentVolumeSource] = None
    capacity: Optional[JSONDict] = None
    cephfs: Optional[CephFSPersistentVolumeSource] = None
    cinder: Optional[CinderPersistentVolumeSource] = None
    claimRef: Optional[ObjectReference] = None
    csi: Optional[CSIPersistentVolumeSource] = None
    fc: Optional[FCVolumeSource] = None
    flexVolume: Optional[FlexPersistentVolumeSource] = None
    flocker: Optional[FlockerVolumeSource] = None
    gcePersistentDisk: Optional[GCEPersistentDiskVolumeSource] = None
    glusterfs: Optional[GlusterfsPersistentVolumeSource] = None
    hostPath: Optional[HostPathVolumeSource] = None
    iscsi: Optional[ISCSIPersistentVolumeSource] = None
    local: Optional[LocalVolumeSource] = None
    mountOptions: Optional[List[str]] = None
    nfs: Optional[NFSVolumeSource] = None
    nodeAffinity: Optional[VolumeNodeAffinity] = None
    persistentVolumeReclaimPolicy: Optional[str] = None
    photonPersistentDisk: Optional[PhotonPersistentDiskVolumeSource] = None
    portworxVolume: Optional[PortworxVolumeSource] = None
    quobyte: Optional[QuobyteVolumeSource] = None
    rbd: Optional[RBDPersistentVolumeSource] = None
    scaleIO: Optional[ScaleIOPersistentVolumeSource] = None
    storageClassName: Optional[str] = None
    storageos: Optional[StorageOSPersistentVolumeSource] = None
    volumeAttributesClassName: Optional[str] = None
    volumeMode: Optional[str] = None
    vsphereVolume: Optional[VsphereVirtualDiskVolumeSource] = None


@dataclass
class PhotonPersistentDiskVolumeSource(K8sSpec):
    """Represents a Photon Controller persistent disk resource.

    Attributes:
        fsType: fsType is the filesystem type to mount. Must be a filesystem type supported by the host
            operating system. Ex. 'ext4', 'xfs', 'ntfs'. Implicitly inferred to be 'ext4' if unspecified.
        pdID: pdID is the ID that identifies Photon Controller persistent disk

    """

    pdID: str
    fsType: Optional[str] = None


@dataclass
class PortworxVolumeSource(K8sSpec):
    """PortworxVolumeSource represents a Portworx volume resource.

    Attributes:
        fsType: fSType represents the filesystem type to mount Must be a filesystem type supported by the host
            operating system. Ex. 'ext4', 'xfs'. Implicitly inferred to be 'ext4' if unspecified.
        readOnly: readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in
            VolumeMounts.
        volumeID: volumeID uniquely identifies a Portworx volume

    """

    volumeID: str
    fsType: Optional[str] = None
    readOnly: Optional[bool] = None


@dataclass
class QuobyteVolumeSource(K8sSpec):
    """Represents a Quobyte mount that lasts the lifetime of a pod. Quobyte volumes do not support ownership
    management or SELinux relabeling.

    Attributes:
        group: group to map volume access to Default is no group
        readOnly: readOnly here will force the Quobyte volume to be mounted with read-only permissions.
            Defaults to false.
        registry: registry represents a single or multiple Quobyte Registry services specified as a string as
            host:port pair (multiple entries are separated with commas) which acts as the central registry for
            volumes
        tenant: tenant owning the given Quobyte volume in the Backend Used with dynamically provisioned
            Quobyte volumes, value is set by the plugin
        user: user to map volume access to Defaults to serivceaccount user
        volume: volume is a string that references an already created Quobyte volume by name.

    """

    registry: str
    volume: str
    group: Optional[str] = None
    readOnly: Optional[bool] = None
    tenant: Optional[str] = None
    user: Optional[str] = None


@dataclass
class RBDPersistentVolumeSource(K8sSpec):
    """Represents a Rados Block Device mount that lasts the lifetime of a pod. RBD volumes support ownership
    management and SELinux relabeling.

    Attributes:
        fsType: fsType is the filesystem type of the volume that you want to mount. Tip: Ensure that the
            filesystem type is supported by the host operating system. Examples: 'ext4', 'xfs', 'ntfs'.
            Implicitly inferred to be 'ext4' if unspecified.
        image: image is the rados image name.
        keyring: keyring is the path to key ring for RBDUser. Default is /etc/ceph/keyring.
        monitors: monitors is a collection of Ceph monitors.
        pool: pool is the rados pool name. Default is rbd.
        readOnly: readOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false.
        secretRef: secretRef is name of the authentication secret for RBDUser. If provided overrides keyring.
            Default is nil.
        user: user is the rados user name. Default is admin.

    """

    monitors: List[str]
    image: str
    fsType: Optional[str] = None
    keyring: Optional[str] = None
    pool: Optional[str] = None
    readOnly: Optional[bool] = None
    secretRef: Optional[SecretReference] = None
    user: Optional[str] = None


@dataclass
class ScaleIOPersistentVolumeSource(K8sSpec):
    """ScaleIOPersistentVolumeSource represents a persistent ScaleIO volume
    Attributes:
        fsType: fsType is the filesystem type to mount. Must be a filesystem type supported by the host
            operating system. Ex. 'ext4', 'xfs', 'ntfs'. Default is 'xfs'
        gateway: gateway is the host address of the ScaleIO API Gateway.
        protectionDomain: protectionDomain is the name of the ScaleIO Protection Domain for the configured
            storage.
        readOnly: readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in
            VolumeMounts.
        secretRef: secretRef references to the secret for ScaleIO user and other sensitive information. If
            this is not provided, Login operation will fail.
        sslEnabled: sslEnabled is the flag to enable/disable SSL communication with Gateway, default false
        storageMode: storageMode indicates whether the storage for a volume should be ThickProvisioned or
            ThinProvisioned. Default is ThinProvisioned.
        storagePool: storagePool is the ScaleIO Storage Pool associated with the protection domain.
        system: system is the name of the storage system as configured in ScaleIO.
        volumeName: volumeName is the name of a volume already created in the ScaleIO system that is
            associated with this volume source.

    """

    gateway: str
    system: str
    secretRef: SecretReference
    fsType: Optional[str] = None
    protectionDomain: Optional[str] = None
    readOnly: Optional[bool] = None
    sslEnabled: Optional[bool] = None
    storageMode: Optional[str] = None
    storagePool: Optional[str] = None
    volumeName: Optional[str] = None


@dataclass
class SecretReference(K8sSpec):
    """SecretReference represents a Secret Reference. It has enough information to retrieve secret in any
    namespace
    Attributes:
        name: name is unique within a namespace to reference a secret resource.
        namespace: namespace defines the space within which the secret name must be unique.

    """

    name: Optional[str] = None
    namespace: Optional[str] = None


@dataclass
class StorageOSPersistentVolumeSource(K8sSpec):
    """Represents a StorageOS persistent volume resource.

    Attributes:
        fsType: fsType is the filesystem type to mount. Must be a filesystem type supported by the host
            operating system. Ex. 'ext4', 'xfs', 'ntfs'. Implicitly inferred to be 'ext4' if unspecified.
        readOnly: readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in
            VolumeMounts.
        secretRef: secretRef specifies the secret to use for obtaining the StorageOS API credentials.  If not
            specified, default values will be attempted.
        volumeName: volumeName is the human-readable name of the StorageOS volume.  Volume names are only
            unique within a namespace.
        volumeNamespace: volumeNamespace specifies the scope of the volume within StorageOS.  If no namespace
            is specified then the Pod's namespace will be used.  This allows the Kubernetes name scoping to be
            mirrored within StorageOS for tighter integration. Set VolumeName to any name to override the
            default behaviour. Set to 'default' if you are not using namespaces within StorageOS. Namespaces
            that do not pre-exist within StorageOS will be created.

    """

    fsType: Optional[str] = None
    readOnly: Optional[bool] = None
    secretRef: Optional[ObjectReference] = None
    volumeName: Optional[str] = None
    volumeNamespace: Optional[str] = None


@dataclass
class TopologySelectorLabelRequirement(K8sSpec):
    """A topology selector requirement is a selector that matches given label. This is an alpha feature and
    may change in the future.

    Attributes:
        key: The label key that the selector applies to.
        values: An array of string values. One value must match the label to be selected. Each entry in Values
            is ORed.

    """

    key: str
    values: List[str]


@dataclass
class TopologySelectorTerm(K8sSpec):
    """A topology selector term represents the result of label queries. A null or empty topology selector
    term matches no objects. The requirements of them are ANDed. It provides a subset of functionality as
    NodeSelectorTerm. This is an alpha feature and may change in the future.

    Attributes:
        matchLabelExpressions: A list of topology selector requirements by labels.

    """

    matchLabelExpressions: Optional[List[TopologySelectorLabelRequirement]] = None


@dataclass
class VolumeNodeAffinity(K8sSpec):
    """VolumeNodeAffinity defines constraints that limit what nodes this volume can be accessed from.

    Attributes:
        required: required specifies hard node constraints that must be met.

    """

    required: Optional[NodeSelector] = None


@dataclass
class VsphereVirtualDiskVolumeSource(K8sSpec):
    """Represents a vSphere volume resource.

    Attributes:
        fsType: fsType is filesystem type to mount. Must be a filesystem type supported by the host operating
            system. Ex. 'ext4', 'xfs', 'ntfs'. Implicitly inferred to be 'ext4' if unspecified.
        storagePolicyID: storagePolicyID is the storage Policy Based Management (SPBM) profile ID associated
            with the StoragePolicyName.
        storagePolicyName: storagePolicyName is the storage Policy Based Management (SPBM) profile name.
        volumePath: volumePath is the path that identifies vSphere volume vmdk

    """

    volumePath: str
    fsType: Optional[str] = None
    storagePolicyID: Optional[str] = None
    storagePolicyName: Optional[str] = None


@dataclass
class Toleration(K8sSpec):
    """The pod this Toleration is attached to tolerates any taint that matches the triple <key,value,effect>
    using the matching operator <operator>.

    Attributes:
        effect: Effect indicates the taint effect to match. Empty means match all taint effects. When
            specified, allowed values are NoSchedule, PreferNoSchedule and NoExecute.
        key: Key is the taint key that the toleration applies to. Empty means match all taint keys. If the key
            is empty, operator must be Exists; this combination means to match all values and all keys.
        operator: Operator represents a key's relationship to the value. Valid operators are Exists and Equal.
            Defaults to Equal. Exists is equivalent to wildcard for value, so that a pod can tolerate all
            taints of a particular category.
        tolerationSeconds: TolerationSeconds represents the period of time the toleration (which must be of
            effect NoExecute, otherwise this field is ignored) tolerates the taint. By default, it is not set,
            which means tolerate the taint forever (do not evict). Zero and negative values will be treated as
            0 (evict immediately) by the system.
        value: Value is the taint value the toleration matches to. If the operator is Exists, the value should
            be empty, otherwise just a regular string.

    """

    effect: Optional[str] = None
    key: Optional[str] = None
    operator: Optional[str] = None
    tolerationSeconds: Optional[int] = None
    value: Optional[str] = None


@dataclass
class Affinity(K8sSpec):
    """Affinity is a group of affinity scheduling rules.

    Attributes:
        nodeAffinity: Describes node affinity scheduling rules for the pod.
        podAffinity: Describes pod affinity scheduling rules (e.g. co-locate this pod in the same node, zone,
            etc. as some other pod(s)).
        podAntiAffinity: Describes pod anti-affinity scheduling rules (e.g. avoid putting this pod in the same
            node, zone, etc. as some other pod(s)).

    """

    nodeAffinity: Optional[NodeAffinity] = None
    podAffinity: Optional[PodAffinity] = None
    podAntiAffinity: Optional[PodAntiAffinity] = None


@dataclass
class AppArmorProfile(K8sSpec):
    """AppArmorProfile defines a pod or container's AppArmor settings.

    Attributes:
        localhostProfile: localhostProfile indicates a profile loaded on the node that should be used. The
            profile must be preconfigured on the node to work. Must match the loaded name of the profile. Must
            be set if and only if type is 'Localhost'.
        type: type indicates which kind of AppArmor profile will be applied. Valid options are:   Localhost -
            a profile pre-loaded on the node.   RuntimeDefault - the container runtime's default profile.
            Unconfined - no AppArmor enforcement.

    """

    type: str
    localhostProfile: Optional[str] = None


@dataclass
class AzureFileVolumeSource(K8sSpec):
    """AzureFile represents an Azure File Service mount on the host and bind mount to the pod.

    Attributes:
        readOnly: readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in
            VolumeMounts.
        secretName: secretName is the  name of secret that contains Azure Storage Account Name and Key
        shareName: shareName is the azure share Name

    """

    secretName: str
    shareName: str
    readOnly: Optional[bool] = None


@dataclass
class CSIVolumeSource(K8sSpec):
    """Represents a source location of a volume to mount, managed by an external CSI driver
    Attributes:
        driver: driver is the name of the CSI driver that handles this volume. Consult with your admin for the
            correct name as registered in the cluster.
        fsType: fsType to mount. Ex. 'ext4', 'xfs', 'ntfs'. If not provided, the empty value is passed to the
            associated CSI driver which will determine the default filesystem to apply.
        nodePublishSecretRef: nodePublishSecretRef is a reference to the secret object containing sensitive
            information to pass to the CSI driver to complete the CSI NodePublishVolume and
            NodeUnpublishVolume calls. This field is optional, and  may be empty if no secret is required. If
            the secret object contains more than one secret, all secret references are passed.
        readOnly: readOnly specifies a read-only configuration for the volume. Defaults to false (read/write).
        volumeAttributes: volumeAttributes stores driver-specific properties that are passed to the CSI
            driver. Consult your driver's documentation for supported values.

    """

    driver: str
    fsType: Optional[str] = None
    nodePublishSecretRef: Optional[LocalObjectReference] = None
    readOnly: Optional[bool] = None
    volumeAttributes: Optional[JSONDict] = None


@dataclass
class Capabilities(K8sSpec):
    """Adds and removes POSIX capabilities from running containers.

    Attributes:
        add: Added capabilities
        drop: Removed capabilities

    """

    add: Optional[List[str]] = None
    drop: Optional[List[str]] = None


@dataclass
class CephFSVolumeSource(K8sSpec):
    """Represents a Ceph Filesystem mount that lasts the lifetime of a pod Cephfs volumes do not support
    ownership management or SELinux relabeling.

    Attributes:
        monitors: monitors is Required: Monitors is a collection of Ceph monitors
        path: path is Optional: Used as the mounted root, rather than the full Ceph tree, default is /
        readOnly: readOnly is Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly
            setting in VolumeMounts.
        secretFile: secretFile is Optional: SecretFile is the path to key ring for User, default is
            /etc/ceph/user.secret
        secretRef: secretRef is Optional: SecretRef is reference to the authentication secret for User,
            default is empty.
        user: user is optional: User is the rados user name, default is admin

    """

    monitors: List[str]
    path: Optional[str] = None
    readOnly: Optional[bool] = None
    secretFile: Optional[str] = None
    secretRef: Optional[LocalObjectReference] = None
    user: Optional[str] = None


@dataclass
class CinderVolumeSource(K8sSpec):
    """Represents a cinder volume resource in Openstack. A Cinder volume must exist before mounting to a
    container. The volume must also be in the same region as the kubelet. Cinder volumes support ownership
    management and SELinux relabeling.

    Attributes:
        fsType: fsType is the filesystem type to mount. Must be a filesystem type supported by the host
            operating system. Examples: 'ext4', 'xfs', 'ntfs'. Implicitly inferred to be 'ext4' if
            unspecified.
        readOnly: readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in
            VolumeMounts.
        secretRef: secretRef is optional: points to a secret object containing parameters used to connect to
            OpenStack.
        volumeID: volumeID used to identify the volume in cinder.

    """

    volumeID: str
    fsType: Optional[str] = None
    readOnly: Optional[bool] = None
    secretRef: Optional[LocalObjectReference] = None


@dataclass
class ClusterTrustBundleProjection(K8sSpec):
    """ClusterTrustBundleProjection describes how to select a set of ClusterTrustBundle objects and project
    their contents into the pod filesystem.

    Attributes:
        labelSelector: Select all ClusterTrustBundles that match this label selector.  Only has effect if
            signerName is set.  Mutually-exclusive with name.  If unset, interpreted as 'match nothing'.  If
            set but empty, interpreted as 'match everything'.
        name: Select a single ClusterTrustBundle by object name.  Mutually-exclusive with signerName and
            labelSelector.
        optional: If true, don't block pod startup if the referenced ClusterTrustBundle(s) aren't available.
            If using name, then the named ClusterTrustBundle is allowed not to exist.  If using signerName,
            then the combination of signerName and labelSelector is allowed to match zero ClusterTrustBundles.
        path: Relative path from the volume root to write the bundle.
        signerName: Select all ClusterTrustBundles that match this signer name. Mutually-exclusive with name.
            The contents of all selected ClusterTrustBundles will be unified and deduplicated.

    """

    path: str
    labelSelector: Optional[gybe.k8s.v1_31.meta.v1.LabelSelector] = None
    name: Optional[str] = None
    optional: Optional[bool] = None
    signerName: Optional[str] = None


@dataclass
class ConfigMapEnvSource(K8sSpec):
    """ConfigMapEnvSource selects a ConfigMap to populate the environment variables with.  The contents of
    the target ConfigMap's Data field will represent the key-value pairs as environment variables.

    Attributes:
        name: Name of the referent. This field is effectively required, but due to backwards compatibility is
            allowed to be empty. Instances of this type with an empty value here are almost certainly wrong.
        optional: Specify whether the ConfigMap must be defined

    """

    name: Optional[str] = None
    optional: Optional[bool] = None


@dataclass
class ConfigMapKeySelector(K8sSpec):
    """Selects a key from a ConfigMap.

    Attributes:
        key: The key to select.
        name: Name of the referent. This field is effectively required, but due to backwards compatibility is
            allowed to be empty. Instances of this type with an empty value here are almost certainly wrong.
        optional: Specify whether the ConfigMap or its key must be defined

    """

    key: str
    name: Optional[str] = None
    optional: Optional[bool] = None


@dataclass
class ConfigMapProjection(K8sSpec):
    """Adapts a ConfigMap into a projected volume.  The contents of the target ConfigMap's Data field will be
    presented in a projected volume as files using the keys in the Data field as the file names, unless
    the items element is populated with specific mappings of keys to paths. Note that this is identical to
    a configmap volume source without the default mode.

    Attributes:
        items: items if unspecified, each key-value pair in the Data field of the referenced ConfigMap will be
            projected into the volume as a file whose name is the key and content is the value. If specified,
            the listed keys will be projected into the specified paths, and unlisted keys will not be present.
            If a key is specified which is not present in the ConfigMap, the volume setup will error unless it
            is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.
        name: Name of the referent. This field is effectively required, but due to backwards compatibility is
            allowed to be empty. Instances of this type with an empty value here are almost certainly wrong.
        optional: optional specify whether the ConfigMap or its keys must be defined

    """

    items: Optional[List[KeyToPath]] = None
    name: Optional[str] = None
    optional: Optional[bool] = None


@dataclass
class ConfigMapVolumeSource(K8sSpec):
    """Adapts a ConfigMap into a volume.  The contents of the target ConfigMap's Data field will be presented
    in a volume as files using the keys in the Data field as the file names, unless the items element is
    populated with specific mappings of keys to paths. ConfigMap volumes support ownership management and
    SELinux relabeling.

    Attributes:
        defaultMode: defaultMode is optional: mode bits used to set permissions on created files by default.
            Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts
            both octal and decimal values, JSON requires decimal values for mode bits. Defaults to 0644.
            Directories within the path are not affected by this setting. This might be in conflict with other
            options that affect the file mode, like fsGroup, and the result can be other mode bits set.
        items: items if unspecified, each key-value pair in the Data field of the referenced ConfigMap will be
            projected into the volume as a file whose name is the key and content is the value. If specified,
            the listed keys will be projected into the specified paths, and unlisted keys will not be present.
            If a key is specified which is not present in the ConfigMap, the volume setup will error unless it
            is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.
        name: Name of the referent. This field is effectively required, but due to backwards compatibility is
            allowed to be empty. Instances of this type with an empty value here are almost certainly wrong.
        optional: optional specify whether the ConfigMap or its keys must be defined

    """

    defaultMode: Optional[int] = None
    items: Optional[List[KeyToPath]] = None
    name: Optional[str] = None
    optional: Optional[bool] = None


@dataclass
class Container(K8sSpec):
    """A single application container that you want to run within a pod.

    Attributes:
        args: Arguments to the entrypoint. The container image's CMD is used if this is not provided. Variable
            references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be
            resolved, the reference in the input string will be unchanged. Double $$ are reduced to a single
            $, which allows for escaping the $(VAR_NAME) syntax: i.e. '$$(VAR_NAME)' will produce the string
            literal '$(VAR_NAME)'. Escaped references will never be expanded, regardless of whether the
            variable exists or not. Cannot be updated.
        command: Entrypoint array. Not executed within a shell. The container image's ENTRYPOINT is used if
            this is not provided. Variable references $(VAR_NAME) are expanded using the container's
            environment. If a variable cannot be resolved, the reference in the input string will be
            unchanged. Double $$ are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax:
            i.e. '$$(VAR_NAME)' will produce the string literal '$(VAR_NAME)'. Escaped references will never
            be expanded, regardless of whether the variable exists or not. Cannot be updated.
        env: List of environment variables to set in the container. Cannot be updated.
        envFrom: List of sources to populate environment variables in the container. The keys defined within a
            source must be a C_IDENTIFIER. All invalid keys will be reported as an event when the container is
            starting. When a key exists in multiple sources, the value associated with the last source will
            take precedence. Values defined by an Env with a duplicate key will take precedence. Cannot be
            updated.
        image: Container image name.
        imagePullPolicy: Image pull policy. One of Always, Never, IfNotPresent. Defaults to Always if :latest
            tag is specified, or IfNotPresent otherwise. Cannot be updated.
        lifecycle: Actions that the management system should take in response to container lifecycle events.
            Cannot be updated.
        livenessProbe: Periodic probe of container liveness. Container will be restarted if the probe fails.
            Cannot be updated.
        name: Name of the container specified as a DNS_LABEL. Each container in a pod must have a unique name
            (DNS_LABEL). Cannot be updated.
        ports: List of ports to expose from the container. Not specifying a port here DOES NOT prevent that
            port from being exposed. Any port which is listening on the default '0.0.0.0' address inside a
            container will be accessible from the network. Modifying this array with strategic merge patch may
            corrupt the data. For more information See https://github.com/kubernetes/kubernetes/issues/108255.
            Cannot be updated.
        readinessProbe: Periodic probe of container service readiness. Container will be removed from service
            endpoints if the probe fails. Cannot be updated.
        resizePolicy: Resources resize policy for the container.
        resources: Compute Resources required by this container. Cannot be updated.
        restartPolicy: RestartPolicy defines the restart behavior of individual containers in a pod. This
            field may only be set for init containers, and the only allowed value is 'Always'. For non-init
            containers or when this field is not specified, the restart behavior is defined by the Pod's
            restart policy and the container type. Setting the RestartPolicy as 'Always' for the init
            container will have the following effect: this init container will be continually restarted on
            exit until all regular containers have terminated. Once all regular containers have completed, all
            init containers with restartPolicy 'Always' will be shut down. This lifecycle differs from normal
            init containers and is often referred to as a 'sidecar' container. Although this init container
            still starts in the init container sequence, it does not wait for the container to complete before
            proceeding to the next init container. Instead, the next init container starts immediately after
            this init container is started, or after any startupProbe has successfully completed.
        securityContext: SecurityContext defines the security options the container should be run with. If
            set, the fields of SecurityContext override the equivalent fields of PodSecurityContext.
        startupProbe: StartupProbe indicates that the Pod has successfully initialized. If specified, no other
            probes are executed until this completes successfully. If this probe fails, the Pod will be
            restarted, just as if the livenessProbe failed. This can be used to provide different probe
            parameters at the beginning of a Pod's lifecycle, when it might take a long time to load data or
            warm a cache, than during steady-state operation. This cannot be updated.
        stdin: Whether this container should allocate a buffer for stdin in the container runtime. If this is
            not set, reads from stdin in the container will always result in EOF. Default is false.
        stdinOnce: Whether the container runtime should close the stdin channel after it has been opened by a
            single attach. When stdin is true the stdin stream will remain open across multiple attach
            sessions. If stdinOnce is set to true, stdin is opened on container start, is empty until the
            first client attaches to stdin, and then remains open and accepts data until the client
            disconnects, at which time stdin is closed and remains closed until the container is restarted. If
            this flag is false, a container processes that reads from stdin will never receive an EOF. Default
            is false
        terminationMessagePath: Optional: Path at which the file to which the container's termination message
            will be written is mounted into the container's filesystem. Message written is intended to be
            brief final status, such as an assertion failure message. Will be truncated by the node if greater
            than 4096 bytes. The total message length across all containers will be limited to 12kb. Defaults
            to /dev/termination-log. Cannot be updated.
        terminationMessagePolicy: Indicate how the termination message should be populated. File will use the
            contents of terminationMessagePath to populate the container status message on both success and
            failure. FallbackToLogsOnError will use the last chunk of container log output if the termination
            message file is empty and the container exited with an error. The log output is limited to 2048
            bytes or 80 lines, whichever is smaller. Defaults to File. Cannot be updated.
        tty: Whether this container should allocate a TTY for itself, also requires 'stdin' to be true.
            Default is false.
        volumeDevices: volumeDevices is the list of block devices to be used by the container.
        volumeMounts: Pod volumes to mount into the container's filesystem. Cannot be updated.
        workingDir: Container's working directory. If not specified, the container runtime's default will be
            used, which might be configured in the container image. Cannot be updated.

    """

    name: str
    args: Optional[List[str]] = None
    command: Optional[List[str]] = None
    env: Optional[List[EnvVar]] = None
    envFrom: Optional[List[EnvFromSource]] = None
    image: Optional[str] = None
    imagePullPolicy: Optional[str] = None
    lifecycle: Optional[Lifecycle] = None
    livenessProbe: Optional[Probe] = None
    ports: Optional[List[ContainerPort]] = None
    readinessProbe: Optional[Probe] = None
    resizePolicy: Optional[List[ContainerResizePolicy]] = None
    resources: Optional[ResourceRequirements] = None
    restartPolicy: Optional[str] = None
    securityContext: Optional[SecurityContext] = None
    startupProbe: Optional[Probe] = None
    stdin: Optional[bool] = None
    stdinOnce: Optional[bool] = None
    terminationMessagePath: Optional[str] = None
    terminationMessagePolicy: Optional[str] = None
    tty: Optional[bool] = None
    volumeDevices: Optional[List[VolumeDevice]] = None
    volumeMounts: Optional[List[VolumeMount]] = None
    workingDir: Optional[str] = None


@dataclass
class ContainerPort(K8sSpec):
    """ContainerPort represents a network port in a single container.

    Attributes:
        containerPort: Number of port to expose on the pod's IP address. This must be a valid port number, 0 <
            x < 65536.
        hostIP: What host IP to bind the external port to.
        hostPort: Number of port to expose on the host. If specified, this must be a valid port number, 0 < x
            < 65536. If HostNetwork is specified, this must match ContainerPort. Most containers do not need
            this.
        name: If specified, this must be an IANA_SVC_NAME and unique within the pod. Each named port in a pod
            must have a unique name. Name for the port that can be referred to by services.
        protocol: Protocol for port. Must be UDP, TCP, or SCTP. Defaults to 'TCP'.

    """

    containerPort: int
    hostIP: Optional[str] = None
    hostPort: Optional[int] = None
    name: Optional[str] = None
    protocol: Optional[str] = None


@dataclass
class ContainerResizePolicy(K8sSpec):
    """ContainerResizePolicy represents resource resize policy for the container.

    Attributes:
        resourceName: Name of the resource to which this resource resize policy applies. Supported values:
            cpu, memory.
        restartPolicy: Restart policy to apply when specified resource is resized. If not specified, it
            defaults to NotRequired.

    """

    resourceName: str
    restartPolicy: str


@dataclass
class DownwardAPIProjection(K8sSpec):
    """Represents downward API info for projecting into a projected volume. Note that this is identical to a
    downwardAPI volume source without the default mode.

    Attributes:
        items: Items is a list of DownwardAPIVolume file

    """

    items: Optional[List[DownwardAPIVolumeFile]] = None


@dataclass
class DownwardAPIVolumeFile(K8sSpec):
    """DownwardAPIVolumeFile represents information to create the file containing the pod field
    Attributes:
        fieldRef: Required: Selects a field of the pod: only annotations, labels, name, namespace and uid are
            supported.
        mode: Optional: mode bits used to set permissions on this file, must be an octal value between 0000
            and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON
            requires decimal values for mode bits. If not specified, the volume defaultMode will be used. This
            might be in conflict with other options that affect the file mode, like fsGroup, and the result
            can be other mode bits set.
        path: Required: Path is  the relative path name of the file to be created. Must not be absolute or
            contain the '..' path. Must be utf-8 encoded. The first item of the relative path must not start
            with '..'
        resourceFieldRef: Selects a resource of the container: only resources limits and requests (limits.cpu,
            limits.memory, requests.cpu and requests.memory) are currently supported.

    """

    path: str
    fieldRef: Optional[ObjectFieldSelector] = None
    mode: Optional[int] = None
    resourceFieldRef: Optional[ResourceFieldSelector] = None


@dataclass
class DownwardAPIVolumeSource(K8sSpec):
    """DownwardAPIVolumeSource represents a volume containing downward API info. Downward API volumes support
    ownership management and SELinux relabeling.

    Attributes:
        defaultMode: Optional: mode bits to use on created files by default. Must be a Optional: mode bits
            used to set permissions on created files by default. Must be an octal value between 0000 and 0777
            or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires
            decimal values for mode bits. Defaults to 0644. Directories within the path are not affected by
            this setting. This might be in conflict with other options that affect the file mode, like
            fsGroup, and the result can be other mode bits set.
        items: Items is a list of downward API volume file

    """

    defaultMode: Optional[int] = None
    items: Optional[List[DownwardAPIVolumeFile]] = None


@dataclass
class EmptyDirVolumeSource(K8sSpec):
    """Represents an empty directory for a pod. Empty directory volumes support ownership management and
    SELinux relabeling.

    Attributes:
        medium: medium represents what type of storage medium should back this directory. The default is ''
            which means to use the node's default medium. Must be an empty string (default) or Memory.
        sizeLimit: sizeLimit is the total amount of local storage required for this EmptyDir volume. The size
            limit is also applicable for memory medium. The maximum usage on memory medium EmptyDir would be
            the minimum value between the SizeLimit specified here and the sum of memory limits of all
            containers in a pod. The default is nil which means that the limit is undefined.

    """

    medium: Optional[str] = None
    sizeLimit: Optional[gybe.k8s.v1_31.api.resource.Quantity] = None


@dataclass
class EnvFromSource(K8sSpec):
    """EnvFromSource represents the source of a set of ConfigMaps
    Attributes:
        configMapRef: The ConfigMap to select from
        prefix: An optional identifier to prepend to each key in the ConfigMap. Must be a C_IDENTIFIER.
        secretRef: The Secret to select from

    """

    configMapRef: Optional[ConfigMapEnvSource] = None
    prefix: Optional[str] = None
    secretRef: Optional[SecretEnvSource] = None


@dataclass
class EnvVar(K8sSpec):
    """EnvVar represents an environment variable present in a Container.

    Attributes:
        name: Name of the environment variable. Must be a C_IDENTIFIER.
        value: Variable references $(VAR_NAME) are expanded using the previously defined environment variables
            in the container and any service environment variables. If a variable cannot be resolved, the
            reference in the input string will be unchanged. Double $$ are reduced to a single $, which allows
            for escaping the $(VAR_NAME) syntax: i.e. '$$(VAR_NAME)' will produce the string literal
            '$(VAR_NAME)'. Escaped references will never be expanded, regardless of whether the variable
            exists or not. Defaults to ''.
        valueFrom: Source for the environment variable's value. Cannot be used if value is not empty.

    """

    name: str
    value: Optional[str] = None
    valueFrom: Optional[EnvVarSource] = None


@dataclass
class EnvVarSource(K8sSpec):
    """EnvVarSource represents a source for the value of an EnvVar.

    Attributes:
        configMapKeyRef: Selects a key of a ConfigMap.
        fieldRef: Selects a field of the pod: supports metadata.name, metadata.namespace,
            `metadata.labels['<KEY>']`, `metadata.annotations['<KEY>']`, spec.nodeName,
            spec.serviceAccountName, status.hostIP, status.podIP, status.podIPs.
        resourceFieldRef: Selects a resource of the container: only resources limits and requests (limits.cpu,
            limits.memory, limits.ephemeral-storage, requests.cpu, requests.memory and requests.ephemeral-
            storage) are currently supported.
        secretKeyRef: Selects a key of a secret in the pod's namespace

    """

    configMapKeyRef: Optional[ConfigMapKeySelector] = None
    fieldRef: Optional[ObjectFieldSelector] = None
    resourceFieldRef: Optional[ResourceFieldSelector] = None
    secretKeyRef: Optional[SecretKeySelector] = None


@dataclass
class EphemeralContainer(K8sSpec):
    """An EphemeralContainer is a temporary container that you may add to an existing Pod for user-initiated
    activities such as debugging. Ephemeral containers have no resource or scheduling guarantees, and they
    will not be restarted when they exit or when a Pod is removed or restarted. The kubelet may evict a
    Pod if an ephemeral container causes the Pod to exceed its resource allocation.  To add an ephemeral
    container, use the ephemeralcontainers subresource of an existing Pod. Ephemeral containers may not be
    removed or restarted.

    Attributes:
        args: Arguments to the entrypoint. The image's CMD is used if this is not provided. Variable
            references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be
            resolved, the reference in the input string will be unchanged. Double $$ are reduced to a single
            $, which allows for escaping the $(VAR_NAME) syntax: i.e. '$$(VAR_NAME)' will produce the string
            literal '$(VAR_NAME)'. Escaped references will never be expanded, regardless of whether the
            variable exists or not. Cannot be updated.
        command: Entrypoint array. Not executed within a shell. The image's ENTRYPOINT is used if this is not
            provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a
            variable cannot be resolved, the reference in the input string will be unchanged. Double $$ are
            reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. '$$(VAR_NAME)' will
            produce the string literal '$(VAR_NAME)'. Escaped references will never be expanded, regardless of
            whether the variable exists or not. Cannot be updated.
        env: List of environment variables to set in the container. Cannot be updated.
        envFrom: List of sources to populate environment variables in the container. The keys defined within a
            source must be a C_IDENTIFIER. All invalid keys will be reported as an event when the container is
            starting. When a key exists in multiple sources, the value associated with the last source will
            take precedence. Values defined by an Env with a duplicate key will take precedence. Cannot be
            updated.
        image: Container image name.
        imagePullPolicy: Image pull policy. One of Always, Never, IfNotPresent. Defaults to Always if :latest
            tag is specified, or IfNotPresent otherwise. Cannot be updated.
        lifecycle: Lifecycle is not allowed for ephemeral containers.
        livenessProbe: Probes are not allowed for ephemeral containers.
        name: Name of the ephemeral container specified as a DNS_LABEL. This name must be unique among all
            containers, init containers and ephemeral containers.
        ports: Ports are not allowed for ephemeral containers.
        readinessProbe: Probes are not allowed for ephemeral containers.
        resizePolicy: Resources resize policy for the container.
        resources: Resources are not allowed for ephemeral containers. Ephemeral containers use spare
            resources already allocated to the pod.
        restartPolicy: Restart policy for the container to manage the restart behavior of each container
            within a pod. This may only be set for init containers. You cannot set this field on ephemeral
            containers.
        securityContext: Optional: SecurityContext defines the security options the ephemeral container should
            be run with. If set, the fields of SecurityContext override the equivalent fields of
            PodSecurityContext.
        startupProbe: Probes are not allowed for ephemeral containers.
        stdin: Whether this container should allocate a buffer for stdin in the container runtime. If this is
            not set, reads from stdin in the container will always result in EOF. Default is false.
        stdinOnce: Whether the container runtime should close the stdin channel after it has been opened by a
            single attach. When stdin is true the stdin stream will remain open across multiple attach
            sessions. If stdinOnce is set to true, stdin is opened on container start, is empty until the
            first client attaches to stdin, and then remains open and accepts data until the client
            disconnects, at which time stdin is closed and remains closed until the container is restarted. If
            this flag is false, a container processes that reads from stdin will never receive an EOF. Default
            is false
        targetContainerName: If set, the name of the container from PodSpec that this ephemeral container
            targets. The ephemeral container will be run in the namespaces (IPC, PID, etc) of this container.
            If not set then the ephemeral container uses the namespaces configured in the Pod spec.  The
            container runtime must implement support for this feature. If the runtime does not support
            namespace targeting then the result of setting this field is undefined.
        terminationMessagePath: Optional: Path at which the file to which the container's termination message
            will be written is mounted into the container's filesystem. Message written is intended to be
            brief final status, such as an assertion failure message. Will be truncated by the node if greater
            than 4096 bytes. The total message length across all containers will be limited to 12kb. Defaults
            to /dev/termination-log. Cannot be updated.
        terminationMessagePolicy: Indicate how the termination message should be populated. File will use the
            contents of terminationMessagePath to populate the container status message on both success and
            failure. FallbackToLogsOnError will use the last chunk of container log output if the termination
            message file is empty and the container exited with an error. The log output is limited to 2048
            bytes or 80 lines, whichever is smaller. Defaults to File. Cannot be updated.
        tty: Whether this container should allocate a TTY for itself, also requires 'stdin' to be true.
            Default is false.
        volumeDevices: volumeDevices is the list of block devices to be used by the container.
        volumeMounts: Pod volumes to mount into the container's filesystem. Subpath mounts are not allowed for
            ephemeral containers. Cannot be updated.
        workingDir: Container's working directory. If not specified, the container runtime's default will be
            used, which might be configured in the container image. Cannot be updated.

    """

    name: str
    args: Optional[List[str]] = None
    command: Optional[List[str]] = None
    env: Optional[List[EnvVar]] = None
    envFrom: Optional[List[EnvFromSource]] = None
    image: Optional[str] = None
    imagePullPolicy: Optional[str] = None
    lifecycle: Optional[Lifecycle] = None
    livenessProbe: Optional[Probe] = None
    ports: Optional[List[ContainerPort]] = None
    readinessProbe: Optional[Probe] = None
    resizePolicy: Optional[List[ContainerResizePolicy]] = None
    resources: Optional[ResourceRequirements] = None
    restartPolicy: Optional[str] = None
    securityContext: Optional[SecurityContext] = None
    startupProbe: Optional[Probe] = None
    stdin: Optional[bool] = None
    stdinOnce: Optional[bool] = None
    targetContainerName: Optional[str] = None
    terminationMessagePath: Optional[str] = None
    terminationMessagePolicy: Optional[str] = None
    tty: Optional[bool] = None
    volumeDevices: Optional[List[VolumeDevice]] = None
    volumeMounts: Optional[List[VolumeMount]] = None
    workingDir: Optional[str] = None


@dataclass
class EphemeralVolumeSource(K8sSpec):
    """Represents an ephemeral volume that is handled by a normal storage driver.

    Attributes:
        volumeClaimTemplate: Will be used to create a stand-alone PVC to provision the volume. The pod in
            which this EphemeralVolumeSource is embedded will be the owner of the PVC, i.e. the PVC will be
            deleted together with the pod.  The name of the PVC will be `<pod name>-<volume name>` where
            `<volume name>` is the name from the `PodSpec.Volumes` array entry. Pod validation will reject the
            pod if the concatenated name is not valid for a PVC (for example, too long).  An existing PVC with
            that name that is not owned by the pod will *not* be used for the pod to avoid using an unrelated
            volume by mistake. Starting the pod is then blocked until the unrelated PVC is removed. If such a
            pre-created PVC is meant to be used by the pod, the PVC has to updated with an owner reference to
            the pod once the pod exists. Normally this should not be necessary, but it may be useful when
            manually reconstructing a broken cluster.  This field is read-only and no changes will be made by
            Kubernetes to the PVC after it has been created.  Required, must not be nil.

    """

    volumeClaimTemplate: Optional[PersistentVolumeClaimTemplate] = None


@dataclass
class ExecAction(K8sSpec):
    """ExecAction describes a 'run in container' action.

    Attributes:
        command: Command is the command line to execute inside the container, the working directory for the
            command  is root ('/') in the container's filesystem. The command is simply exec'd, it is not run
            inside a shell, so traditional shell instructions ('|', etc) won't work. To use a shell, you need
            to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is
            unhealthy.

    """

    command: Optional[List[str]] = None


@dataclass
class FlexVolumeSource(K8sSpec):
    """FlexVolume represents a generic volume resource that is provisioned/attached using an exec based
    plugin.

    Attributes:
        driver: driver is the name of the driver to use for this volume.
        fsType: fsType is the filesystem type to mount. Must be a filesystem type supported by the host
            operating system. Ex. 'ext4', 'xfs', 'ntfs'. The default filesystem depends on FlexVolume script.
        options: options is Optional: this field holds extra command options if any.
        readOnly: readOnly is Optional: defaults to false (read/write). ReadOnly here will force the ReadOnly
            setting in VolumeMounts.
        secretRef: secretRef is Optional: secretRef is reference to the secret object containing sensitive
            information to pass to the plugin scripts. This may be empty if no secret object is specified. If
            the secret object contains more than one secret, all secrets are passed to the plugin scripts.

    """

    driver: str
    fsType: Optional[str] = None
    options: Optional[JSONDict] = None
    readOnly: Optional[bool] = None
    secretRef: Optional[LocalObjectReference] = None


@dataclass
class GRPCAction(K8sSpec):
    """Schema model io.k8s.api.core.v1.GRPCAction.

    Attributes:
        port: Port number of the gRPC service. Number must be in the range 1 to 65535.
        service: Service is the name of the service to place in the gRPC HealthCheckRequest (see
            https://github.com/grpc/grpc/blob/master/doc/health-checking.md).  If this is not specified, the
            default behavior is defined by gRPC.

    """

    port: int
    service: Optional[str] = None


@dataclass
class GitRepoVolumeSource(K8sSpec):
    """Represents a volume that is populated with the contents of a git repository. Git repo volumes do not
    support ownership management. Git repo volumes support SELinux relabeling.  DEPRECATED: GitRepo is
    deprecated. To provision a container with a git repo, mount an EmptyDir into an InitContainer that
    clones the repo using git, then mount the EmptyDir into the Pod's container.

    Attributes:
        directory: directory is the target directory name. Must not contain or start with '..'.  If '.' is
            supplied, the volume directory will be the git repository.  Otherwise, if specified, the volume
            will contain the git repository in the subdirectory with the given name.
        repository: repository is the URL
        revision: revision is the commit hash for the specified revision.

    """

    repository: str
    directory: Optional[str] = None
    revision: Optional[str] = None


@dataclass
class GlusterfsVolumeSource(K8sSpec):
    """Represents a Glusterfs mount that lasts the lifetime of a pod. Glusterfs volumes do not support
    ownership management or SELinux relabeling.

    Attributes:
        endpoints: endpoints is the endpoint name that details Glusterfs topology.
        path: path is the Glusterfs volume path.
        readOnly: readOnly here will force the Glusterfs volume to be mounted with read-only permissions.
            Defaults to false.

    """

    endpoints: str
    path: str
    readOnly: Optional[bool] = None


@dataclass
class HTTPGetAction(K8sSpec):
    """HTTPGetAction describes an action based on HTTP Get requests.

    Attributes:
        host: Host name to connect to, defaults to the pod IP. You probably want to set 'Host' in httpHeaders
            instead.
        httpHeaders: Custom headers to set in the request. HTTP allows repeated headers.
        path: Path to access on the HTTP server.
        port: Name or number of the port to access on the container. Number must be in the range 1 to 65535.
            Name must be an IANA_SVC_NAME.
        scheme: Scheme to use for connecting to the host. Defaults to HTTP.

    """

    port: str
    host: Optional[str] = None
    httpHeaders: Optional[List[HTTPHeader]] = None
    path: Optional[str] = None
    scheme: Optional[str] = None


@dataclass
class HTTPHeader(K8sSpec):
    """HTTPHeader describes a custom header to be used in HTTP probes
    Attributes:
        name: The header field name. This will be canonicalized upon output, so case-variant names will be
            understood as the same header.
        value: The header field value

    """

    name: str
    value: str


@dataclass
class HostAlias(K8sSpec):
    """HostAlias holds the mapping between IP and hostnames that will be injected as an entry in the pod's
    hosts file.

    Attributes:
        hostnames: Hostnames for the above IP address.
        ip: IP address of the host file entry.

    """

    ip: str
    hostnames: Optional[List[str]] = None


@dataclass
class ISCSIVolumeSource(K8sSpec):
    """Represents an ISCSI disk. ISCSI volumes can only be mounted as read/write once. ISCSI volumes support
    ownership management and SELinux relabeling.

    Attributes:
        chapAuthDiscovery: chapAuthDiscovery defines whether support iSCSI Discovery CHAP authentication
        chapAuthSession: chapAuthSession defines whether support iSCSI Session CHAP authentication
        fsType: fsType is the filesystem type of the volume that you want to mount. Tip: Ensure that the
            filesystem type is supported by the host operating system. Examples: 'ext4', 'xfs', 'ntfs'.
            Implicitly inferred to be 'ext4' if unspecified.
        initiatorName: initiatorName is the custom iSCSI Initiator Name. If initiatorName is specified with
            iscsiInterface simultaneously, new iSCSI interface <target portal>:<volume name> will be created
            for the connection.
        iqn: iqn is the target iSCSI Qualified Name.
        iscsiInterface: iscsiInterface is the interface Name that uses an iSCSI transport. Defaults to
            'default' (tcp).
        lun: lun represents iSCSI Target Lun number.
        portals: portals is the iSCSI Target Portal List. The portal is either an IP or ip_addr:port if the
            port is other than default (typically TCP ports 860 and 3260).
        readOnly: readOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false.
        secretRef: secretRef is the CHAP Secret for iSCSI target and initiator authentication
        targetPortal: targetPortal is iSCSI Target Portal. The Portal is either an IP or ip_addr:port if the
            port is other than default (typically TCP ports 860 and 3260).

    """

    targetPortal: str
    iqn: str
    lun: int
    chapAuthDiscovery: Optional[bool] = None
    chapAuthSession: Optional[bool] = None
    fsType: Optional[str] = None
    initiatorName: Optional[str] = None
    iscsiInterface: Optional[str] = None
    portals: Optional[List[str]] = None
    readOnly: Optional[bool] = None
    secretRef: Optional[LocalObjectReference] = None


@dataclass
class ImageVolumeSource(K8sSpec):
    """ImageVolumeSource represents a image volume resource.

    Attributes:
        pullPolicy: Policy for pulling OCI objects. Possible values are: Always: the kubelet always attempts
            to pull the reference. Container creation will fail If the pull fails. Never: the kubelet never
            pulls the reference and only uses a local image or artifact. Container creation will fail if the
            reference isn't present. IfNotPresent: the kubelet pulls if the reference isn't already present on
            disk. Container creation will fail if the reference isn't present and the pull fails. Defaults to
            Always if :latest tag is specified, or IfNotPresent otherwise.
        reference: Required: Image or artifact reference to be used. Behaves in the same way as
            pod.spec.containers[*].image. Pull secrets will be assembled in the same way as for the container
            image by looking up node credentials, SA image pull secrets, and pod spec image pull secrets.

    """

    pullPolicy: Optional[str] = None
    reference: Optional[str] = None


@dataclass
class KeyToPath(K8sSpec):
    """Maps a string key to a path within a volume.

    Attributes:
        key: key is the key to project.
        mode: mode is Optional: mode bits used to set permissions on this file. Must be an octal value between
            0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values,
            JSON requires decimal values for mode bits. If not specified, the volume defaultMode will be used.
            This might be in conflict with other options that affect the file mode, like fsGroup, and the
            result can be other mode bits set.
        path: path is the relative path of the file to map the key to. May not be an absolute path. May not
            contain the path element '..'. May not start with the string '..'.

    """

    key: str
    path: str
    mode: Optional[int] = None


@dataclass
class Lifecycle(K8sSpec):
    """Lifecycle describes actions that the management system should take in response to container lifecycle
    events. For the PostStart and PreStop lifecycle handlers, management of the container blocks until the
    action is complete, unless the container process fails, in which case the handler is aborted.

    Attributes:
        postStart: PostStart is called immediately after a container is created. If the handler fails, the
            container is terminated and restarted according to its restart policy. Other management of the
            container blocks until the hook completes.
        preStop: PreStop is called immediately before a container is terminated due to an API request or
            management event such as liveness/startup probe failure, preemption, resource contention, etc. The
            handler is not called if the container crashes or exits. The Pod's termination grace period
            countdown begins before the PreStop hook is executed. Regardless of the outcome of the handler,
            the container will eventually terminate within the Pod's termination grace period (unless delayed
            by finalizers). Other management of the container blocks until the hook completes or until the
            termination grace period is reached.

    """

    postStart: Optional[LifecycleHandler] = None
    preStop: Optional[LifecycleHandler] = None


@dataclass
class LifecycleHandler(K8sSpec):
    """LifecycleHandler defines a specific action that should be taken in a lifecycle hook. One and only one
    of the fields, except TCPSocket must be specified.

    Attributes:
        exec: Exec specifies the action to take.
        httpGet: HTTPGet specifies the http request to perform.
        sleep: Sleep represents the duration that the container should sleep before being terminated.
        tcpSocket: Deprecated. TCPSocket is NOT supported as a LifecycleHandler and kept for the backward
            compatibility. There are no validation of this field and lifecycle hooks will fail in runtime when
            tcp handler is specified.

    """

    exec: Optional[ExecAction] = None
    httpGet: Optional[HTTPGetAction] = None
    sleep: Optional[SleepAction] = None
    tcpSocket: Optional[TCPSocketAction] = None


@dataclass
class LocalObjectReference(K8sSpec):
    """LocalObjectReference contains enough information to let you locate the referenced object inside the
    same namespace.

    Attributes:
        name: Name of the referent. This field is effectively required, but due to backwards compatibility is
            allowed to be empty. Instances of this type with an empty value here are almost certainly wrong.

    """

    name: Optional[str] = None


@dataclass
class ModifyVolumeStatus(K8sSpec):
    """ModifyVolumeStatus represents the status object of ControllerModifyVolume operation
    Attributes:
        status: status is the status of the ControllerModifyVolume operation. It can be in any of following
            states:  - Pending    Pending indicates that the PersistentVolumeClaim cannot be modified due to
            unmet requirements, such as    the specified VolumeAttributesClass not existing.  - InProgress
            InProgress indicates that the volume is being modified.  - Infeasible   Infeasible indicates that
            the request has been rejected as invalid by the CSI driver. To           resolve the error, a
            valid VolumeAttributesClass needs to be specified. Note: New statuses can be added in the future.
            Consumers should check for unknown statuses and fail appropriately.
        targetVolumeAttributesClassName: targetVolumeAttributesClassName is the name of the
            VolumeAttributesClass the PVC currently being reconciled

    """

    status: str
    targetVolumeAttributesClassName: Optional[str] = None


@dataclass
class NodeAffinity(K8sSpec):
    """Node affinity is a group of node affinity scheduling rules.

    Attributes:
        preferredDuringSchedulingIgnoredDuringExecution: The scheduler will prefer to schedule pods to nodes
            that satisfy the affinity expressions specified by this field, but it may choose a node that
            violates one or more of the expressions. The node that is most preferred is the one with the
            greatest sum of weights, i.e. for each node that meets all of the scheduling requirements
            (resource request, requiredDuringScheduling affinity expressions, etc.), compute a sum by
            iterating through the elements of this field and adding 'weight' to the sum if the node matches
            the corresponding matchExpressions; the node(s) with the highest sum are the most preferred.
        requiredDuringSchedulingIgnoredDuringExecution: If the affinity requirements specified by this field
            are not met at scheduling time, the pod will not be scheduled onto the node. If the affinity
            requirements specified by this field cease to be met at some point during pod execution (e.g. due
            to an update), the system may or may not try to eventually evict the pod from its node.

    """

    preferredDuringSchedulingIgnoredDuringExecution: Optional[List[PreferredSchedulingTerm]] = None
    requiredDuringSchedulingIgnoredDuringExecution: Optional[NodeSelector] = None


@dataclass
class ObjectFieldSelector(K8sSpec):
    """ObjectFieldSelector selects an APIVersioned field of an object.

    Attributes:
        apiVersion: Version of the schema the FieldPath is written in terms of, defaults to 'v1'.
        fieldPath: Path of the field to select in the specified API version.

    """

    fieldPath: str
    apiVersion: Optional[str] = None


@dataclass
class PersistentVolumeClaim(K8sResource):
    """PersistentVolumeClaim is a user's request for and claim to a persistent volume
    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object's metadata.
        spec: spec defines the desired characteristics of a volume requested by a pod author.
        status: status represents the current information/status of a persistent volume claim. Read-only.

    """

    apiVersion: Literal['v1'] = 'v1'
    kind: Literal['PersistentVolumeClaim'] = 'PersistentVolumeClaim'
    metadata: Optional[gybe.k8s.v1_31.meta.v1.ObjectMeta] = None
    spec: Optional[PersistentVolumeClaimSpec] = None
    status: Optional[PersistentVolumeClaimStatus] = None


@dataclass
class PersistentVolumeClaimCondition(K8sSpec):
    """PersistentVolumeClaimCondition contains details about state of pvc
    Attributes:
        lastProbeTime: lastProbeTime is the time we probed the condition.
        lastTransitionTime: lastTransitionTime is the time the condition transitioned from one status to
            another.
        message: message is the human-readable message indicating details about last transition.
        reason: reason is a unique, this should be a short, machine understandable string that gives the
            reason for condition's last transition. If it reports 'Resizing' that means the underlying
            persistent volume is being resized.
        status: ...
        type: ...

    """

    type: str
    status: str
    lastProbeTime: Optional[str] = None
    lastTransitionTime: Optional[str] = None
    message: Optional[str] = None
    reason: Optional[str] = None


@dataclass
class PersistentVolumeClaimSpec(K8sSpec):
    """PersistentVolumeClaimSpec describes the common attributes of storage devices and allows a Source for
    provider-specific attributes
    Attributes:
        accessModes: accessModes contains the desired access modes the volume should have.
        dataSource: dataSource field can be used to specify either: * An existing VolumeSnapshot object
            (snapshot.storage.k8s.io/VolumeSnapshot) * An existing PVC (PersistentVolumeClaim) If the
            provisioner or an external controller can support the specified data source, it will create a new
            volume based on the contents of the specified data source. When the AnyVolumeDataSource feature
            gate is enabled, dataSource contents will be copied to dataSourceRef, and dataSourceRef contents
            will be copied to dataSource when dataSourceRef.namespace is not specified. If the namespace is
            specified, then dataSourceRef will not be copied to dataSource.
        dataSourceRef: dataSourceRef specifies the object from which to populate the volume with data, if a
            non-empty volume is desired. This may be any object from a non-empty API group (non core object)
            or a PersistentVolumeClaim object. When this field is specified, volume binding will only succeed
            if the type of the specified object matches some installed volume populator or dynamic
            provisioner. This field will replace the functionality of the dataSource field and as such if both
            fields are non-empty, they must have the same value. For backwards compatibility, when namespace
            isn't specified in dataSourceRef, both fields (dataSource and dataSourceRef) will be set to the
            same value automatically if one of them is empty and the other is non-empty. When namespace is
            specified in dataSourceRef, dataSource isn't set to the same value and must be empty. There are
            three important differences between dataSource and dataSourceRef: * While dataSource only allows
            two specific types of objects, dataSourceRef   allows any non-core object, as well as
            PersistentVolumeClaim objects. * While dataSource ignores disallowed values (dropping them),
            dataSourceRef   preserves all values, and generates an error if a disallowed value is   specified.
            * While dataSource only allows local objects, dataSourceRef allows objects   in any namespaces.
            (Beta) Using this field requires the AnyVolumeDataSource feature gate to be enabled. (Alpha) Using
            the namespace field of dataSourceRef requires the CrossNamespaceVolumeDataSource feature gate to
            be enabled.
        resources: resources represents the minimum resources the volume should have. If
            RecoverVolumeExpansionFailure feature is enabled users are allowed to specify resource
            requirements that are lower than previous value but must still be higher than capacity recorded in
            the status field of the claim.
        selector: selector is a label query over volumes to consider for binding.
        storageClassName: storageClassName is the name of the StorageClass required by the claim.
        volumeAttributesClassName: volumeAttributesClassName may be used to set the VolumeAttributesClass used
            by this claim. If specified, the CSI driver will create or update the volume with the attributes
            defined in the corresponding VolumeAttributesClass. This has a different purpose than
            storageClassName, it can be changed after the claim is created. An empty string value means that
            no VolumeAttributesClass will be applied to the claim but it's not allowed to reset this field to
            empty string once it is set. If unspecified and the PersistentVolumeClaim is unbound, the default
            VolumeAttributesClass will be set by the persistentvolume controller if it exists. If the resource
            referred to by volumeAttributesClass does not exist, this PersistentVolumeClaim will be set to a
            Pending state, as reflected by the modifyVolumeStatus field, until such as a resource exists.
        volumeMode: volumeMode defines what type of volume is required by the claim. Value of Filesystem is
            implied when not included in claim spec.
        volumeName: volumeName is the binding reference to the PersistentVolume backing this claim.

    """

    accessModes: Optional[List[str]] = None
    dataSource: Optional[TypedLocalObjectReference] = None
    dataSourceRef: Optional[TypedObjectReference] = None
    resources: Optional[VolumeResourceRequirements] = None
    selector: Optional[gybe.k8s.v1_31.meta.v1.LabelSelector] = None
    storageClassName: Optional[str] = None
    volumeAttributesClassName: Optional[str] = None
    volumeMode: Optional[str] = None
    volumeName: Optional[str] = None


@dataclass
class PersistentVolumeClaimStatus(K8sSpec):
    """PersistentVolumeClaimStatus is the current status of a persistent volume claim.

    Attributes:
        accessModes: accessModes contains the actual access modes the volume backing the PVC has.
        allocatedResourceStatuses: allocatedResourceStatuses stores status of resource being resized for the
            given PVC. Key names follow standard Kubernetes label syntax. Valid values are either:         *
            Un-prefixed keys:                 - storage - the capacity of the volume.         * Custom
            resources must use implementation-defined prefixed names such as 'example.com/my-custom-resource'
            Apart from above values - keys that are unprefixed or have kubernetes.io prefix are considered
            reserved and hence may not be used.  ClaimResourceStatus can be in any of following states:
            - ControllerResizeInProgress:                 State set when resize controller starts resizing the
            volume in control-plane.         - ControllerResizeFailed:                 State set when resize
            has failed in resize controller with a terminal error.         - NodeResizePending:
            State set when resize controller has finished resizing the volume but further resizing of
            volume is needed on the node.         - NodeResizeInProgress:                 State set when
            kubelet starts resizing the volume.         - NodeResizeFailed:                 State set when
            resizing has failed in kubelet with a terminal error. Transient errors don't set
            NodeResizeFailed. For example: if expanding a PVC for more capacity - this field can be one of the
            following states:         - pvc.status.allocatedResourceStatus['storage'] =
            'ControllerResizeInProgress'      - pvc.status.allocatedResourceStatus['storage'] =
            'ControllerResizeFailed'      - pvc.status.allocatedResourceStatus['storage'] =
            'NodeResizePending'      - pvc.status.allocatedResourceStatus['storage'] = 'NodeResizeInProgress'
            - pvc.status.allocatedResourceStatus['storage'] = 'NodeResizeFailed' When this field is not set,
            it means that no resize operation is in progress for the given PVC.  A controller that receives
            PVC update with previously unknown resourceName or ClaimResourceStatus should ignore the update
            for the purpose it was designed. For example - a controller that only is responsible for resizing
            capacity of the volume, should ignore PVC updates that change other valid resources associated
            with PVC.  This is an alpha field and requires enabling RecoverVolumeExpansionFailure feature.
        allocatedResources: allocatedResources tracks the resources allocated to a PVC including its capacity.
            Key names follow standard Kubernetes label syntax. Valid values are either:         * Un-prefixed
            keys:                 - storage - the capacity of the volume.         * Custom resources must use
            implementation-defined prefixed names such as 'example.com/my-custom-resource' Apart from above
            values - keys that are unprefixed or have kubernetes.io prefix are considered reserved and hence
            may not be used.  Capacity reported here may be larger than the actual capacity when a volume
            expansion operation is requested. For storage quota, the larger value from allocatedResources and
            PVC.spec.resources is used. If allocatedResources is not set, PVC.spec.resources alone is used for
            quota calculation. If a volume expansion capacity request is lowered, allocatedResources is only
            lowered if there are no expansion operations in progress and if the actual volume capacity is
            equal or lower than the requested capacity.  A controller that receives PVC update with previously
            unknown resourceName should ignore the update for the purpose it was designed. For example - a
            controller that only is responsible for resizing capacity of the volume, should ignore PVC updates
            that change other valid resources associated with PVC.  This is an alpha field and requires
            enabling RecoverVolumeExpansionFailure feature.
        capacity: capacity represents the actual resources of the underlying volume.
        conditions: conditions is the current Condition of persistent volume claim. If underlying persistent
            volume is being resized then the Condition will be set to 'Resizing'.
        currentVolumeAttributesClassName: currentVolumeAttributesClassName is the current name of the
            VolumeAttributesClass the PVC is using. When unset, there is no VolumeAttributeClass applied to
            this PersistentVolumeClaim This is a beta field and requires enabling VolumeAttributesClass
            feature (off by default).
        modifyVolumeStatus: ModifyVolumeStatus represents the status object of ControllerModifyVolume
            operation. When this is unset, there is no ModifyVolume operation being attempted. This is a beta
            field and requires enabling VolumeAttributesClass feature (off by default).
        phase: phase represents the current phase of PersistentVolumeClaim.

    """

    accessModes: Optional[List[str]] = None
    allocatedResourceStatuses: Optional[JSONDict] = None
    allocatedResources: Optional[JSONDict] = None
    capacity: Optional[JSONDict] = None
    conditions: Optional[List[PersistentVolumeClaimCondition]] = None
    currentVolumeAttributesClassName: Optional[str] = None
    modifyVolumeStatus: Optional[ModifyVolumeStatus] = None
    phase: Optional[str] = None


@dataclass
class PersistentVolumeClaimTemplate(K8sSpec):
    """PersistentVolumeClaimTemplate is used to produce PersistentVolumeClaim objects as part of an
    EphemeralVolumeSource.

    Attributes:
        metadata: May contain labels and annotations that will be copied into the PVC when creating it. No
            other fields are allowed and will be rejected during validation.
        spec: The specification for the PersistentVolumeClaim. The entire content is copied unchanged into the
            PVC that gets created from this template. The same fields as in a PersistentVolumeClaim are also
            valid here.

    """

    spec: PersistentVolumeClaimSpec
    metadata: Optional[gybe.k8s.v1_31.meta.v1.ObjectMeta] = None


@dataclass
class PersistentVolumeClaimVolumeSource(K8sSpec):
    """PersistentVolumeClaimVolumeSource references the user's PVC in the same namespace. This volume finds
    the bound PV and mounts that volume for the pod. A PersistentVolumeClaimVolumeSource is, essentially,
    a wrapper around another type of volume that is owned by someone else (the system).

    Attributes:
        claimName: claimName is the name of a PersistentVolumeClaim in the same namespace as the pod using
            this volume.
        readOnly: readOnly Will force the ReadOnly setting in VolumeMounts. Default false.

    """

    claimName: str
    readOnly: Optional[bool] = None


@dataclass
class PodAffinity(K8sSpec):
    """Pod affinity is a group of inter pod affinity scheduling rules.

    Attributes:
        preferredDuringSchedulingIgnoredDuringExecution: The scheduler will prefer to schedule pods to nodes
            that satisfy the affinity expressions specified by this field, but it may choose a node that
            violates one or more of the expressions. The node that is most preferred is the one with the
            greatest sum of weights, i.e. for each node that meets all of the scheduling requirements
            (resource request, requiredDuringScheduling affinity expressions, etc.), compute a sum by
            iterating through the elements of this field and adding 'weight' to the sum if the node has pods
            which matches the corresponding podAffinityTerm; the node(s) with the highest sum are the most
            preferred.
        requiredDuringSchedulingIgnoredDuringExecution: If the affinity requirements specified by this field
            are not met at scheduling time, the pod will not be scheduled onto the node. If the affinity
            requirements specified by this field cease to be met at some point during pod execution (e.g. due
            to a pod label update), the system may or may not try to eventually evict the pod from its node.
            When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are
            intersected, i.e. all terms must be satisfied.

    """

    preferredDuringSchedulingIgnoredDuringExecution: Optional[List[WeightedPodAffinityTerm]] = None
    requiredDuringSchedulingIgnoredDuringExecution: Optional[List[PodAffinityTerm]] = None


@dataclass
class PodAffinityTerm(K8sSpec):
    """Defines a set of pods (namely those matching the labelSelector relative to the given namespace(s))
    that this pod should be co-located (affinity) or not co-located (anti-affinity) with, where co-located
    is defined as running on a node whose value of the label with key <topologyKey> matches that of any
    node on which a pod of the set of pods is running
    Attributes:
        labelSelector: A label query over a set of resources, in this case pods. If it's null, this
            PodAffinityTerm matches with no Pods.
        matchLabelKeys: MatchLabelKeys is a set of pod label keys to select which pods will be taken into
            consideration. The keys are used to lookup values from the incoming pod labels, those key-value
            labels are merged with `labelSelector` as `key in (value)` to select the group of existing pods
            which pods will be taken into consideration for the incoming pod's pod (anti) affinity. Keys that
            don't exist in the incoming pod labels will be ignored. The default value is empty. The same key
            is forbidden to exist in both matchLabelKeys and labelSelector. Also, matchLabelKeys cannot be set
            when labelSelector isn't set. This is a beta field and requires enabling
            MatchLabelKeysInPodAffinity feature gate (enabled by default).
        mismatchLabelKeys: MismatchLabelKeys is a set of pod label keys to select which pods will be taken
            into consideration. The keys are used to lookup values from the incoming pod labels, those key-
            value labels are merged with `labelSelector` as `key notin (value)` to select the group of
            existing pods which pods will be taken into consideration for the incoming pod's pod (anti)
            affinity. Keys that don't exist in the incoming pod labels will be ignored. The default value is
            empty. The same key is forbidden to exist in both mismatchLabelKeys and labelSelector. Also,
            mismatchLabelKeys cannot be set when labelSelector isn't set. This is a beta field and requires
            enabling MatchLabelKeysInPodAffinity feature gate (enabled by default).
        namespaceSelector: A label query over the set of namespaces that the term applies to. The term is
            applied to the union of the namespaces selected by this field and the ones listed in the
            namespaces field. null selector and null or empty namespaces list means 'this pod's namespace'. An
            empty selector ({}) matches all namespaces.
        namespaces: namespaces specifies a static list of namespace names that the term applies to. The term
            is applied to the union of the namespaces listed in this field and the ones selected by
            namespaceSelector. null or empty namespaces list and null namespaceSelector means 'this pod's
            namespace'.
        topologyKey: This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods
            matching the labelSelector in the specified namespaces, where co-located is defined as running on
            a node whose value of the label with key topologyKey matches that of any node on which any of the
            selected pods is running. Empty topologyKey is not allowed.

    """

    topologyKey: str
    labelSelector: Optional[gybe.k8s.v1_31.meta.v1.LabelSelector] = None
    matchLabelKeys: Optional[List[str]] = None
    mismatchLabelKeys: Optional[List[str]] = None
    namespaceSelector: Optional[gybe.k8s.v1_31.meta.v1.LabelSelector] = None
    namespaces: Optional[List[str]] = None


@dataclass
class PodAntiAffinity(K8sSpec):
    """Pod anti affinity is a group of inter pod anti affinity scheduling rules.

    Attributes:
        preferredDuringSchedulingIgnoredDuringExecution: The scheduler will prefer to schedule pods to nodes
            that satisfy the anti-affinity expressions specified by this field, but it may choose a node that
            violates one or more of the expressions. The node that is most preferred is the one with the
            greatest sum of weights, i.e. for each node that meets all of the scheduling requirements
            (resource request, requiredDuringScheduling anti-affinity expressions, etc.), compute a sum by
            iterating through the elements of this field and adding 'weight' to the sum if the node has pods
            which matches the corresponding podAffinityTerm; the node(s) with the highest sum are the most
            preferred.
        requiredDuringSchedulingIgnoredDuringExecution: If the anti-affinity requirements specified by this
            field are not met at scheduling time, the pod will not be scheduled onto the node. If the anti-
            affinity requirements specified by this field cease to be met at some point during pod execution
            (e.g. due to a pod label update), the system may or may not try to eventually evict the pod from
            its node. When there are multiple elements, the lists of nodes corresponding to each
            podAffinityTerm are intersected, i.e. all terms must be satisfied.

    """

    preferredDuringSchedulingIgnoredDuringExecution: Optional[List[WeightedPodAffinityTerm]] = None
    requiredDuringSchedulingIgnoredDuringExecution: Optional[List[PodAffinityTerm]] = None


@dataclass
class PodDNSConfig(K8sSpec):
    """PodDNSConfig defines the DNS parameters of a pod in addition to those generated from DNSPolicy.

    Attributes:
        nameservers: A list of DNS name server IP addresses. This will be appended to the base nameservers
            generated from DNSPolicy. Duplicated nameservers will be removed.
        options: A list of DNS resolver options. This will be merged with the base options generated from
            DNSPolicy. Duplicated entries will be removed. Resolution options given in Options will override
            those that appear in the base DNSPolicy.
        searches: A list of DNS search domains for host-name lookup. This will be appended to the base search
            paths generated from DNSPolicy. Duplicated search paths will be removed.

    """

    nameservers: Optional[List[str]] = None
    options: Optional[List[PodDNSConfigOption]] = None
    searches: Optional[List[str]] = None


@dataclass
class PodDNSConfigOption(K8sSpec):
    """PodDNSConfigOption defines DNS resolver options of a pod.

    Attributes:
        name: Required.
        value: ...

    """

    name: Optional[str] = None
    value: Optional[str] = None


@dataclass
class PodOS(K8sSpec):
    """PodOS defines the OS parameters of a pod.

    Attributes:
        name: Name is the name of the operating system. The currently supported values are linux and windows.
            Additional value may be defined in future and can be one of:
            https://github.com/opencontainers/runtime-spec/blob/master/config.md#platform-specific-
            configuration Clients should expect to handle additional values and treat unrecognized values in
            this field as os: null

    """

    name: str


@dataclass
class PodReadinessGate(K8sSpec):
    """PodReadinessGate contains the reference to a pod condition
    Attributes:
        conditionType: ConditionType refers to a condition in the pod's condition list with matching type.

    """

    conditionType: str


@dataclass
class PodResourceClaim(K8sSpec):
    """PodResourceClaim references exactly one ResourceClaim, either directly or by naming a
    ResourceClaimTemplate which is then turned into a ResourceClaim for the pod.  It adds a name to it
    that uniquely identifies the ResourceClaim inside the Pod. Containers that need access to the
    ResourceClaim reference it with this name.

    Attributes:
        name: Name uniquely identifies this resource claim inside the pod. This must be a DNS_LABEL.
        resourceClaimName: ResourceClaimName is the name of a ResourceClaim object in the same namespace as
            this pod.  Exactly one of ResourceClaimName and ResourceClaimTemplateName must be set.
        resourceClaimTemplateName: ResourceClaimTemplateName is the name of a ResourceClaimTemplate object in
            the same namespace as this pod.  The template will be used to create a new ResourceClaim, which
            will be bound to this pod. When this pod is deleted, the ResourceClaim will also be deleted. The
            pod name and resource name, along with a generated component, will be used to form a unique name
            for the ResourceClaim, which will be recorded in pod.status.resourceClaimStatuses.  This field is
            immutable and no changes will be made to the corresponding ResourceClaim by the control plane
            after creating the ResourceClaim.  Exactly one of ResourceClaimName and ResourceClaimTemplateName
            must be set.

    """

    name: str
    resourceClaimName: Optional[str] = None
    resourceClaimTemplateName: Optional[str] = None


@dataclass
class PodSchedulingGate(K8sSpec):
    """PodSchedulingGate is associated to a Pod to guard its scheduling.

    Attributes:
        name: Name of the scheduling gate. Each scheduling gate must have a unique name field.

    """

    name: str


@dataclass
class PodSecurityContext(K8sSpec):
    """PodSecurityContext holds pod-level security attributes and common container settings. Some fields are
    also present in container.securityContext.  Field values of container.securityContext take precedence
    over field values of PodSecurityContext.

    Attributes:
        appArmorProfile: appArmorProfile is the AppArmor options to use by the containers in this pod. Note
            that this field cannot be set when spec.os.name is windows.
        fsGroup: A special supplemental group that applies to all containers in a pod. Some volume types allow
            the Kubelet to change the ownership of that volume to be owned by the pod:  1. The owning GID will
            be the FSGroup 2. The setgid bit is set (new files created in the volume will be owned by FSGroup)
            3. The permission bits are OR'd with rw-rw----  If unset, the Kubelet will not modify the
            ownership and permissions of any volume. Note that this field cannot be set when spec.os.name is
            windows.
        fsGroupChangePolicy: fsGroupChangePolicy defines behavior of changing ownership and permission of the
            volume before being exposed inside Pod. This field will only apply to volume types which support
            fsGroup based ownership(and permissions). It will have no effect on ephemeral volume types such
            as: secret, configmaps and emptydir. Valid values are 'OnRootMismatch' and 'Always'. If not
            specified, 'Always' is used. Note that this field cannot be set when spec.os.name is windows.
        runAsGroup: The GID to run the entrypoint of the container process. Uses runtime default if unset. May
            also be set in SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value
            specified in SecurityContext takes precedence for that container. Note that this field cannot be
            set when spec.os.name is windows.
        runAsNonRoot: Indicates that the container must run as a non-root user. If true, the Kubelet will
            validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the
            container if it does. If unset or false, no such validation will be performed. May also be set in
            SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in
            SecurityContext takes precedence.
        runAsUser: The UID to run the entrypoint of the container process. Defaults to user specified in image
            metadata if unspecified. May also be set in SecurityContext.  If set in both SecurityContext and
            PodSecurityContext, the value specified in SecurityContext takes precedence for that container.
            Note that this field cannot be set when spec.os.name is windows.
        seLinuxOptions: The SELinux context to be applied to all containers. If unspecified, the container
            runtime will allocate a random SELinux context for each container.  May also be set in
            SecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in
            SecurityContext takes precedence for that container. Note that this field cannot be set when
            spec.os.name is windows.
        seccompProfile: The seccomp options to use by the containers in this pod. Note that this field cannot
            be set when spec.os.name is windows.
        supplementalGroups: A list of groups applied to the first process run in each container, in addition
            to the container's primary GID and fsGroup (if specified).  If the SupplementalGroupsPolicy
            feature is enabled, the supplementalGroupsPolicy field determines whether these are in addition to
            or instead of any group memberships defined in the container image. If unspecified, no additional
            groups are added, though group memberships defined in the container image may still be used,
            depending on the supplementalGroupsPolicy field. Note that this field cannot be set when
            spec.os.name is windows.
        supplementalGroupsPolicy: Defines how supplemental groups of the first container processes are
            calculated. Valid values are 'Merge' and 'Strict'. If not specified, 'Merge' is used. (Alpha)
            Using the field requires the SupplementalGroupsPolicy feature gate to be enabled and the container
            runtime must implement support for this feature. Note that this field cannot be set when
            spec.os.name is windows.
        sysctls: Sysctls hold a list of namespaced sysctls used for the pod. Pods with unsupported sysctls (by
            the container runtime) might fail to launch. Note that this field cannot be set when spec.os.name
            is windows.
        windowsOptions: The Windows specific settings applied to all containers. If unspecified, the options
            within a container's SecurityContext will be used. If set in both SecurityContext and
            PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field
            cannot be set when spec.os.name is linux.

    """

    appArmorProfile: Optional[AppArmorProfile] = None
    fsGroup: Optional[int] = None
    fsGroupChangePolicy: Optional[str] = None
    runAsGroup: Optional[int] = None
    runAsNonRoot: Optional[bool] = None
    runAsUser: Optional[int] = None
    seLinuxOptions: Optional[SELinuxOptions] = None
    seccompProfile: Optional[SeccompProfile] = None
    supplementalGroups: Optional[List[int]] = None
    supplementalGroupsPolicy: Optional[str] = None
    sysctls: Optional[List[Sysctl]] = None
    windowsOptions: Optional[WindowsSecurityContextOptions] = None


@dataclass
class PodSpec(K8sSpec):
    """PodSpec is a description of a pod.

    Attributes:
        activeDeadlineSeconds: Optional duration in seconds the pod may be active on the node relative to
            StartTime before the system will actively try to mark it failed and kill associated containers.
            Value must be a positive integer.
        affinity: If specified, the pod's scheduling constraints
        automountServiceAccountToken: AutomountServiceAccountToken indicates whether a service account token
            should be automatically mounted.
        containers: List of containers belonging to the pod. Containers cannot currently be added or removed.
            There must be at least one container in a Pod. Cannot be updated.
        dnsConfig: Specifies the DNS parameters of a pod. Parameters specified here will be merged to the
            generated DNS configuration based on DNSPolicy.
        dnsPolicy: Set DNS policy for the pod. Defaults to 'ClusterFirst'. Valid values are
            'ClusterFirstWithHostNet', 'ClusterFirst', 'Default' or 'None'. DNS parameters given in DNSConfig
            will be merged with the policy selected with DNSPolicy. To have DNS options set along with
            hostNetwork, you have to specify DNS policy explicitly to 'ClusterFirstWithHostNet'.
        enableServiceLinks: EnableServiceLinks indicates whether information about services should be injected
            into pod's environment variables, matching the syntax of Docker links. Optional: Defaults to true.
        ephemeralContainers: List of ephemeral containers run in this pod. Ephemeral containers may be run in
            an existing pod to perform user-initiated actions such as debugging. This list cannot be specified
            when creating a pod, and it cannot be modified by updating the pod spec. In order to add an
            ephemeral container to an existing pod, use the pod's ephemeralcontainers subresource.
        hostAliases: HostAliases is an optional list of hosts and IPs that will be injected into the pod's
            hosts file if specified.
        hostIPC: Use the host's ipc namespace. Optional: Default to false.
        hostNetwork: Host networking requested for this pod. Use the host's network namespace. If this option
            is set, the ports that will be used must be specified. Default to false.
        hostPID: Use the host's pid namespace. Optional: Default to false.
        hostUsers: Use the host's user namespace. Optional: Default to true. If set to true or not present,
            the pod will be run in the host user namespace, useful for when the pod needs a feature only
            available to the host user namespace, such as loading a kernel module with CAP_SYS_MODULE. When
            set to false, a new userns is created for the pod. Setting false is useful for mitigating
            container breakout vulnerabilities even allowing users to run their containers as root without
            actually having root privileges on the host. This field is alpha-level and is only honored by
            servers that enable the UserNamespacesSupport feature.
        hostname: Specifies the hostname of the Pod If not specified, the pod's hostname will be set to a
            system-defined value.
        imagePullSecrets: ImagePullSecrets is an optional list of references to secrets in the same namespace
            to use for pulling any of the images used by this PodSpec. If specified, these secrets will be
            passed to individual puller implementations for them to use.
        initContainers: List of initialization containers belonging to the pod. Init containers are executed
            in order prior to containers being started. If any init container fails, the pod is considered to
            have failed and is handled according to its restartPolicy. The name for an init container or
            normal container must be unique among all containers. Init containers may not have Lifecycle
            actions, Readiness probes, Liveness probes, or Startup probes. The resourceRequirements of an init
            container are taken into account during scheduling by finding the highest request/limit for each
            resource type, and then using the max of of that value or the sum of the normal containers. Limits
            are applied to init containers in a similar fashion. Init containers cannot currently be added or
            removed. Cannot be updated.
        nodeName: NodeName indicates in which node this pod is scheduled. If empty, this pod is a candidate
            for scheduling by the scheduler defined in schedulerName. Once this field is set, the kubelet for
            this node becomes responsible for the lifecycle of this pod. This field should not be used to
            express a desire for the pod to be scheduled on a specific node.
            https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#nodename
        nodeSelector: NodeSelector is a selector which must be true for the pod to fit on a node. Selector
            which must match a node's labels for the pod to be scheduled on that node.
        os: Specifies the OS of the containers in the pod. Some pod and container fields are restricted if
            this is set.  If the OS field is set to linux, the following fields must be unset:
            -securityContext.windowsOptions  If the OS field is set to windows, following fields must be
            unset: - spec.hostPID - spec.hostIPC - spec.hostUsers - spec.securityContext.appArmorProfile -
            spec.securityContext.seLinuxOptions - spec.securityContext.seccompProfile -
            spec.securityContext.fsGroup - spec.securityContext.fsGroupChangePolicy -
            spec.securityContext.sysctls - spec.shareProcessNamespace - spec.securityContext.runAsUser -
            spec.securityContext.runAsGroup - spec.securityContext.supplementalGroups -
            spec.securityContext.supplementalGroupsPolicy - spec.containers[*].securityContext.appArmorProfile
            - spec.containers[*].securityContext.seLinuxOptions -
            spec.containers[*].securityContext.seccompProfile -
            spec.containers[*].securityContext.capabilities -
            spec.containers[*].securityContext.readOnlyRootFilesystem -
            spec.containers[*].securityContext.privileged -
            spec.containers[*].securityContext.allowPrivilegeEscalation -
            spec.containers[*].securityContext.procMount - spec.containers[*].securityContext.runAsUser -
            spec.containers[*].securityContext.runAsGroup
        overhead: Overhead represents the resource overhead associated with running a pod for a given
            RuntimeClass. This field will be autopopulated at admission time by the RuntimeClass admission
            controller. If the RuntimeClass admission controller is enabled, overhead must not be set in Pod
            create requests. The RuntimeClass admission controller will reject Pod create requests which have
            the overhead already set. If RuntimeClass is configured and selected in the PodSpec, Overhead will
            be set to the value defined in the corresponding RuntimeClass, otherwise it will remain unset and
            treated as zero.
        preemptionPolicy: PreemptionPolicy is the Policy for preempting pods with lower priority. One of
            Never, PreemptLowerPriority. Defaults to PreemptLowerPriority if unset.
        priority: The priority value. Various system components use this field to find the priority of the
            pod. When Priority Admission Controller is enabled, it prevents users from setting this field. The
            admission controller populates this field from PriorityClassName. The higher the value, the higher
            the priority.
        priorityClassName: If specified, indicates the pod's priority. 'system-node-critical' and 'system-
            cluster-critical' are two special keywords which indicate the highest priorities with the former
            being the highest priority. Any other name must be defined by creating a PriorityClass object with
            that name. If not specified, the pod priority will be default or zero if there is no default.
        readinessGates: If specified, all readiness gates will be evaluated for pod readiness. A pod is ready
            when all its containers are ready AND all conditions specified in the readiness gates have status
            equal to 'True'
        resourceClaims: ResourceClaims defines which ResourceClaims must be allocated and reserved before the
            Pod is allowed to start. The resources will be made available to those containers which consume
            them by name.  This is an alpha field and requires enabling the DynamicResourceAllocation feature
            gate.  This field is immutable.
        restartPolicy: Restart policy for all containers within the pod. One of Always, OnFailure, Never. In
            some contexts, only a subset of those values may be permitted. Default to Always.
        runtimeClassName: RuntimeClassName refers to a RuntimeClass object in the node.k8s.io group, which
            should be used to run this pod.  If no RuntimeClass resource matches the named class, the pod will
            not be run. If unset or empty, the 'legacy' RuntimeClass will be used, which is an implicit class
            with an empty definition that uses the default runtime handler.
        schedulerName: If specified, the pod will be dispatched by specified scheduler. If not specified, the
            pod will be dispatched by default scheduler.
        schedulingGates: SchedulingGates is an opaque list of values that if specified will block scheduling
            the pod. If schedulingGates is not empty, the pod will stay in the SchedulingGated state and the
            scheduler will not attempt to schedule the pod.  SchedulingGates can only be set at pod creation
            time, and be removed only afterwards.
        securityContext: SecurityContext holds pod-level security attributes and common container settings.
            Optional: Defaults to empty.  See type description for default values of each field.
        serviceAccount: DeprecatedServiceAccount is a deprecated alias for ServiceAccountName. Deprecated: Use
            serviceAccountName instead.
        serviceAccountName: ServiceAccountName is the name of the ServiceAccount to use to run this pod.
        setHostnameAsFQDN: If true the pod's hostname will be configured as the pod's FQDN, rather than the
            leaf name (the default). In Linux containers, this means setting the FQDN in the hostname field of
            the kernel (the nodename field of struct utsname). In Windows containers, this means setting the
            registry value of hostname for the registry key
            HKEY_LOCAL_MACHINESYSTEMCurrentControlSetServicesTcpipParameters to FQDN. If a pod does not
            have FQDN, this has no effect. Default to false.
        shareProcessNamespace: Share a single process namespace between all of the containers in a pod. When
            this is set containers will be able to view and signal processes from other containers in the same
            pod, and the first process in each container will not be assigned PID 1. HostPID and
            ShareProcessNamespace cannot both be set. Optional: Default to false.
        subdomain: If specified, the fully qualified Pod hostname will be '<hostname>.<subdomain>.<pod
            namespace>.svc.<cluster domain>'. If not specified, the pod will not have a domainname at all.
        terminationGracePeriodSeconds: Optional duration in seconds the pod needs to terminate gracefully. May
            be decreased in delete request. Value must be non-negative integer. The value zero indicates stop
            immediately via the kill signal (no opportunity to shut down). If this value is nil, the default
            grace period will be used instead. The grace period is the duration in seconds after the processes
            running in the pod are sent a termination signal and the time when the processes are forcibly
            halted with a kill signal. Set this value longer than the expected cleanup time for your process.
            Defaults to 30 seconds.
        tolerations: If specified, the pod's tolerations.
        topologySpreadConstraints: TopologySpreadConstraints describes how a group of pods ought to spread
            across topology domains. Scheduler will schedule pods in a way which abides by the constraints.
            All topologySpreadConstraints are ANDed.
        volumes: List of volumes that can be mounted by containers belonging to the pod.

    """

    containers: List[Container]
    activeDeadlineSeconds: Optional[int] = None
    affinity: Optional[Affinity] = None
    automountServiceAccountToken: Optional[bool] = None
    dnsConfig: Optional[PodDNSConfig] = None
    dnsPolicy: Optional[str] = None
    enableServiceLinks: Optional[bool] = None
    ephemeralContainers: Optional[List[EphemeralContainer]] = None
    hostAliases: Optional[List[HostAlias]] = None
    hostIPC: Optional[bool] = None
    hostNetwork: Optional[bool] = None
    hostPID: Optional[bool] = None
    hostUsers: Optional[bool] = None
    hostname: Optional[str] = None
    imagePullSecrets: Optional[List[LocalObjectReference]] = None
    initContainers: Optional[List[Container]] = None
    nodeName: Optional[str] = None
    nodeSelector: Optional[JSONDict] = None
    os: Optional[PodOS] = None
    overhead: Optional[JSONDict] = None
    preemptionPolicy: Optional[str] = None
    priority: Optional[int] = None
    priorityClassName: Optional[str] = None
    readinessGates: Optional[List[PodReadinessGate]] = None
    resourceClaims: Optional[List[PodResourceClaim]] = None
    restartPolicy: Optional[str] = None
    runtimeClassName: Optional[str] = None
    schedulerName: Optional[str] = None
    schedulingGates: Optional[List[PodSchedulingGate]] = None
    securityContext: Optional[PodSecurityContext] = None
    serviceAccount: Optional[str] = None
    serviceAccountName: Optional[str] = None
    setHostnameAsFQDN: Optional[bool] = None
    shareProcessNamespace: Optional[bool] = None
    subdomain: Optional[str] = None
    terminationGracePeriodSeconds: Optional[int] = None
    tolerations: Optional[List[Toleration]] = None
    topologySpreadConstraints: Optional[List[TopologySpreadConstraint]] = None
    volumes: Optional[List[Volume]] = None


@dataclass
class PodTemplateSpec(K8sSpec):
    """PodTemplateSpec describes the data a pod should have when created from a template
    Attributes:
        metadata: Standard object's metadata.
        spec: Specification of the desired behavior of the pod.

    """

    metadata: Optional[gybe.k8s.v1_31.meta.v1.ObjectMeta] = None
    spec: Optional[PodSpec] = None


@dataclass
class PreferredSchedulingTerm(K8sSpec):
    """An empty preferred scheduling term matches all objects with implicit weight 0 (i.e. it's a no-op). A
    null preferred scheduling term matches no objects (i.e. is also a no-op).

    Attributes:
        preference: A node selector term, associated with the corresponding weight.
        weight: Weight associated with matching the corresponding nodeSelectorTerm, in the range 1-100.

    """

    weight: int
    preference: NodeSelectorTerm


@dataclass
class Probe(K8sSpec):
    """Probe describes a health check to be performed against a container to determine whether it is alive or
    ready to receive traffic.

    Attributes:
        exec: Exec specifies the action to take.
        failureThreshold: Minimum consecutive failures for the probe to be considered failed after having
            succeeded. Defaults to 3. Minimum value is 1.
        grpc: GRPC specifies an action involving a GRPC port.
        httpGet: HTTPGet specifies the http request to perform.
        initialDelaySeconds: Number of seconds after the container has started before liveness probes are
            initiated.
        periodSeconds: How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1.
        successThreshold: Minimum consecutive successes for the probe to be considered successful after having
            failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1.
        tcpSocket: TCPSocket specifies an action involving a TCP port.
        terminationGracePeriodSeconds: Optional duration in seconds the pod needs to terminate gracefully upon
            probe failure. The grace period is the duration in seconds after the processes running in the pod
            are sent a termination signal and the time when the processes are forcibly halted with a kill
            signal. Set this value longer than the expected cleanup time for your process. If this value is
            nil, the pod's terminationGracePeriodSeconds will be used. Otherwise, this value overrides the
            value provided by the pod spec. Value must be non-negative integer. The value zero indicates stop
            immediately via the kill signal (no opportunity to shut down). This is a beta field and requires
            enabling ProbeTerminationGracePeriod feature gate. Minimum value is 1.
            spec.terminationGracePeriodSeconds is used if unset.
        timeoutSeconds: Number of seconds after which the probe times out. Defaults to 1 second. Minimum value
            is 1.

    """

    exec: Optional[ExecAction] = None
    failureThreshold: Optional[int] = None
    grpc: Optional[GRPCAction] = None
    httpGet: Optional[HTTPGetAction] = None
    initialDelaySeconds: Optional[int] = None
    periodSeconds: Optional[int] = None
    successThreshold: Optional[int] = None
    tcpSocket: Optional[TCPSocketAction] = None
    terminationGracePeriodSeconds: Optional[int] = None
    timeoutSeconds: Optional[int] = None


@dataclass
class ProjectedVolumeSource(K8sSpec):
    """Represents a projected volume source
    Attributes:
        defaultMode: defaultMode are the mode bits used to set permissions on created files by default. Must
            be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both
            octal and decimal values, JSON requires decimal values for mode bits. Directories within the path
            are not affected by this setting. This might be in conflict with other options that affect the
            file mode, like fsGroup, and the result can be other mode bits set.
        sources: sources is the list of volume projections. Each entry in this list handles one source.

    """

    defaultMode: Optional[int] = None
    sources: Optional[List[VolumeProjection]] = None


@dataclass
class RBDVolumeSource(K8sSpec):
    """Represents a Rados Block Device mount that lasts the lifetime of a pod. RBD volumes support ownership
    management and SELinux relabeling.

    Attributes:
        fsType: fsType is the filesystem type of the volume that you want to mount. Tip: Ensure that the
            filesystem type is supported by the host operating system. Examples: 'ext4', 'xfs', 'ntfs'.
            Implicitly inferred to be 'ext4' if unspecified.
        image: image is the rados image name.
        keyring: keyring is the path to key ring for RBDUser. Default is /etc/ceph/keyring.
        monitors: monitors is a collection of Ceph monitors.
        pool: pool is the rados pool name. Default is rbd.
        readOnly: readOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false.
        secretRef: secretRef is name of the authentication secret for RBDUser. If provided overrides keyring.
            Default is nil.
        user: user is the rados user name. Default is admin.

    """

    monitors: List[str]
    image: str
    fsType: Optional[str] = None
    keyring: Optional[str] = None
    pool: Optional[str] = None
    readOnly: Optional[bool] = None
    secretRef: Optional[LocalObjectReference] = None
    user: Optional[str] = None


@dataclass
class ResourceClaim(K8sSpec):
    """ResourceClaim references one entry in PodSpec.ResourceClaims.

    Attributes:
        name: Name must match the name of one entry in pod.spec.resourceClaims of the Pod where this field is
            used. It makes that resource available inside a container.
        request: Request is the name chosen for a request in the referenced claim. If empty, everything from
            the claim is made available, otherwise only the result of this request.

    """

    name: str
    request: Optional[str] = None


@dataclass
class ResourceFieldSelector(K8sSpec):
    """ResourceFieldSelector represents container resources (cpu, memory) and their output format
    Attributes:
        containerName: Container name: required for volumes, optional for env vars
        divisor: Specifies the output format of the exposed resources, defaults to '1'
        resource: Required: resource to select

    """

    resource: str
    containerName: Optional[str] = None
    divisor: Optional[gybe.k8s.v1_31.api.resource.Quantity] = None


@dataclass
class ResourceRequirements(K8sSpec):
    """ResourceRequirements describes the compute resource requirements.

    Attributes:
        claims: Claims lists the names of resources, defined in spec.resourceClaims, that are used by this
            container.  This is an alpha field and requires enabling the DynamicResourceAllocation feature
            gate.  This field is immutable. It can only be set for containers.
        limits: Limits describes the maximum amount of compute resources allowed.
        requests: Requests describes the minimum amount of compute resources required. If Requests is omitted
            for a container, it defaults to Limits if that is explicitly specified, otherwise to an
            implementation-defined value. Requests cannot exceed Limits.

    """

    claims: Optional[List[ResourceClaim]] = None
    limits: Optional[JSONDict] = None
    requests: Optional[JSONDict] = None


@dataclass
class SELinuxOptions(K8sSpec):
    """SELinuxOptions are the labels to be applied to the container
    Attributes:
        level: Level is SELinux level label that applies to the container.
        role: Role is a SELinux role label that applies to the container.
        type: Type is a SELinux type label that applies to the container.
        user: User is a SELinux user label that applies to the container.

    """

    level: Optional[str] = None
    role: Optional[str] = None
    type: Optional[str] = None
    user: Optional[str] = None


@dataclass
class ScaleIOVolumeSource(K8sSpec):
    """ScaleIOVolumeSource represents a persistent ScaleIO volume
    Attributes:
        fsType: fsType is the filesystem type to mount. Must be a filesystem type supported by the host
            operating system. Ex. 'ext4', 'xfs', 'ntfs'. Default is 'xfs'.
        gateway: gateway is the host address of the ScaleIO API Gateway.
        protectionDomain: protectionDomain is the name of the ScaleIO Protection Domain for the configured
            storage.
        readOnly: readOnly Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in
            VolumeMounts.
        secretRef: secretRef references to the secret for ScaleIO user and other sensitive information. If
            this is not provided, Login operation will fail.
        sslEnabled: sslEnabled Flag enable/disable SSL communication with Gateway, default false
        storageMode: storageMode indicates whether the storage for a volume should be ThickProvisioned or
            ThinProvisioned. Default is ThinProvisioned.
        storagePool: storagePool is the ScaleIO Storage Pool associated with the protection domain.
        system: system is the name of the storage system as configured in ScaleIO.
        volumeName: volumeName is the name of a volume already created in the ScaleIO system that is
            associated with this volume source.

    """

    gateway: str
    system: str
    secretRef: LocalObjectReference
    fsType: Optional[str] = None
    protectionDomain: Optional[str] = None
    readOnly: Optional[bool] = None
    sslEnabled: Optional[bool] = None
    storageMode: Optional[str] = None
    storagePool: Optional[str] = None
    volumeName: Optional[str] = None


@dataclass
class SeccompProfile(K8sSpec):
    """SeccompProfile defines a pod/container's seccomp profile settings. Only one profile source may be set.

    Attributes:
        localhostProfile: localhostProfile indicates a profile defined in a file on the node should be used.
            The profile must be preconfigured on the node to work. Must be a descending path, relative to the
            kubelet's configured seccomp profile location. Must be set if type is 'Localhost'. Must NOT be set
            for any other type.
        type: type indicates which kind of seccomp profile will be applied. Valid options are:  Localhost - a
            profile defined in a file on the node should be used. RuntimeDefault - the container runtime
            default profile should be used. Unconfined - no profile should be applied.

    """

    type: str
    localhostProfile: Optional[str] = None


@dataclass
class SecretEnvSource(K8sSpec):
    """SecretEnvSource selects a Secret to populate the environment variables with.  The contents of the
    target Secret's Data field will represent the key-value pairs as environment variables.

    Attributes:
        name: Name of the referent. This field is effectively required, but due to backwards compatibility is
            allowed to be empty. Instances of this type with an empty value here are almost certainly wrong.
        optional: Specify whether the Secret must be defined

    """

    name: Optional[str] = None
    optional: Optional[bool] = None


@dataclass
class SecretKeySelector(K8sSpec):
    """SecretKeySelector selects a key of a Secret.

    Attributes:
        key: The key of the secret to select from.  Must be a valid secret key.
        name: Name of the referent. This field is effectively required, but due to backwards compatibility is
            allowed to be empty. Instances of this type with an empty value here are almost certainly wrong.
        optional: Specify whether the Secret or its key must be defined

    """

    key: str
    name: Optional[str] = None
    optional: Optional[bool] = None


@dataclass
class SecretProjection(K8sSpec):
    """Adapts a secret into a projected volume.  The contents of the target Secret's Data field will be
    presented in a projected volume as files using the keys in the Data field as the file names. Note that
    this is identical to a secret volume source without the default mode.

    Attributes:
        items: items if unspecified, each key-value pair in the Data field of the referenced Secret will be
            projected into the volume as a file whose name is the key and content is the value. If specified,
            the listed keys will be projected into the specified paths, and unlisted keys will not be present.
            If a key is specified which is not present in the Secret, the volume setup will error unless it is
            marked optional. Paths must be relative and may not contain the '..' path or start with '..'.
        name: Name of the referent. This field is effectively required, but due to backwards compatibility is
            allowed to be empty. Instances of this type with an empty value here are almost certainly wrong.
        optional: optional field specify whether the Secret or its key must be defined

    """

    items: Optional[List[KeyToPath]] = None
    name: Optional[str] = None
    optional: Optional[bool] = None


@dataclass
class SecretVolumeSource(K8sSpec):
    """Adapts a Secret into a volume.  The contents of the target Secret's Data field will be presented in a
    volume as files using the keys in the Data field as the file names. Secret volumes support ownership
    management and SELinux relabeling.

    Attributes:
        defaultMode: defaultMode is Optional: mode bits used to set permissions on created files by default.
            Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts
            both octal and decimal values, JSON requires decimal values for mode bits. Defaults to 0644.
            Directories within the path are not affected by this setting. This might be in conflict with other
            options that affect the file mode, like fsGroup, and the result can be other mode bits set.
        items: items If unspecified, each key-value pair in the Data field of the referenced Secret will be
            projected into the volume as a file whose name is the key and content is the value. If specified,
            the listed keys will be projected into the specified paths, and unlisted keys will not be present.
            If a key is specified which is not present in the Secret, the volume setup will error unless it is
            marked optional. Paths must be relative and may not contain the '..' path or start with '..'.
        optional: optional field specify whether the Secret or its keys must be defined
        secretName: secretName is the name of the secret in the pod's namespace to use.

    """

    defaultMode: Optional[int] = None
    items: Optional[List[KeyToPath]] = None
    optional: Optional[bool] = None
    secretName: Optional[str] = None


@dataclass
class SecurityContext(K8sSpec):
    """SecurityContext holds security configuration that will be applied to a container. Some fields are
    present in both SecurityContext and PodSecurityContext.  When both are set, the values in
    SecurityContext take precedence.

    Attributes:
        allowPrivilegeEscalation: AllowPrivilegeEscalation controls whether a process can gain more privileges
            than its parent process. This bool directly controls if the no_new_privs flag will be set on the
            container process. AllowPrivilegeEscalation is true always when the container is: 1) run as
            Privileged 2) has CAP_SYS_ADMIN Note that this field cannot be set when spec.os.name is windows.
        appArmorProfile: appArmorProfile is the AppArmor options to use by this container. If set, this
            profile overrides the pod's appArmorProfile. Note that this field cannot be set when spec.os.name
            is windows.
        capabilities: The capabilities to add/drop when running containers. Defaults to the default set of
            capabilities granted by the container runtime. Note that this field cannot be set when
            spec.os.name is windows.
        privileged: Run container in privileged mode. Processes in privileged containers are essentially
            equivalent to root on the host. Defaults to false. Note that this field cannot be set when
            spec.os.name is windows.
        procMount: procMount denotes the type of proc mount to use for the containers. The default value is
            Default which uses the container runtime defaults for readonly paths and masked paths. This
            requires the ProcMountType feature flag to be enabled. Note that this field cannot be set when
            spec.os.name is windows.
        readOnlyRootFilesystem: Whether this container has a read-only root filesystem. Default is false. Note
            that this field cannot be set when spec.os.name is windows.
        runAsGroup: The GID to run the entrypoint of the container process. Uses runtime default if unset. May
            also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the
            value specified in SecurityContext takes precedence. Note that this field cannot be set when
            spec.os.name is windows.
        runAsNonRoot: Indicates that the container must run as a non-root user. If true, the Kubelet will
            validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the
            container if it does. If unset or false, no such validation will be performed. May also be set in
            PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in
            SecurityContext takes precedence.
        runAsUser: The UID to run the entrypoint of the container process. Defaults to user specified in image
            metadata if unspecified. May also be set in PodSecurityContext.  If set in both SecurityContext
            and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this
            field cannot be set when spec.os.name is windows.
        seLinuxOptions: The SELinux context to be applied to the container. If unspecified, the container
            runtime will allocate a random SELinux context for each container.  May also be set in
            PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in
            SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is windows.
        seccompProfile: The seccomp options to use by this container. If seccomp options are provided at both
            the pod & container level, the container options override the pod options. Note that this field
            cannot be set when spec.os.name is windows.
        windowsOptions: The Windows specific settings applied to all containers. If unspecified, the options
            from the PodSecurityContext will be used. If set in both SecurityContext and PodSecurityContext,
            the value specified in SecurityContext takes precedence. Note that this field cannot be set when
            spec.os.name is linux.

    """

    allowPrivilegeEscalation: Optional[bool] = None
    appArmorProfile: Optional[AppArmorProfile] = None
    capabilities: Optional[Capabilities] = None
    privileged: Optional[bool] = None
    procMount: Optional[str] = None
    readOnlyRootFilesystem: Optional[bool] = None
    runAsGroup: Optional[int] = None
    runAsNonRoot: Optional[bool] = None
    runAsUser: Optional[int] = None
    seLinuxOptions: Optional[SELinuxOptions] = None
    seccompProfile: Optional[SeccompProfile] = None
    windowsOptions: Optional[WindowsSecurityContextOptions] = None


@dataclass
class ServiceAccountTokenProjection(K8sSpec):
    """ServiceAccountTokenProjection represents a projected service account token volume. This projection can
    be used to insert a service account token into the pods runtime filesystem for use against APIs
    (Kubernetes API Server or otherwise).

    Attributes:
        audience: audience is the intended audience of the token. A recipient of a token must identify itself
            with an identifier specified in the audience of the token, and otherwise should reject the token.
            The audience defaults to the identifier of the apiserver.
        expirationSeconds: expirationSeconds is the requested duration of validity of the service account
            token. As the token approaches expiration, the kubelet volume plugin will proactively rotate the
            service account token. The kubelet will start trying to rotate the token if the token is older
            than 80 percent of its time to live or if the token is older than 24 hours.Defaults to 1 hour and
            must be at least 10 minutes.
        path: path is the path relative to the mount point of the file to project the token into.

    """

    path: str
    audience: Optional[str] = None
    expirationSeconds: Optional[int] = None


@dataclass
class SleepAction(K8sSpec):
    """SleepAction describes a 'sleep' action.

    Attributes:
        seconds: Seconds is the number of seconds to sleep.

    """

    seconds: int


@dataclass
class StorageOSVolumeSource(K8sSpec):
    """Represents a StorageOS persistent volume resource.

    Attributes:
        fsType: fsType is the filesystem type to mount. Must be a filesystem type supported by the host
            operating system. Ex. 'ext4', 'xfs', 'ntfs'. Implicitly inferred to be 'ext4' if unspecified.
        readOnly: readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in
            VolumeMounts.
        secretRef: secretRef specifies the secret to use for obtaining the StorageOS API credentials.  If not
            specified, default values will be attempted.
        volumeName: volumeName is the human-readable name of the StorageOS volume.  Volume names are only
            unique within a namespace.
        volumeNamespace: volumeNamespace specifies the scope of the volume within StorageOS.  If no namespace
            is specified then the Pod's namespace will be used.  This allows the Kubernetes name scoping to be
            mirrored within StorageOS for tighter integration. Set VolumeName to any name to override the
            default behaviour. Set to 'default' if you are not using namespaces within StorageOS. Namespaces
            that do not pre-exist within StorageOS will be created.

    """

    fsType: Optional[str] = None
    readOnly: Optional[bool] = None
    secretRef: Optional[LocalObjectReference] = None
    volumeName: Optional[str] = None
    volumeNamespace: Optional[str] = None


@dataclass
class Sysctl(K8sSpec):
    """Sysctl defines a kernel parameter to be set
    Attributes:
        name: Name of a property to set
        value: Value of a property to set

    """

    name: str
    value: str


@dataclass
class TCPSocketAction(K8sSpec):
    """TCPSocketAction describes an action based on opening a socket
    Attributes:
        host: Optional: Host name to connect to, defaults to the pod IP.
        port: Number or name of the port to access on the container. Number must be in the range 1 to 65535.
            Name must be an IANA_SVC_NAME.

    """

    port: str
    host: Optional[str] = None


@dataclass
class TopologySpreadConstraint(K8sSpec):
    """TopologySpreadConstraint specifies how to spread matching pods among the given topology.

    Attributes:
        labelSelector: LabelSelector is used to find matching pods. Pods that match this label selector are
            counted to determine the number of pods in their corresponding topology domain.
        matchLabelKeys: MatchLabelKeys is a set of pod label keys to select the pods over which spreading will
            be calculated. The keys are used to lookup values from the incoming pod labels, those key-value
            labels are ANDed with labelSelector to select the group of existing pods over which spreading will
            be calculated for the incoming pod. The same key is forbidden to exist in both MatchLabelKeys and
            LabelSelector. MatchLabelKeys cannot be set when LabelSelector isn't set. Keys that don't exist in
            the incoming pod labels will be ignored. A null or empty list means only match against
            labelSelector.  This is a beta field and requires the MatchLabelKeysInPodTopologySpread feature
            gate to be enabled (enabled by default).
        maxSkew: MaxSkew describes the degree to which pods may be unevenly distributed. When
            `whenUnsatisfiable=DoNotSchedule`, it is the maximum permitted difference between the number of
            matching pods in the target topology and the global minimum. The global minimum is the minimum
            number of matching pods in an eligible domain or zero if the number of eligible domains is less
            than MinDomains. For example, in a 3-zone cluster, MaxSkew is set to 1, and pods with the same
            labelSelector spread as 2/2/1: In this case, the global minimum is 1. | zone1 | zone2 | zone3 | |
            P P  |  P P  |   P   | - if MaxSkew is 1, incoming pod can only be scheduled to zone3 to become
            2/2/2; scheduling it onto zone1(zone2) would make the ActualSkew(3-1) on zone1(zone2) violate
            MaxSkew(1). - if MaxSkew is 2, incoming pod can be scheduled onto any zone. When
            `whenUnsatisfiable=ScheduleAnyway`, it is used to give higher precedence to topologies that
            satisfy it. It's a required field. Default value is 1 and 0 is not allowed.
        minDomains: MinDomains indicates a minimum number of eligible domains. When the number of eligible
            domains with matching topology keys is less than minDomains, Pod Topology Spread treats 'global
            minimum' as 0, and then the calculation of Skew is performed. And when the number of eligible
            domains with matching topology keys equals or greater than minDomains, this value has no effect on
            scheduling. As a result, when the number of eligible domains is less than minDomains, scheduler
            won't schedule more than maxSkew Pods to those domains. If value is nil, the constraint behaves as
            if MinDomains is equal to 1. Valid values are integers greater than 0. When value is not nil,
            WhenUnsatisfiable must be DoNotSchedule.  For example, in a 3-zone cluster, MaxSkew is set to 2,
            MinDomains is set to 5 and pods with the same labelSelector spread as 2/2/2: | zone1 | zone2 |
            zone3 | |  P P  |  P P  |  P P  | The number of domains is less than 5(MinDomains), so 'global
            minimum' is treated as 0. In this situation, new pod with the same labelSelector cannot be
            scheduled, because computed skew will be 3(3 - 0) if new Pod is scheduled to any of the three
            zones, it will violate MaxSkew.
        nodeAffinityPolicy: NodeAffinityPolicy indicates how we will treat Pod's nodeAffinity/nodeSelector
            when calculating pod topology spread skew. Options are: - Honor: only nodes matching
            nodeAffinity/nodeSelector are included in the calculations. - Ignore: nodeAffinity/nodeSelector
            are ignored. All nodes are included in the calculations.  If this value is nil, the behavior is
            equivalent to the Honor policy. This is a beta-level feature default enabled by the
            NodeInclusionPolicyInPodTopologySpread feature flag.
        nodeTaintsPolicy: NodeTaintsPolicy indicates how we will treat node taints when calculating pod
            topology spread skew. Options are: - Honor: nodes without taints, along with tainted nodes for
            which the incoming pod has a toleration, are included. - Ignore: node taints are ignored. All
            nodes are included.  If this value is nil, the behavior is equivalent to the Ignore policy. This
            is a beta-level feature default enabled by the NodeInclusionPolicyInPodTopologySpread feature
            flag.
        topologyKey: TopologyKey is the key of node labels. Nodes that have a label with this key and
            identical values are considered to be in the same topology. We consider each <key, value> as a
            'bucket', and try to put balanced number of pods into each bucket. We define a domain as a
            particular instance of a topology. Also, we define an eligible domain as a domain whose nodes meet
            the requirements of nodeAffinityPolicy and nodeTaintsPolicy. e.g. If TopologyKey is
            'kubernetes.io/hostname', each Node is a domain of that topology. And, if TopologyKey is
            'topology.kubernetes.io/zone', each zone is a domain of that topology. It's a required field.
        whenUnsatisfiable: WhenUnsatisfiable indicates how to deal with a pod if it doesn't satisfy the spread
            constraint. - DoNotSchedule (default) tells the scheduler not to schedule it. - ScheduleAnyway
            tells the scheduler to schedule the pod in any location,   but giving higher precedence to
            topologies that would help reduce the   skew. A constraint is considered 'Unsatisfiable' for an
            incoming pod if and only if every possible node assignment for that pod would violate 'MaxSkew' on
            some topology. For example, in a 3-zone cluster, MaxSkew is set to 1, and pods with the same
            labelSelector spread as 3/1/1: | zone1 | zone2 | zone3 | | P P P |   P   |   P   | If
            WhenUnsatisfiable is set to DoNotSchedule, incoming pod can only be scheduled to zone2(zone3) to
            become 3/2/1(3/1/2) as ActualSkew(2-1) on zone2(zone3) satisfies MaxSkew(1). In other words, the
            cluster can still be imbalanced, but scheduler won't make it *more* imbalanced. It's a required
            field.

    """

    maxSkew: int
    topologyKey: str
    whenUnsatisfiable: str
    labelSelector: Optional[gybe.k8s.v1_31.meta.v1.LabelSelector] = None
    matchLabelKeys: Optional[List[str]] = None
    minDomains: Optional[int] = None
    nodeAffinityPolicy: Optional[str] = None
    nodeTaintsPolicy: Optional[str] = None


@dataclass
class TypedLocalObjectReference(K8sSpec):
    """TypedLocalObjectReference contains enough information to let you locate the typed referenced object
    inside the same namespace.

    Attributes:
        apiGroup: APIGroup is the group for the resource being referenced. If APIGroup is not specified, the
            specified Kind must be in the core API group. For any other third-party types, APIGroup is
            required.
        kind: Kind is the type of resource being referenced
        name: Name is the name of resource being referenced

    """

    kind: str
    name: str
    apiGroup: Optional[str] = None


@dataclass
class TypedObjectReference(K8sSpec):
    """Schema model io.k8s.api.core.v1.TypedObjectReference.

    Attributes:
        apiGroup: APIGroup is the group for the resource being referenced. If APIGroup is not specified, the
            specified Kind must be in the core API group. For any other third-party types, APIGroup is
            required.
        kind: Kind is the type of resource being referenced
        name: Name is the name of resource being referenced
        namespace: Namespace is the namespace of resource being referenced Note that when a namespace is
            specified, a gateway.networking.k8s.io/ReferenceGrant object is required in the referent namespace
            to allow that namespace's owner to accept the reference. See the ReferenceGrant documentation for
            details. (Alpha) This field requires the CrossNamespaceVolumeDataSource feature gate to be
            enabled.

    """

    kind: str
    name: str
    apiGroup: Optional[str] = None
    namespace: Optional[str] = None


@dataclass
class Volume(K8sSpec):
    """Volume represents a named volume in a pod that may be accessed by any container in the pod.

    Attributes:
        awsElasticBlockStore: awsElasticBlockStore represents an AWS Disk resource that is attached to a
            kubelet's host machine and then exposed to the pod.
        azureDisk: azureDisk represents an Azure Data Disk mount on the host and bind mount to the pod.
        azureFile: azureFile represents an Azure File Service mount on the host and bind mount to the pod.
        cephfs: cephFS represents a Ceph FS mount on the host that shares a pod's lifetime
        cinder: cinder represents a cinder volume attached and mounted on kubelets host machine.
        configMap: configMap represents a configMap that should populate this volume
        csi: csi (Container Storage Interface) represents ephemeral storage that is handled by certain
            external CSI drivers (Beta feature).
        downwardAPI: downwardAPI represents downward API about the pod that should populate this volume
        emptyDir: emptyDir represents a temporary directory that shares a pod's lifetime.
        ephemeral: ephemeral represents a volume that is handled by a cluster storage driver. The volume's
            lifecycle is tied to the pod that defines it - it will be created before the pod starts, and
            deleted when the pod is removed.  Use this if: a) the volume is only needed while the pod runs, b)
            features of normal volumes like restoring from snapshot or capacity    tracking are needed, c) the
            storage driver is specified through a storage class, and d) the storage driver supports dynamic
            volume provisioning through    a PersistentVolumeClaim (see EphemeralVolumeSource for more
            information on the connection between this volume type    and PersistentVolumeClaim).  Use
            PersistentVolumeClaim or one of the vendor-specific APIs for volumes that persist for longer than
            the lifecycle of an individual pod.  Use CSI for light-weight local ephemeral volumes if the CSI
            driver is meant to be used that way - see the documentation of the driver for more information.  A
            pod can use both types of ephemeral volumes and persistent volumes at the same time.
        fc: fc represents a Fibre Channel resource that is attached to a kubelet's host machine and then
            exposed to the pod.
        flexVolume: flexVolume represents a generic volume resource that is provisioned/attached using an exec
            based plugin.
        flocker: flocker represents a Flocker volume attached to a kubelet's host machine. This depends on the
            Flocker control service being running
        gcePersistentDisk: gcePersistentDisk represents a GCE Disk resource that is attached to a kubelet's
            host machine and then exposed to the pod.
        gitRepo: gitRepo represents a git repository at a particular revision. DEPRECATED: GitRepo is
            deprecated. To provision a container with a git repo, mount an EmptyDir into an InitContainer that
            clones the repo using git, then mount the EmptyDir into the Pod's container.
        glusterfs: glusterfs represents a Glusterfs mount on the host that shares a pod's lifetime.
        hostPath: hostPath represents a pre-existing file or directory on the host machine that is directly
            exposed to the container. This is generally used for system agents or other privileged things that
            are allowed to see the host machine. Most containers will NOT need this.
        image: image represents an OCI object (a container image or artifact) pulled and mounted on the
            kubelet's host machine. The volume is resolved at pod startup depending on which PullPolicy value
            is provided:  - Always: the kubelet always attempts to pull the reference. Container creation will
            fail If the pull fails. - Never: the kubelet never pulls the reference and only uses a local image
            or artifact. Container creation will fail if the reference isn't present. - IfNotPresent: the
            kubelet pulls if the reference isn't already present on disk. Container creation will fail if the
            reference isn't present and the pull fails.  The volume gets re-resolved if the pod gets deleted
            and recreated, which means that new remote content will become available on pod recreation. A
            failure to resolve or pull the image during pod startup will block containers from starting and
            may add significant latency. Failures will be retried using normal volume backoff and will be
            reported on the pod reason and message. The types of objects that may be mounted by this volume
            are defined by the container runtime implementation on a host machine and at minimum must include
            all valid types supported by the container image field. The OCI object gets mounted in a single
            directory (spec.containers[*].volumeMounts.mountPath) by merging the manifest layers in the same
            way as for container images. The volume will be mounted read-only (ro) and non-executable files
            (noexec). Sub path mounts for containers are not supported
            (spec.containers[*].volumeMounts.subpath). The field spec.securityContext.fsGroupChangePolicy has
            no effect on this volume type.
        iscsi: iscsi represents an ISCSI Disk resource that is attached to a kubelet's host machine and then
            exposed to the pod.
        name: name of the volume. Must be a DNS_LABEL and unique within the pod.
        nfs: nfs represents an NFS mount on the host that shares a pod's lifetime
        persistentVolumeClaim: persistentVolumeClaimVolumeSource represents a reference to a
            PersistentVolumeClaim in the same namespace.
        photonPersistentDisk: photonPersistentDisk represents a PhotonController persistent disk attached and
            mounted on kubelets host machine
        portworxVolume: portworxVolume represents a portworx volume attached and mounted on kubelets host
            machine
        projected: projected items for all in one resources secrets, configmaps, and downward API
        quobyte: quobyte represents a Quobyte mount on the host that shares a pod's lifetime
        rbd: rbd represents a Rados Block Device mount on the host that shares a pod's lifetime.
        scaleIO: scaleIO represents a ScaleIO persistent volume attached and mounted on Kubernetes nodes.
        secret: secret represents a secret that should populate this volume.
        storageos: storageOS represents a StorageOS volume attached and mounted on Kubernetes nodes.
        vsphereVolume: vsphereVolume represents a vSphere volume attached and mounted on kubelets host machine

    """

    name: str
    awsElasticBlockStore: Optional[AWSElasticBlockStoreVolumeSource] = None
    azureDisk: Optional[AzureDiskVolumeSource] = None
    azureFile: Optional[AzureFileVolumeSource] = None
    cephfs: Optional[CephFSVolumeSource] = None
    cinder: Optional[CinderVolumeSource] = None
    configMap: Optional[ConfigMapVolumeSource] = None
    csi: Optional[CSIVolumeSource] = None
    downwardAPI: Optional[DownwardAPIVolumeSource] = None
    emptyDir: Optional[EmptyDirVolumeSource] = None
    ephemeral: Optional[EphemeralVolumeSource] = None
    fc: Optional[FCVolumeSource] = None
    flexVolume: Optional[FlexVolumeSource] = None
    flocker: Optional[FlockerVolumeSource] = None
    gcePersistentDisk: Optional[GCEPersistentDiskVolumeSource] = None
    gitRepo: Optional[GitRepoVolumeSource] = None
    glusterfs: Optional[GlusterfsVolumeSource] = None
    hostPath: Optional[HostPathVolumeSource] = None
    image: Optional[ImageVolumeSource] = None
    iscsi: Optional[ISCSIVolumeSource] = None
    nfs: Optional[NFSVolumeSource] = None
    persistentVolumeClaim: Optional[PersistentVolumeClaimVolumeSource] = None
    photonPersistentDisk: Optional[PhotonPersistentDiskVolumeSource] = None
    portworxVolume: Optional[PortworxVolumeSource] = None
    projected: Optional[ProjectedVolumeSource] = None
    quobyte: Optional[QuobyteVolumeSource] = None
    rbd: Optional[RBDVolumeSource] = None
    scaleIO: Optional[ScaleIOVolumeSource] = None
    secret: Optional[SecretVolumeSource] = None
    storageos: Optional[StorageOSVolumeSource] = None
    vsphereVolume: Optional[VsphereVirtualDiskVolumeSource] = None


@dataclass
class VolumeDevice(K8sSpec):
    """volumeDevice describes a mapping of a raw block device within a container.

    Attributes:
        devicePath: devicePath is the path inside of the container that the device will be mapped to.
        name: name must match the name of a persistentVolumeClaim in the pod

    """

    name: str
    devicePath: str


@dataclass
class VolumeMount(K8sSpec):
    """VolumeMount describes a mounting of a Volume within a container.

    Attributes:
        mountPath: Path within the container at which the volume should be mounted.  Must not contain ':'.
        mountPropagation: mountPropagation determines how mounts are propagated from the host to container and
            the other way around. When not set, MountPropagationNone is used. This field is beta in 1.10. When
            RecursiveReadOnly is set to IfPossible or to Enabled, MountPropagation must be None or unspecified
            (which defaults to None).
        name: This must match the Name of a Volume.
        readOnly: Mounted read-only if true, read-write otherwise (false or unspecified). Defaults to false.
        recursiveReadOnly: RecursiveReadOnly specifies whether read-only mounts should be handled recursively.
            If ReadOnly is false, this field has no meaning and must be unspecified.  If ReadOnly is true, and
            this field is set to Disabled, the mount is not made recursively read-only.  If this field is set
            to IfPossible, the mount is made recursively read-only, if it is supported by the container
            runtime.  If this field is set to Enabled, the mount is made recursively read-only if it is
            supported by the container runtime, otherwise the pod will not be started and an error will be
            generated to indicate the reason.  If this field is set to IfPossible or Enabled, MountPropagation
            must be set to None (or be unspecified, which defaults to None).  If this field is not specified,
            it is treated as an equivalent of Disabled.
        subPath: Path within the volume from which the container's volume should be mounted. Defaults to ''
            (volume's root).
        subPathExpr: Expanded path within the volume from which the container's volume should be mounted.
            Behaves similarly to SubPath but environment variable references $(VAR_NAME) are expanded using
            the container's environment. Defaults to '' (volume's root). SubPathExpr and SubPath are mutually
            exclusive.

    """

    name: str
    mountPath: str
    mountPropagation: Optional[str] = None
    readOnly: Optional[bool] = None
    recursiveReadOnly: Optional[str] = None
    subPath: Optional[str] = None
    subPathExpr: Optional[str] = None


@dataclass
class VolumeProjection(K8sSpec):
    """Projection that may be projected along with other supported volume types. Exactly one of these fields
    must be set.

    Attributes:
        clusterTrustBundle: ClusterTrustBundle allows a pod to access the `.spec.trustBundle` field of
            ClusterTrustBundle objects in an auto-updating file.  Alpha, gated by the
            ClusterTrustBundleProjection feature gate.  ClusterTrustBundle objects can either be selected by
            name, or by the combination of signer name and a label selector.  Kubelet performs aggressive
            normalization of the PEM contents written into the pod filesystem.  Esoteric PEM features such as
            inter-block comments and block headers are stripped.  Certificates are deduplicated. The ordering
            of certificates within the file is arbitrary, and Kubelet may change the order over time.
        configMap: configMap information about the configMap data to project
        downwardAPI: downwardAPI information about the downwardAPI data to project
        secret: secret information about the secret data to project
        serviceAccountToken: serviceAccountToken is information about the serviceAccountToken data to project

    """

    clusterTrustBundle: Optional[ClusterTrustBundleProjection] = None
    configMap: Optional[ConfigMapProjection] = None
    downwardAPI: Optional[DownwardAPIProjection] = None
    secret: Optional[SecretProjection] = None
    serviceAccountToken: Optional[ServiceAccountTokenProjection] = None


@dataclass
class VolumeResourceRequirements(K8sSpec):
    """VolumeResourceRequirements describes the storage resource requirements for a volume.

    Attributes:
        limits: Limits describes the maximum amount of compute resources allowed.
        requests: Requests describes the minimum amount of compute resources required. If Requests is omitted
            for a container, it defaults to Limits if that is explicitly specified, otherwise to an
            implementation-defined value. Requests cannot exceed Limits.

    """

    limits: Optional[JSONDict] = None
    requests: Optional[JSONDict] = None


@dataclass
class WeightedPodAffinityTerm(K8sSpec):
    """The weights of all of the matched WeightedPodAffinityTerm fields are added per-node to find the most
    preferred node(s)

    Attributes:
        podAffinityTerm: Required. A pod affinity term, associated with the corresponding weight.
        weight: weight associated with matching the corresponding podAffinityTerm, in the range 1-100.

    """

    weight: int
    podAffinityTerm: PodAffinityTerm


@dataclass
class WindowsSecurityContextOptions(K8sSpec):
    """WindowsSecurityContextOptions contain Windows-specific options and credentials.

    Attributes:
        gmsaCredentialSpec: GMSACredentialSpec is where the GMSA admission webhook
            (https://github.com/kubernetes-sigs/windows-gmsa) inlines the contents of the GMSA credential spec
            named by the GMSACredentialSpecName field.
        gmsaCredentialSpecName: GMSACredentialSpecName is the name of the GMSA credential spec to use.
        hostProcess: HostProcess determines if a container should be run as a 'Host Process' container. All of
            a Pod's containers must have the same effective HostProcess value (it is not allowed to have a mix
            of HostProcess containers and non-HostProcess containers). In addition, if HostProcess is true
            then HostNetwork must also be set to true.
        runAsUserName: The UserName in Windows to run the entrypoint of the container process. Defaults to the
            user specified in image metadata if unspecified. May also be set in PodSecurityContext. If set in
            both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes
            precedence.

    """

    gmsaCredentialSpec: Optional[str] = None
    gmsaCredentialSpecName: Optional[str] = None
    hostProcess: Optional[bool] = None
    runAsUserName: Optional[str] = None


@dataclass
class AttachedVolume(K8sSpec):
    """AttachedVolume describes a volume attached to a node
    Attributes:
        devicePath: DevicePath represents the device path where the volume should be available
        name: Name of the attached volume

    """

    name: str
    devicePath: str


@dataclass
class Binding(K8sSpec):
    """Binding ties one object to another; for example, a pod is bound to a node by a scheduler. Deprecated
    in 1.7, please use the bindings subresource of pods instead.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object's metadata.
        target: The target object that you want to bind to the standard object.

    """

    target: ObjectReference
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[gybe.k8s.v1_31.meta.v1.ObjectMeta] = None


@dataclass
class ClientIPConfig(K8sSpec):
    """ClientIPConfig represents the configurations of Client IP based session affinity.

    Attributes:
        timeoutSeconds: timeoutSeconds specifies the seconds of ClientIP type session sticky time. The value
            must be >0 && <=86400(for 1 day) if ServiceAffinity == 'ClientIP'. Default value is 10800(for 3
            hours).

    """

    timeoutSeconds: Optional[int] = None


@dataclass
class ComponentCondition(K8sSpec):
    """Information about the condition of a component.

    Attributes:
        error: Condition error code for a component. For example, a health check error code.
        message: Message about the condition for a component. For example, information about a health check.
        status: Status of the condition for a component. Valid values for 'Healthy': 'True', 'False', or
            'Unknown'.
        type: Type of condition for a component. Valid value: 'Healthy'

    """

    type: str
    status: str
    error: Optional[str] = None
    message: Optional[str] = None


@dataclass
class ComponentStatus(K8sSpec):
    """ComponentStatus (and ComponentStatusList) holds the cluster validation info. Deprecated: This API is
    deprecated in v1.19+
    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        conditions: List of component conditions observed
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object's metadata.

    """

    apiVersion: Optional[str] = None
    conditions: Optional[List[ComponentCondition]] = None
    kind: Optional[str] = None
    metadata: Optional[gybe.k8s.v1_31.meta.v1.ObjectMeta] = None


@dataclass
class ComponentStatusList(K8sSpec):
    """Status of all the conditions for the component as a list of ComponentStatus objects. Deprecated: This
    API is deprecated in v1.19+
    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        items: List of ComponentStatus objects.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard list metadata.

    """

    items: List[ComponentStatus]
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[JSONObj] = None


@dataclass
class ConfigMap(K8sSpec):
    """ConfigMap holds configuration data for pods to consume.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        binaryData: BinaryData contains the binary data. Each key must consist of alphanumeric characters,
            '-', '_' or '.'. BinaryData can contain byte sequences that are not in the UTF-8 range. The keys
            stored in BinaryData must not overlap with the ones in the Data field, this is enforced during
            validation process. Using this field will require 1.10+ apiserver and kubelet.
        data: Data contains the configuration data. Each key must consist of alphanumeric characters, '-', '_'
            or '.'. Values with non-UTF-8 byte sequences must use the BinaryData field. The keys stored in
            Data must not overlap with the keys in the BinaryData field, this is enforced during validation
            process.
        immutable: Immutable, if set to true, ensures that data stored in the ConfigMap cannot be updated
            (only object metadata can be modified). If not set to true, the field can be modified at any time.
            Defaulted to nil.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object's metadata.

    """

    apiVersion: Optional[str] = None
    binaryData: Optional[JSONDict] = None
    data: Optional[JSONDict] = None
    immutable: Optional[bool] = None
    kind: Optional[str] = None
    metadata: Optional[gybe.k8s.v1_31.meta.v1.ObjectMeta] = None


@dataclass
class ConfigMapList(K8sSpec):
    """ConfigMapList is a resource containing a list of ConfigMap objects.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        items: Items is the list of ConfigMaps.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata:

    """

    items: List[ConfigMap]
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[JSONObj] = None


@dataclass
class ConfigMapNodeConfigSource(K8sSpec):
    """ConfigMapNodeConfigSource contains the information to reference a ConfigMap as a config source for the
    Node. This API is deprecated since 1.22: https://git.k8s.io/enhancements/keps/sig-node/281-dynamic-
    kubelet-configuration
    Attributes:
        kubeletConfigKey: KubeletConfigKey declares which key of the referenced ConfigMap corresponds to the
            KubeletConfiguration structure This field is required in all cases.
        name: Name is the metadata.name of the referenced ConfigMap. This field is required in all cases.
        namespace: Namespace is the metadata.namespace of the referenced ConfigMap. This field is required in
            all cases.
        resourceVersion: ResourceVersion is the metadata.ResourceVersion of the referenced ConfigMap. This
            field is forbidden in Node.Spec, and required in Node.Status.
        uid: UID is the metadata.UID of the referenced ConfigMap. This field is forbidden in Node.Spec, and
            required in Node.Status.

    """

    namespace: str
    name: str
    kubeletConfigKey: str
    resourceVersion: Optional[str] = None
    uid: Optional[str] = None


@dataclass
class ContainerImage(K8sSpec):
    """Describe a container image
    Attributes:
        names: Names by which this image is known. e.g. ['kubernetes.example/hyperkube:v1.0.7', 'cloud-
            vendor.registry.example/cloud-vendor/hyperkube:v1.0.7']
        sizeBytes: The size of the image in bytes.

    """

    names: Optional[List[str]] = None
    sizeBytes: Optional[int] = None


@dataclass
class ContainerState(K8sSpec):
    """ContainerState holds a possible state of container. Only one of its members may be specified. If none
    of them is specified, the default one is ContainerStateWaiting.

    Attributes:
        running: Details about a running container
        terminated: Details about a terminated container
        waiting: Details about a waiting container

    """

    running: Optional[ContainerStateRunning] = None
    terminated: Optional[ContainerStateTerminated] = None
    waiting: Optional[ContainerStateWaiting] = None


@dataclass
class ContainerStateRunning(K8sSpec):
    """ContainerStateRunning is a running state of a container.

    Attributes:
        startedAt: Time at which the container was last (re-)started

    """

    startedAt: Optional[str] = None


@dataclass
class ContainerStateTerminated(K8sSpec):
    """ContainerStateTerminated is a terminated state of a container.

    Attributes:
        containerID: Container's ID in the format '<type>://<container_id>'
        exitCode: Exit status from the last termination of the container
        finishedAt: Time at which the container last terminated
        message: Message regarding the last termination of the container
        reason: (brief) reason from the last termination of the container
        signal: Signal from the last termination of the container
        startedAt: Time at which previous execution of the container started

    """

    exitCode: int
    containerID: Optional[str] = None
    finishedAt: Optional[str] = None
    message: Optional[str] = None
    reason: Optional[str] = None
    signal: Optional[int] = None
    startedAt: Optional[str] = None


@dataclass
class ContainerStateWaiting(K8sSpec):
    """ContainerStateWaiting is a waiting state of a container.

    Attributes:
        message: Message regarding why the container is not yet running.
        reason: (brief) reason the container is not yet running.

    """

    message: Optional[str] = None
    reason: Optional[str] = None


@dataclass
class ContainerStatus(K8sSpec):
    """ContainerStatus contains details for the current status of this container.

    Attributes:
        allocatedResources: AllocatedResources represents the compute resources allocated for this container
            by the node. Kubelet sets this value to Container.Resources.Requests upon successful pod admission
            and after successfully admitting desired pod resize.
        allocatedResourcesStatus: AllocatedResourcesStatus represents the status of various resources
            allocated for this Pod.
        containerID: ContainerID is the ID of the container in the format '<type>://<container_id>'. Where
            type is a container runtime identifier, returned from Version call of CRI API (for example
            'containerd').
        image: Image is the name of container image that the container is running. The container image may not
            match the image used in the PodSpec, as it may have been resolved by the runtime.
        imageID: ImageID is the image ID of the container's image. The image ID may not match the image ID of
            the image used in the PodSpec, as it may have been resolved by the runtime.
        lastState: LastTerminationState holds the last termination state of the container to help debug
            container crashes and restarts. This field is not populated if the container is still running and
            RestartCount is 0.
        name: Name is a DNS_LABEL representing the unique name of the container. Each container in a pod must
            have a unique name across all container types. Cannot be updated.
        ready: Ready specifies whether the container is currently passing its readiness check. The value will
            change as readiness probes keep executing. If no readiness probes are specified, this field
            defaults to true once the container is fully started (see Started field).  The value is typically
            used to determine whether a container is ready to accept traffic.
        resources: Resources represents the compute resource requests and limits that have been successfully
            enacted on the running container after it has been started or has been successfully resized.
        restartCount: RestartCount holds the number of times the container has been restarted. Kubelet makes
            an effort to always increment the value, but there are cases when the state may be lost due to
            node restarts and then the value may be reset to 0. The value is never negative.
        started: Started indicates whether the container has finished its postStart lifecycle hook and passed
            its startup probe. Initialized as false, becomes true after startupProbe is considered successful.
            Resets to false when the container is restarted, or if kubelet loses state temporarily. In both
            cases, startup probes will run again. Is always true when no startupProbe is defined and container
            is running and has passed the postStart lifecycle hook. The null value must be treated the same as
            false.
        state: State holds details about the container's current condition.
        user: User represents user identity information initially attached to the first process of the
            container
        volumeMounts: Status of volume mounts.

    """

    name: str
    ready: bool
    restartCount: int
    image: str
    imageID: str
    allocatedResources: Optional[JSONDict] = None
    allocatedResourcesStatus: Optional[List[ResourceStatus]] = None
    containerID: Optional[str] = None
    lastState: Optional[ContainerState] = None
    resources: Optional[ResourceRequirements] = None
    started: Optional[bool] = None
    state: Optional[ContainerState] = None
    user: Optional[ContainerUser] = None
    volumeMounts: Optional[List[VolumeMountStatus]] = None


@dataclass
class ContainerUser(K8sSpec):
    """ContainerUser represents user identity information
    Attributes:
        linux: Linux holds user identity information initially attached to the first process of the containers
            in Linux. Note that the actual running identity can be changed if the process has enough privilege
            to do so.

    """

    linux: Optional[LinuxContainerUser] = None


@dataclass
class DaemonEndpoint(K8sSpec):
    """DaemonEndpoint contains information about a single Daemon endpoint.

    Attributes:
        Port: Port number of the given endpoint.

    """

    Port: int


@dataclass
class EndpointAddress(K8sSpec):
    """EndpointAddress is a tuple that describes single IP address.

    Attributes:
        hostname: The Hostname of this endpoint
        ip: The IP of this endpoint. May not be loopback (127.0.0.0/8 or ::1), link-local (169.254.0.0/16 or
            fe80::/10), or link-local multicast (224.0.0.0/24 or ff02::/16).
        nodeName: Optional: Node hosting this endpoint. This can be used to determine endpoints local to a
            node.
        targetRef: Reference to object providing the endpoint.

    """

    ip: str
    hostname: Optional[str] = None
    nodeName: Optional[str] = None
    targetRef: Optional[ObjectReference] = None


@dataclass
class EndpointPort(K8sSpec):
    """EndpointPort is a tuple that describes a single port.

    Attributes:
        appProtocol: The application protocol for this port. This is used as a hint for implementations to
            offer richer behavior for protocols that they understand. This field follows standard Kubernetes
            label syntax. Valid values are either:  * Un-prefixed protocol names - reserved for IANA standard
            service names (as per RFC-6335 and https://www.iana.org/assignments/service-names).  * Kubernetes-
            defined prefixed names:   * 'kubernetes.io/h2c' - HTTP/2 prior knowledge over cleartext as
            described in https://www.rfc-editor.org/rfc/rfc9113.html#name-starting-http-2-with-prior-   *
            'kubernetes.io/ws'  - WebSocket over cleartext as described in https://www.rfc-
            editor.org/rfc/rfc6455   * 'kubernetes.io/wss' - WebSocket over TLS as described in
            https://www.rfc-editor.org/rfc/rfc6455  * Other protocols should use implementation-defined
            prefixed names such as mycompany.com/my-custom-protocol.
        name: The name of this port.  This must match the 'name' field in the corresponding ServicePort. Must
            be a DNS_LABEL. Optional only if one port is defined.
        port: The port number of the endpoint.
        protocol: The IP protocol for this port. Must be UDP, TCP, or SCTP. Default is TCP.

    """

    port: int
    appProtocol: Optional[str] = None
    name: Optional[str] = None
    protocol: Optional[str] = None


@dataclass
class EndpointSubset(K8sSpec):
    """EndpointSubset is a group of addresses with a common set of ports. The expanded set of endpoints is
    the Cartesian product of Addresses x Ports. For example, given:          {           Addresses:
    [{'ip': '10.10.1.1'}, {'ip': '10.10.2.2'}],           Ports:     [{'name': 'a', 'port': 8675},
    {'name': 'b', 'port': 309}]         }  The resulting set of endpoints can be viewed as:          a: [
    10.10.1.1:8675, 10.10.2.2:8675 ],         b: [ 10.10.1.1:309, 10.10.2.2:309 ]

    Attributes:
        addresses: IP addresses which offer the related ports that are marked as ready. These endpoints should
            be considered safe for load balancers and clients to utilize.
        notReadyAddresses: IP addresses which offer the related ports but are not currently marked as ready
            because they have not yet finished starting, have recently failed a readiness check, or have
            recently failed a liveness check.
        ports: Port numbers available on the related IP addresses.

    """

    addresses: Optional[List[EndpointAddress]] = None
    notReadyAddresses: Optional[List[EndpointAddress]] = None
    ports: Optional[List[EndpointPort]] = None


@dataclass
class Endpoints(K8sSpec):
    """Endpoints is a collection of endpoints that implement the actual service. Example:           Name:
    'mysvc',          Subsets: [            {              Addresses: [{'ip': '10.10.1.1'}, {'ip':
    '10.10.2.2'}],              Ports: [{'name': 'a', 'port': 8675}, {'name': 'b', 'port': 309}]
    },            {              Addresses: [{'ip': '10.10.3.3'}],              Ports: [{'name': 'a',
    'port': 93}, {'name': 'b', 'port': 76}]            },         ]

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object's metadata.
        subsets: The set of all endpoints is the union of all subsets. Addresses are placed into subsets
            according to the IPs they share. A single address with multiple ports, some of which are ready and
            some of which are not (because they come from different containers) will result in the address
            being displayed in different subsets for the different ports. No address will appear in both
            Addresses and NotReadyAddresses in the same subset. Sets of addresses and ports that comprise a
            service.

    """

    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[gybe.k8s.v1_31.meta.v1.ObjectMeta] = None
    subsets: Optional[List[EndpointSubset]] = None


@dataclass
class EndpointsList(K8sSpec):
    """EndpointsList is a list of endpoints.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        items: List of endpoints.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard list metadata.

    """

    items: List[Endpoints]
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[JSONObj] = None


@dataclass
class Event(K8sSpec):
    """Event is a report of an event somewhere in the cluster.  Events have a limited retention time and
    triggers and messages may evolve with time.  Event consumers should not rely on the timing of an event
    with a given Reason reflecting a consistent underlying trigger, or the continued existence of events
    with that Reason.  Events should be treated as informative, best-effort, supplemental data.

    Attributes:
        action: What action was taken/failed regarding to the Regarding object.
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        count: The number of times this event has occurred.
        eventTime: Time when this Event was first observed.
        firstTimestamp: The time at which the event was first recorded. (Time of server receipt is in
            TypeMeta.)
        involvedObject: The object that this event is about.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        lastTimestamp: The time at which the most recent occurrence of this event was recorded.
        message: A human-readable description of the status of this operation.
        metadata: Standard object's metadata.
        reason: This should be a short, machine understandable string that gives the reason for the transition
            into the object's current status.
        related: Optional secondary object for more complex actions.
        reportingComponent: Name of the controller that emitted this Event, e.g. `kubernetes.io/kubelet`.
        reportingInstance: ID of the controller instance, e.g. `kubelet-xyzf`.
        series: Data about the Event series this event represents or nil if it's a singleton Event.
        source: The component reporting this event. Should be a short machine understandable string.
        type: Type of this event (Normal, Warning), new types could be added in the future

    """

    metadata: gybe.k8s.v1_31.meta.v1.ObjectMeta
    involvedObject: ObjectReference
    action: Optional[str] = None
    apiVersion: Optional[str] = None
    count: Optional[int] = None
    eventTime: Optional[str] = None
    firstTimestamp: Optional[str] = None
    kind: Optional[str] = None
    lastTimestamp: Optional[str] = None
    message: Optional[str] = None
    reason: Optional[str] = None
    related: Optional[ObjectReference] = None
    reportingComponent: Optional[str] = None
    reportingInstance: Optional[str] = None
    series: Optional[EventSeries] = None
    source: Optional[EventSource] = None
    type: Optional[str] = None


@dataclass
class EventList(K8sSpec):
    """EventList is a list of events.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        items: List of events
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard list metadata.

    """

    items: List[Event]
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[JSONObj] = None


@dataclass
class EventSeries(K8sSpec):
    """EventSeries contain information on series of events, i.e. thing that was/is happening continuously for
    some time.

    Attributes:
        count: Number of occurrences in this series up to the last heartbeat time
        lastObservedTime: Time of the last occurrence observed

    """

    count: Optional[int] = None
    lastObservedTime: Optional[str] = None


@dataclass
class HostIP(K8sSpec):
    """HostIP represents a single IP address allocated to the host.

    Attributes:
        ip: IP is the IP address assigned to the host

    """

    ip: str


@dataclass
class LimitRange(K8sSpec):
    """LimitRange sets resource usage limits for each kind of resource in a Namespace.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object's metadata.
        spec: Spec defines the limits enforced.

    """

    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[gybe.k8s.v1_31.meta.v1.ObjectMeta] = None
    spec: Optional[LimitRangeSpec] = None


@dataclass
class LimitRangeItem(K8sSpec):
    """LimitRangeItem defines a min/max usage limit for any resource that matches on kind.

    Attributes:
        default: Default resource requirement limit value by resource name if resource limit is omitted.
        defaultRequest: DefaultRequest is the default resource requirement request value by resource name if
            resource request is omitted.
        max: Max usage constraints on this kind by resource name.
        maxLimitRequestRatio: MaxLimitRequestRatio if specified, the named resource must have a request and
            limit that are both non-zero where limit divided by request is less than or equal to the
            enumerated value; this represents the max burst for the named resource.
        min: Min usage constraints on this kind by resource name.
        type: Type of resource that this limit applies to.

    """

    type: str
    default: Optional[JSONDict] = None
    defaultRequest: Optional[JSONDict] = None
    max: Optional[JSONDict] = None
    maxLimitRequestRatio: Optional[JSONDict] = None
    min: Optional[JSONDict] = None


@dataclass
class LimitRangeList(K8sSpec):
    """LimitRangeList is a list of LimitRange items.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        items: Items is a list of LimitRange objects.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard list metadata.

    """

    items: List[LimitRange]
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[JSONObj] = None


@dataclass
class LimitRangeSpec(K8sSpec):
    """LimitRangeSpec defines a min/max usage limit for resources that match on kind.

    Attributes:
        limits: Limits is the list of LimitRangeItem objects that are enforced.

    """

    limits: List[LimitRangeItem]


@dataclass
class LinuxContainerUser(K8sSpec):
    """LinuxContainerUser represents user identity information in Linux containers
    Attributes:
        gid: GID is the primary gid initially attached to the first process in the container
        supplementalGroups: SupplementalGroups are the supplemental groups initially attached to the first
            process in the container
        uid: UID is the primary uid initially attached to the first process in the container

    """

    uid: int
    gid: int
    supplementalGroups: Optional[List[int]] = None


@dataclass
class LoadBalancerIngress(K8sSpec):
    """LoadBalancerIngress represents the status of a load-balancer ingress point: traffic intended for the
    service should be sent to an ingress point.

    Attributes:
        hostname: Hostname is set for load-balancer ingress points that are DNS based (typically AWS load-
            balancers)
        ip: IP is set for load-balancer ingress points that are IP based (typically GCE or OpenStack load-
            balancers)
        ipMode: IPMode specifies how the load-balancer IP behaves, and may only be specified when the ip field
            is specified. Setting this to 'VIP' indicates that traffic is delivered to the node with the
            destination set to the load-balancer's IP and port. Setting this to 'Proxy' indicates that traffic
            is delivered to the node or pod with the destination set to the node's IP and node port or the
            pod's IP and port. Service implementations may use this information to adjust traffic routing.
        ports: Ports is a list of records of service ports If used, every port defined in the service should
            have an entry in it

    """

    hostname: Optional[str] = None
    ip: Optional[str] = None
    ipMode: Optional[str] = None
    ports: Optional[List[PortStatus]] = None


@dataclass
class LoadBalancerStatus(K8sSpec):
    """LoadBalancerStatus represents the status of a load-balancer.

    Attributes:
        ingress: Ingress is a list containing ingress points for the load-balancer. Traffic intended for the
            service should be sent to these ingress points.

    """

    ingress: Optional[List[LoadBalancerIngress]] = None


@dataclass
class Namespace(K8sResource):
    """Namespace provides a scope for Names. Use of multiple namespaces is optional.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object's metadata.
        spec: Spec defines the behavior of the Namespace.
        status: Status describes the current status of a Namespace.

    """

    apiVersion: Literal['v1'] = 'v1'
    kind: Literal['Namespace'] = 'Namespace'
    metadata: Optional[gybe.k8s.v1_31.meta.v1.ObjectMeta] = None
    spec: Optional[NamespaceSpec] = None
    status: Optional[NamespaceStatus] = None


@dataclass
class NamespaceCondition(K8sSpec):
    """NamespaceCondition contains details about state of namespace.

    Attributes:
        lastTransitionTime: ...
        message: ...
        reason: ...
        status: Status of the condition, one of True, False, Unknown.
        type: Type of namespace controller condition.

    """

    type: str
    status: str
    lastTransitionTime: Optional[str] = None
    message: Optional[str] = None
    reason: Optional[str] = None


@dataclass
class NamespaceList(K8sSpec):
    """NamespaceList is a list of Namespaces.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        items: Items is the list of Namespace objects in the list.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard list metadata.

    """

    items: List[Namespace]
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[JSONObj] = None


@dataclass
class NamespaceSpec(K8sSpec):
    """NamespaceSpec describes the attributes on a Namespace.

    Attributes:
        finalizers: Finalizers is an opaque list of values that must be empty to permanently remove object
            from storage.

    """

    finalizers: Optional[List[str]] = None


@dataclass
class NamespaceStatus(K8sSpec):
    """NamespaceStatus is information about the current status of a Namespace.

    Attributes:
        conditions: Represents the latest available observations of a namespace's current state.
        phase: Phase is the current lifecycle phase of the namespace.

    """

    conditions: Optional[List[NamespaceCondition]] = None
    phase: Optional[str] = None


@dataclass
class Node(K8sResource):
    """Node is a worker node in Kubernetes. Each node will have a unique identifier in the cache (i.e. in
    etcd).

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object's metadata.
        spec: Spec defines the behavior of a node. https://git.k8s.io/community/contributors/devel/sig-
            architecture/api-conventions.md#spec-and-status
        status: Most recently observed status of the node. Populated by the system. Read-only.

    """

    apiVersion: Literal['v1'] = 'v1'
    kind: Literal['Node'] = 'Node'
    metadata: Optional[gybe.k8s.v1_31.meta.v1.ObjectMeta] = None
    spec: Optional[NodeSpec] = None
    status: Optional[NodeStatus] = None


@dataclass
class NodeAddress(K8sSpec):
    """NodeAddress contains information for the node's address.

    Attributes:
        address: The node address.
        type: Node address type, one of Hostname, ExternalIP or InternalIP.

    """

    type: str
    address: str


@dataclass
class NodeCondition(K8sSpec):
    """NodeCondition contains condition information for a node.

    Attributes:
        lastHeartbeatTime: Last time we got an update on a given condition.
        lastTransitionTime: Last time the condition transit from one status to another.
        message: Human readable message indicating details about last transition.
        reason: (brief) reason for the condition's last transition.
        status: Status of the condition, one of True, False, Unknown.
        type: Type of node condition.

    """

    type: str
    status: str
    lastHeartbeatTime: Optional[str] = None
    lastTransitionTime: Optional[str] = None
    message: Optional[str] = None
    reason: Optional[str] = None


@dataclass
class NodeConfigSource(K8sSpec):
    """NodeConfigSource specifies a source of node configuration. Exactly one subfield (excluding metadata)
    must be non-nil. This API is deprecated since 1.22
    Attributes:
        configMap: ConfigMap is a reference to a Node's ConfigMap

    """

    configMap: Optional[ConfigMapNodeConfigSource] = None


@dataclass
class NodeConfigStatus(K8sSpec):
    """NodeConfigStatus describes the status of the config assigned by Node.Spec.ConfigSource.

    Attributes:
        active: Active reports the checkpointed config the node is actively using. Active will represent
            either the current version of the Assigned config, or the current LastKnownGood config, depending
            on whether attempting to use the Assigned config results in an error.
        assigned: Assigned reports the checkpointed config the node will try to use. When
            Node.Spec.ConfigSource is updated, the node checkpoints the associated config payload to local
            disk, along with a record indicating intended config. The node refers to this record to choose its
            config checkpoint, and reports this record in Assigned. Assigned only updates in the status after
            the record has been checkpointed to disk. When the Kubelet is restarted, it tries to make the
            Assigned config the Active config by loading and validating the checkpointed payload identified by
            Assigned.
        error: Error describes any problems reconciling the Spec.ConfigSource to the Active config. Errors may
            occur, for example, attempting to checkpoint Spec.ConfigSource to the local Assigned record,
            attempting to checkpoint the payload associated with Spec.ConfigSource, attempting to load or
            validate the Assigned config, etc. Errors may occur at different points while syncing config.
            Earlier errors (e.g. download or checkpointing errors) will not result in a rollback to
            LastKnownGood, and may resolve across Kubelet retries. Later errors (e.g. loading or validating a
            checkpointed config) will result in a rollback to LastKnownGood. In the latter case, it is usually
            possible to resolve the error by fixing the config assigned in Spec.ConfigSource. You can find
            additional information for debugging by searching the error message in the Kubelet log. Error is a
            human-readable description of the error state; machines can check whether or not Error is empty,
            but should not rely on the stability of the Error text across Kubelet versions.
        lastKnownGood: LastKnownGood reports the checkpointed config the node will fall back to when it
            encounters an error attempting to use the Assigned config. The Assigned config becomes the
            LastKnownGood config when the node determines that the Assigned config is stable and correct. This
            is currently implemented as a 10-minute soak period starting when the local record of Assigned
            config is updated. If the Assigned config is Active at the end of this period, it becomes the
            LastKnownGood. Note that if Spec.ConfigSource is reset to nil (use local defaults), the
            LastKnownGood is also immediately reset to nil, because the local default config is always assumed
            good. You should not make assumptions about the node's method of determining config stability and
            correctness, as this may change or become configurable in the future.

    """

    active: Optional[NodeConfigSource] = None
    assigned: Optional[NodeConfigSource] = None
    error: Optional[str] = None
    lastKnownGood: Optional[NodeConfigSource] = None


@dataclass
class NodeDaemonEndpoints(K8sSpec):
    """NodeDaemonEndpoints lists ports opened by daemons running on the Node.

    Attributes:
        kubeletEndpoint: Endpoint on which Kubelet is listening.

    """

    kubeletEndpoint: Optional[DaemonEndpoint] = None


@dataclass
class NodeFeatures(K8sSpec):
    """NodeFeatures describes the set of features implemented by the CRI implementation. The features
    contained in the NodeFeatures should depend only on the cri implementation independent of runtime
    handlers.

    Attributes:
        supplementalGroupsPolicy: SupplementalGroupsPolicy is set to true if the runtime supports
            SupplementalGroupsPolicy and ContainerUser.

    """

    supplementalGroupsPolicy: Optional[bool] = None


@dataclass
class NodeList(K8sSpec):
    """NodeList is the whole list of all Nodes which have been registered with master.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        items: List of nodes
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard list metadata.

    """

    items: List[Node]
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[JSONObj] = None


@dataclass
class NodeRuntimeHandler(K8sSpec):
    """NodeRuntimeHandler is a set of runtime handler information.

    Attributes:
        features: Supported features.
        name: Runtime handler name. Empty for the default runtime handler.

    """

    features: Optional[NodeRuntimeHandlerFeatures] = None
    name: Optional[str] = None


@dataclass
class NodeRuntimeHandlerFeatures(K8sSpec):
    """NodeRuntimeHandlerFeatures is a set of features implemented by the runtime handler.

    Attributes:
        recursiveReadOnlyMounts: RecursiveReadOnlyMounts is set to true if the runtime handler supports
            RecursiveReadOnlyMounts.
        userNamespaces: UserNamespaces is set to true if the runtime handler supports UserNamespaces,
            including for volumes.

    """

    recursiveReadOnlyMounts: Optional[bool] = None
    userNamespaces: Optional[bool] = None


@dataclass
class NodeSpec(K8sSpec):
    """NodeSpec describes the attributes that a node is created with.

    Attributes:
        configSource: Deprecated: Previously used to specify the source of the node's configuration for the
            DynamicKubeletConfig feature. This feature is removed.
        externalID: Deprecated. Not all kubelets will set this field. Remove field after 1.13. see:
            https://issues.k8s.io/61966
        podCIDR: PodCIDR represents the pod IP range assigned to the node.
        podCIDRs: podCIDRs represents the IP ranges assigned to the node for usage by Pods on that node. If
            this field is specified, the 0th entry must match the podCIDR field. It may contain at most 1
            value for each of IPv4 and IPv6.
        providerID: ID of the node assigned by the cloud provider in the format:
            <ProviderName>://<ProviderSpecificNodeID>
        taints: If specified, the node's taints.
        unschedulable: Unschedulable controls node schedulability of new pods. By default, node is
            schedulable.

    """

    configSource: Optional[NodeConfigSource] = None
    externalID: Optional[str] = None
    podCIDR: Optional[str] = None
    podCIDRs: Optional[List[str]] = None
    providerID: Optional[str] = None
    taints: Optional[List[Taint]] = None
    unschedulable: Optional[bool] = None


@dataclass
class NodeStatus(K8sSpec):
    """NodeStatus is information about the current status of a node.

    Attributes:
        addresses: List of addresses reachable to the node. Queried from cloud provider, if available.
        allocatable: Allocatable represents the resources of a node that are available for scheduling.
            Defaults to Capacity.
        capacity: Capacity represents the total resources of a node.
        conditions: Conditions is an array of current observed node conditions.
        config: Status of the config assigned to the node via the dynamic Kubelet config feature.
        daemonEndpoints: Endpoints of daemons running on the Node.
        features: Features describes the set of features implemented by the CRI implementation.
        images: List of container images on this node
        nodeInfo: Set of ids/uuids to uniquely identify the node.
        phase: NodePhase is the recently observed lifecycle phase of the node.
        runtimeHandlers: The available runtime handlers.
        volumesAttached: List of volumes that are attached to the node.
        volumesInUse: List of attachable volumes in use (mounted) by the node.

    """

    addresses: Optional[List[NodeAddress]] = None
    allocatable: Optional[JSONDict] = None
    capacity: Optional[JSONDict] = None
    conditions: Optional[List[NodeCondition]] = None
    config: Optional[NodeConfigStatus] = None
    daemonEndpoints: Optional[NodeDaemonEndpoints] = None
    features: Optional[NodeFeatures] = None
    images: Optional[List[ContainerImage]] = None
    nodeInfo: Optional[NodeSystemInfo] = None
    phase: Optional[str] = None
    runtimeHandlers: Optional[List[NodeRuntimeHandler]] = None
    volumesAttached: Optional[List[AttachedVolume]] = None
    volumesInUse: Optional[List[str]] = None


@dataclass
class NodeSystemInfo(K8sSpec):
    """NodeSystemInfo is a set of ids/uuids to uniquely identify the node.

    Attributes:
        architecture: The Architecture reported by the node
        bootID: Boot ID reported by the node.
        containerRuntimeVersion: ContainerRuntime Version reported by the node through runtime remote API
            (e.g. containerd://1.4.2).
        kernelVersion: Kernel Version reported by the node from 'uname -r' (e.g. 3.16.0-0.bpo.4-amd64).
        kubeProxyVersion: Deprecated: KubeProxy Version reported by the node.
        kubeletVersion: Kubelet Version reported by the node.
        machineID: MachineID reported by the node. For unique machine identification in the cluster this field
            is preferred. Learn more from man(5) machine-id: http://man7.org/linux/man-pages/man5/machine-
            id.5.html
        operatingSystem: The Operating System reported by the node
        osImage: OS Image reported by the node from /etc/os-release (e.g. Debian GNU/Linux 7 (wheezy)).
        systemUUID: SystemUUID reported by the node. For unique machine identification MachineID is preferred.
            This field is specific to Red Hat hosts https://access.redhat.com/documentation/en-
            us/red_hat_subscription_management/1/html/rhsm/uuid

    """

    machineID: str
    systemUUID: str
    bootID: str
    kernelVersion: str
    osImage: str
    containerRuntimeVersion: str
    kubeletVersion: str
    kubeProxyVersion: str
    operatingSystem: str
    architecture: str


@dataclass
class PersistentVolume(K8sResource):
    """PersistentVolume (PV) is a storage resource provisioned by an administrator. It is analogous to a
    node. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes
    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object's metadata.
        spec: spec defines a specification of a persistent volume owned by the cluster. Provisioned by an
            administrator.
        status: status represents the current information/status for the persistent volume. Populated by the
            system. Read-only.

    """

    apiVersion: Literal['v1'] = 'v1'
    kind: Literal['PersistentVolume'] = 'PersistentVolume'
    metadata: Optional[gybe.k8s.v1_31.meta.v1.ObjectMeta] = None
    spec: Optional[PersistentVolumeSpec] = None
    status: Optional[PersistentVolumeStatus] = None


@dataclass
class PersistentVolumeClaimList(K8sSpec):
    """PersistentVolumeClaimList is a list of PersistentVolumeClaim items.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        items: items is a list of persistent volume claims.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard list metadata.

    """

    items: List[PersistentVolumeClaim]
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[JSONObj] = None


@dataclass
class PersistentVolumeList(K8sSpec):
    """PersistentVolumeList is a list of PersistentVolume items.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        items: items is a list of persistent volumes.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard list metadata.

    """

    items: List[PersistentVolume]
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[JSONObj] = None


@dataclass
class PersistentVolumeStatus(K8sSpec):
    """PersistentVolumeStatus is the current status of a persistent volume.

    Attributes:
        lastPhaseTransitionTime: lastPhaseTransitionTime is the time the phase transitioned from one to
            another and automatically resets to current time everytime a volume phase transitions.
        message: message is a human-readable message indicating details about why the volume is in this state.
        phase: phase indicates if a volume is available, bound to a claim, or released by a claim.
        reason: reason is a brief CamelCase string that describes any failure and is meant for machine parsing
            and tidy display in the CLI.

    """

    lastPhaseTransitionTime: Optional[str] = None
    message: Optional[str] = None
    phase: Optional[str] = None
    reason: Optional[str] = None


@dataclass
class Pod(K8sResource):
    """Pod is a collection of containers that can run on a host. This resource is created by clients and
    scheduled onto hosts.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object's metadata.
        spec: Specification of the desired behavior of the pod.
        status: Most recently observed status of the pod. This data may not be up to date. Populated by the
            system. Read-only.

    """

    apiVersion: Literal['v1'] = 'v1'
    kind: Literal['Pod'] = 'Pod'
    metadata: Optional[gybe.k8s.v1_31.meta.v1.ObjectMeta] = None
    spec: Optional[PodSpec] = None
    status: Optional[PodStatus] = None


@dataclass
class PodCondition(K8sSpec):
    """PodCondition contains details for the current condition of this pod.

    Attributes:
        lastProbeTime: Last time we probed the condition.
        lastTransitionTime: Last time the condition transitioned from one status to another.
        message: Human-readable message indicating details about last transition.
        reason: Unique, one-word, CamelCase reason for the condition's last transition.
        status: Status is the status of the condition. Can be True, False, Unknown.
        type: Type is the type of the condition.

    """

    type: str
    status: str
    lastProbeTime: Optional[str] = None
    lastTransitionTime: Optional[str] = None
    message: Optional[str] = None
    reason: Optional[str] = None


@dataclass
class PodIP(K8sSpec):
    """PodIP represents a single IP address allocated to the pod.

    Attributes:
        ip: IP is the IP address assigned to the pod

    """

    ip: str


@dataclass
class PodList(K8sSpec):
    """PodList is a list of Pods.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        items: List of pods.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard list metadata.

    """

    items: List[Pod]
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[JSONObj] = None


@dataclass
class PodResourceClaimStatus(K8sSpec):
    """PodResourceClaimStatus is stored in the PodStatus for each PodResourceClaim which references a
    ResourceClaimTemplate. It stores the generated name for the corresponding ResourceClaim.

    Attributes:
        name: Name uniquely identifies this resource claim inside the pod. This must match the name of an
            entry in pod.spec.resourceClaims, which implies that the string must be a DNS_LABEL.
        resourceClaimName: ResourceClaimName is the name of the ResourceClaim that was generated for the Pod
            in the namespace of the Pod. If this is unset, then generating a ResourceClaim was not necessary.
            The pod.spec.resourceClaims entry can be ignored in this case.

    """

    name: str
    resourceClaimName: Optional[str] = None


@dataclass
class PodStatus(K8sSpec):
    """PodStatus represents information about the status of a pod. Status may trail the actual state of a
    system, especially if the node that hosts the pod cannot contact the control plane.

    Attributes:
        conditions: Current service state of pod.
        containerStatuses: The list has one entry per container in the manifest.
        ephemeralContainerStatuses: Status for any ephemeral containers that have run in this pod.
        hostIP: hostIP holds the IP address of the host to which the pod is assigned. Empty if the pod has not
            started yet. A pod can be assigned to a node that has a problem in kubelet which in turns mean
            that HostIP will not be updated even if there is a node is assigned to pod
        hostIPs: hostIPs holds the IP addresses allocated to the host. If this field is specified, the first
            entry must match the hostIP field. This list is empty if the pod has not started yet. A pod can be
            assigned to a node that has a problem in kubelet which in turns means that HostIPs will not be
            updated even if there is a node is assigned to this pod.
        initContainerStatuses: The list has one entry per init container in the manifest. The most recent
            successful init container will have ready = true, the most recently started container will have
            startTime set.
        message: A human readable message indicating details about why the pod is in this condition.
        nominatedNodeName: nominatedNodeName is set only when this pod preempts other pods on the node, but it
            cannot be scheduled right away as preemption victims receive their graceful termination periods.
            This field does not guarantee that the pod will be scheduled on this node. Scheduler may decide to
            place the pod elsewhere if other nodes become available sooner. Scheduler may also decide to give
            the resources on this node to a higher priority pod that is created after preemption. As a result,
            this field may be different than PodSpec.nodeName when the pod is scheduled.
        phase: The phase of a Pod is a simple, high-level summary of where the Pod is in its lifecycle. The
            conditions array, the reason and message fields, and the individual container status arrays
            contain more detail about the pod's status. There are five possible phase values:  Pending: The
            pod has been accepted by the Kubernetes system, but one or more of the container images has not
            been created. This includes time before being scheduled as well as time spent downloading images
            over the network, which could take a while. Running: The pod has been bound to a node, and all of
            the containers have been created. At least one container is still running, or is in the process of
            starting or restarting. Succeeded: All containers in the pod have terminated in success, and will
            not be restarted. Failed: All containers in the pod have terminated, and at least one container
            has terminated in failure. The container either exited with non-zero status or was terminated by
            the system. Unknown: For some reason the state of the pod could not be obtained, typically due to
            an error in communicating with the host of the pod.
        podIP: podIP address allocated to the pod. Routable at least within the cluster. Empty if not yet
            allocated.
        podIPs: podIPs holds the IP addresses allocated to the pod. If this field is specified, the 0th entry
            must match the podIP field. Pods may be allocated at most 1 value for each of IPv4 and IPv6. This
            list is empty if no IPs have been allocated yet.
        qosClass: The Quality of Service (QOS) classification assigned to the pod based on resource
            requirements See PodQOSClass type for available QOS classes
        reason: A brief CamelCase message indicating details about why the pod is in this state. e.g.
            'Evicted'
        resize: Status of resources resize desired for pod's containers. It is empty if no resources resize is
            pending. Any changes to container resources will automatically set this to 'Proposed'
        resourceClaimStatuses: Status of resource claims.
        startTime: RFC 3339 date and time at which the object was acknowledged by the Kubelet. This is before
            the Kubelet pulled the container image(s) for the pod.

    """

    conditions: Optional[List[PodCondition]] = None
    containerStatuses: Optional[List[ContainerStatus]] = None
    ephemeralContainerStatuses: Optional[List[ContainerStatus]] = None
    hostIP: Optional[str] = None
    hostIPs: Optional[List[HostIP]] = None
    initContainerStatuses: Optional[List[ContainerStatus]] = None
    message: Optional[str] = None
    nominatedNodeName: Optional[str] = None
    phase: Optional[str] = None
    podIP: Optional[str] = None
    podIPs: Optional[List[PodIP]] = None
    qosClass: Optional[str] = None
    reason: Optional[str] = None
    resize: Optional[str] = None
    resourceClaimStatuses: Optional[List[PodResourceClaimStatus]] = None
    startTime: Optional[str] = None


@dataclass
class PodTemplate(K8sSpec):
    """PodTemplate describes a template for creating copies of a predefined pod.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object's metadata.
        template: Template defines the pods that will be created from this pod template.
            https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-
            status

    """

    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[gybe.k8s.v1_31.meta.v1.ObjectMeta] = None
    template: Optional[PodTemplateSpec] = None


@dataclass
class PodTemplateList(K8sSpec):
    """PodTemplateList is a list of PodTemplates.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        items: List of pod templates
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard list metadata.

    """

    items: List[PodTemplate]
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[JSONObj] = None


@dataclass
class PortStatus(K8sSpec):
    """Schema model io.k8s.api.core.v1.PortStatus.

    Attributes:
        error: Error is to record the problem with the service port The format of the error shall comply with
            the following rules: - built-in error values shall be specified in this file and those shall use
            CamelCase names - cloud provider specific error values must have names that comply with the
            format foo.example.com/CamelCase.
        port: Port is the port number of the service port of which status is recorded here
        protocol: Protocol is the protocol of the service port of which status is recorded here The supported
            values are: 'TCP', 'UDP', 'SCTP'

    """

    port: int
    protocol: str
    error: Optional[str] = None


@dataclass
class ReplicationController(K8sResource):
    """ReplicationController represents the configuration of a replication controller.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: If the Labels of a ReplicationController are empty, they are defaulted to be the same as the
            Pod(s) that the replication controller manages. Standard object's metadata.
        spec: Spec defines the specification of the desired behavior of the replication controller.
        status: Status is the most recently observed status of the replication controller. This data may be
            out of date by some window of time. Populated by the system. Read-only.

    """

    apiVersion: Literal['v1'] = 'v1'
    kind: Literal['ReplicationController'] = 'ReplicationController'
    metadata: Optional[gybe.k8s.v1_31.meta.v1.ObjectMeta] = None
    spec: Optional[ReplicationControllerSpec] = None
    status: Optional[ReplicationControllerStatus] = None


@dataclass
class ReplicationControllerCondition(K8sSpec):
    """ReplicationControllerCondition describes the state of a replication controller at a certain point.

    Attributes:
        lastTransitionTime: The last time the condition transitioned from one status to another.
        message: A human readable message indicating details about the transition.
        reason: The reason for the condition's last transition.
        status: Status of the condition, one of True, False, Unknown.
        type: Type of replication controller condition.

    """

    type: str
    status: str
    lastTransitionTime: Optional[str] = None
    message: Optional[str] = None
    reason: Optional[str] = None


@dataclass
class ReplicationControllerList(K8sSpec):
    """ReplicationControllerList is a collection of replication controllers.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        items: List of replication controllers.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard list metadata.

    """

    items: List[ReplicationController]
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[JSONObj] = None


@dataclass
class ReplicationControllerSpec(K8sSpec):
    """ReplicationControllerSpec is the specification of a replication controller.

    Attributes:
        minReadySeconds: Minimum number of seconds for which a newly created pod should be ready without any
            of its container crashing, for it to be considered available. Defaults to 0 (pod will be
            considered available as soon as it is ready)
        replicas: Replicas is the number of desired replicas. This is a pointer to distinguish between
            explicit zero and unspecified. Defaults to 1.
        selector: Selector is a label query over pods that should match the Replicas count. If Selector is
            empty, it is defaulted to the labels present on the Pod template. Label keys and values that must
            match in order to be controlled by this replication controller, if empty defaulted to labels on
            Pod template.
        template: Template is the object that describes the pod that will be created if insufficient replicas
            are detected. This takes precedence over a TemplateRef. The only allowed
            template.spec.restartPolicy value is 'Always'.

    """

    minReadySeconds: Optional[int] = None
    replicas: Optional[int] = None
    selector: Optional[JSONDict] = None
    template: Optional[PodTemplateSpec] = None


@dataclass
class ReplicationControllerStatus(K8sSpec):
    """ReplicationControllerStatus represents the current status of a replication controller.

    Attributes:
        availableReplicas: The number of available replicas (ready for at least minReadySeconds) for this
            replication controller.
        conditions: Represents the latest available observations of a replication controller's current state.
        fullyLabeledReplicas: The number of pods that have labels matching the labels of the pod template of
            the replication controller.
        observedGeneration: ObservedGeneration reflects the generation of the most recently observed
            replication controller.
        readyReplicas: The number of ready replicas for this replication controller.
        replicas: Replicas is the most recently observed number of replicas.

    """

    replicas: int
    availableReplicas: Optional[int] = None
    conditions: Optional[List[ReplicationControllerCondition]] = None
    fullyLabeledReplicas: Optional[int] = None
    observedGeneration: Optional[int] = None
    readyReplicas: Optional[int] = None


@dataclass
class ResourceHealth(K8sSpec):
    """ResourceHealth represents the health of a resource. It has the latest device health information. This
    is a part of KEP https://kep.k8s.io/4680 and historical health changes are planned to be added in
    future iterations of a KEP.

    Attributes:
        health: Health of the resource. can be one of:  - Healthy: operates as normal  - Unhealthy: reported
            unhealthy. We consider this a temporary health issue               since we do not have a
            mechanism today to distinguish               temporary and permanent issues.  - Unknown: The
            status cannot be determined.             For example, Device Plugin got unregistered and hasn't
            been re-registered since.  In future we may want to introduce the PermanentlyUnhealthy Status.
        resourceID: ResourceID is the unique identifier of the resource. See the ResourceID type for more
            information.

    """

    resourceID: str
    health: Optional[str] = None


@dataclass
class ResourceQuota(K8sResource):
    """ResourceQuota sets aggregate quota restrictions enforced per namespace
    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object's metadata.
        spec: Spec defines the desired quota. https://git.k8s.io/community/contributors/devel/sig-
            architecture/api-conventions.md#spec-and-status
        status: Status defines the actual enforced quota and its current usage.
            https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-
            status

    """

    apiVersion: Literal['v1'] = 'v1'
    kind: Literal['ResourceQuota'] = 'ResourceQuota'
    metadata: Optional[gybe.k8s.v1_31.meta.v1.ObjectMeta] = None
    spec: Optional[ResourceQuotaSpec] = None
    status: Optional[ResourceQuotaStatus] = None


@dataclass
class ResourceQuotaList(K8sSpec):
    """ResourceQuotaList is a list of ResourceQuota items.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        items: Items is a list of ResourceQuota objects.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard list metadata.

    """

    items: List[ResourceQuota]
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[JSONObj] = None


@dataclass
class ResourceQuotaSpec(K8sSpec):
    """ResourceQuotaSpec defines the desired hard limits to enforce for Quota.

    Attributes:
        hard: hard is the set of desired hard limits for each named resource.
        scopeSelector: scopeSelector is also a collection of filters like scopes that must match each object
            tracked by a quota but expressed using ScopeSelectorOperator in combination with possible values.
            For a resource to match, both scopes AND scopeSelector (if specified in spec), must be matched.
        scopes: A collection of filters that must match each object tracked by a quota. If not specified, the
            quota matches all objects.

    """

    hard: Optional[JSONDict] = None
    scopeSelector: Optional[ScopeSelector] = None
    scopes: Optional[List[str]] = None


@dataclass
class ResourceQuotaStatus(K8sSpec):
    """ResourceQuotaStatus defines the enforced hard limits and observed use.

    Attributes:
        hard: Hard is the set of enforced hard limits for each named resource.
        used: Used is the current observed total usage of the resource in the namespace.

    """

    hard: Optional[JSONDict] = None
    used: Optional[JSONDict] = None


@dataclass
class ResourceStatus(K8sSpec):
    """Schema model io.k8s.api.core.v1.ResourceStatus.

    Attributes:
        name: Name of the resource. Must be unique within the pod and match one of the resources from the pod
            spec.
        resources: List of unique Resources health. Each element in the list contains an unique resource ID
            and resource health. At a minimum, ResourceID must uniquely identify the Resource allocated to the
            Pod on the Node for the lifetime of a Pod. See ResourceID type for it's definition.

    """

    name: str
    resources: Optional[List[ResourceHealth]] = None


@dataclass
class ScopeSelector(K8sSpec):
    """A scope selector represents the AND of the selectors represented by the scoped-resource selector
    requirements.

    Attributes:
        matchExpressions: A list of scope selector requirements by scope of the resources.

    """

    matchExpressions: Optional[List[ScopedResourceSelectorRequirement]] = None


@dataclass
class ScopedResourceSelectorRequirement(K8sSpec):
    """A scoped-resource selector requirement is a selector that contains values, a scope name, and an
    operator that relates the scope name and values.

    Attributes:
        operator: Represents a scope's relationship to a set of values. Valid operators are In, NotIn, Exists,
            DoesNotExist.
        scopeName: The name of the scope that the selector applies to.
        values: An array of string values. If the operator is In or NotIn, the values array must be non-empty.
            If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced
            during a strategic merge patch.

    """

    scopeName: str
    operator: str
    values: Optional[List[str]] = None


@dataclass
class Secret(K8sSpec):
    """Secret holds secret data of a certain type. The total bytes of the values in the Data field must be
    less than MaxSecretSize bytes.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        data: Data contains the secret data. Each key must consist of alphanumeric characters, '-', '_' or
            '.'. The serialized form of the secret data is a base64 encoded string, representing the arbitrary
            (possibly non-string) data value here. Described in https://tools.ietf.org/html/rfc4648#section-4
        immutable: Immutable, if set to true, ensures that data stored in the Secret cannot be updated (only
            object metadata can be modified). If not set to true, the field can be modified at any time.
            Defaulted to nil.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object's metadata.
        stringData: stringData allows specifying non-binary secret data in string form. It is provided as a
            write-only input field for convenience. All keys and values are merged into the data field on
            write, overwriting any existing values. The stringData field is never output when reading from the
            API.
        type: Used to facilitate programmatic handling of secret data.

    """

    apiVersion: Optional[str] = None
    data: Optional[JSONDict] = None
    immutable: Optional[bool] = None
    kind: Optional[str] = None
    metadata: Optional[gybe.k8s.v1_31.meta.v1.ObjectMeta] = None
    stringData: Optional[JSONDict] = None
    type: Optional[str] = None


@dataclass
class SecretList(K8sSpec):
    """SecretList is a list of Secret.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        items: Items is a list of secret objects.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard list metadata.

    """

    items: List[Secret]
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[JSONObj] = None


@dataclass
class Service(K8sResource):
    """Service is a named abstraction of software service (for example, mysql) consisting of local port (for
    example 3306) that the proxy listens on, and the selector that determines which pods will answer
    requests sent through the proxy.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object's metadata.
        spec: Spec defines the behavior of a service. https://git.k8s.io/community/contributors/devel/sig-
            architecture/api-conventions.md#spec-and-status
        status: Most recently observed status of the service. Populated by the system. Read-only.

    """

    apiVersion: Literal['v1'] = 'v1'
    kind: Literal['Service'] = 'Service'
    metadata: Optional[gybe.k8s.v1_31.meta.v1.ObjectMeta] = None
    spec: Optional[ServiceSpec] = None
    status: Optional[ServiceStatus] = None


@dataclass
class ServiceAccount(K8sSpec):
    """ServiceAccount binds together: * a name, understood by users, and perhaps by peripheral systems, for
    an identity * a principal that can be authenticated and authorized * a set of secrets
    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        automountServiceAccountToken: AutomountServiceAccountToken indicates whether pods running as this
            service account should have an API token automatically mounted. Can be overridden at the pod
            level.
        imagePullSecrets: ImagePullSecrets is a list of references to secrets in the same namespace to use for
            pulling any images in pods that reference this ServiceAccount. ImagePullSecrets are distinct from
            Secrets because Secrets can be mounted in the pod, but ImagePullSecrets are only accessed by the
            kubelet.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object's metadata.
        secrets: Secrets is a list of the secrets in the same namespace that pods running using this
            ServiceAccount are allowed to use. Pods are only limited to this list if this service account has
            a 'kubernetes.io/enforce-mountable-secrets' annotation set to 'true'. This field should not be
            used to find auto-generated service account token secrets for use outside of pods. Instead, tokens
            can be requested directly using the TokenRequest API, or service account token secrets can be
            manually created.

    """

    apiVersion: Optional[str] = None
    automountServiceAccountToken: Optional[bool] = None
    imagePullSecrets: Optional[List[LocalObjectReference]] = None
    kind: Optional[str] = None
    metadata: Optional[gybe.k8s.v1_31.meta.v1.ObjectMeta] = None
    secrets: Optional[List[ObjectReference]] = None


@dataclass
class ServiceAccountList(K8sSpec):
    """ServiceAccountList is a list of ServiceAccount objects
    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        items: List of ServiceAccounts.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard list metadata.

    """

    items: List[ServiceAccount]
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[JSONObj] = None


@dataclass
class ServiceList(K8sSpec):
    """ServiceList holds a list of services.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        items: List of services
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard list metadata.

    """

    items: List[Service]
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[JSONObj] = None


@dataclass
class ServicePort(K8sSpec):
    """ServicePort contains information on service's port.

    Attributes:
        appProtocol: The application protocol for this port. This is used as a hint for implementations to
            offer richer behavior for protocols that they understand. This field follows standard Kubernetes
            label syntax. Valid values are either:  * Un-prefixed protocol names - reserved for IANA standard
            service names (as per RFC-6335 and https://www.iana.org/assignments/service-names).  * Kubernetes-
            defined prefixed names:   * 'kubernetes.io/h2c' - HTTP/2 prior knowledge over cleartext as
            described in https://www.rfc-editor.org/rfc/rfc9113.html#name-starting-http-2-with-prior-   *
            'kubernetes.io/ws'  - WebSocket over cleartext as described in https://www.rfc-
            editor.org/rfc/rfc6455   * 'kubernetes.io/wss' - WebSocket over TLS as described in
            https://www.rfc-editor.org/rfc/rfc6455  * Other protocols should use implementation-defined
            prefixed names such as mycompany.com/my-custom-protocol.
        name: The name of this port within the service. This must be a DNS_LABEL. All ports within a
            ServiceSpec must have unique names. When considering the endpoints for a Service, this must match
            the 'name' field in the EndpointPort. Optional if only one ServicePort is defined on this service.
        nodePort: The port on each node on which this service is exposed when type is NodePort or
            LoadBalancer.  Usually assigned by the system. If a value is specified, in-range, and not in use
            it will be used, otherwise the operation will fail.  If not specified, a port will be allocated if
            this Service requires one.  If this field is specified when creating a Service which does not need
            it, creation will fail. This field will be wiped when updating a Service to no longer need it
            (e.g. changing type from NodePort to ClusterIP).
        port: The port that will be exposed by this service.
        protocol: The IP protocol for this port. Supports 'TCP', 'UDP', and 'SCTP'. Default is TCP.
        targetPort: Number or name of the port to access on the pods targeted by the service. Number must be
            in the range 1 to 65535. Name must be an IANA_SVC_NAME. If this is a string, it will be looked up
            as a named port in the target Pod's container ports. If this is not specified, the value of the
            'port' field is used (an identity map). This field is ignored for services with clusterIP=None,
            and should be omitted or set equal to the 'port' field.

    """

    port: int
    appProtocol: Optional[str] = None
    name: Optional[str] = None
    nodePort: Optional[int] = None
    protocol: Optional[str] = None
    targetPort: Optional[str] = None


@dataclass
class ServiceSpec(K8sSpec):
    """ServiceSpec describes the attributes that a user creates on a service.

    Attributes:
        allocateLoadBalancerNodePorts: allocateLoadBalancerNodePorts defines if NodePorts will be
            automatically allocated for services with type LoadBalancer.  Default is 'true'. It may be set to
            'false' if the cluster load-balancer does not rely on NodePorts.  If the caller requests specific
            NodePorts (by specifying a value), those requests will be respected, regardless of this field.
            This field may only be set for services with type LoadBalancer and will be cleared if the type is
            changed to any other type.
        clusterIP: clusterIP is the IP address of the service and is usually assigned randomly. If an address
            is specified manually, is in-range (as per system configuration), and is not in use, it will be
            allocated to the service; otherwise creation of the service will fail. This field may not be
            changed through updates unless the type field is also being changed to ExternalName (which
            requires this field to be blank) or the type field is being changed from ExternalName (in which
            case this field may optionally be specified, as describe above).  Valid values are 'None', empty
            string (''), or a valid IP address. Setting this to 'None' makes a 'headless service' (no virtual
            IP), which is useful when direct endpoint connections are preferred and proxying is not required.
            Only applies to types ClusterIP, NodePort, and LoadBalancer. If this field is specified when
            creating a Service of type ExternalName, creation will fail. This field will be wiped when
            updating a Service to type ExternalName.
        clusterIPs: ClusterIPs is a list of IP addresses assigned to this service, and are usually assigned
            randomly.  If an address is specified manually, is in-range (as per system configuration), and is
            not in use, it will be allocated to the service; otherwise creation of the service will fail. This
            field may not be changed through updates unless the type field is also being changed to
            ExternalName (which requires this field to be empty) or the type field is being changed from
            ExternalName (in which case this field may optionally be specified, as describe above).  Valid
            values are 'None', empty string (''), or a valid IP address.  Setting this to 'None' makes a
            'headless service' (no virtual IP), which is useful when direct endpoint connections are preferred
            and proxying is not required.  Only applies to types ClusterIP, NodePort, and LoadBalancer. If
            this field is specified when creating a Service of type ExternalName, creation will fail. This
            field will be wiped when updating a Service to type ExternalName.  If this field is not specified,
            it will be initialized from the clusterIP field.  If this field is specified, clients must ensure
            that clusterIPs[0] and clusterIP have the same value.  This field may hold a maximum of two
            entries (dual-stack IPs, in either order). These IPs must correspond to the values of the
            ipFamilies field. Both clusterIPs and ipFamilies are governed by the ipFamilyPolicy field.
        externalIPs: externalIPs is a list of IP addresses for which nodes in the cluster will also accept
            traffic for this service.  These IPs are not managed by Kubernetes.  The user is responsible for
            ensuring that traffic arrives at a node with this IP.  A common example is external load-balancers
            that are not part of the Kubernetes system.
        externalName: externalName is the external reference that discovery mechanisms will return as an alias
            for this service (e.g. a DNS CNAME record). No proxying will be involved.  Must be a lowercase
            RFC-1123 hostname (https://tools.ietf.org/html/rfc1123) and requires `type` to be 'ExternalName'.
        externalTrafficPolicy: externalTrafficPolicy describes how nodes distribute service traffic they
            receive on one of the Service's 'externally-facing' addresses (NodePorts, ExternalIPs, and
            LoadBalancer IPs). If set to 'Local', the proxy will configure the service in a way that assumes
            that external load balancers will take care of balancing the service traffic between nodes, and so
            each node will deliver traffic only to the node-local endpoints of the service, without
            masquerading the client source IP. (Traffic mistakenly sent to a node with no endpoints will be
            dropped.) The default value, 'Cluster', uses the standard behavior of routing to all endpoints
            evenly (possibly modified by topology and other features). Note that traffic sent to an External
            IP or LoadBalancer IP from within the cluster will always get 'Cluster' semantics, but clients
            sending to a NodePort from within the cluster may need to take traffic policy into account when
            picking a node.
        healthCheckNodePort: healthCheckNodePort specifies the healthcheck nodePort for the service. This only
            applies when type is set to LoadBalancer and externalTrafficPolicy is set to Local. If a value is
            specified, is in-range, and is not in use, it will be used.  If not specified, a value will be
            automatically allocated.  External systems (e.g. load-balancers) can use this port to determine if
            a given node holds endpoints for this service or not.  If this field is specified when creating a
            Service which does not need it, creation will fail. This field will be wiped when updating a
            Service to no longer need it (e.g. changing type). This field cannot be updated once set.
        internalTrafficPolicy: InternalTrafficPolicy describes how nodes distribute service traffic they
            receive on the ClusterIP. If set to 'Local', the proxy will assume that pods only want to talk to
            endpoints of the service on the same node as the pod, dropping the traffic if there are no local
            endpoints. The default value, 'Cluster', uses the standard behavior of routing to all endpoints
            evenly (possibly modified by topology and other features).
        ipFamilies: IPFamilies is a list of IP families (e.g. IPv4, IPv6) assigned to this service. This field
            is usually assigned automatically based on cluster configuration and the ipFamilyPolicy field. If
            this field is specified manually, the requested family is available in the cluster, and
            ipFamilyPolicy allows it, it will be used; otherwise creation of the service will fail. This field
            is conditionally mutable: it allows for adding or removing a secondary IP family, but it does not
            allow changing the primary IP family of the Service. Valid values are 'IPv4' and 'IPv6'.  This
            field only applies to Services of types ClusterIP, NodePort, and LoadBalancer, and does apply to
            'headless' services. This field will be wiped when updating a Service to type ExternalName.  This
            field may hold a maximum of two entries (dual-stack families, in either order).  These families
            must correspond to the values of the clusterIPs field, if specified. Both clusterIPs and
            ipFamilies are governed by the ipFamilyPolicy field.
        ipFamilyPolicy: IPFamilyPolicy represents the dual-stack-ness requested or required by this Service.
            If there is no value provided, then this field will be set to SingleStack. Services can be
            'SingleStack' (a single IP family), 'PreferDualStack' (two IP families on dual-stack configured
            clusters or a single IP family on single-stack clusters), or 'RequireDualStack' (two IP families
            on dual-stack configured clusters, otherwise fail). The ipFamilies and clusterIPs fields depend on
            the value of this field. This field will be wiped when updating a service to type ExternalName.
        loadBalancerClass: loadBalancerClass is the class of the load balancer implementation this Service
            belongs to. If specified, the value of this field must be a label-style identifier, with an
            optional prefix, e.g. 'internal-vip' or 'example.com/internal-vip'. Unprefixed names are reserved
            for end-users. This field can only be set when the Service type is 'LoadBalancer'. If not set, the
            default load balancer implementation is used, today this is typically done through the cloud
            provider integration, but should apply for any default implementation. If set, it is assumed that
            a load balancer implementation is watching for Services with a matching class. Any default load
            balancer implementation (e.g. cloud providers) should ignore Services that set this field. This
            field can only be set when creating or updating a Service to type 'LoadBalancer'. Once set, it can
            not be changed. This field will be wiped when a service is updated to a non 'LoadBalancer' type.
        loadBalancerIP: Only applies to Service Type: LoadBalancer. This feature depends on whether the
            underlying cloud-provider supports specifying the loadBalancerIP when a load balancer is created.
            This field will be ignored if the cloud-provider does not support the feature. Deprecated: This
            field was under-specified and its meaning varies across implementations. Using it is non-portable
            and it may not support dual-stack. Users are encouraged to use implementation-specific annotations
            when available.
        loadBalancerSourceRanges: If specified and supported by the platform, this will restrict traffic
            through the cloud-provider load-balancer will be restricted to the specified client IPs. This
            field will be ignored if the cloud-provider does not support the feature.'
        ports: The list of ports that are exposed by this service.
        publishNotReadyAddresses: publishNotReadyAddresses indicates that any agent which deals with endpoints
            for this Service should disregard any indications of ready/not-ready. The primary use case for
            setting this field is for a StatefulSet's Headless Service to propagate SRV DNS records for its
            Pods for the purpose of peer discovery. The Kubernetes controllers that generate Endpoints and
            EndpointSlice resources for Services interpret this to mean that all endpoints are considered
            'ready' even if the Pods themselves are not. Agents which consume only Kubernetes generated
            endpoints through the Endpoints or EndpointSlice resources can safely assume this behavior.
        selector: Route service traffic to pods with label keys and values matching this selector. If empty or
            not present, the service is assumed to have an external process managing its endpoints, which
            Kubernetes will not modify. Only applies to types ClusterIP, NodePort, and LoadBalancer. Ignored
            if type is ExternalName.
        sessionAffinity: Supports 'ClientIP' and 'None'. Used to maintain session affinity. Enable client IP
            based session affinity. Must be ClientIP or None. Defaults to None.
        sessionAffinityConfig: sessionAffinityConfig contains the configurations of session affinity.
        trafficDistribution: TrafficDistribution offers a way to express preferences for how traffic is
            distributed to Service endpoints. Implementations can use this field as a hint, but are not
            required to guarantee strict adherence. If the field is not set, the implementation will apply its
            default routing strategy. If set to 'PreferClose', implementations should prioritize endpoints
            that are topologically close (e.g., same zone). This is an alpha field and requires enabling
            ServiceTrafficDistribution feature.
        type: type determines how the Service is exposed. Defaults to ClusterIP. Valid options are
            ExternalName, ClusterIP, NodePort, and LoadBalancer. 'ClusterIP' allocates a cluster-internal IP
            address for load-balancing to endpoints. Endpoints are determined by the selector or if that is
            not specified, by manual construction of an Endpoints object or EndpointSlice objects. If
            clusterIP is 'None', no virtual IP is allocated and the endpoints are published as a set of
            endpoints rather than a virtual IP. 'NodePort' builds on ClusterIP and allocates a port on every
            node which routes to the same endpoints as the clusterIP. 'LoadBalancer' builds on NodePort and
            creates an external load-balancer (if supported in the current cloud) which routes to the same
            endpoints as the clusterIP. 'ExternalName' aliases this service to the specified externalName.
            Several other fields do not apply to ExternalName services.

    """

    allocateLoadBalancerNodePorts: Optional[bool] = None
    clusterIP: Optional[str] = None
    clusterIPs: Optional[List[str]] = None
    externalIPs: Optional[List[str]] = None
    externalName: Optional[str] = None
    externalTrafficPolicy: Optional[str] = None
    healthCheckNodePort: Optional[int] = None
    internalTrafficPolicy: Optional[str] = None
    ipFamilies: Optional[List[str]] = None
    ipFamilyPolicy: Optional[str] = None
    loadBalancerClass: Optional[str] = None
    loadBalancerIP: Optional[str] = None
    loadBalancerSourceRanges: Optional[List[str]] = None
    ports: Optional[List[ServicePort]] = None
    publishNotReadyAddresses: Optional[bool] = None
    selector: Optional[JSONDict] = None
    sessionAffinity: Optional[str] = None
    sessionAffinityConfig: Optional[SessionAffinityConfig] = None
    trafficDistribution: Optional[str] = None
    type: Optional[str] = None


@dataclass
class ServiceStatus(K8sSpec):
    """ServiceStatus represents the current status of a service.

    Attributes:
        conditions: Current service state
        loadBalancer: LoadBalancer contains the current status of the load-balancer, if one is present.

    """

    conditions: Optional[List[gybe.k8s.v1_31.meta.v1.Condition]] = None
    loadBalancer: Optional[LoadBalancerStatus] = None


@dataclass
class SessionAffinityConfig(K8sSpec):
    """SessionAffinityConfig represents the configurations of session affinity.

    Attributes:
        clientIP: clientIP contains the configurations of Client IP based session affinity.

    """

    clientIP: Optional[ClientIPConfig] = None


@dataclass
class Taint(K8sSpec):
    """The node this Taint is attached to has the 'effect' on any pod that does not tolerate the Taint.

    Attributes:
        effect: Required. The effect of the taint on pods that do not tolerate the taint. Valid effects are
            NoSchedule, PreferNoSchedule and NoExecute.
        key: Required. The taint key to be applied to a node.
        timeAdded: TimeAdded represents the time at which the taint was added. It is only written for
            NoExecute taints.
        value: The taint value corresponding to the taint key.

    """

    key: str
    effect: str
    timeAdded: Optional[str] = None
    value: Optional[str] = None


@dataclass
class VolumeMountStatus(K8sSpec):
    """VolumeMountStatus shows status of volume mounts.

    Attributes:
        mountPath: MountPath corresponds to the original VolumeMount.
        name: Name corresponds to the name of the original VolumeMount.
        readOnly: ReadOnly corresponds to the original VolumeMount.
        recursiveReadOnly: RecursiveReadOnly must be set to Disabled, Enabled, or unspecified (for non-
            readonly mounts). An IfPossible value in the original VolumeMount must be translated to Disabled
            or Enabled, depending on the mount result.

    """

    name: str
    mountPath: str
    readOnly: Optional[bool] = None
    recursiveReadOnly: Optional[str] = None
