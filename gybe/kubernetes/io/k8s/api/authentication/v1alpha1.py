from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field
from ...apimachinery.pkg.apis.meta import v1 as v1_1
from . import v1


class SelfSubjectReviewStatus(BaseModel):
    userInfo: Optional[v1.UserInfo] = Field(
        None, description="User attributes of the user making this request."
    )


class SelfSubjectReview(BaseModel):
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
    metadata: Optional[v1_1.ObjectMeta] = Field(
        None,
        description=(
            "Standard object's metadata. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata"
        ),
    )
    status: Optional[SelfSubjectReviewStatus] = Field(
        None, description="Status is filled in by the server with the user attributes."
    )
