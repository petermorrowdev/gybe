from __future__ import annotations
from typing import List, Optional
from pydantic import BaseModel, Field
from ...apimachinery.pkg.apis.meta import v1


class ExemptPriorityLevelConfiguration(BaseModel):
    lendablePercent: Optional[int] = Field(
        None,
        description=(
            "`lendablePercent` prescribes the fraction of the level's NominalCL that"
            " can be borrowed by other priority levels.  This value of this field must"
            " be between 0 and 100, inclusive, and it defaults to 0. The number of"
            " seats that other levels can borrow from this level, known as this level's"
            " LendableConcurrencyLimit (LendableCL), is defined as"
            " follows.\n\nLendableCL(i) = round( NominalCL(i) *"
            " lendablePercent(i)/100.0 )"
        ),
    )
    nominalConcurrencyShares: Optional[int] = Field(
        None,
        description=(
            "`nominalConcurrencyShares` (NCS) contributes to the computation of the"
            " NominalConcurrencyLimit (NominalCL) of this level. This is the number of"
            " execution seats nominally reserved for this priority level. This DOES NOT"
            " limit the dispatching from this priority level but affects the other"
            " priority levels through the borrowing mechanism. The server's concurrency"
            " limit (ServerCL) is divided among all the priority levels in proportion"
            " to their NCS values:\n\nNominalCL(i)  = ceil( ServerCL * NCS(i) / sum_ncs"
            " ) sum_ncs = sum[priority level k] NCS(k)\n\nBigger numbers mean a larger"
            " nominal concurrency limit, at the expense of every other priority level."
            " This field has a default value of zero."
        ),
    )


class FlowDistinguisherMethod(BaseModel):
    type: str = Field(
        ...,
        description=(
            "`type` is the type of flow distinguisher method The supported types are"
            ' "ByUser" and "ByNamespace". Required.'
        ),
    )


class GroupSubject(BaseModel):
    name: str = Field(
        ...,
        description=(
            'name is the user group that matches, or "*" to match all user groups. See'
            " https://github.com/kubernetes/apiserver/blob/master/pkg/authentication/user/user.go"
            " for some well-known group names. Required."
        ),
    )


class NonResourcePolicyRule(BaseModel):
    nonResourceURLs: List[str] = Field(
        ...,
        description=(
            "`nonResourceURLs` is a set of url prefixes that a user should have access"
            ' to and may not be empty. For example:\n  - "/healthz" is legal\n  -'
            ' "/hea*" is illegal\n  - "/hea" is legal but matches nothing\n  - "/hea/*"'
            ' also matches nothing\n  - "/healthz/*" matches all per-component health'
            ' checks.\n"*" matches all non-resource urls. if it is present, it must be'
            " the only entry. Required."
        ),
    )
    verbs: List[str] = Field(
        ...,
        description=(
            '`verbs` is a list of matching verbs and may not be empty. "*" matches all'
            " verbs. If it is present, it must be the only entry. Required."
        ),
    )


class PriorityLevelConfigurationReference(BaseModel):
    name: str = Field(
        ...,
        description=(
            "`name` is the name of the priority level configuration being referenced"
            " Required."
        ),
    )


class QueuingConfiguration(BaseModel):
    handSize: Optional[int] = Field(
        0,
        description=(
            "`handSize` is a small positive number that configures the shuffle sharding"
            " of requests into queues.  When enqueuing a request at this priority level"
            " the request's flow identifier (a string pair) is hashed and the hash"
            " value is used to shuffle the list of queues and deal a hand of the size"
            " specified here.  The request is put into one of the shortest queues in"
            " that hand. `handSize` must be no larger than `queues`, and should be"
            " significantly smaller (so that a few heavy flows do not saturate most of"
            " the queues).  See the user-facing documentation for more extensive"
            " guidance on setting this field.  This field has a default value of 8."
        ),
    )
    queueLengthLimit: Optional[int] = Field(
        0,
        description=(
            "`queueLengthLimit` is the maximum number of requests allowed to be waiting"
            " in a given queue of this priority level at a time; excess requests are"
            " rejected.  This value must be positive.  If not specified, it will be"
            " defaulted to 50."
        ),
    )
    queues: Optional[int] = Field(
        0,
        description=(
            "`queues` is the number of queues for this priority level. The queues exist"
            " independently at each apiserver. The value must be positive.  Setting it"
            " to 1 effectively precludes shufflesharding and thus makes the"
            " distinguisher method of associated flow schemas irrelevant.  This field"
            " has a default value of 64."
        ),
    )


