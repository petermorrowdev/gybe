"""Models generated from Kubernetes OpenAPI Spec."""
from __future__ import annotations
from typing import List, Optional, Literal
from dataclasses import dataclass
from gybe.k8s.types import JSONObj, JSONDict, K8sSpec, K8sResource
import gybe.k8s.v1_31.meta.v1

@dataclass
class VolumeAttributesClass(K8sResource):
    """
    VolumeAttributesClass represents a specification of mutable volume attributes defined by the CSI
    driver. The class can be specified during dynamic provisioning of PersistentVolumeClaims, and changed
    in the PersistentVolumeClaim spec after provisioning.
    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        driverName: Name of the CSI driver This field is immutable.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object's metadata.
        parameters: parameters hold volume attributes defined by the CSI driver. These values are opaque to
            the Kubernetes and are passed directly to the CSI driver. The underlying storage provider supports
            changing these attributes on an existing volume, however the parameters field itself is immutable.
            To invoke a volume update, a new VolumeAttributesClass should be created with new parameters, and
            the PersistentVolumeClaim should be updated to reference the new VolumeAttributesClass.  This
            field is required and must contain at least one key/value pair. The keys cannot be empty, and the
            maximum number of parameters is 512, with a cumulative max size of 256K. If the CSI driver rejects
            invalid parameters, the target PersistentVolumeClaim will be set to an 'Infeasible' state in the
            modifyVolumeStatus field.

"""
    driverName: str
    apiVersion: Literal['storage.k8s.io/v1beta1'] = 'storage.k8s.io/v1beta1'
    kind: Literal['VolumeAttributesClass'] = 'VolumeAttributesClass'
    metadata: Optional[gybe.k8s.v1_31.meta.v1.ObjectMeta] = None
    parameters: Optional[JSONDict] = None