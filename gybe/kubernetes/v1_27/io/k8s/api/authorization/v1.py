from __future__ import annotations
from typing import Dict, List, Optional
from pydantic import BaseModel, Field
from ...apimachinery.pkg.apis.meta import v1


class NonResourceAttributes(BaseModel):
    path: Optional[str] = Field(None, description="Path is the URL path of the request")
    verb: Optional[str] = Field(None, description="Verb is the standard HTTP verb")


class NonResourceRule(BaseModel):
    nonResourceURLs: Optional[List[str]] = Field(
        None,
        description=(
            "NonResourceURLs is a set of partial urls that a user should have access"
            ' to.  *s are allowed, but only as the full, final step in the path.  "*"'
            " means all."
        ),
    )
    verbs: List[str] = Field(
        ...,
        description=(
            "Verb is a list of kubernetes non-resource API verbs, like: get, post, put,"
            ' delete, patch, head, options.  "*" means all.'
        ),
    )


class ResourceAttributes(BaseModel):
    group: Optional[str] = Field(
        None, description='Group is the API Group of the Resource.  "*" means all.'
    )
    name: Optional[str] = Field(
        None,
        description=(
            'Name is the name of the resource being requested for a "get" or deleted'
            ' for a "delete". "" (empty) means all.'
        ),
    )
    namespace: Optional[str] = Field(
        None,
        description=(
            "Namespace is the namespace of the action being requested.  Currently,"
            ' there is no distinction between no namespace and all namespaces ""'
            ' (empty) is defaulted for LocalSubjectAccessReviews "" (empty) is empty'
            ' for cluster-scoped resources "" (empty) means "all" for namespace scoped'
            " resources from a SubjectAccessReview or SelfSubjectAccessReview"
        ),
    )
    resource: Optional[str] = Field(
        None,
        description='Resource is one of the existing resource types.  "*" means all.',
    )
    subresource: Optional[str] = Field(
        None,
        description=(
            'Subresource is one of the existing resource types.  "" means none.'
        ),
    )
    verb: Optional[str] = Field(
        None,
        description=(
            "Verb is a kubernetes resource API verb, like: get, list, watch, create,"
            ' update, delete, proxy.  "*" means all.'
        ),
    )
    version: Optional[str] = Field(
        None, description='Version is the API Version of the Resource.  "*" means all.'
    )


class ResourceRule(BaseModel):
    apiGroups: Optional[List[str]] = Field(
        None,
        description=(
            "APIGroups is the name of the APIGroup that contains the resources.  If"
            " multiple API groups are specified, any action requested against one of"
            ' the enumerated resources in any API group will be allowed.  "*" means'
            " all."
        ),
    )
    resourceNames: Optional[List[str]] = Field(
        None,
        description=(
            "ResourceNames is an optional white list of names that the rule applies to."
            '  An empty set means that everything is allowed.  "*" means all.'
        ),
    )
    resources: Optional[List[str]] = Field(
        None,
        description=(
            'Resources is a list of resources this rule applies to.  "*" means all in'
            " the specified apiGroups.\n \"*/foo\" represents the subresource 'foo' for"
            " all resources in the specified apiGroups."
        ),
    )
    verbs: List[str] = Field(
        ...,
        description=(
            "Verb is a list of kubernetes resource API verbs, like: get, list, watch,"
            ' create, update, delete, proxy.  "*" means all.'
        ),
    )


class SelfSubjectAccessReviewSpec(BaseModel):
    nonResourceAttributes: Optional[NonResourceAttributes] = Field(
        None,
        description=(
            "NonResourceAttributes describes information for a non-resource access"
            " request"
        ),
    )
    resourceAttributes: Optional[ResourceAttributes] = Field(
        None,
        description=(
            "ResourceAuthorizationAttributes describes information for a resource"
            " access request"
        ),
    )


class SelfSubjectRulesReviewSpec(BaseModel):
    namespace: Optional[str] = Field(
        None, description="Namespace to evaluate rules for. Required."
    )


class SubjectAccessReviewSpec(BaseModel):
    extra: Optional[Dict[str, List[str]]] = Field(
        None,
        description=(
            "Extra corresponds to the user.Info.GetExtra() method from the"
            " authenticator.  Since that is input to the authorizer it needs a"
            " reflection here."
        ),
    )
    groups: Optional[List[str]] = Field(
        None, description="Groups is the groups you're testing for."
    )
    nonResourceAttributes: Optional[NonResourceAttributes] = Field(
        None,
        description=(
            "NonResourceAttributes describes information for a non-resource access"
            " request"
        ),
    )
    resourceAttributes: Optional[ResourceAttributes] = Field(
        None,
        description=(
            "ResourceAuthorizationAttributes describes information for a resource"
            " access request"
        ),
    )
    uid: Optional[str] = Field(
        None, description="UID information about the requesting user."
    )
    user: Optional[str] = Field(
        None,
        description=(
            'User is the user you\'re testing for. If you specify "User" but not'
            ' "Groups", then is it interpreted as "What if User were not a member of'
            " any groups"
        ),
    )


