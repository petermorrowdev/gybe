"""Models generated from Kubernetes OpenAPI Spec."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

import gybe.k8s.v1_32.meta.v1
from gybe.k8s.types import JSONObj, K8sSpec


@dataclass
class ApplyConfiguration(K8sSpec):
    """ApplyConfiguration defines the desired configuration values of an object.

    Attributes:
        expression: expression will be evaluated by CEL to create an apply configuration. ref:
            https://github.com/google/cel-spec  Apply configurations are declared in CEL using object
            initialization. For example, this CEL expression returns an apply configuration to set a single
            field:          Object{           spec: Object.spec{             serviceAccountName: 'example'
            }         }  Apply configurations may not modify atomic structs, maps or arrays due to the risk of
            accidental deletion of values not included in the apply configuration.  CEL expressions have
            access to the object types needed to create apply configurations:  - 'Object' - CEL type of the
            resource object. - 'Object.<fieldName>' - CEL type of object field (such as 'Object.spec') -
            'Object.<fieldName1>.<fieldName2>...<fieldNameN>` - CEL type of nested field (such as
            'Object.spec.containers')  CEL expressions have access to the contents of the API request,
            organized into CEL variables as well as some other useful variables:  - 'object' - The object from
            the incoming request. The value is null for DELETE requests. - 'oldObject' - The existing object.
            The value is null for CREATE requests. - 'request' - Attributes of the API
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
            `[a-zA-Z_.-/][a-zA-Z0-9_.-/]*` are accessible. Required.

    """

    expression: Optional[str] = None


@dataclass
class JSONPatch(K8sSpec):
    """JSONPatch defines a JSON Patch.

    Attributes:
        expression: expression will be evaluated by CEL to create a [JSON patch](https://jsonpatch.com/). ref:
            https://github.com/google/cel-spec  expression must return an array of JSONPatch values.  For
            example, this CEL expression returns a JSON patch to conditionally modify a value:            [
            JSONPatch{op: 'test', path: '/spec/example', value: 'Red'},             JSONPatch{op: 'replace',
            path: '/spec/example', value: 'Green'}           ]  To define an object for the patch value, use
            Object types. For example:            [             JSONPatch{               op: 'add',
            path: '/spec/selector',               value: Object.spec.selector{matchLabels: {'environment':
            'test'}}             }           ]  To use strings containing '/' and '~' as JSONPatch path keys,
            use 'jsonpatch.escapeKey'. For example:            [             JSONPatch{               op:
            'add',               path: '/metadata/labels/' + jsonpatch.escapeKey('example.com/environment'),
            value: 'test'             },           ]  CEL expressions have access to the types needed to
            create JSON patches and objects:  - 'JSONPatch' - CEL type of JSON Patch operations. JSONPatch has
            the fields 'op', 'from', 'path' and 'value'.   See [JSON patch](https://jsonpatch.com/) for more
            details. The 'value' field may be set to any of: string,   integer, array, map or object.  If set,
            the 'path' and 'from' fields must be set to a   [JSON
            pointer](https://datatracker.ietf.org/doc/html/rfc6901/) string, where the 'jsonpatch.escapeKey()'
            CEL   function may be used to escape path keys containing '/' and '~'. - 'Object' - CEL type of
            the resource object. - 'Object.<fieldName>' - CEL type of object field (such as 'Object.spec') -
            'Object.<fieldName1>.<fieldName2>...<fieldNameN>` - CEL type of nested field (such as
            'Object.spec.containers')  CEL expressions have access to the contents of the API request,
            organized into CEL variables as well as some other useful variables:  - 'object' - The object from
            the incoming request. The value is null for DELETE requests. - 'oldObject' - The existing object.
            The value is null for CREATE requests. - 'request' - Attributes of the API
            request([ref](/pkg/apis/admission/types.go#AdmissionRequest)). - 'params' - Parameter resource
            referred to by the policy binding being evaluated. Only populated if the policy has a ParamKind. -
            'namespaceObject' - The namespace object that the incoming object belongs to. The value is null
            for cluster-scoped resources. - 'variables' - Map of composited variables, from its name to its
            lazily evaluated value.   For example, a variable named 'foo' can be accessed as 'variables.foo'.
            - 'authorizer' - A CEL Authorizer. May be used to perform authorization checks for the principal
            (user or service account) of the request.   See
            https://pkg.go.dev/k8s.io/apiserver/pkg/cel/library#Authz - 'authorizer.requestResource' - A CEL
            ResourceCheck constructed from the 'authorizer' and configured with the   request resource.  CEL
            expressions have access to [Kubernetes CEL function
            libraries](https://kubernetes.io/docs/reference/using-api/cel/#cel-options-language-features-and-
            libraries) as well as:  - 'jsonpatch.escapeKey' - Performs JSONPatch key escaping. '~' and  '/'
            are escaped as '~0' and `~1' respectively).  Only property names of the form `[a-zA-
            Z_.-/][a-zA-Z0-9_.-/]*` are accessible. Required.

    """

    expression: Optional[str] = None


@dataclass
class MatchCondition(K8sSpec):
    """Schema model io.k8s.api.admissionregistration.v1alpha1.MatchCondition.

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
    namespaceSelector: Optional[gybe.k8s.v1_32.meta.v1.LabelSelector] = None
    objectSelector: Optional[gybe.k8s.v1_32.meta.v1.LabelSelector] = None
    resourceRules: Optional[List[NamedRuleWithOperations]] = None


@dataclass
class MutatingAdmissionPolicy(K8sSpec):
    """MutatingAdmissionPolicy describes the definition of an admission mutation policy that mutates the
    object coming into admission chain.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object metadata;
        spec: Specification of the desired behavior of the MutatingAdmissionPolicy.

    """

    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[gybe.k8s.v1_32.meta.v1.ObjectMeta] = None
    spec: Optional[MutatingAdmissionPolicySpec] = None


@dataclass
class MutatingAdmissionPolicyBinding(K8sSpec):
    """MutatingAdmissionPolicyBinding binds the MutatingAdmissionPolicy with parametrized resources.
    MutatingAdmissionPolicyBinding and the optional parameter resource together define how cluster
    administrators configure policies for clusters.  For a given admission request, each binding will
    cause its policy to be evaluated N times, where N is 1 for policies/bindings that don't use params,
    otherwise N is the number of parameters selected by the binding. Each evaluation is constrained by a
    [runtime cost budget](https://kubernetes.io/docs/reference/using-api/cel/#runtime-cost-budget).
    Adding/removing policies, bindings, or params can not affect whether a given (policy, binding, param)
    combination is within its own CEL budget.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object metadata;
        spec: Specification of the desired behavior of the MutatingAdmissionPolicyBinding.

    """

    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[gybe.k8s.v1_32.meta.v1.ObjectMeta] = None
    spec: Optional[MutatingAdmissionPolicyBindingSpec] = None


@dataclass
class MutatingAdmissionPolicyBindingList(K8sSpec):
    """MutatingAdmissionPolicyBindingList is a list of MutatingAdmissionPolicyBinding.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        items: List of PolicyBinding.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard list metadata.

    """

    items: List[MutatingAdmissionPolicyBinding]
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[JSONObj] = None


@dataclass
class MutatingAdmissionPolicyBindingSpec(K8sSpec):
    """MutatingAdmissionPolicyBindingSpec is the specification of the MutatingAdmissionPolicyBinding.

    Attributes:
        matchResources: matchResources limits what resources match this binding and may be mutated by it. Note
            that if matchResources matches a resource, the resource must also match a policy's
            matchConstraints and matchConditions before the resource may be mutated. When matchResources is
            unset, it does not constrain resource matching, and only the policy's matchConstraints and
            matchConditions must match for the resource to be mutated. Additionally,
            matchResources.resourceRules are optional and do not constraint matching when unset. Note that
            this is differs from MutatingAdmissionPolicy matchConstraints, where resourceRules are required.
            The CREATE, UPDATE and CONNECT operations are allowed.  The DELETE operation may not be matched.
            '*' matches CREATE, UPDATE and CONNECT.
        paramRef: paramRef specifies the parameter resource used to configure the admission control policy. It
            should point to a resource of the type specified in spec.ParamKind of the bound
            MutatingAdmissionPolicy. If the policy specifies a ParamKind and the resource referred to by
            ParamRef does not exist, this binding is considered mis-configured and the FailurePolicy of the
            MutatingAdmissionPolicy applied. If the policy does not specify a ParamKind then this field is
            ignored, and the rules are evaluated without a param.
        policyName: policyName references a MutatingAdmissionPolicy name which the
            MutatingAdmissionPolicyBinding binds to. If the referenced resource does not exist, this binding
            is considered invalid and will be ignored Required.

    """

    matchResources: Optional[MatchResources] = None
    paramRef: Optional[ParamRef] = None
    policyName: Optional[str] = None


@dataclass
class MutatingAdmissionPolicyList(K8sSpec):
    """MutatingAdmissionPolicyList is a list of MutatingAdmissionPolicy.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        items: List of ValidatingAdmissionPolicy.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard list metadata.

    """

    items: List[MutatingAdmissionPolicy]
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[JSONObj] = None


@dataclass
class MutatingAdmissionPolicySpec(K8sSpec):
    """MutatingAdmissionPolicySpec is the specification of the desired behavior of the admission policy.

    Attributes:
        failurePolicy: failurePolicy defines how to handle failures for the admission policy. Failures can
            occur from CEL expression parse errors, type check errors, runtime errors and invalid or mis-
            configured policy definitions or bindings.  A policy is invalid if paramKind refers to a non-
            existent Kind. A binding is invalid if paramRef.name refers to a non-existent resource.
            failurePolicy does not define how validations that evaluate to false are handled.  Allowed values
            are Ignore or Fail. Defaults to Fail.
        matchConditions: matchConditions is a list of conditions that must be met for a request to be
            validated. Match conditions filter requests that have already been matched by the
            matchConstraints. An empty list of matchConditions matches all requests. There are a maximum of 64
            match conditions allowed.  If a parameter object is provided, it can be accessed via the `params`
            handle in the same manner as validation expressions.  The exact matching logic is (in order):   1.
            If ANY matchCondition evaluates to FALSE, the policy is skipped.   2. If ALL matchConditions
            evaluate to TRUE, the policy is evaluated.   3. If any matchCondition evaluates to an error (but
            none are FALSE):      - If failurePolicy=Fail, reject the request      - If failurePolicy=Ignore,
            the policy is skipped
        matchConstraints: matchConstraints specifies what resources this policy is designed to validate. The
            MutatingAdmissionPolicy cares about a request if it matches _all_ Constraints. However, in order
            to prevent clusters from being put into an unstable state that cannot be recovered from via the
            API MutatingAdmissionPolicy cannot match MutatingAdmissionPolicy and
            MutatingAdmissionPolicyBinding. The CREATE, UPDATE and CONNECT operations are allowed.  The DELETE
            operation may not be matched. '*' matches CREATE, UPDATE and CONNECT. Required.
        mutations: mutations contain operations to perform on matching objects. mutations may not be empty; a
            minimum of one mutation is required. mutations are evaluated in order, and are reinvoked according
            to the reinvocationPolicy. The mutations of a policy are invoked for each binding of this policy
            and reinvocation of mutations occurs on a per binding basis.
        paramKind: paramKind specifies the kind of resources used to parameterize this policy. If absent,
            there are no parameters for this policy and the param CEL variable will not be provided to
            validation expressions. If paramKind refers to a non-existent kind, this policy definition is mis-
            configured and the FailurePolicy is applied. If paramKind is specified but paramRef is unset in
            MutatingAdmissionPolicyBinding, the params variable will be null.
        reinvocationPolicy: reinvocationPolicy indicates whether mutations may be called multiple times per
            MutatingAdmissionPolicyBinding as part of a single admission evaluation. Allowed values are
            'Never' and 'IfNeeded'.  Never: These mutations will not be called more than once per binding in a
            single admission evaluation.  IfNeeded: These mutations may be invoked more than once per binding
            for a single admission request and there is no guarantee of order with respect to other admission
            plugins, admission webhooks, bindings of this policy and admission policies.  Mutations are only
            reinvoked when mutations change the object after this mutation is invoked. Required.
        variables: variables contain definitions of variables that can be used in composition of other
            expressions. Each variable is defined as a named CEL expression. The variables defined here will
            be available under `variables` in other expressions of the policy except matchConditions because
            matchConditions are evaluated before the rest of the policy.  The expression of a variable can
            refer to other variables defined earlier in the list but not those after. Thus, variables must be
            sorted by the order of first appearance and acyclic.

    """

    failurePolicy: Optional[str] = None
    matchConditions: Optional[List[MatchCondition]] = None
    matchConstraints: Optional[MatchResources] = None
    mutations: Optional[List[Mutation]] = None
    paramKind: Optional[ParamKind] = None
    reinvocationPolicy: Optional[str] = None
    variables: Optional[List[Variable]] = None


@dataclass
class Mutation(K8sSpec):
    """Mutation specifies the CEL expression which is used to apply the Mutation.

    Attributes:
        applyConfiguration: applyConfiguration defines the desired configuration values of an object. The
            configuration is applied to the admission object using [structured merge
            diff](https://github.com/kubernetes-sigs/structured-merge-diff). A CEL expression is used to
            create apply configuration.
        jsonPatch: jsonPatch defines a [JSON patch](https://jsonpatch.com/) operation to perform a mutation to
            the object. A CEL expression is used to create the JSON patch.
        patchType: patchType indicates the patch strategy used. Allowed values are 'ApplyConfiguration' and
            'JSONPatch'. Required.

    """

    patchType: str
    applyConfiguration: Optional[ApplyConfiguration] = None
    jsonPatch: Optional[JSONPatch] = None


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
        name: `name` is the name of the resource being referenced.  `name` and `selector` are mutually
            exclusive properties. If one is set, the other must be unset.
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
            `failurePolicy` of the policy.  Allowed values are `Allow` or `Deny` Default to `Deny`
        selector: selector can be used to match multiple param objects based on their labels. Supply selector:
            {} to match all resources of the ParamKind.  If multiple params are found, they are all evaluated
            with the policy expressions and the results are ANDed together.  One of `name` or `selector` must
            be set, but `name` and `selector` are mutually exclusive properties. If one is set, the other must
            be unset.

    """

    name: Optional[str] = None
    namespace: Optional[str] = None
    parameterNotFoundAction: Optional[str] = None
    selector: Optional[gybe.k8s.v1_32.meta.v1.LabelSelector] = None


@dataclass
class Variable(K8sSpec):
    """Variable is the definition of a variable that is used for composition.

    Attributes:
        expression: Expression is the expression that will be evaluated as the value of the variable. The CEL
            expression has access to the same identifiers as the CEL expressions in Validation.
        name: Name is the name of the variable. The name must be a valid CEL identifier and unique among all
            variables. The variable can be accessed in other expressions through `variables` For example, if
            name is 'foo', the variable will be available as `variables.foo`

    """

    name: str
    expression: str
