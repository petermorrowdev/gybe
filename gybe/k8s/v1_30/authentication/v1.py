"""Models generated from Kubernetes OpenAPI Spec."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Literal, Optional

import gybe.k8s.v1_30.meta.v1
from gybe.k8s.types import JSONDict, K8sResource, K8sSpec


@dataclass
class UserInfo(K8sSpec):
    """UserInfo holds the information about the user needed to implement the user.Info interface.

    Attributes:
        extra: Any additional information provided by the authenticator.
        groups: The names of groups this user is a part of.
        uid: A unique value that identifies this user across time. If this user is deleted and another user by
            the same name is added, they will have different UIDs.
        username: The name that uniquely identifies this user among all active users.

    """

    extra: Optional[JSONDict] = None
    groups: Optional[List[str]] = None
    uid: Optional[str] = None
    username: Optional[str] = None


@dataclass
class BoundObjectReference(K8sSpec):
    """BoundObjectReference is a reference to an object that a token is bound to.

    Attributes:
        apiVersion: API version of the referent.
        kind: Kind of the referent. Valid kinds are 'Pod' and 'Secret'.
        name: Name of the referent.
        uid: UID of the referent.

    """

    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    name: Optional[str] = None
    uid: Optional[str] = None


@dataclass
class TokenRequest(K8sResource):
    """TokenRequest requests a token for a given service account.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object's metadata.
        spec: Spec holds information about the request being evaluated
        status: Status is filled in by the server and indicates whether the token can be authenticated.

    """

    spec: TokenRequestSpec
    apiVersion: Literal['authentication.k8s.io/v1'] = 'authentication.k8s.io/v1'
    kind: Literal['TokenRequest'] = 'TokenRequest'
    metadata: Optional[gybe.k8s.v1_30.meta.v1.ObjectMeta] = None
    status: Optional[TokenRequestStatus] = None


@dataclass
class TokenRequestSpec(K8sSpec):
    """TokenRequestSpec contains client provided parameters of a token request.

    Attributes:
        audiences: Audiences are the intendend audiences of the token. A recipient of a token must identify
            themself with an identifier in the list of audiences of the token, and otherwise should reject the
            token. A token issued for multiple audiences may be used to authenticate against any of the
            audiences listed but implies a high degree of trust between the target audiences.
        boundObjectRef: BoundObjectRef is a reference to an object that the token will be bound to. The token
            will only be valid for as long as the bound object exists. NOTE: The API server's TokenReview
            endpoint will validate the BoundObjectRef, but other audiences may not. Keep ExpirationSeconds
            small if you want prompt revocation.
        expirationSeconds: ExpirationSeconds is the requested duration of validity of the request. The token
            issuer may return a token with a different validity duration so a client needs to check the
            'expiration' field in a response.

    """

    audiences: List[str]
    boundObjectRef: Optional[BoundObjectReference] = None
    expirationSeconds: Optional[int] = None


@dataclass
class TokenRequestStatus(K8sSpec):
    """TokenRequestStatus is the result of a token request.

    Attributes:
        expirationTimestamp: ExpirationTimestamp is the time of expiration of the returned token.
        token: Token is the opaque bearer token.

    """

    token: str
    expirationTimestamp: str


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
    metadata: Optional[gybe.k8s.v1_30.meta.v1.ObjectMeta] = None
    status: Optional[SelfSubjectReviewStatus] = None


@dataclass
class SelfSubjectReviewStatus(K8sSpec):
    """SelfSubjectReviewStatus is filled by the kube-apiserver and sent back to a user.

    Attributes:
        userInfo: User attributes of the user making this request.

    """

    userInfo: Optional[UserInfo] = None


@dataclass
class TokenReview(K8sResource):
    """TokenReview attempts to authenticate a token to a known user. Note: TokenReview requests may be cached
    by the webhook token authenticator plugin in the kube-apiserver.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object's metadata.
        spec: Spec holds information about the request being evaluated
        status: Status is filled in by the server and indicates whether the request can be authenticated.

    """

    spec: TokenReviewSpec
    apiVersion: Literal['authentication.k8s.io/v1'] = 'authentication.k8s.io/v1'
    kind: Literal['TokenReview'] = 'TokenReview'
    metadata: Optional[gybe.k8s.v1_30.meta.v1.ObjectMeta] = None
    status: Optional[TokenReviewStatus] = None


@dataclass
class TokenReviewSpec(K8sSpec):
    """TokenReviewSpec is a description of the token authentication request.

    Attributes:
        audiences: Audiences is a list of the identifiers that the resource server presented with the token
            identifies as. Audience-aware token authenticators will verify that the token was intended for at
            least one of the audiences in this list. If no audiences are provided, the audience will default
            to the audience of the Kubernetes apiserver.
        token: Token is the opaque bearer token.

    """

    audiences: Optional[List[str]] = None
    token: Optional[str] = None


@dataclass
class TokenReviewStatus(K8sSpec):
    """TokenReviewStatus is the result of the token authentication request.

    Attributes:
        audiences: Audiences are audience identifiers chosen by the authenticator that are compatible with
            both the TokenReview and token. An identifier is any identifier in the intersection of the
            TokenReviewSpec audiences and the token's audiences. A client of the TokenReview API that sets the
            spec.audiences field should validate that a compatible audience identifier is returned in the
            status.audiences field to ensure that the TokenReview server is audience aware. If a TokenReview
            returns an empty status.audience field where status.authenticated is 'true', the token is valid
            against the audience of the Kubernetes API server.
        authenticated: Authenticated indicates that the token was associated with a known user.
        error: Error indicates that the token couldn't be checked
        user: User is the UserInfo associated with the provided token.

    """

    audiences: Optional[List[str]] = None
    authenticated: Optional[bool] = None
    error: Optional[str] = None
    user: Optional[UserInfo] = None
