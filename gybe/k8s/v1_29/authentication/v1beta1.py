"""Models generated from Kubernetes OpenAPI Spec."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

import gybe.k8s.v1_29.authentication.v1
import gybe.k8s.v1_29.meta.v1
from gybe.k8s.types import K8sSpec


@dataclass
class SelfSubjectReview(K8sSpec):
    """SelfSubjectReview contains the user information that the kube-apiserver has about the user making this
    request. When using impersonation, users will receive the user info of the user being impersonated.
    If impersonation or request header authentication is used, any extra keys will have their case ignored
    and returned as lowercase.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object's metadata.
        status: Status is filled in by the server with the user attributes.

    """

    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[gybe.k8s.v1_29.meta.v1.ObjectMeta] = None
    status: Optional[SelfSubjectReviewStatus] = None


@dataclass
class SelfSubjectReviewStatus(K8sSpec):
    """SelfSubjectReviewStatus is filled by the kube-apiserver and sent back to a user.

    Attributes:
        userInfo: User attributes of the user making this request.

    """

    userInfo: Optional[gybe.k8s.v1_29.authentication.v1.UserInfo] = None
