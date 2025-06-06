"""Models generated from Kubernetes OpenAPI Spec."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Literal, Optional

import gybe.k8s.v1_33.meta.v1
from gybe.k8s.types import K8sResource, K8sSpec


@dataclass
class AuditAnnotation(K8sSpec):
    """AuditAnnotation describes how to produce an audit annotation for an API request.

    Attributes:
        key: key specifies the audit annotation key. The audit annotation keys of a ValidatingAdmissionPolicy
            must be unique. The key must be a qualified name ([A-Za-z0-9][-A-Za-z0-9_.]*) no more than 63
            bytes in length.  The key is combined with the resource name of the ValidatingAdmissionPolicy to
            construct an audit annotation key: '{ValidatingAdmissionPolicy name}/{key}'.  If an admission
            webhook uses the same resource name as this ValidatingAdmissionPolicy and the same audit
            annotation key, the annotation key will be identical. In this case, the first annotation written
            with the key will be included in the audit event and all subsequent annotations with the same key
            will be discarded.  Required.
        valueExpression: valueExpression represents the expression which is evaluated by CEL to produce an
            audit annotation value. The expression must evaluate to either a string or null value. If the
            expression evaluates to a string, the audit annotation is included with the string value. If the
            expression evaluates to null or empty string the audit annotation will be omitted. The
            valueExpression may be no longer than 5kb in length. If the result of the valueExpression is more
            than 10kb in length, it will be truncated to 10kb.  If multiple ValidatingAdmissionPolicyBinding
            resources match an API request, then the valueExpression will be evaluated for each binding. All
            unique values produced by the valueExpressions will be joined together in a comma-separated list.
            Required.

    """

    key: str
    valueExpression: str


@dataclass
class ExpressionWarning(K8sSpec):
    """ExpressionWarning is a warning information that targets a specific expression.

    Attributes:
        fieldRef: The path to the field that refers the expression. For example, the reference to the
            expression of the first item of validations is 'spec.validations[0].expression'
        warning: The content of type checking information in a human-readable form. Each line of the warning
            contains the type that the expression is checked against, followed by the type check error from
            the compiler.

    """

    fieldRef: str
    warning: str


@dataclass
class MatchCondition(K8sSpec):
    """MatchCondition represents a condition which must be fulfilled for a request to be sent to a webhook.

    Attributes:
        expression: Expression represents the expression which will be evaluated by CEL. Must evaluate to
            bool. CEL expressions have access to the contents of the AdmissionRequest and Authorizer,
            organized into CEL variables:  'object' - The object from the incoming request. The value is null
            for DELETE requests. 'oldObject' - The existing object. The value is null for CREATE requests.
            'request' - Attributes of the admission request(/pkg/apis/admission/types.go#AdmissionRequest).
            'authorizer' - A CEL Authorizer. May be used to perform authorization checks for the principal
            (user or service account) of the request.   See
            https://pkg.go.dev/k8s.io/apiserver/pkg/cel/library#Authz 'authorizer.requestResource' - A CEL
            ResourceCheck constructed from the 'authorizer' and configured with the   request resource.
            Documentation on CEL: https://kubernetes.io/docs/reference/using-api/cel/  Required.
        name: Name is an identifier for this match condition, used for strategic merging of MatchConditions,
            as well as providing an identifier for logging purposes. A good name should be descriptive of the
            associated expression. Name must be a qualified name consisting of alphanumeric characters, '-',
            '_' or '.', and must start and end with an alphanumeric character (e.g. 'MyName',  or 'my.name',
            or '123-abc', regex used for validation is '([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9]') with an
            optional DNS subdomain prefix and '/' (e.g. 'example.com/MyName')  Required.

    """

    name: str
    expression: str


@dataclass
class MatchResources(K8sSpec):
    """MatchResources decides whether to run the admission control policy on an object based on whether it
    meets the match criteria. The exclude rules take precedence over include rules (if a resource matches
    both, it is excluded)

    Attributes:
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
    namespaceSelector: Optional[gybe.k8s.v1_33.meta.v1.LabelSelector] = None
    objectSelector: Optional[gybe.k8s.v1_33.meta.v1.LabelSelector] = None
    resourceRules: Optional[List[NamedRuleWithOperations]] = None


@dataclass
class NamedRuleWithOperations(K8sSpec):
    """NamedRuleWithOperations is a tuple of Operations and Resources with ResourceNames.

    Attributes:
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

    Attributes:
        apiVersion: APIVersion is the API group version the resources belong to. In format of 'group/version'.
            Required.
        kind: Kind is the API kind the resources belong to. Required.

    """

    apiVersion: Optional[str] = None
    kind: Optional[str] = None


@dataclass
class ParamRef(K8sSpec):
    """ParamRef describes how to locate the params to be used as input to expressions of rules applied by a
    policy binding.

    Attributes:
        name: name is the name of the resource being referenced.  One of `name` or `selector` must be set, but
            `name` and `selector` are mutually exclusive properties. If one is set, the other must be unset.
            A single parameter used for all admission requests can be configured by setting the `name` field,
            leaving `selector` blank, and setting namespace if `paramKind` is namespace-scoped.
        namespace: namespace is the namespace of the referenced resource. Allows limiting the search for
            params to a specific namespace. Applies to both `name` and `selector` fields.  A per-namespace
            parameter may be used by specifying a namespace-scoped `paramKind` in the policy and leaving this
            field empty.  - If `paramKind` is cluster-scoped, this field MUST be unset. Setting this field
            results in a configuration error.  - If `paramKind` is namespace-scoped, the namespace of the
            object being evaluated for admission will be used when this field is left unset. Take care that if
            this is left empty the binding must not match any cluster-scoped resources, which will result in
            an error.
        parameterNotFoundAction: `parameterNotFoundAction` controls the behavior of the binding when the
            resource exists, and name or selector is valid, but there are no parameters matched by the
            binding. If the value is set to `Allow`, then no matched parameters will be treated as successful
            validation by the binding. If set to `Deny`, then no matched parameters will be subject to the
            `failurePolicy` of the policy.  Allowed values are `Allow` or `Deny`  Required
        selector: selector can be used to match multiple param objects based on their labels. Supply selector:
            {} to match all resources of the ParamKind.  If multiple params are found, they are all evaluated
            with the policy expressions and the results are ANDed together.  One of `name` or `selector` must
            be set, but `name` and `selector` are mutually exclusive properties. If one is set, the other must
            be unset.

    """

    name: Optional[str] = None
    namespace: Optional[str] = None
    parameterNotFoundAction: Optional[str] = None
    selector: Optional[gybe.k8s.v1_33.meta.v1.LabelSelector] = None


@dataclass
class TypeChecking(K8sSpec):
    """TypeChecking contains results of type checking the expressions in the ValidatingAdmissionPolicy
    Attributes:
        expressionWarnings: The type checking warnings for each expression.

    """

    expressionWarnings: Optional[List[ExpressionWarning]] = None


@dataclass
class ValidatingAdmissionPolicy(K8sResource):
    """ValidatingAdmissionPolicy describes the definition of an admission validation policy that accepts or
    rejects an object without changing it.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object metadata;
        spec: Specification of the desired behavior of the ValidatingAdmissionPolicy.
        status: The status of the ValidatingAdmissionPolicy, including warnings that are useful to determine
            if the policy behaves in the expected way. Populated by the system. Read-only.

    """

    apiVersion: Literal['admissionregistration.k8s.io/v1beta1'] = 'admissionregistration.k8s.io/v1beta1'
    kind: Literal['ValidatingAdmissionPolicy'] = 'ValidatingAdmissionPolicy'
    metadata: Optional[gybe.k8s.v1_33.meta.v1.ObjectMeta] = None
    spec: Optional[ValidatingAdmissionPolicySpec] = None
    status: Optional[ValidatingAdmissionPolicyStatus] = None


@dataclass
class ValidatingAdmissionPolicyBinding(K8sResource):
    """ValidatingAdmissionPolicyBinding binds the ValidatingAdmissionPolicy with paramerized resources.
    ValidatingAdmissionPolicyBinding and parameter CRDs together define how cluster administrators
    configure policies for clusters.  For a given admission request, each binding will cause its policy to
    be evaluated N times, where N is 1 for policies/bindings that don't use params, otherwise N is the
    number of parameters selected by the binding.  The CEL expressions of a policy must have a computed
    CEL cost below the maximum CEL budget. Each evaluation of the policy is given an independent CEL cost
    budget. Adding/removing policies, bindings, or params can not affect whether a given (policy, binding,
    param) combination is within its own CEL budget.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object metadata;
        spec: Specification of the desired behavior of the ValidatingAdmissionPolicyBinding.

    """

    apiVersion: Literal['admissionregistration.k8s.io/v1beta1'] = 'admissionregistration.k8s.io/v1beta1'
    kind: Literal['ValidatingAdmissionPolicyBinding'] = 'ValidatingAdmissionPolicyBinding'
    metadata: Optional[gybe.k8s.v1_33.meta.v1.ObjectMeta] = None
    spec: Optional[ValidatingAdmissionPolicyBindingSpec] = None


@dataclass
class ValidatingAdmissionPolicyBindingSpec(K8sSpec):
    """ValidatingAdmissionPolicyBindingSpec is the specification of the ValidatingAdmissionPolicyBinding.

    Attributes:
        matchResources: MatchResources declares what resources match this binding and will be validated by it.
            Note that this is intersected with the policy's matchConstraints, so only requests that are
            matched by the policy can be selected by this. If this is unset, all resources matched by the
            policy are validated by this binding When resourceRules is unset, it does not constrain resource
            matching. If a resource is matched by the other fields of this object, it will be validated. Note
            that this is differs from ValidatingAdmissionPolicy matchConstraints, where resourceRules are
            required.
        paramRef: paramRef specifies the parameter resource used to configure the admission control policy. It
            should point to a resource of the type specified in ParamKind of the bound
            ValidatingAdmissionPolicy. If the policy specifies a ParamKind and the resource referred to by
            ParamRef does not exist, this binding is considered mis-configured and the FailurePolicy of the
            ValidatingAdmissionPolicy applied. If the policy does not specify a ParamKind then this field is
            ignored, and the rules are evaluated without a param.
        policyName: PolicyName references a ValidatingAdmissionPolicy name which the
            ValidatingAdmissionPolicyBinding binds to. If the referenced resource does not exist, this binding
            is considered invalid and will be ignored Required.
        validationActions: validationActions declares how Validations of the referenced
            ValidatingAdmissionPolicy are enforced. If a validation evaluates to false it is always enforced
            according to these actions.  Failures defined by the ValidatingAdmissionPolicy's FailurePolicy are
            enforced according to these actions only if the FailurePolicy is set to Fail, otherwise the
            failures are ignored. This includes compilation errors, runtime errors and misconfigurations of
            the policy.  validationActions is declared as a set of action values. Order does not matter.
            validationActions may not contain duplicates of the same action.  The supported actions values
            are:  'Deny' specifies that a validation failure results in a denied request.  'Warn' specifies
            that a validation failure is reported to the request client in HTTP Warning headers, with a
            warning code of 299. Warnings can be sent both for allowed or denied admission responses.  'Audit'
            specifies that a validation failure is included in the published audit event for the request. The
            audit event will contain a `validation.policy.admission.k8s.io/validation_failure` audit
            annotation with a value containing the details of the validation failures, formatted as a JSON
            list of objects, each with the following fields: - message: The validation failure message string
            - policy: The resource name of the ValidatingAdmissionPolicy - binding: The resource name of the
            ValidatingAdmissionPolicyBinding - expressionIndex: The index of the failed validations in the
            ValidatingAdmissionPolicy - validationActions: The enforcement actions enacted for the validation
            failure Example audit annotation: `'validation.policy.admission.k8s.io/validation_failure':
            '[{'message': 'Invalid value', {'policy': 'policy.example.com', {'binding':
            'policybinding.example.com', {'expressionIndex': '1', {'validationActions':
            ['Audit']}]'`  Clients should expect to handle additional values by ignoring any values not
            recognized.  'Deny' and 'Warn' may not be used together since this combination needlessly
            duplicates the validation failure both in the API response body and the HTTP warning headers.
            Required.

    """

    matchResources: Optional[MatchResources] = None
    paramRef: Optional[ParamRef] = None
    policyName: Optional[str] = None
    validationActions: Optional[List[str]] = None


@dataclass
class ValidatingAdmissionPolicySpec(K8sSpec):
    """ValidatingAdmissionPolicySpec is the specification of the desired behavior of the AdmissionPolicy.

    Attributes:
        auditAnnotations: auditAnnotations contains CEL expressions which are used to produce audit
            annotations for the audit event of the API request. validations and auditAnnotations may not both
            be empty; a least one of validations or auditAnnotations is required.
        failurePolicy: failurePolicy defines how to handle failures for the admission policy. Failures can
            occur from CEL expression parse errors, type check errors, runtime errors and invalid or mis-
            configured policy definitions or bindings.  A policy is invalid if spec.paramKind refers to a non-
            existent Kind. A binding is invalid if spec.paramRef.name refers to a non-existent resource.
            failurePolicy does not define how validations that evaluate to false are handled.  When
            failurePolicy is set to Fail, ValidatingAdmissionPolicyBinding validationActions define how
            failures are enforced.  Allowed values are Ignore or Fail. Defaults to Fail.
        matchConditions: MatchConditions is a list of conditions that must be met for a request to be
            validated. Match conditions filter requests that have already been matched by the rules,
            namespaceSelector, and objectSelector. An empty list of matchConditions matches all requests.
            There are a maximum of 64 match conditions allowed.  If a parameter object is provided, it can be
            accessed via the `params` handle in the same manner as validation expressions.  The exact matching
            logic is (in order):   1. If ANY matchCondition evaluates to FALSE, the policy is skipped.   2. If
            ALL matchConditions evaluate to TRUE, the policy is evaluated.   3. If any matchCondition
            evaluates to an error (but none are FALSE):      - If failurePolicy=Fail, reject the request
            - If failurePolicy=Ignore, the policy is skipped
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
        validations: Validations contain CEL expressions which is used to apply the validation. Validations
            and AuditAnnotations may not both be empty; a minimum of one Validations or AuditAnnotations is
            required.
        variables: Variables contain definitions of variables that can be used in composition of other
            expressions. Each variable is defined as a named CEL expression. The variables defined here will
            be available under `variables` in other expressions of the policy except MatchConditions because
            MatchConditions are evaluated before the rest of the policy.  The expression of a variable can
            refer to other variables defined earlier in the list but not those after. Thus, Variables must be
            sorted by the order of first appearance and acyclic.

    """

    auditAnnotations: Optional[List[AuditAnnotation]] = None
    failurePolicy: Optional[str] = None
    matchConditions: Optional[List[MatchCondition]] = None
    matchConstraints: Optional[MatchResources] = None
    paramKind: Optional[ParamKind] = None
    validations: Optional[List[Validation]] = None
    variables: Optional[List[Variable]] = None


@dataclass
class ValidatingAdmissionPolicyStatus(K8sSpec):
    """ValidatingAdmissionPolicyStatus represents the status of an admission validation policy.

    Attributes:
        conditions: The conditions represent the latest available observations of a policy's current state.
        observedGeneration: The generation observed by the controller.
        typeChecking: The results of type checking for each expression. Presence of this field indicates the
            completion of the type checking.

    """

    conditions: Optional[List[gybe.k8s.v1_33.meta.v1.Condition]] = None
    observedGeneration: Optional[int] = None
    typeChecking: Optional[TypeChecking] = None


@dataclass
class Validation(K8sSpec):
    """Validation specifies the CEL expression which is used to apply the validation.

    Attributes:
        expression: Expression represents the expression which will be evaluated by CEL. ref:
            https://github.com/google/cel-spec CEL expressions have access to the contents of the API
            request/response, organized into CEL variables as well as some other useful variables:  - 'object'
            - The object from the incoming request. The value is null for DELETE requests. - 'oldObject' - The
            existing object. The value is null for CREATE requests. - 'request' - Attributes of the API
            request([ref](/pkg/apis/admission/types.go#AdmissionRequest)). - 'params' - Parameter resource
            referred to by the policy binding being evaluated. Only populated if the policy has a ParamKind. -
            'namespaceObject' - The namespace object that the incoming object belongs to. The value is null
            for cluster-scoped resources. - 'variables' - Map of composited variables, from its name to its
            lazily evaluated value.   For example, a variable named 'foo' can be accessed as 'variables.foo'.
            - 'authorizer' - A CEL Authorizer. May be used to perform authorization checks for the principal
            (user or service account) of the request.   See
            https://pkg.go.dev/k8s.io/apiserver/pkg/cel/library#Authz - 'authorizer.requestResource' - A CEL
            ResourceCheck constructed from the 'authorizer' and configured with the   request resource.  The
            `apiVersion`, `kind`, `metadata.name` and `metadata.generateName` are always accessible from the
            root of the object. No other metadata properties are accessible.  Only property names of the form
            `[a-zA-Z_.-/][a-zA-Z0-9_.-/]*` are accessible. Accessible property names are escaped according to
            the following rules when accessed in the expression: - '__' escapes to '__underscores__' - '.'
            escapes to '__dot__' - '-' escapes to '__dash__' - '/' escapes to '__slash__' - Property names
            that exactly match a CEL RESERVED keyword escape to '__{keyword}__'. The keywords are:
            'true', 'false', 'null', 'in', 'as', 'break', 'const', 'continue', 'else', 'for', 'function',
            'if',           'import', 'let', 'loop', 'package', 'namespace', 'return'. Examples:   -
            Expression accessing a property named 'namespace': {'Expression': 'object.__namespace__ > 0'}   -
            Expression accessing a property named 'x-prop': {'Expression': 'object.x__dash__prop > 0'}   -
            Expression accessing a property named 'redact__d': {'Expression': 'object.redact__underscores__d >
            0'}  Equality on arrays with list type of 'set' or 'map' ignores element order, i.e. [1, 2] == [2,
            1]. Concatenation on arrays with x-kubernetes-list-type use the semantics of the list type:   -
            'set': `X + Y` performs a union where the array positions of all elements in `X` are preserved and
            non-intersecting elements in `Y` are appended, retaining their partial order.   - 'map': `X + Y`
            performs a merge where the array positions of all keys in `X` are preserved but the values     are
            overwritten by values in `Y` when the key sets of `X` and `Y` intersect. Elements in `Y` with
            non-intersecting keys are appended, retaining their partial order. Required.
        message: Message represents the message displayed when validation fails. The message is required if
            the Expression contains line breaks. The message must not contain line breaks. If unset, the
            message is 'failed rule: {Rule}'. e.g. 'must be a URL with the host matching spec.host' If the
            Expression contains line breaks. Message is required. The message must not contain line breaks. If
            unset, the message is 'failed Expression: {Expression}'.
        messageExpression: messageExpression declares a CEL expression that evaluates to the validation
            failure message that is returned when this rule fails. Since messageExpression is used as a
            failure message, it must evaluate to a string. If both message and messageExpression are present
            on a validation, then messageExpression will be used if validation fails. If messageExpression
            results in a runtime error, the runtime error is logged, and the validation failure message is
            produced as if the messageExpression field were unset. If messageExpression evaluates to an empty
            string, a string with only spaces, or a string that contains line breaks, then the validation
            failure message will also be produced as if the messageExpression field were unset, and the fact
            that messageExpression produced an empty string/string with only spaces/string with line breaks
            will be logged. messageExpression has access to all the same variables as the `expression` except
            for 'authorizer' and 'authorizer.requestResource'. Example: 'object.x must be less than max
            ('+string(params.max)+')'
        reason: Reason represents a machine-readable description of why this validation failed. If this is the
            first validation in the list to fail, this reason, as well as the corresponding HTTP response
            code, are used in the HTTP response to the client. The currently supported reasons are:
            'Unauthorized', 'Forbidden', 'Invalid', 'RequestEntityTooLarge'. If not set, StatusReasonInvalid
            is used in the response to the client.

    """

    expression: str
    message: Optional[str] = None
    messageExpression: Optional[str] = None
    reason: Optional[str] = None


@dataclass
class Variable(K8sSpec):
    """Variable is the definition of a variable that is used for composition. A variable is defined as a
    named expression.

    Attributes:
        expression: Expression is the expression that will be evaluated as the value of the variable. The CEL
            expression has access to the same identifiers as the CEL expressions in Validation.
        name: Name is the name of the variable. The name must be a valid CEL identifier and unique among all
            variables. The variable can be accessed in other expressions through `variables` For example, if
            name is 'foo', the variable will be available as `variables.foo`

    """

    name: str
    expression: str
