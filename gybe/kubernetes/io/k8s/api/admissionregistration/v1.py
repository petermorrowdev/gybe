from __future__ import annotations
from typing import List, Optional
from pydantic import BaseModel, Field
from ...apimachinery.pkg.apis.meta import v1


class MatchCondition(BaseModel):
    expression: str = Field(
        ...,
        description=(
            "Expression represents the expression which will be evaluated by CEL. Must"
            " evaluate to bool. CEL expressions have access to the contents of the"
            " AdmissionRequest and Authorizer, organized into CEL"
            " variables:\n\n'object' - The object from the incoming request. The value"
            " is null for DELETE requests. 'oldObject' - The existing object. The value"
            " is null for CREATE requests. 'request' - Attributes of the admission"
            " request(/pkg/apis/admission/types.go#AdmissionRequest). 'authorizer' - A"
            " CEL Authorizer. May be used to perform authorization checks for the"
            " principal (user or service account) of the request.\n  See"
            " https://pkg.go.dev/k8s.io/apiserver/pkg/cel/library#Authz\n'authorizer.requestResource'"
            " - A CEL ResourceCheck constructed from the 'authorizer' and configured"
            " with the\n  request resource.\nDocumentation on CEL:"
            " https://kubernetes.io/docs/reference/using-api/cel/\n\nRequired."
        ),
    )
    name: str = Field(
        ...,
        description=(
            "Name is an identifier for this match condition, used for strategic merging"
            " of MatchConditions, as well as providing an identifier for logging"
            " purposes. A good name should be descriptive of the associated expression."
            " Name must be a qualified name consisting of alphanumeric characters, '-',"
            " '_' or '.', and must start and end with an alphanumeric character (e.g."
            " 'MyName',  or 'my.name',  or '123-abc', regex used for validation is"
            " '([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9]') with an optional DNS"
            " subdomain prefix and '/' (e.g. 'example.com/MyName')\n\nRequired."
        ),
    )


class RuleWithOperations(BaseModel):
    apiGroups: Optional[List[str]] = Field(
        None,
        description=(
            "APIGroups is the API groups the resources belong to. '*' is all groups. If"
            " '*' is present, the length of the slice must be one. Required."
        ),
    )
    apiVersions: Optional[List[str]] = Field(
        None,
        description=(
            "APIVersions is the API versions the resources belong to. '*' is all"
            " versions. If '*' is present, the length of the slice must be one."
            " Required."
        ),
    )
    operations: Optional[List[str]] = Field(
        None,
        description=(
            "Operations is the operations the admission hook cares about - CREATE,"
            " UPDATE, DELETE, CONNECT or * for all of those operations and any future"
            " admission operations that are added. If '*' is present, the length of the"
            " slice must be one. Required."
        ),
    )
    resources: Optional[List[str]] = Field(
        None,
        description=(
            "Resources is a list of resources this rule applies to.\n\nFor example:"
            " 'pods' means pods. 'pods/log' means the log subresource of pods. '*'"
            " means all resources, but not subresources. 'pods/*' means all"
            " subresources of pods. '*/scale' means all scale subresources. '*/*' means"
            " all resources and their subresources.\n\nIf wildcard is present, the"
            " validation rule will ensure resources do not overlap with each"
            " other.\n\nDepending on the enclosing object, subresources might not be"
            " allowed. Required."
        ),
    )
    scope: Optional[str] = Field(
        None,
        description=(
            'scope specifies the scope of this rule. Valid values are "Cluster",'
            ' "Namespaced", and "*" "Cluster" means that only cluster-scoped resources'
            " will match this rule. Namespace API objects are cluster-scoped."
            ' "Namespaced" means that only namespaced resources will match this rule.'
            ' "*" means that there are no scope restrictions. Subresources match the'
            ' scope of their parent resource. Default is "*".'
        ),
    )


class ServiceReference(BaseModel):
    name: str = Field(..., description="`name` is the name of the service. Required")
    namespace: str = Field(
        ..., description="`namespace` is the namespace of the service. Required"
    )
    path: Optional[str] = Field(
        None,
        description=(
            "`path` is an optional URL path which will be sent in any request to this"
            " service."
        ),
    )
    port: Optional[int] = Field(
        None,
        description=(
            "If specified, the port on the service that hosting webhook. Default to 443"
            " for backward compatibility. `port` should be a valid port number"
            " (1-65535, inclusive)."
        ),
    )