class SubjectAccessReviewStatus(BaseModel):
    allowed: bool = Field(
        ...,
        description=(
            "Allowed is required. True if the action would be allowed, false otherwise."
        ),
    )
    denied: Optional[bool] = Field(
        None,
        description=(
            "Denied is optional. True if the action would be denied, otherwise false."
            " If both allowed is false and denied is false, then the authorizer has no"
            " opinion on whether to authorize the action. Denied may not be true if"
            " Allowed is true."
        ),
    )
    evaluationError: Optional[str] = Field(
        None,
        description=(
            "EvaluationError is an indication that some error occurred during the"
            " authorization check. It is entirely possible to get an error and be able"
            " to continue determine authorization status in spite of it. For instance,"
            " RBAC can be missing a role, but enough roles are still present and bound"
            " to reason about the request."
        ),
    )
    reason: Optional[str] = Field(
        None,
        description=(
            "Reason is optional.  It indicates why a request was allowed or denied."
        ),
    )


class SubjectRulesReviewStatus(BaseModel):
    evaluationError: Optional[str] = Field(
        None,
        description=(
            "EvaluationError can appear in combination with Rules. It indicates an"
            " error occurred during rule evaluation, such as an authorizer that doesn't"
            " support rule evaluation, and that ResourceRules and/or NonResourceRules"
            " may be incomplete."
        ),
    )
    incomplete: bool = Field(
        ...,
        description=(
            "Incomplete is true when the rules returned by this call are incomplete."
            " This is most commonly encountered when an authorizer, such as an external"
            " authorizer, doesn't support rules evaluation."
        ),
    )
    nonResourceRules: List[NonResourceRule] = Field(
        ...,
        description=(
            "NonResourceRules is the list of actions the subject is allowed to perform"
            " on non-resources. The list ordering isn't significant, may contain"
            " duplicates, and possibly be incomplete."
        ),
    )
    resourceRules: List[ResourceRule] = Field(
        ...,
        description=(
            "ResourceRules is the list of actions the subject is allowed to perform on"
            " resources. The list ordering isn't significant, may contain duplicates,"
            " and possibly be incomplete."
        ),
    )


class LocalSubjectAccessReview(BaseModel):
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
            "Standard list metadata. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata"
        ),
    )
    spec: SubjectAccessReviewSpec = Field(
        ...,
        description=(
            "Spec holds information about the request being evaluated.  spec.namespace"
            " must be equal to the namespace you made the request against.  If empty,"
            " it is defaulted."
        ),
    )
    status: Optional[SubjectAccessReviewStatus] = Field(
        None,
        description=(
            "Status is filled in by the server and indicates whether the request is"
            " allowed or not"
        ),
    )


class SelfSubjectAccessReview(BaseModel):
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
            "Standard list metadata. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata"
        ),
    )
    spec: SelfSubjectAccessReviewSpec = Field(
        ...,
        description=(
            "Spec holds information about the request being evaluated.  user and groups"
            " must be empty"
        ),
    )
    status: Optional[SubjectAccessReviewStatus] = Field(
        None,
        description=(
            "Status is filled in by the server and indicates whether the request is"
            " allowed or not"
        ),
    )


class SelfSubjectRulesReview(BaseModel):
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
            "Standard list metadata. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata"
        ),
    )
    spec: SelfSubjectRulesReviewSpec = Field(
        ..., description="Spec holds information about the request being evaluated."
    )
    status: Optional[SubjectRulesReviewStatus] = Field(
        None,
        description=(
            "Status is filled in by the server and indicates the set of actions a user"
            " can perform."
        ),
    )


class SubjectAccessReview(BaseModel):
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
            "Standard list metadata. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata"
        ),
    )
    spec: SubjectAccessReviewSpec = Field(
        ..., description="Spec holds information about the request being evaluated"
    )
    status: Optional[SubjectAccessReviewStatus] = Field(
        None,
        description=(
            "Status is filled in by the server and indicates whether the request is"
            " allowed or not"
        ),
    )
