"""Models generated from Kubernetes OpenAPI Spec."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Literal, Optional

import gybe.k8s.v1_29.meta.v1
from gybe.k8s.types import JSONDict, K8sResource, K8sSpec


@dataclass
class LocalSubjectAccessReview(K8sResource):
    """LocalSubjectAccessReview checks whether or not a user or group can perform an action in a given
    namespace. Having a namespace scoped resource makes it much easier to grant namespace scoped policy
    that includes permissions checking.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard list metadata.
        spec: Spec holds information about the request being evaluated.  spec.namespace must be equal to the
            namespace you made the request against.  If empty, it is defaulted.
        status: Status is filled in by the server and indicates whether the request is allowed or not

    """

    spec: SubjectAccessReviewSpec
    apiVersion: Literal['rbac.authorization.k8s.io/v1'] = 'rbac.authorization.k8s.io/v1'
    kind: Literal['LocalSubjectAccessReview'] = 'LocalSubjectAccessReview'
    metadata: Optional[gybe.k8s.v1_29.meta.v1.ObjectMeta] = None
    status: Optional[SubjectAccessReviewStatus] = None


@dataclass
class NonResourceAttributes(K8sSpec):
    """NonResourceAttributes includes the authorization attributes available for non-resource requests to the
    Authorizer interface
    Attributes:
        path: Path is the URL path of the request
        verb: Verb is the standard HTTP verb

    """

    path: Optional[str] = None
    verb: Optional[str] = None


@dataclass
class NonResourceRule(K8sSpec):
    """NonResourceRule holds information that describes a rule for the non-resource
    Attributes:
        nonResourceURLs: NonResourceURLs is a set of partial urls that a user should have access to.  *s are
            allowed, but only as the full, final step in the path.  '*' means all.
        verbs: Verb is a list of kubernetes non-resource API verbs, like: get, post, put, delete, patch, head,
            options.  '*' means all.

    """

    verbs: List[str]
    nonResourceURLs: Optional[List[str]] = None


@dataclass
class ResourceAttributes(K8sSpec):
    """ResourceAttributes includes the authorization attributes available for resource requests to the
    Authorizer interface
    Attributes:
        group: Group is the API Group of the Resource.  '*' means all.
        name: Name is the name of the resource being requested for a 'get' or deleted for a 'delete'. ''
            (empty) means all.
        namespace: Namespace is the namespace of the action being requested.  Currently, there is no
            distinction between no namespace and all namespaces '' (empty) is defaulted for
            LocalSubjectAccessReviews '' (empty) is empty for cluster-scoped resources '' (empty) means 'all'
            for namespace scoped resources from a SubjectAccessReview or SelfSubjectAccessReview
        resource: Resource is one of the existing resource types.  '*' means all.
        subresource: Subresource is one of the existing resource types.  '' means none.
        verb: Verb is a kubernetes resource API verb, like: get, list, watch, create, update, delete, proxy.
            '*' means all.
        version: Version is the API Version of the Resource.  '*' means all.

    """

    group: Optional[str] = None
    name: Optional[str] = None
    namespace: Optional[str] = None
    resource: Optional[str] = None
    subresource: Optional[str] = None
    verb: Optional[str] = None
    version: Optional[str] = None


@dataclass
class ResourceRule(K8sSpec):
    """ResourceRule is the list of actions the subject is allowed to perform on resources. The list ordering
    isn't significant, may contain duplicates, and possibly be incomplete.

    Attributes:
        apiGroups: APIGroups is the name of the APIGroup that contains the resources.  If multiple API groups
            are specified, any action requested against one of the enumerated resources in any API group will
            be allowed.  '*' means all.
        resourceNames: ResourceNames is an optional white list of names that the rule applies to.  An empty
            set means that everything is allowed.  '*' means all.
        resources: Resources is a list of resources this rule applies to.  '*' means all in the specified
            apiGroups.  '*/foo' represents the subresource 'foo' for all resources in the specified apiGroups.
        verbs: Verb is a list of kubernetes resource API verbs, like: get, list, watch, create, update,
            delete, proxy.  '*' means all.

    """

    verbs: List[str]
    apiGroups: Optional[List[str]] = None
    resourceNames: Optional[List[str]] = None
    resources: Optional[List[str]] = None


@dataclass
class SelfSubjectAccessReview(K8sResource):
    """SelfSubjectAccessReview checks whether or the current user can perform an action.  Not filling in a
    spec.namespace means 'in all namespaces'.  Self is a special case, because users should always be able
    to check whether they can perform an action
    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard list metadata.
        spec: Spec holds information about the request being evaluated.  user and groups must be empty
        status: Status is filled in by the server and indicates whether the request is allowed or not

    """

    spec: SelfSubjectAccessReviewSpec
    apiVersion: Literal['rbac.authorization.k8s.io/v1'] = 'rbac.authorization.k8s.io/v1'
    kind: Literal['SelfSubjectAccessReview'] = 'SelfSubjectAccessReview'
    metadata: Optional[gybe.k8s.v1_29.meta.v1.ObjectMeta] = None
    status: Optional[SubjectAccessReviewStatus] = None


@dataclass
class SelfSubjectAccessReviewSpec(K8sSpec):
    """SelfSubjectAccessReviewSpec is a description of the access request.  Exactly one of
    ResourceAuthorizationAttributes and NonResourceAuthorizationAttributes must be set
    Attributes:
        nonResourceAttributes: NonResourceAttributes describes information for a non-resource access request
        resourceAttributes: ResourceAuthorizationAttributes describes information for a resource access
            request

    """

    nonResourceAttributes: Optional[NonResourceAttributes] = None
    resourceAttributes: Optional[ResourceAttributes] = None


@dataclass
class SelfSubjectRulesReview(K8sResource):
    """SelfSubjectRulesReview enumerates the set of actions the current user can perform within a namespace.
    The returned list of actions may be incomplete depending on the server's authorization mode, and any
    errors experienced during the evaluation. SelfSubjectRulesReview should be used by UIs to show/hide
    actions, or to quickly let an end user reason about their permissions. It should NOT Be used by
    external systems to drive authorization decisions as this raises confused deputy, cache
    lifetime/revocation, and correctness concerns. SubjectAccessReview, and LocalAccessReview are the
    correct way to defer authorization decisions to the API server.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard list metadata.
        spec: Spec holds information about the request being evaluated.
        status: Status is filled in by the server and indicates the set of actions a user can perform.

    """

    spec: SelfSubjectRulesReviewSpec
    apiVersion: Literal['rbac.authorization.k8s.io/v1'] = 'rbac.authorization.k8s.io/v1'
    kind: Literal['SelfSubjectRulesReview'] = 'SelfSubjectRulesReview'
    metadata: Optional[gybe.k8s.v1_29.meta.v1.ObjectMeta] = None
    status: Optional[SubjectRulesReviewStatus] = None


@dataclass
class SelfSubjectRulesReviewSpec(K8sSpec):
    """SelfSubjectRulesReviewSpec defines the specification for SelfSubjectRulesReview.

    Attributes:
        namespace: Namespace to evaluate rules for. Required.

    """

    namespace: Optional[str] = None


@dataclass
class SubjectAccessReview(K8sResource):
    """SubjectAccessReview checks whether or not a user or group can perform an action.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard list metadata.
        spec: Spec holds information about the request being evaluated
        status: Status is filled in by the server and indicates whether the request is allowed or not

    """

    spec: SubjectAccessReviewSpec
    apiVersion: Literal['rbac.authorization.k8s.io/v1'] = 'rbac.authorization.k8s.io/v1'
    kind: Literal['SubjectAccessReview'] = 'SubjectAccessReview'
    metadata: Optional[gybe.k8s.v1_29.meta.v1.ObjectMeta] = None
    status: Optional[SubjectAccessReviewStatus] = None


@dataclass
class SubjectAccessReviewSpec(K8sSpec):
    """SubjectAccessReviewSpec is a description of the access request.  Exactly one of
    ResourceAuthorizationAttributes and NonResourceAuthorizationAttributes must be set
    Attributes:
        extra: Extra corresponds to the user.Info.GetExtra() method from the authenticator.  Since that is
            input to the authorizer it needs a reflection here.
        groups: Groups is the groups you're testing for.
        nonResourceAttributes: NonResourceAttributes describes information for a non-resource access request
        resourceAttributes: ResourceAuthorizationAttributes describes information for a resource access
            request
        uid: UID information about the requesting user.
        user: User is the user you're testing for. If you specify 'User' but not 'Groups', then is it
            interpreted as 'What if User were not a member of any groups

    """

    extra: Optional[JSONDict] = None
    groups: Optional[List[str]] = None
    nonResourceAttributes: Optional[NonResourceAttributes] = None
    resourceAttributes: Optional[ResourceAttributes] = None
    uid: Optional[str] = None
    user: Optional[str] = None


@dataclass
class SubjectAccessReviewStatus(K8sSpec):
    """SubjectAccessReviewStatus
    Attributes:
        allowed: Allowed is required. True if the action would be allowed, false otherwise.
        denied: Denied is optional. True if the action would be denied, otherwise false. If both allowed is
            false and denied is false, then the authorizer has no opinion on whether to authorize the action.
            Denied may not be true if Allowed is true.
        evaluationError: EvaluationError is an indication that some error occurred during the authorization
            check. It is entirely possible to get an error and be able to continue determine authorization
            status in spite of it. For instance, RBAC can be missing a role, but enough roles are still
            present and bound to reason about the request.
        reason: Reason is optional.  It indicates why a request was allowed or denied.

    """

    allowed: bool
    denied: Optional[bool] = None
    evaluationError: Optional[str] = None
    reason: Optional[str] = None


@dataclass
class SubjectRulesReviewStatus(K8sSpec):
    """SubjectRulesReviewStatus contains the result of a rules check. This check can be incomplete depending
    on the set of authorizers the server is configured with and any errors experienced during evaluation.
    Because authorization rules are additive, if a rule appears in a list it's safe to assume the subject
    has that permission, even if that list is incomplete.

    Attributes:
        evaluationError: EvaluationError can appear in combination with Rules. It indicates an error occurred
            during rule evaluation, such as an authorizer that doesn't support rule evaluation, and that
            ResourceRules and/or NonResourceRules may be incomplete.
        incomplete: Incomplete is true when the rules returned by this call are incomplete. This is most
            commonly encountered when an authorizer, such as an external authorizer, doesn't support rules
            evaluation.
        nonResourceRules: NonResourceRules is the list of actions the subject is allowed to perform on non-
            resources. The list ordering isn't significant, may contain duplicates, and possibly be
            incomplete.
        resourceRules: ResourceRules is the list of actions the subject is allowed to perform on resources.
            The list ordering isn't significant, may contain duplicates, and possibly be incomplete.

    """

    resourceRules: List[ResourceRule]
    nonResourceRules: List[NonResourceRule]
    incomplete: bool
    evaluationError: Optional[str] = None