class ResourcePolicyRule(BaseModel):
    apiGroups: List[str] = Field(
        ...,
        description=(
            '`apiGroups` is a list of matching API groups and may not be empty. "*"'
            " matches all API groups and, if present, must be the only entry. Required."
        ),
    )
    clusterScope: Optional[bool] = Field(
        None,
        description=(
            "`clusterScope` indicates whether to match requests that do not specify a"
            " namespace (which happens either because the resource is not namespaced or"
            " the request targets all namespaces). If this field is omitted or false"
            " then the `namespaces` field must contain a non-empty list."
        ),
    )
    namespaces: Optional[List[str]] = Field(
        None,
        description=(
            "`namespaces` is a list of target namespaces that restricts matches.  A"
            " request that specifies a target namespace matches only if either (a) this"
            ' list contains that target namespace or (b) this list contains "*".  Note'
            ' that "*" matches any specified namespace but does not match a request'
            " that _does not specify_ a namespace (see the `clusterScope` field for"
            " that). This list may be empty, but only if `clusterScope` is true."
        ),
    )
    resources: List[str] = Field(
        ...,
        description=(
            "`resources` is a list of matching resources (i.e., lowercase and plural)"
            ' with, if desired, subresource.  For example, [ "services", "nodes/status"'
            ' ].  This list may not be empty. "*" matches all resources and, if'
            " present, must be the only entry. Required."
        ),
    )
    verbs: List[str] = Field(
        ...,
        description=(
            '`verbs` is a list of matching verbs and may not be empty. "*" matches all'
            " verbs and, if present, must be the only entry. Required."
        ),
    )


class ServiceAccountSubject(BaseModel):
    name: str = Field(
        ...,
        description=(
            '`name` is the name of matching ServiceAccount objects, or "*" to match'
            " regardless of name. Required."
        ),
    )
    namespace: str = Field(
        ...,
        description=(
            "`namespace` is the namespace of matching ServiceAccount objects. Required."
        ),
    )


class UserSubject(BaseModel):
    name: str = Field(
        ...,
        description=(
            '`name` is the username that matches, or "*" to match all usernames.'
            " Required."
        ),
    )


class FlowSchemaCondition(BaseModel):
    lastTransitionTime: Optional[v1.Time] = Field(
        None,
        description=(
            "`lastTransitionTime` is the last time the condition transitioned from one"
            " status to another."
        ),
    )
    message: Optional[str] = Field(
        None,
        description=(
            "`message` is a human-readable message indicating details about last"
            " transition."
        ),
    )
    reason: Optional[str] = Field(
        None,
        description=(
            "`reason` is a unique, one-word, CamelCase reason for the condition's last"
            " transition."
        ),
    )
    status: Optional[str] = Field(
        None,
        description=(
            "`status` is the status of the condition. Can be True, False, Unknown."
            " Required."
        ),
    )
    type: Optional[str] = Field(
        None, description="`type` is the type of the condition. Required."
    )


class FlowSchemaStatus(BaseModel):
    conditions: Optional[List[FlowSchemaCondition]] = Field(
        None, description="`conditions` is a list of the current states of FlowSchema."
    )


class LimitResponse(BaseModel):
    queuing: Optional[QueuingConfiguration] = Field(
        None,
        description=(
            "`queuing` holds the configuration parameters for queuing. This field may"
            ' be non-empty only if `type` is `"Queue"`.'
        ),
    )
    type: str = Field(
        ...,
        description=(
            '`type` is "Queue" or "Reject". "Queue" means that requests that can not be'
            " executed upon arrival are held in a queue until they can be executed or a"
            ' queuing limit is reached. "Reject" means that requests that can not be'
            " executed upon arrival are rejected. Required."
        ),
    )