class WebhookClientConfig(BaseModel):
    caBundle: Optional[str] = Field(
        None,
        description=(
            "`caBundle` is a PEM encoded CA bundle which will be used to validate the"
            " webhook's server certificate. If unspecified, system trust roots on the"
            " apiserver are used."
        ),
    )
    service: Optional[ServiceReference] = Field(
        None,
        description=(
            "`service` is a reference to the service for this webhook. Either `service`"
            " or `url` must be specified.\n\nIf the webhook is running within the"
            " cluster, then you should use `service`."
        ),
    )
    url: Optional[str] = Field(
        None,
        description=(
            "`url` gives the location of the webhook, in standard URL form"
            " (`scheme://host:port/path`). Exactly one of `url` or `service` must be"
            " specified.\n\nThe `host` should not refer to a service running in the"
            " cluster; use the `service` field instead. The host might be resolved via"
            " external DNS in some apiservers (e.g., `kube-apiserver` cannot resolve"
            " in-cluster DNS as that would be a layering violation). `host` may also be"
            " an IP address.\n\nPlease note that using `localhost` or `127.0.0.1` as a"
            " `host` is risky unless you take great care to run this webhook on all"
            " hosts which run an apiserver which might need to make calls to this"
            " webhook. Such installs are likely to be non-portable, i.e., not easy to"
            ' turn up in a new cluster.\n\nThe scheme must be "https"; the URL must'
            ' begin with "https://".\n\nA path is optional, and if present may be any'
            " string permissible in a URL. You may use the path to pass an arbitrary"
            " string to the webhook, for example, a cluster identifier.\n\nAttempting"
            ' to use a user or basic auth e.g. "user:password@" is not allowed.'
            ' Fragments ("#...") and query parameters ("?...") are not allowed, either.'
        ),
    )


