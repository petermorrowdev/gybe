"""Models generated from Kubernetes OpenAPI Spec."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Literal, Optional

import gybe.k8s.v1_29.meta.v1
from gybe.k8s.types import JSONObj, K8sResource, K8sSpec


@dataclass
class ExemptPriorityLevelConfiguration(K8sSpec):
    """ExemptPriorityLevelConfiguration describes the configurable aspects of the handling of exempt
    requests. In the mandatory exempt configuration object the values in the fields here can be modified
    by authorized users, unlike the rest of the `spec`.

    Attributes:
        lendablePercent: `lendablePercent` prescribes the fraction of the level's NominalCL that can be
            borrowed by other priority levels.  This value of this field must be between 0 and 100, inclusive,
            and it defaults to 0. The number of seats that other levels can borrow from this level, known as
            this level's LendableConcurrencyLimit (LendableCL), is defined as follows.  LendableCL(i) = round(
            NominalCL(i) * lendablePercent(i)/100.0 )
        nominalConcurrencyShares: `nominalConcurrencyShares` (NCS) contributes to the computation of the
            NominalConcurrencyLimit (NominalCL) of this level. This is the number of execution seats nominally
            reserved for this priority level. This DOES NOT limit the dispatching from this priority level but
            affects the other priority levels through the borrowing mechanism. The server's concurrency limit
            (ServerCL) is divided among all the priority levels in proportion to their NCS values:
            NominalCL(i)  = ceil( ServerCL * NCS(i) / sum_ncs ) sum_ncs = sum[priority level k] NCS(k)  Bigger
            numbers mean a larger nominal concurrency limit, at the expense of every other priority level.
            This field has a default value of zero.

    """

    lendablePercent: Optional[int] = None
    nominalConcurrencyShares: Optional[int] = None


@dataclass
class FlowDistinguisherMethod(K8sSpec):
    """FlowDistinguisherMethod specifies the method of a flow distinguisher.

    Attributes:
        type: `type` is the type of flow distinguisher method The supported types are 'ByUser' and
            'ByNamespace'. Required.

    """

    type: str


@dataclass
class FlowSchema(K8sResource):
    """FlowSchema defines the schema of a group of flows. Note that a flow is made up of a set of inbound API
    requests with similar attributes and is identified by a pair of strings: the name of the FlowSchema
    and a 'flow distinguisher'.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: `metadata` is the standard object's metadata.
        spec: `spec` is the specification of the desired behavior of a FlowSchema.
        status: `status` is the current status of a FlowSchema.

    """

    apiVersion: Literal['flowcontrol.apiserver.k8s.io/v1beta3'] = 'flowcontrol.apiserver.k8s.io/v1beta3'
    kind: Literal['FlowSchema'] = 'FlowSchema'
    metadata: Optional[gybe.k8s.v1_29.meta.v1.ObjectMeta] = None
    spec: Optional[FlowSchemaSpec] = None
    status: Optional[FlowSchemaStatus] = None


@dataclass
class FlowSchemaCondition(K8sSpec):
    """FlowSchemaCondition describes conditions for a FlowSchema.

    Attributes:
        lastTransitionTime: `lastTransitionTime` is the last time the condition transitioned from one status
            to another.
        message: `message` is a human-readable message indicating details about last transition.
        reason: `reason` is a unique, one-word, CamelCase reason for the condition's last transition.
        status: `status` is the status of the condition. Can be True, False, Unknown. Required.
        type: `type` is the type of the condition. Required.

    """

    lastTransitionTime: Optional[str] = None
    message: Optional[str] = None
    reason: Optional[str] = None
    status: Optional[str] = None
    type: Optional[str] = None


@dataclass
class FlowSchemaList(K8sSpec):
    """FlowSchemaList is a list of FlowSchema objects.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        items: `items` is a list of FlowSchemas.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: `metadata` is the standard list metadata.

    """

    items: List[FlowSchema]
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[JSONObj] = None


@dataclass
class FlowSchemaSpec(K8sSpec):
    """FlowSchemaSpec describes how the FlowSchema's specification looks like.

    Attributes:
        distinguisherMethod: `distinguisherMethod` defines how to compute the flow distinguisher for requests
            that match this schema. `nil` specifies that the distinguisher is disabled and thus will always be
            the empty string.
        matchingPrecedence: `matchingPrecedence` is used to choose among the FlowSchemas that match a given
            request. The chosen FlowSchema is among those with the numerically lowest (which we take to be
            logically highest) MatchingPrecedence.  Each MatchingPrecedence value must be ranged in [1,10000].
            Note that if the precedence is not specified, it will be set to 1000 as default.
        priorityLevelConfiguration: `priorityLevelConfiguration` should reference a PriorityLevelConfiguration
            in the cluster. If the reference cannot be resolved, the FlowSchema will be ignored and marked as
            invalid in its status. Required.
        rules: `rules` describes which requests will match this flow schema. This FlowSchema matches a request
            if and only if at least one member of rules matches the request. if it is an empty slice, there
            will be no requests matching the FlowSchema.

    """

    priorityLevelConfiguration: PriorityLevelConfigurationReference
    distinguisherMethod: Optional[FlowDistinguisherMethod] = None
    matchingPrecedence: Optional[int] = None
    rules: Optional[List[PolicyRulesWithSubjects]] = None


@dataclass
class FlowSchemaStatus(K8sSpec):
    """FlowSchemaStatus represents the current state of a FlowSchema.

    Attributes:
        conditions: `conditions` is a list of the current states of FlowSchema.

    """

    conditions: Optional[List[FlowSchemaCondition]] = None


@dataclass
class GroupSubject(K8sSpec):
    """GroupSubject holds detailed information for group-kind subject.

    Attributes:
        name: name is the user group that matches, or '*' to match all user groups. See
            https://github.com/kubernetes/apiserver/blob/master/pkg/authentication/user/user.go for some well-
            known group names. Required.

    """

    name: str


@dataclass
class LimitResponse(K8sSpec):
    """LimitResponse defines how to handle requests that can not be executed right now.

    Attributes:
        queuing: `queuing` holds the configuration parameters for queuing. This field may be non-empty only if
            `type` is `'Queue'`.
        type: `type` is 'Queue' or 'Reject'. 'Queue' means that requests that can not be executed upon arrival
            are held in a queue until they can be executed or a queuing limit is reached. 'Reject' means that
            requests that can not be executed upon arrival are rejected. Required.

    """

    type: str
    queuing: Optional[QueuingConfiguration] = None


@dataclass
class LimitedPriorityLevelConfiguration(K8sSpec):
    """LimitedPriorityLevelConfiguration specifies how to handle requests that are subject to limits. It
    addresses two issues:   - How are requests for this priority level limited?   - What should be done
    with requests that exceed the limit?
    Attributes:
        borrowingLimitPercent: `borrowingLimitPercent`, if present, configures a limit on how many seats this
            priority level can borrow from other priority levels. The limit is known as this level's
            BorrowingConcurrencyLimit (BorrowingCL) and is a limit on the total number of seats that this
            level may borrow at any one time. This field holds the ratio of that limit to the level's nominal
            concurrency limit. When this field is non-nil, it must hold a non-negative integer and the limit
            is calculated as follows.  BorrowingCL(i) = round( NominalCL(i) * borrowingLimitPercent(i)/100.0 )
            The value of this field can be more than 100, implying that this priority level can borrow a
            number of seats that is greater than its own nominal concurrency limit (NominalCL). When this
            field is left `nil`, the limit is effectively infinite.
        lendablePercent: `lendablePercent` prescribes the fraction of the level's NominalCL that can be
            borrowed by other priority levels. The value of this field must be between 0 and 100, inclusive,
            and it defaults to 0. The number of seats that other levels can borrow from this level, known as
            this level's LendableConcurrencyLimit (LendableCL), is defined as follows.  LendableCL(i) = round(
            NominalCL(i) * lendablePercent(i)/100.0 )
        limitResponse: `limitResponse` indicates what to do with requests that can not be executed right now
        nominalConcurrencyShares: `nominalConcurrencyShares` (NCS) contributes to the computation of the
            NominalConcurrencyLimit (NominalCL) of this level. This is the number of execution seats available
            at this priority level. This is used both for requests dispatched from this priority level as well
            as requests dispatched from other priority levels borrowing seats from this level. The server's
            concurrency limit (ServerCL) is divided among the Limited priority levels in proportion to their
            NCS values:  NominalCL(i)  = ceil( ServerCL * NCS(i) / sum_ncs ) sum_ncs = sum[priority level k]
            NCS(k)  Bigger numbers mean a larger nominal concurrency limit, at the expense of every other
            priority level. This field has a default value of 30.

    """

    borrowingLimitPercent: Optional[int] = None
    lendablePercent: Optional[int] = None
    limitResponse: Optional[LimitResponse] = None
    nominalConcurrencyShares: Optional[int] = None


@dataclass
class NonResourcePolicyRule(K8sSpec):
    """NonResourcePolicyRule is a predicate that matches non-resource requests according to their verb and
    the target non-resource URL. A NonResourcePolicyRule matches a request if and only if both (a) at
    least one member of verbs matches the request and (b) at least one member of nonResourceURLs matches
    the request.

    Attributes:
        nonResourceURLs: `nonResourceURLs` is a set of url prefixes that a user should have access to and may
            not be empty. For example:   - '/healthz' is legal   - '/hea*' is illegal   - '/hea' is legal but
            matches nothing   - '/hea/*' also matches nothing   - '/healthz/*' matches all per-component
            health checks. '*' matches all non-resource urls. if it is present, it must be the only entry.
            Required.
        verbs: `verbs` is a list of matching verbs and may not be empty. '*' matches all verbs. If it is
            present, it must be the only entry. Required.

    """

    verbs: List[str]
    nonResourceURLs: List[str]


@dataclass
class PolicyRulesWithSubjects(K8sSpec):
    """PolicyRulesWithSubjects prescribes a test that applies to a request to an apiserver. The test
    considers the subject making the request, the verb being requested, and the resource to be acted upon.
    This PolicyRulesWithSubjects matches a request if and only if both (a) at least one member of subjects
    matches the request and (b) at least one member of resourceRules or nonResourceRules matches the
    request.

    Attributes:
        nonResourceRules: `nonResourceRules` is a list of NonResourcePolicyRules that identify matching
            requests according to their verb and the target non-resource URL.
        resourceRules: `resourceRules` is a slice of ResourcePolicyRules that identify matching requests
            according to their verb and the target resource. At least one of `resourceRules` and
            `nonResourceRules` has to be non-empty.
        subjects: subjects is the list of normal user, serviceaccount, or group that this rule cares about.
            There must be at least one member in this slice. A slice that includes both the
            system:authenticated and system:unauthenticated user groups matches every request. Required.

    """

    subjects: List[Subject]
    nonResourceRules: Optional[List[NonResourcePolicyRule]] = None
    resourceRules: Optional[List[ResourcePolicyRule]] = None


@dataclass
class PriorityLevelConfiguration(K8sResource):
    """PriorityLevelConfiguration represents the configuration of a priority level.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: `metadata` is the standard object's metadata.
        spec: `spec` is the specification of the desired behavior of a 'request-priority'.
        status: `status` is the current status of a 'request-priority'.

    """

    apiVersion: Literal['flowcontrol.apiserver.k8s.io/v1beta3'] = 'flowcontrol.apiserver.k8s.io/v1beta3'
    kind: Literal['PriorityLevelConfiguration'] = 'PriorityLevelConfiguration'
    metadata: Optional[gybe.k8s.v1_29.meta.v1.ObjectMeta] = None
    spec: Optional[PriorityLevelConfigurationSpec] = None
    status: Optional[PriorityLevelConfigurationStatus] = None


@dataclass
class PriorityLevelConfigurationCondition(K8sSpec):
    """PriorityLevelConfigurationCondition defines the condition of priority level.

    Attributes:
        lastTransitionTime: `lastTransitionTime` is the last time the condition transitioned from one status
            to another.
        message: `message` is a human-readable message indicating details about last transition.
        reason: `reason` is a unique, one-word, CamelCase reason for the condition's last transition.
        status: `status` is the status of the condition. Can be True, False, Unknown. Required.
        type: `type` is the type of the condition. Required.

    """

    lastTransitionTime: Optional[str] = None
    message: Optional[str] = None
    reason: Optional[str] = None
    status: Optional[str] = None
    type: Optional[str] = None


@dataclass
class PriorityLevelConfigurationList(K8sSpec):
    """PriorityLevelConfigurationList is a list of PriorityLevelConfiguration objects.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        items: `items` is a list of request-priorities.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: `metadata` is the standard object's metadata.

    """

    items: List[PriorityLevelConfiguration]
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[JSONObj] = None


@dataclass
class PriorityLevelConfigurationReference(K8sSpec):
    """PriorityLevelConfigurationReference contains information that points to the 'request-priority' being
    used.

    Attributes:
        name: `name` is the name of the priority level configuration being referenced Required.

    """

    name: str


@dataclass
class PriorityLevelConfigurationSpec(K8sSpec):
    """PriorityLevelConfigurationSpec specifies the configuration of a priority level.

    Attributes:
        exempt: `exempt` specifies how requests are handled for an exempt priority level. This field MUST be
            empty if `type` is `'Limited'`. This field MAY be non-empty if `type` is `'Exempt'`. If empty and
            `type` is `'Exempt'` then the default values for `ExemptPriorityLevelConfiguration` apply.
        limited: `limited` specifies how requests are handled for a Limited priority level. This field must be
            non-empty if and only if `type` is `'Limited'`.
        type: `type` indicates whether this priority level is subject to limitation on request execution.  A
            value of `'Exempt'` means that requests of this priority level are not subject to a limit (and
            thus are never queued) and do not detract from the capacity made available to other priority
            levels.  A value of `'Limited'` means that (a) requests of this priority level _are_ subject to
            limits and (b) some of the server's limited capacity is made available exclusively to this
            priority level. Required.

    """

    type: str
    exempt: Optional[ExemptPriorityLevelConfiguration] = None
    limited: Optional[LimitedPriorityLevelConfiguration] = None


@dataclass
class PriorityLevelConfigurationStatus(K8sSpec):
    """PriorityLevelConfigurationStatus represents the current state of a 'request-priority'.

    Attributes:
        conditions: `conditions` is the current state of 'request-priority'.

    """

    conditions: Optional[List[PriorityLevelConfigurationCondition]] = None


@dataclass
class QueuingConfiguration(K8sSpec):
    """QueuingConfiguration holds the configuration parameters for queuing
    Attributes:
        handSize: `handSize` is a small positive number that configures the shuffle sharding of requests into
            queues.  When enqueuing a request at this priority level the request's flow identifier (a string
            pair) is hashed and the hash value is used to shuffle the list of queues and deal a hand of the
            size specified here.  The request is put into one of the shortest queues in that hand. `handSize`
            must be no larger than `queues`, and should be significantly smaller (so that a few heavy flows do
            not saturate most of the queues).  See the user-facing documentation for more extensive guidance
            on setting this field.  This field has a default value of 8.
        queueLengthLimit: `queueLengthLimit` is the maximum number of requests allowed to be waiting in a
            given queue of this priority level at a time; excess requests are rejected.  This value must be
            positive.  If not specified, it will be defaulted to 50.
        queues: `queues` is the number of queues for this priority level. The queues exist independently at
            each apiserver. The value must be positive.  Setting it to 1 effectively precludes shufflesharding
            and thus makes the distinguisher method of associated flow schemas irrelevant.  This field has a
            default value of 64.

    """

    handSize: Optional[int] = None
    queueLengthLimit: Optional[int] = None
    queues: Optional[int] = None


@dataclass
class ResourcePolicyRule(K8sSpec):
    """ResourcePolicyRule is a predicate that matches some resource requests, testing the request's verb and
    the target resource. A ResourcePolicyRule matches a resource request if and only if: (a) at least one
    member of verbs matches the request, (b) at least one member of apiGroups matches the request, (c) at
    least one member of resources matches the request, and (d) either (d1) the request does not specify a
    namespace (i.e., `Namespace==''`) and clusterScope is true or (d2) the request specifies a namespace
    and least one member of namespaces matches the request's namespace.

    Attributes:
        apiGroups: `apiGroups` is a list of matching API groups and may not be empty. '*' matches all API
            groups and, if present, must be the only entry. Required.
        clusterScope: `clusterScope` indicates whether to match requests that do not specify a namespace
            (which happens either because the resource is not namespaced or the request targets all
            namespaces). If this field is omitted or false then the `namespaces` field must contain a non-
            empty list.
        namespaces: `namespaces` is a list of target namespaces that restricts matches.  A request that
            specifies a target namespace matches only if either (a) this list contains that target namespace
            or (b) this list contains '*'.  Note that '*' matches any specified namespace but does not match a
            request that _does not specify_ a namespace (see the `clusterScope` field for that). This list may
            be empty, but only if `clusterScope` is true.
        resources: `resources` is a list of matching resources (i.e., lowercase and plural) with, if desired,
            subresource.  For example, [ 'services', 'nodes/status' ].  This list may not be empty. '*'
            matches all resources and, if present, must be the only entry. Required.
        verbs: `verbs` is a list of matching verbs and may not be empty. '*' matches all verbs and, if
            present, must be the only entry. Required.

    """

    verbs: List[str]
    apiGroups: List[str]
    resources: List[str]
    clusterScope: Optional[bool] = None
    namespaces: Optional[List[str]] = None


@dataclass
class ServiceAccountSubject(K8sSpec):
    """ServiceAccountSubject holds detailed information for service-account-kind subject.

    Attributes:
        name: `name` is the name of matching ServiceAccount objects, or '*' to match regardless of name.
            Required.
        namespace: `namespace` is the namespace of matching ServiceAccount objects. Required.

    """

    namespace: str
    name: str


@dataclass
class Subject(K8sSpec):
    """Subject matches the originator of a request, as identified by the request authentication system. There
    are three ways of matching an originator; by user, group, or service account.

    Attributes:
        group: `group` matches based on user group name.
        kind: `kind` indicates which one of the other fields is non-empty. Required
        serviceAccount: `serviceAccount` matches ServiceAccounts.
        user: `user` matches based on username.

    """

    kind: str
    group: Optional[GroupSubject] = None
    serviceAccount: Optional[ServiceAccountSubject] = None
    user: Optional[UserSubject] = None


@dataclass
class UserSubject(K8sSpec):
    """UserSubject holds detailed information for user-kind subject.

    Attributes:
        name: `name` is the username that matches, or '*' to match all usernames. Required.

    """

    name: str