class LimitedPriorityLevelConfiguration(BaseModel):
    borrowingLimitPercent: Optional[int] = Field(
        None,
        description=(
            "`borrowingLimitPercent`, if present, configures a limit on how many seats"
            " this priority level can borrow from other priority levels. The limit is"
            " known as this level's BorrowingConcurrencyLimit (BorrowingCL) and is a"
            " limit on the total number of seats that this level may borrow at any one"
            " time. This field holds the ratio of that limit to the level's nominal"
            " concurrency limit. When this field is non-nil, it must hold a"
            " non-negative integer and the limit is calculated as"
            " follows.\n\nBorrowingCL(i) = round( NominalCL(i) *"
            " borrowingLimitPercent(i)/100.0 )\n\nThe value of this field can be more"
            " than 100, implying that this priority level can borrow a number of seats"
            " that is greater than its own nominal concurrency limit (NominalCL). When"
            " this field is left `nil`, the limit is effectively infinite."
        ),
    )
    lendablePercent: Optional[int] = Field(
        None,
        description=(
            "`lendablePercent` prescribes the fraction of the level's NominalCL that"
            " can be borrowed by other priority levels. The value of this field must be"
            " between 0 and 100, inclusive, and it defaults to 0. The number of seats"
            " that other levels can borrow from this level, known as this level's"
            " LendableConcurrencyLimit (LendableCL), is defined as"
            " follows.\n\nLendableCL(i) = round( NominalCL(i) *"
            " lendablePercent(i)/100.0 )"
        ),
    )
    limitResponse: Optional[LimitResponse] = Field(
        None,
        description=(
            "`limitResponse` indicates what to do with requests that can not be"
            " executed right now"
        ),
    )
    nominalConcurrencyShares: Optional[int] = Field(
        0,
        description=(
            "`nominalConcurrencyShares` (NCS) contributes to the computation of the"
            " NominalConcurrencyLimit (NominalCL) of this level. This is the number of"
            " execution seats available at this priority level. This is used both for"
            " requests dispatched from this priority level as well as requests"
            " dispatched from other priority levels borrowing seats from this level."
            " The server's concurrency limit (ServerCL) is divided among the Limited"
            " priority levels in proportion to their NCS values:\n\nNominalCL(i)  ="
            " ceil( ServerCL * NCS(i) / sum_ncs ) sum_ncs = sum[priority level k]"
            " NCS(k)\n\nBigger numbers mean a larger nominal concurrency limit, at the"
            " expense of every other priority level. This field has a default value"
            " of 30."
        ),
    )


class PriorityLevelConfigurationCondition(BaseModel):
    lastTransitionTime: Optional[v1.Time] = Field(
        None,
        description=(
            "`lastTransitionTime` is the last time the condition transitioned from one"
            " status to another."
        ),
    )
    message: Optional[str] = Field(
        None,
        description=(
            "`message` is a human-readable message indicating details about last"
            " transition."
        ),
    )
    reason: Optional[str] = Field(
        None,
        description=(
            "`reason` is a unique, one-word, CamelCase reason for the condition's last"
            " transition."
        ),
    )
    status: Optional[str] = Field(
        None,
        description=(
            "`status` is the status of the condition. Can be True, False, Unknown."
            " Required."
        ),
    )
    type: Optional[str] = Field(
        None, description="`type` is the type of the condition. Required."
    )


class PriorityLevelConfigurationSpec(BaseModel):
    exempt: Optional[ExemptPriorityLevelConfiguration] = Field(
        None,
        description=(
            "`exempt` specifies how requests are handled for an exempt priority level."
            ' This field MUST be empty if `type` is `"Limited"`. This field MAY be'
            ' non-empty if `type` is `"Exempt"`. If empty and `type` is `"Exempt"` then'
            " the default values for `ExemptPriorityLevelConfiguration` apply."
        ),
    )
    limited: Optional[LimitedPriorityLevelConfiguration] = Field(
        None,
        description=(
            "`limited` specifies how requests are handled for a Limited priority level."
            ' This field must be non-empty if and only if `type` is `"Limited"`.'
        ),
    )
    type: str = Field(
        ...,
        description=(
            "`type` indicates whether this priority level is subject to limitation on"
            ' request execution.  A value of `"Exempt"` means that requests of this'
            " priority level are not subject to a limit (and thus are never queued) and"
            " do not detract from the capacity made available to other priority levels."
            '  A value of `"Limited"` means that (a) requests of this priority level'
            " _are_ subject to limits and (b) some of the server's limited capacity is"
            " made available exclusively to this priority level. Required."
        ),
    )


class PriorityLevelConfigurationStatus(BaseModel):
    conditions: Optional[List[PriorityLevelConfigurationCondition]] = Field(
        None, description='`conditions` is the current state of "request-priority".'
    )


class Subject(BaseModel):
    group: Optional[GroupSubject] = Field(
        None, description="`group` matches based on user group name."
    )
    kind: str = Field(
        ...,
        description=(
            "`kind` indicates which one of the other fields is non-empty. Required"
        ),
    )
    serviceAccount: Optional[ServiceAccountSubject] = Field(
        None, description="`serviceAccount` matches ServiceAccounts."
    )
    user: Optional[UserSubject] = Field(
        None, description="`user` matches based on username."
    )