class MutatingWebhook(BaseModel):
    admissionReviewVersions: List[str] = Field(
        ...,
        description=(
            "AdmissionReviewVersions is an ordered list of preferred `AdmissionReview`"
            " versions the Webhook expects. API server will try to use first version in"
            " the list which it supports. If none of the versions specified in this"
            " list supported by API server, validation will fail for this object. If a"
            " persisted webhook configuration specifies allowed versions and does not"
            " include any versions known to the API Server, calls to the webhook will"
            " fail and be subject to the failure policy."
        ),
    )
    clientConfig: WebhookClientConfig = Field(
        ...,
        description="ClientConfig defines how to communicate with the hook. Required",
    )
    failurePolicy: Optional[str] = Field(
        None,
        description=(
            "FailurePolicy defines how unrecognized errors from the admission endpoint"
            " are handled - allowed values are Ignore or Fail. Defaults to Fail."
        ),
    )
    matchConditions: Optional[List[MatchCondition]] = Field(
        None,
        description=(
            "MatchConditions is a list of conditions that must be met for a request to"
            " be sent to this webhook. Match conditions filter requests that have"
            " already been matched by the rules, namespaceSelector, and objectSelector."
            " An empty list of matchConditions matches all requests. There are a"
            " maximum of 64 match conditions allowed.\n\nThe exact matching logic is"
            " (in order):\n  1. If ANY matchCondition evaluates to FALSE, the webhook"
            " is skipped.\n  2. If ALL matchConditions evaluate to TRUE, the webhook is"
            " called.\n  3. If any matchCondition evaluates to an error (but none are"
            " FALSE):\n     - If failurePolicy=Fail, reject the request\n     - If"
            " failurePolicy=Ignore, the error is ignored and the webhook is"
            " skipped\n\nThis is an alpha feature and managed by the"
            " AdmissionWebhookMatchConditions feature gate."
        ),
    )
    matchPolicy: Optional[str] = Field(
        None,
        description=(
            'matchPolicy defines how the "rules" list is used to match incoming'
            ' requests. Allowed values are "Exact" or "Equivalent".\n\n- Exact: match a'
            " request only if it exactly matches a specified rule. For example, if"
            " deployments can be modified via apps/v1, apps/v1beta1, and"
            ' extensions/v1beta1, but "rules" only included `apiGroups:["apps"],'
            ' apiVersions:["v1"], resources: ["deployments"]`, a request to'
            " apps/v1beta1 or extensions/v1beta1 would not be sent to the webhook.\n\n-"
            " Equivalent: match a request if modifies a resource listed in rules, even"
            " via another API group or version. For example, if deployments can be"
            ' modified via apps/v1, apps/v1beta1, and extensions/v1beta1, and "rules"'
            ' only included `apiGroups:["apps"], apiVersions:["v1"], resources:'
            ' ["deployments"]`, a request to apps/v1beta1 or extensions/v1beta1 would'
            " be converted to apps/v1 and sent to the webhook.\n\nDefaults to"
            ' "Equivalent"'
        ),
    )
    name: str = Field(
        ...,
        description=(
            "The name of the admission webhook. Name should be fully qualified, e.g.,"
            ' imagepolicy.kubernetes.io, where "imagepolicy" is the name of the'
            " webhook, and kubernetes.io is the name of the organization. Required."
        ),
    )
    namespaceSelector: Optional[v1.LabelSelector] = Field(
        None,
        description=(
            "NamespaceSelector decides whether to run the webhook on an object based on"
            " whether the namespace for that object matches the selector. If the object"
            " itself is a namespace, the matching is performed on"
            " object.metadata.labels. If the object is another cluster scoped resource,"
            " it never skips the webhook.\n\nFor example, to run the webhook on any"
            ' objects whose namespace is not associated with "runlevel" of "0" or "1"; '
            ' you will set the selector as follows: "namespaceSelector": {\n '
            ' "matchExpressions": [\n    {\n      "key": "runlevel",\n      "operator":'
            ' "NotIn",\n      "values": [\n        "0",\n        "1"\n      ]\n    }\n '
            " ]\n}\n\nIf instead you want to only run the webhook on any objects whose"
            ' namespace is associated with the "environment" of "prod" or "staging";'
            ' you will set the selector as follows: "namespaceSelector": {\n '
            ' "matchExpressions": [\n    {\n      "key": "environment",\n     '
            ' "operator": "In",\n      "values": [\n        "prod",\n       '
            ' "staging"\n      ]\n    }\n  ]\n}\n\nSee'
            " https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/"
            " for more examples of label selectors.\n\nDefault to the empty"
            " LabelSelector, which matches everything."
        ),
    )
    objectSelector: Optional[v1.LabelSelector] = Field(
        None,
        description=(
            "ObjectSelector decides whether to run the webhook based on if the object"
            " has matching labels. objectSelector is evaluated against both the"
            " oldObject and newObject that would be sent to the webhook, and is"
            " considered to match if either object matches the selector. A null object"
            " (oldObject in the case of create, or newObject in the case of delete) or"
            " an object that cannot have labels (like a DeploymentRollback or a"
            " PodProxyOptions object) is not considered to match. Use the object"
            " selector only if the webhook is opt-in, because end users may skip the"
            " admission webhook by setting the labels. Default to the empty"
            " LabelSelector, which matches everything."
        ),
    )
    reinvocationPolicy: Optional[str] = Field(
        None,
        description=(
            "reinvocationPolicy indicates whether this webhook should be called"
            " multiple times as part of a single admission evaluation. Allowed values"
            ' are "Never" and "IfNeeded".\n\nNever: the webhook will not be called more'
            " than once in a single admission evaluation.\n\nIfNeeded: the webhook will"
            " be called at least one additional time as part of the admission"
            " evaluation if the object being admitted is modified by other admission"
            " plugins after the initial webhook call. Webhooks that specify this option"
            " *must* be idempotent, able to process objects they previously admitted."
            " Note: * the number of additional invocations is not guaranteed to be"
            " exactly one. * if additional invocations result in further modifications"
            " to the object, webhooks are not guaranteed to be invoked again. *"
            " webhooks that use this option may be reordered to minimize the number of"
            " additional invocations. * to validate an object after all mutations are"
            " guaranteed complete, use a validating admission webhook"
            ' instead.\n\nDefaults to "Never".'
        ),
    )
    rules: Optional[List[RuleWithOperations]] = Field(
        None,
        description=(
            "Rules describes what operations on what resources/subresources the webhook"
            " cares about. The webhook cares about an operation if it matches _any_"
            " Rule. However, in order to prevent ValidatingAdmissionWebhooks and"
            " MutatingAdmissionWebhooks from putting the cluster in a state which"
            " cannot be recovered from without completely disabling the plugin,"
            " ValidatingAdmissionWebhooks and MutatingAdmissionWebhooks are never"
            " called on admission requests for ValidatingWebhookConfiguration and"
            " MutatingWebhookConfiguration objects."
        ),
    )
    sideEffects: str = Field(
        ...,
        description=(
            "SideEffects states whether this webhook has side effects. Acceptable"
            " values are: None, NoneOnDryRun (webhooks created via v1beta1 may also"
            " specify Some or Unknown). Webhooks with side effects MUST implement a"
            " reconciliation system, since a request may be rejected by a future step"
            " in the admission chain and the side effects therefore need to be undone."
            " Requests with the dryRun attribute will be auto-rejected if they match a"
            " webhook with sideEffects == Unknown or Some."
        ),
    )
    timeoutSeconds: Optional[int] = Field(
        None,
        description=(
            "TimeoutSeconds specifies the timeout for this webhook. After the timeout"
            " passes, the webhook call will be ignored or the API call will fail based"
            " on the failure policy. The timeout value must be between 1 and 30"
            " seconds. Default to 10 seconds."
        ),
    )


