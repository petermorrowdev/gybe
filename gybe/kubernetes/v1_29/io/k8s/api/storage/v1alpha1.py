from __future__ import annotations
from typing import Dict, List, Optional
from pydantic import BaseModel, Field
from ...apimachinery.pkg.apis.meta import v1


class VolumeAttributesClass(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description=(
            "APIVersion defines the versioned schema of this representation of an"
            " object. Servers should convert recognized schemas to the latest internal"
            " value, and may reject unrecognized values. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources"
        ),
    )
    driverName: str = Field(
        ..., description="Name of the CSI driver This field is immutable."
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
    parameters: Optional[Dict[str, str]] = Field(
        None,
        description=(
            "parameters hold volume attributes defined by the CSI driver. These values"
            " are opaque to the Kubernetes and are passed directly to the CSI driver."
            " The underlying storage provider supports changing these attributes on an"
            " existing volume, however the parameters field itself is immutable. To"
            " invoke a volume update, a new VolumeAttributesClass should be created"
            " with new parameters, and the PersistentVolumeClaim should be updated to"
            " reference the new VolumeAttributesClass.\n\nThis field is required and"
            " must contain at least one key/value pair. The keys cannot be empty, and"
            " the maximum number of parameters is 512, with a cumulative max size of"
            " 256K. If the CSI driver rejects invalid parameters, the target"
            ' PersistentVolumeClaim will be set to an "Infeasible" state in the'
            " modifyVolumeStatus field."
        ),
    )


class VolumeAttributesClassList(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description=(
            "APIVersion defines the versioned schema of this representation of an"
            " object. Servers should convert recognized schemas to the latest internal"
            " value, and may reject unrecognized values. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources"
        ),
    )
    items: List[VolumeAttributesClass] = Field(
        ..., description="items is the list of VolumeAttributesClass objects."
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