class PolicyRulesWithSubjects(BaseModel):
    nonResourceRules: Optional[List[NonResourcePolicyRule]] = Field(
        None,
        description=(
            "`nonResourceRules` is a list of NonResourcePolicyRules that identify"
            " matching requests according to their verb and the target non-resource"
            " URL."
        ),
    )
    resourceRules: Optional[List[ResourcePolicyRule]] = Field(
        None,
        description=(
            "`resourceRules` is a slice of ResourcePolicyRules that identify matching"
            " requests according to their verb and the target resource. At least one of"
            " `resourceRules` and `nonResourceRules` has to be non-empty."
        ),
    )
    subjects: List[Subject] = Field(
        ...,
        description=(
            "subjects is the list of normal user, serviceaccount, or group that this"
            " rule cares about. There must be at least one member in this slice. A"
            " slice that includes both the system:authenticated and"
            " system:unauthenticated user groups matches every request. Required."
        ),
    )


class PriorityLevelConfiguration(BaseModel):
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
            "`metadata` is the standard object's metadata. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata"
        ),
    )
    spec: Optional[PriorityLevelConfigurationSpec] = Field(
        None,
        description=(
            "`spec` is the specification of the desired behavior of a"
            ' "request-priority". More info:'
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status"
        ),
    )
    status: Optional[PriorityLevelConfigurationStatus] = Field(
        None,
        description=(
            '`status` is the current status of a "request-priority". More info:'
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status"
        ),
    )


class PriorityLevelConfigurationList(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description=(
            "APIVersion defines the versioned schema of this representation of an"
            " object. Servers should convert recognized schemas to the latest internal"
            " value, and may reject unrecognized values. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources"
        ),
    )
    items: List[PriorityLevelConfiguration] = Field(
        ..., description="`items` is a list of request-priorities."
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
            "`metadata` is the standard object's metadata. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata"
        ),
    )


class FlowSchemaSpec(BaseModel):
    distinguisherMethod: Optional[FlowDistinguisherMethod] = Field(
        None,
        description=(
            "`distinguisherMethod` defines how to compute the flow distinguisher for"
            " requests that match this schema. `nil` specifies that the distinguisher"
            " is disabled and thus will always be the empty string."
        ),
    )
    matchingPrecedence: Optional[int] = Field(
        0,
        description=(
            "`matchingPrecedence` is used to choose among the FlowSchemas that match a"
            " given request. The chosen FlowSchema is among those with the numerically"
            " lowest (which we take to be logically highest) MatchingPrecedence.  Each"
            " MatchingPrecedence value must be ranged in [1,10000]. Note that if the"
            " precedence is not specified, it will be set to 1000 as default."
        ),
    )
    priorityLevelConfiguration: PriorityLevelConfigurationReference = Field(
        ...,
        description=(
            "`priorityLevelConfiguration` should reference a PriorityLevelConfiguration"
            " in the cluster. If the reference cannot be resolved, the FlowSchema will"
            " be ignored and marked as invalid in its status. Required."
        ),
    )
    rules: Optional[List[PolicyRulesWithSubjects]] = Field(
        None,
        description=(
            "`rules` describes which requests will match this flow schema. This"
            " FlowSchema matches a request if and only if at least one member of rules"
            " matches the request. if it is an empty slice, there will be no requests"
            " matching the FlowSchema."
        ),
    )


class FlowSchema(BaseModel):
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
            "`metadata` is the standard object's metadata. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata"
        ),
    )
    spec: Optional[FlowSchemaSpec] = Field(
        None,
        description=(
            "`spec` is the specification of the desired behavior of a FlowSchema. More"
            " info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status"
        ),
    )
    status: Optional[FlowSchemaStatus] = Field(
        None,
        description=(
            "`status` is the current status of a FlowSchema. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status"
        ),
    )


class FlowSchemaList(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description=(
            "APIVersion defines the versioned schema of this representation of an"
            " object. Servers should convert recognized schemas to the latest internal"
            " value, and may reject unrecognized values. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources"
        ),
    )
    items: List[FlowSchema] = Field(
        ..., description="`items` is a list of FlowSchemas."
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
            "`metadata` is the standard list metadata. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata"
        ),
    )