class MutatingWebhookConfiguration(BaseModel):
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
            "Standard object metadata; More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata."
        ),
    )
    webhooks: Optional[List[MutatingWebhook]] = Field(
        None,
        description=(
            "Webhooks is a list of webhooks and the affected resources and operations."
        ),
    )


class MutatingWebhookConfigurationList(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description=(
            "APIVersion defines the versioned schema of this representation of an"
            " object. Servers should convert recognized schemas to the latest internal"
            " value, and may reject unrecognized values. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources"
        ),
    )
    items: List[MutatingWebhookConfiguration] = Field(
        ..., description="List of MutatingWebhookConfiguration."
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
            "Standard list metadata. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"
        ),
    )


class ValidatingWebhook(BaseModel):
    admissionReviewVersions: List[str] = Field(
        ...,
        description=(
            "AdmissionReviewVersions is an ordered list of preferred `AdmissionReview`"
            " versions the Webhook expects. API server will try to use first version in"
            " the list which it supports. If none of the versions specified in this"
            " list supported by API server, validation will fail for this object. If a"
            " persisted webhook configuration specifies allowed versions and does not"
            " include any versions known to the API Server, calls to the webhook will"
            " fail and be subject to the failure policy."
        ),
    )
    clientConfig: WebhookClientConfig = Field(
        ...,
        description="ClientConfig defines how to communicate with the hook. Required",
    )
    failurePolicy: Optional[str] = Field(
        None,
        description=(
            "FailurePolicy defines how unrecognized errors from the admission endpoint"
            " are handled - allowed values are Ignore or Fail. Defaults to Fail."
        ),
    )
    matchConditions: Optional[List[MatchCondition]] = Field(
        None,
        description=(
            "MatchConditions is a list of conditions that must be met for a request to"
            " be sent to this webhook. Match conditions filter requests that have"
            " already been matched by the rules, namespaceSelector, and objectSelector."
            " An empty list of matchConditions matches all requests. There are a"
            " maximum of 64 match conditions allowed.\n\nThe exact matching logic is"
            " (in order):\n  1. If ANY matchCondition evaluates to FALSE, the webhook"
            " is skipped.\n  2. If ALL matchConditions evaluate to TRUE, the webhook is"
            " called.\n  3. If any matchCondition evaluates to an error (but none are"
            " FALSE):\n     - If failurePolicy=Fail, reject the request\n     - If"
            " failurePolicy=Ignore, the error is ignored and the webhook is"
            " skipped\n\nThis is an alpha feature and managed by the"
            " AdmissionWebhookMatchConditions feature gate."
        ),
    )
    matchPolicy: Optional[str] = Field(
        None,
        description=(
            'matchPolicy defines how the "rules" list is used to match incoming'
            ' requests. Allowed values are "Exact" or "Equivalent".\n\n- Exact: match a'
            " request only if it exactly matches a specified rule. For example, if"
            " deployments can be modified via apps/v1, apps/v1beta1, and"
            ' extensions/v1beta1, but "rules" only included `apiGroups:["apps"],'
            ' apiVersions:["v1"], resources: ["deployments"]`, a request to'
            " apps/v1beta1 or extensions/v1beta1 would not be sent to the webhook.\n\n-"
            " Equivalent: match a request if modifies a resource listed in rules, even"
            " via another API group or version. For example, if deployments can be"
            ' modified via apps/v1, apps/v1beta1, and extensions/v1beta1, and "rules"'
            ' only included `apiGroups:["apps"], apiVersions:["v1"], resources:'
            ' ["deployments"]`, a request to apps/v1beta1 or extensions/v1beta1 would'
            " be converted to apps/v1 and sent to the webhook.\n\nDefaults to"
            ' "Equivalent"'
        ),
    )
    name: str = Field(
        ...,
        description=(
            "The name of the admission webhook. Name should be fully qualified, e.g.,"
            ' imagepolicy.kubernetes.io, where "imagepolicy" is the name of the'
            " webhook, and kubernetes.io is the name of the organization. Required."
        ),
    )
    namespaceSelector: Optional[v1.LabelSelector] = Field(
        None,
        description=(
            "NamespaceSelector decides whether to run the webhook on an object based on"
            " whether the namespace for that object matches the selector. If the object"
            " itself is a namespace, the matching is performed on"
            " object.metadata.labels. If the object is another cluster scoped resource,"
            " it never skips the webhook.\n\nFor example, to run the webhook on any"
            ' objects whose namespace is not associated with "runlevel" of "0" or "1"; '
            ' you will set the selector as follows: "namespaceSelector": {\n '
            ' "matchExpressions": [\n    {\n      "key": "runlevel",\n      "operator":'
            ' "NotIn",\n      "values": [\n        "0",\n        "1"\n      ]\n    }\n '
            " ]\n}\n\nIf instead you want to only run the webhook on any objects whose"
            ' namespace is associated with the "environment" of "prod" or "staging";'
            ' you will set the selector as follows: "namespaceSelector": {\n '
            ' "matchExpressions": [\n    {\n      "key": "environment",\n     '
            ' "operator": "In",\n      "values": [\n        "prod",\n       '
            ' "staging"\n      ]\n    }\n  ]\n}\n\nSee'
            " https://kubernetes.io/docs/concepts/overview/working-with-objects/labels"
            " for more examples of label selectors.\n\nDefault to the empty"
            " LabelSelector, which matches everything."
        ),
    )
    objectSelector: Optional[v1.LabelSelector] = Field(
        None,
        description=(
            "ObjectSelector decides whether to run the webhook based on if the object"
            " has matching labels. objectSelector is evaluated against both the"
            " oldObject and newObject that would be sent to the webhook, and is"
            " considered to match if either object matches the selector. A null object"
            " (oldObject in the case of create, or newObject in the case of delete) or"
            " an object that cannot have labels (like a DeploymentRollback or a"
            " PodProxyOptions object) is not considered to match. Use the object"
            " selector only if the webhook is opt-in, because end users may skip the"
            " admission webhook by setting the labels. Default to the empty"
            " LabelSelector, which matches everything."
        ),
    )
    rules: Optional[List[RuleWithOperations]] = Field(
        None,
        description=(
            "Rules describes what operations on what resources/subresources the webhook"
            " cares about. The webhook cares about an operation if it matches _any_"
            " Rule. However, in order to prevent ValidatingAdmissionWebhooks and"
            " MutatingAdmissionWebhooks from putting the cluster in a state which"
            " cannot be recovered from without completely disabling the plugin,"
            " ValidatingAdmissionWebhooks and MutatingAdmissionWebhooks are never"
            " called on admission requests for ValidatingWebhookConfiguration and"
            " MutatingWebhookConfiguration objects."
        ),
    )
    sideEffects: str = Field(
        ...,
        description=(
            "SideEffects states whether this webhook has side effects. Acceptable"
            " values are: None, NoneOnDryRun (webhooks created via v1beta1 may also"
            " specify Some or Unknown). Webhooks with side effects MUST implement a"
            " reconciliation system, since a request may be rejected by a future step"
            " in the admission chain and the side effects therefore need to be undone."
            " Requests with the dryRun attribute will be auto-rejected if they match a"
            " webhook with sideEffects == Unknown or Some."
        ),
    )
    timeoutSeconds: Optional[int] = Field(
        None,
        description=(
            "TimeoutSeconds specifies the timeout for this webhook. After the timeout"
            " passes, the webhook call will be ignored or the API call will fail based"
            " on the failure policy. The timeout value must be between 1 and 30"
            " seconds. Default to 10 seconds."
        ),
    )


class ValidatingWebhookConfiguration(BaseModel):
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
            "Standard object metadata; More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata."
        ),
    )
    webhooks: Optional[List[ValidatingWebhook]] = Field(
        None,
        description=(
            "Webhooks is a list of webhooks and the affected resources and operations."
        ),
    )


class ValidatingWebhookConfigurationList(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description=(
            "APIVersion defines the versioned schema of this representation of an"
            " object. Servers should convert recognized schemas to the latest internal"
            " value, and may reject unrecognized values. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources"
        ),
    )
    items: List[ValidatingWebhookConfiguration] = Field(
        ..., description="List of ValidatingWebhookConfiguration."
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
            "Standard list metadata. More info:"
            " https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"
        ),
    )
