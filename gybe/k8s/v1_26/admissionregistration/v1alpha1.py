"""Models generated from Kubernetes OpenAPI Spec."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

import gybe.k8s.v1_26.meta.v1
from gybe.k8s.types import JSONObj, K8sSpec


@dataclass
class MatchResources(K8sSpec):
    """MatchResources decides whether to run the admission control policy on an object based on whether it
    meets the match criteria. The exclude rules take precedence over include rules (if a resource matches
    both, it is excluded)

    Attributes
    ----------
        excludeResourceRules: ExcludeResourceRules describes what operations on what resources/subresources
            the ValidatingAdmissionPolicy should not care about. The exclude rules take precedence over
            include rules (if a resource matches both, it is excluded)
        matchPolicy: matchPolicy defines how the 'MatchResources' list is used to match incoming requests.
            Allowed values are 'Exact' or 'Equivalent'.  - Exact: match a request only if it exactly matches a
            specified rule. For example, if deployments can be modified via apps/v1, apps/v1beta1, and
            extensions/v1beta1, but 'rules' only included `apiGroups:['apps'], apiVersions:['v1'], resources:
            ['deployments']`, a request to apps/v1beta1 or extensions/v1beta1 would not be sent to the
            ValidatingAdmissionPolicy.  - Equivalent: match a request if modifies a resource listed in rules,
            even via another API group or version. For example, if deployments can be modified via apps/v1,
            apps/v1beta1, and extensions/v1beta1, and 'rules' only included `apiGroups:['apps'],
            apiVersions:['v1'], resources: ['deployments']`, a request to apps/v1beta1 or extensions/v1beta1
            would be converted to apps/v1 and sent to the ValidatingAdmissionPolicy.  Defaults to 'Equivalent'
        namespaceSelector: NamespaceSelector decides whether to run the admission control policy on an object
            based on whether the namespace for that object matches the selector. If the object itself is a
            namespace, the matching is performed on object.metadata.labels. If the object is another cluster
            scoped resource, it never skips the policy.  For example, to run the webhook on any objects whose
            namespace is not associated with 'runlevel' of '0' or '1';  you will set the selector as follows:
            'namespaceSelector': {   'matchExpressions': [     {       'key': 'runlevel',       'operator':
            'NotIn',       'values': [         '0',         '1'       ]     }   ] }  If instead you want to
            only run the policy on any objects whose namespace is associated with the 'environment' of 'prod'
            or 'staging'; you will set the selector as follows: 'namespaceSelector': {   'matchExpressions': [
            {       'key': 'environment',       'operator': 'In',       'values': [         'prod',
            'staging'       ]     }   ] }  See https://kubernetes.io/docs/concepts/overview/working-with-
            objects/labels/ for more examples of label selectors.  Default to the empty LabelSelector, which
            matches everything.
        objectSelector: ObjectSelector decides whether to run the validation based on if the object has
            matching labels. objectSelector is evaluated against both the oldObject and newObject that would
            be sent to the cel validation, and is considered to match if either object matches the selector. A
            null object (oldObject in the case of create, or newObject in the case of delete) or an object
            that cannot have labels (like a DeploymentRollback or a PodProxyOptions object) is not considered
            to match. Use the object selector only if the webhook is opt-in, because end users may skip the
            admission webhook by setting the labels. Default to the empty LabelSelector, which matches
            everything.
        resourceRules: ResourceRules describes what operations on what resources/subresources the
            ValidatingAdmissionPolicy matches. The policy cares about an operation if it matches _any_ Rule.

    """

    excludeResourceRules: Optional[List[NamedRuleWithOperations]] = None
    matchPolicy: Optional[str] = None
    namespaceSelector: Optional[gybe.k8s.v1_26.meta.v1.LabelSelector] = None
    objectSelector: Optional[gybe.k8s.v1_26.meta.v1.LabelSelector] = None
    resourceRules: Optional[List[NamedRuleWithOperations]] = None


@dataclass
class NamedRuleWithOperations(K8sSpec):
    """NamedRuleWithOperations is a tuple of Operations and Resources with ResourceNames.

    Attributes
    ----------
        apiGroups: APIGroups is the API groups the resources belong to. '*' is all groups. If '*' is present,
            the length of the slice must be one. Required.
        apiVersions: APIVersions is the API versions the resources belong to. '*' is all versions. If '*' is
            present, the length of the slice must be one. Required.
        operations: Operations is the operations the admission hook cares about - CREATE, UPDATE, DELETE,
            CONNECT or * for all of those operations and any future admission operations that are added. If
            '*' is present, the length of the slice must be one. Required.
        resourceNames: ResourceNames is an optional white list of names that the rule applies to.  An empty
            set means that everything is allowed.
        resources: Resources is a list of resources this rule applies to.  For example: 'pods' means pods.
            'pods/log' means the log subresource of pods. '*' means all resources, but not subresources.
            'pods/*' means all subresources of pods. '*/scale' means all scale subresources. '*/*' means all
            resources and their subresources.  If wildcard is present, the validation rule will ensure
            resources do not overlap with each other.  Depending on the enclosing object, subresources might
            not be allowed. Required.
        scope: scope specifies the scope of this rule. Valid values are 'Cluster', 'Namespaced', and '*'
            'Cluster' means that only cluster-scoped resources will match this rule. Namespace API objects are
            cluster-scoped. 'Namespaced' means that only namespaced resources will match this rule. '*' means
            that there are no scope restrictions. Subresources match the scope of their parent resource.
            Default is '*'.

    """

    apiGroups: Optional[List[str]] = None
    apiVersions: Optional[List[str]] = None
    operations: Optional[List[str]] = None
    resourceNames: Optional[List[str]] = None
    resources: Optional[List[str]] = None
    scope: Optional[str] = None


@dataclass
class ParamKind(K8sSpec):
    """ParamKind is a tuple of Group Kind and Version.

    Attributes
    ----------
        apiVersion: APIVersion is the API group version the resources belong to. In format of 'group/version'.
            Required.
        kind: Kind is the API kind the resources belong to. Required.

    """

    apiVersion: Optional[str] = None
    kind: Optional[str] = None


@dataclass
class ParamRef(K8sSpec):
    """ParamRef references a parameter resource
    Attributes:
        name: Name of the resource being referenced.
        namespace: Namespace of the referenced resource. Should be empty for the cluster-scoped resources

    """

    name: Optional[str] = None
    namespace: Optional[str] = None


@dataclass
class ValidatingAdmissionPolicy(K8sSpec):
    """ValidatingAdmissionPolicy describes the definition of an admission validation policy that accepts or
    rejects an object without changing it.

    Attributes
    ----------
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object metadata;
        spec: Specification of the desired behavior of the ValidatingAdmissionPolicy.

    """

    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[gybe.k8s.v1_26.meta.v1.ObjectMeta] = None
    spec: Optional[ValidatingAdmissionPolicySpec] = None


@dataclass
class ValidatingAdmissionPolicyBinding(K8sSpec):
    """ValidatingAdmissionPolicyBinding binds the ValidatingAdmissionPolicy with paramerized resources.
    ValidatingAdmissionPolicyBinding and parameter CRDs together define how cluster administrators
    configure policies for clusters.

    Attributes
    ----------
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object metadata;
        spec: Specification of the desired behavior of the ValidatingAdmissionPolicyBinding.

    """

    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[gybe.k8s.v1_26.meta.v1.ObjectMeta] = None
    spec: Optional[ValidatingAdmissionPolicyBindingSpec] = None


@dataclass
class ValidatingAdmissionPolicyBindingList(K8sSpec):
    """ValidatingAdmissionPolicyBindingList is a list of ValidatingAdmissionPolicyBinding.

    Attributes
    ----------
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        items: List of PolicyBinding.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard list metadata.

    """

    apiVersion: Optional[str] = None
    items: Optional[List[ValidatingAdmissionPolicyBinding]] = None
    kind: Optional[str] = None
    metadata: Optional[JSONObj] = None


@dataclass
class ValidatingAdmissionPolicyBindingSpec(K8sSpec):
    """ValidatingAdmissionPolicyBindingSpec is the specification of the ValidatingAdmissionPolicyBinding.

    Attributes
    ----------
        matchResources: MatchResources declares what resources match this binding and will be validated by it.
            Note that this is intersected with the policy's matchConstraints, so only requests that are
            matched by the policy can be selected by this. If this is unset, all resources matched by the
            policy are validated by this binding When resourceRules is unset, it does not constrain resource
            matching. If a resource is matched by the other fields of this object, it will be validated. Note
            that this is differs from ValidatingAdmissionPolicy matchConstraints, where resourceRules are
            required.
        paramRef: ParamRef specifies the parameter resource used to configure the admission control policy. It
            should point to a resource of the type specified in ParamKind of the bound
            ValidatingAdmissionPolicy. If the policy specifies a ParamKind and the resource referred to by
            ParamRef does not exist, this binding is considered mis-configured and the FailurePolicy of the
            ValidatingAdmissionPolicy applied.
        policyName: PolicyName references a ValidatingAdmissionPolicy name which the
            ValidatingAdmissionPolicyBinding binds to. If the referenced resource does not exist, this binding
            is considered invalid and will be ignored Required.

    """

    matchResources: Optional[MatchResources] = None
    paramRef: Optional[ParamRef] = None
    policyName: Optional[str] = None


@dataclass
class ValidatingAdmissionPolicyList(K8sSpec):
    """ValidatingAdmissionPolicyList is a list of ValidatingAdmissionPolicy.

    Attributes
    ----------
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        items: List of ValidatingAdmissionPolicy.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard list metadata.

    """

    apiVersion: Optional[str] = None
    items: Optional[List[ValidatingAdmissionPolicy]] = None
    kind: Optional[str] = None
    metadata: Optional[JSONObj] = None


@dataclass
class ValidatingAdmissionPolicySpec(K8sSpec):
    """ValidatingAdmissionPolicySpec is the specification of the desired behavior of the AdmissionPolicy.

    Attributes
    ----------
        failurePolicy: FailurePolicy defines how to handle failures for the admission policy. Failures can
            occur from invalid or mis-configured policy definitions or bindings. A policy is invalid if
            spec.paramKind refers to a non-existent Kind. A binding is invalid if spec.paramRef.name refers to
            a non-existent resource. Allowed values are Ignore or Fail. Defaults to Fail.
        matchConstraints: MatchConstraints specifies what resources this policy is designed to validate. The
            AdmissionPolicy cares about a request if it matches _all_ Constraints. However, in order to
            prevent clusters from being put into an unstable state that cannot be recovered from via the API
            ValidatingAdmissionPolicy cannot match ValidatingAdmissionPolicy and
            ValidatingAdmissionPolicyBinding. Required.
        paramKind: ParamKind specifies the kind of resources used to parameterize this policy. If absent,
            there are no parameters for this policy and the param CEL variable will not be provided to
            validation expressions. If ParamKind refers to a non-existent kind, this policy definition is mis-
            configured and the FailurePolicy is applied. If paramKind is specified but paramRef is unset in
            ValidatingAdmissionPolicyBinding, the params variable will be null.
        validations: Validations contain CEL expressions which is used to apply the validation. A minimum of
            one validation is required for a policy definition. Required.

    """

    validations: List[Validation]
    failurePolicy: Optional[str] = None
    matchConstraints: Optional[MatchResources] = None
    paramKind: Optional[ParamKind] = None


@dataclass
class Validation(K8sSpec):
    """Validation specifies the CEL expression which is used to apply the validation.

    Attributes
    ----------
        expression: Expression represents the expression which will be evaluated by CEL. ref:
            https://github.com/google/cel-spec CEL expressions have access to the contents of the Admission
            request/response, organized into CEL variables as well as some other useful variables:  'object' -
            The object from the incoming request. The value is null for DELETE requests. 'oldObject' - The
            existing object. The value is null for CREATE requests. 'request' - Attributes of the admission
            request([ref](/pkg/apis/admission/types.go#AdmissionRequest)). 'params' - Parameter resource
            referred to by the policy binding being evaluated. Only populated if the policy has a ParamKind.
            The `apiVersion`, `kind`, `metadata.name` and `metadata.generateName` are always accessible from
            the root of the object. No other metadata properties are accessible.  Only property names of the
            form `[a-zA-Z_.-/][a-zA-Z0-9_.-/]*` are accessible. Accessible property names are escaped
            according to the following rules when accessed in the expression: - '__' escapes to
            '__underscores__' - '.' escapes to '__dot__' - '-' escapes to '__dash__' - '/' escapes to
            '__slash__' - Property names that exactly match a CEL RESERVED keyword escape to '__{keyword}__'.
            The keywords are:           'true', 'false', 'null', 'in', 'as', 'break', 'const', 'continue',
            'else', 'for', 'function', 'if',           'import', 'let', 'loop', 'package', 'namespace',
            'return'. Examples:   - Expression accessing a property named 'namespace': {'Expression':
            'object.__namespace__ > 0'}   - Expression accessing a property named 'x-prop': {'Expression':
            'object.x__dash__prop > 0'}   - Expression accessing a property named 'redact__d': {'Expression':
            'object.redact__underscores__d > 0'}  Equality on arrays with list type of 'set' or 'map' ignores
            element order, i.e. [1, 2] == [2, 1]. Concatenation on arrays with x-kubernetes-list-type use the
            semantics of the list type:   - 'set': `X + Y` performs a union where the array positions of all
            elements in `X` are preserved and     non-intersecting elements in `Y` are appended, retaining
            their partial order.   - 'map': `X + Y` performs a merge where the array positions of all keys in
            `X` are preserved but the values     are overwritten by values in `Y` when the key sets of `X` and
            `Y` intersect. Elements in `Y` with     non-intersecting keys are appended, retaining their
            partial order. Required.
        message: Message represents the message displayed when validation fails. The message is required if
            the Expression contains line breaks. The message must not contain line breaks. If unset, the
            message is 'failed rule: {Rule}'. e.g. 'must be a URL with the host matching spec.host' If the
            Expression contains line breaks. Message is required. The message must not contain line breaks. If
            unset, the message is 'failed Expression: {Expression}'.
        reason: Reason represents a machine-readable description of why this validation failed. If this is the
            first validation in the list to fail, this reason, as well as the corresponding HTTP response
            code, are used in the HTTP response to the client. The currently supported reasons are:
            'Unauthorized', 'Forbidden', 'Invalid', 'RequestEntityTooLarge'. If not set, StatusReasonInvalid
            is used in the response to the client.

    """

    expression: str
    message: Optional[str] = None
    reason: Optional[str] = None
