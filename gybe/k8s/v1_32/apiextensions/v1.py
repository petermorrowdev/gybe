"""Models generated from Kubernetes OpenAPI Spec."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Literal, Optional

import gybe.k8s.v1_32.meta.v1
from gybe.k8s.types import JSONObj, K8sResource, K8sSpec


@dataclass
class CustomResourceColumnDefinition(K8sSpec):
    """CustomResourceColumnDefinition specifies a column for server side printing.

    Attributes:
        description: description is a human readable description of this column.
        format: format is an optional OpenAPI type definition for this column. The 'name' format is applied to
            the primary identifier column to assist in clients identifying column is the resource name. See
            https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md#data-types for details.
        jsonPath: jsonPath is a simple JSON path (i.e. with array notation) which is evaluated against each
            custom resource to produce the value for this column.
        name: name is a human readable name for the column.
        priority: priority is an integer defining the relative importance of this column compared to others.
            Lower numbers are considered higher priority. Columns that may be omitted in limited space
            scenarios should be given a priority greater than 0.
        type: type is an OpenAPI type definition for this column. See https://github.com/OAI/OpenAPI-
            Specification/blob/master/versions/2.0.md#data-types for details.

    """

    name: str
    type: str
    jsonPath: str
    description: Optional[str] = None
    format: Optional[str] = None
    priority: Optional[int] = None


@dataclass
class CustomResourceConversion(K8sSpec):
    """CustomResourceConversion describes how to convert different versions of a CR.

    Attributes:
        strategy: strategy specifies how custom resources are converted between versions. Allowed values are:
            - `'None'`: The converter only change the apiVersion and would not touch any other field in the
            custom resource. - `'Webhook'`: API Server will call to an external webhook to do the conversion.
            Additional information   is needed for this option. This requires spec.preserveUnknownFields to be
            false, and spec.conversion.webhook to be set.
        webhook: webhook describes how to call the conversion webhook. Required when `strategy` is set to
            `'Webhook'`.

    """

    strategy: str
    webhook: Optional[WebhookConversion] = None


@dataclass
class CustomResourceDefinition(K8sResource):
    """CustomResourceDefinition represents a resource that should be exposed on the API server.  Its name
    MUST be in the format <.spec.name>.<.spec.group>.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object's metadata
        spec: spec describes how the user wants the resources to appear
        status: status indicates the actual state of the CustomResourceDefinition

    """

    spec: CustomResourceDefinitionSpec
    apiVersion: Literal['apiextensions.k8s.io/v1'] = 'apiextensions.k8s.io/v1'
    kind: Literal['CustomResourceDefinition'] = 'CustomResourceDefinition'
    metadata: Optional[gybe.k8s.v1_32.meta.v1.ObjectMeta] = None
    status: Optional[CustomResourceDefinitionStatus] = None


@dataclass
class CustomResourceDefinitionCondition(K8sSpec):
    """CustomResourceDefinitionCondition contains details for the current condition of this pod.

    Attributes:
        lastTransitionTime: lastTransitionTime last time the condition transitioned from one status to
            another.
        message: message is a human-readable message indicating details about last transition.
        reason: reason is a unique, one-word, CamelCase reason for the condition's last transition.
        status: status is the status of the condition. Can be True, False, Unknown.
        type: type is the type of the condition. Types include Established, NamesAccepted and Terminating.

    """

    type: str
    status: str
    lastTransitionTime: Optional[str] = None
    message: Optional[str] = None
    reason: Optional[str] = None


@dataclass
class CustomResourceDefinitionList(K8sSpec):
    """CustomResourceDefinitionList is a list of CustomResourceDefinition objects.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        items: items list individual CustomResourceDefinition objects
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object's metadata

    """

    items: List[CustomResourceDefinition]
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[JSONObj] = None


@dataclass
class CustomResourceDefinitionNames(K8sSpec):
    """CustomResourceDefinitionNames indicates the names to serve this CustomResourceDefinition
    Attributes:
        categories: categories is a list of grouped resources this custom resource belongs to (e.g. 'all').
            This is published in API discovery documents, and used by clients to support invocations like
            `kubectl get all`.
        kind: kind is the serialized kind of the resource. It is normally CamelCase and singular. Custom
            resource instances will use this value as the `kind` attribute in API calls.
        listKind: listKind is the serialized kind of the list for this resource. Defaults to '`kind`List'.
        plural: plural is the plural name of the resource to serve. The custom resources are served under
            `/apis/<group>/<version>/.../<plural>`. Must match the name of the CustomResourceDefinition (in
            the form `<names.plural>.<group>`). Must be all lowercase.
        shortNames: shortNames are short names for the resource, exposed in API discovery documents, and used
            by clients to support invocations like `kubectl get <shortname>`. It must be all lowercase.
        singular: singular is the singular name of the resource. It must be all lowercase. Defaults to
            lowercased `kind`.

    """

    plural: str
    kind: str
    categories: Optional[List[str]] = None
    listKind: Optional[str] = None
    shortNames: Optional[List[str]] = None
    singular: Optional[str] = None


@dataclass
class CustomResourceDefinitionSpec(K8sSpec):
    """CustomResourceDefinitionSpec describes how a user wants their resource to appear
    Attributes:
        conversion: conversion defines conversion settings for the CRD.
        group: group is the API group of the defined custom resource. The custom resources are served under
            `/apis/<group>/...`. Must match the name of the CustomResourceDefinition (in the form
            `<names.plural>.<group>`).
        names: names specify the resource and kind names for the custom resource.
        preserveUnknownFields: preserveUnknownFields indicates that object fields which are not specified in
            the OpenAPI schema should be preserved when persisting to storage. apiVersion, kind, metadata and
            known fields inside metadata are always preserved. This field is deprecated in favor of setting
            `x-preserve-unknown-fields` to true in `spec.versions[*].schema.openAPIV3Schema`. See
            https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-
            definitions/#field-pruning for details.
        scope: scope indicates whether the defined custom resource is cluster- or namespace-scoped. Allowed
            values are `Cluster` and `Namespaced`.
        versions: versions is the list of all API versions of the defined custom resource. Version names are
            used to compute the order in which served versions are listed in API discovery. If the version
            string is 'kube-like', it will sort above non 'kube-like' version strings, which are ordered
            lexicographically. 'Kube-like' versions start with a 'v', then are followed by a number (the major
            version), then optionally the string 'alpha' or 'beta' and another number (the minor version).
            These are sorted first by GA > beta > alpha (where GA is a version with no suffix such as beta or
            alpha), and then by comparing major version, then minor version. An example sorted list of
            versions: v10, v2, v1, v11beta2, v10beta3, v3beta1, v12alpha1, v11alpha2, foo1, foo10.

    """

    group: str
    names: CustomResourceDefinitionNames
    scope: str
    versions: List[CustomResourceDefinitionVersion]
    conversion: Optional[CustomResourceConversion] = None
    preserveUnknownFields: Optional[bool] = None


@dataclass
class CustomResourceDefinitionStatus(K8sSpec):
    """CustomResourceDefinitionStatus indicates the state of the CustomResourceDefinition
    Attributes:
        acceptedNames: acceptedNames are the names that are actually being used to serve discovery. They may
            be different than the names in spec.
        conditions: conditions indicate state for particular aspects of a CustomResourceDefinition
        storedVersions: storedVersions lists all versions of CustomResources that were ever persisted.
            Tracking these versions allows a migration path for stored versions in etcd. The field is mutable
            so a migration controller can finish a migration to another version (ensuring no old objects are
            left in storage), and then remove the rest of the versions from this list. Versions may not be
            removed from `spec.versions` while they exist in this list.

    """

    acceptedNames: Optional[CustomResourceDefinitionNames] = None
    conditions: Optional[List[CustomResourceDefinitionCondition]] = None
    storedVersions: Optional[List[str]] = None


@dataclass
class CustomResourceDefinitionVersion(K8sSpec):
    """CustomResourceDefinitionVersion describes a version for CRD.

    Attributes:
        additionalPrinterColumns: additionalPrinterColumns specifies additional columns returned in Table
            output. See https://kubernetes.io/docs/reference/using-api/api-concepts/#receiving-resources-as-
            tables for details. If no columns are specified, a single column displaying the age of the custom
            resource is used.
        deprecated: deprecated indicates this version of the custom resource API is deprecated. When set to
            true, API requests to this version receive a warning header in the server response. Defaults to
            false.
        deprecationWarning: deprecationWarning overrides the default warning returned to API clients. May only
            be set when `deprecated` is true. The default warning indicates this version is deprecated and
            recommends use of the newest served version of equal or greater stability, if one exists.
        name: name is the version name, e.g. “v1”, “v2beta1”, etc. The custom resources are served under this
            version at `/apis/<group>/<version>/...` if `served` is true.
        schema: schema describes the schema used for validation, pruning, and defaulting of this version of
            the custom resource.
        selectableFields: selectableFields specifies paths to fields that may be used as field selectors. A
            maximum of 8 selectable fields are allowed. See
            https://kubernetes.io/docs/concepts/overview/working-with-objects/field-selectors
        served: served is a flag enabling/disabling this version from being served via REST APIs
        storage: storage indicates this version should be used when persisting custom resources to storage.
            There must be exactly one version with storage=true.
        subresources: subresources specify what subresources this version of the defined custom resource have.

    """

    name: str
    served: bool
    storage: bool
    additionalPrinterColumns: Optional[List[CustomResourceColumnDefinition]] = None
    deprecated: Optional[bool] = None
    deprecationWarning: Optional[str] = None
    schema: Optional[CustomResourceValidation] = None
    selectableFields: Optional[List[SelectableField]] = None
    subresources: Optional[CustomResourceSubresources] = None


@dataclass
class CustomResourceSubresourceScale(K8sSpec):
    """CustomResourceSubresourceScale defines how to serve the scale subresource for CustomResources.

    Attributes:
        labelSelectorPath: labelSelectorPath defines the JSON path inside of a custom resource that
            corresponds to Scale `status.selector`. Only JSON paths without the array notation are allowed.
            Must be a JSON Path under `.status` or `.spec`. Must be set to work with HorizontalPodAutoscaler.
            The field pointed by this JSON path must be a string field (not a complex selector struct) which
            contains a serialized label selector in string form.
        specReplicasPath: specReplicasPath defines the JSON path inside of a custom resource that corresponds
            to Scale `spec.replicas`. Only JSON paths without the array notation are allowed. Must be a JSON
            Path under `.spec`. If there is no value under the given path in the custom resource, the `/scale`
            subresource will return an error on GET.
        statusReplicasPath: statusReplicasPath defines the JSON path inside of a custom resource that
            corresponds to Scale `status.replicas`. Only JSON paths without the array notation are allowed.
            Must be a JSON Path under `.status`. If there is no value under the given path in the custom
            resource, the `status.replicas` value in the `/scale` subresource will default to 0.

    """

    specReplicasPath: str
    statusReplicasPath: str
    labelSelectorPath: Optional[str] = None


@dataclass
class CustomResourceSubresources(K8sSpec):
    """CustomResourceSubresources defines the status and scale subresources for CustomResources.

    Attributes:
        scale: scale indicates the custom resource should serve a `/scale` subresource that returns an
            `autoscaling/v1` Scale object.
        status: status indicates the custom resource should serve a `/status` subresource. When enabled: 1.
            requests to the custom resource primary endpoint ignore changes to the `status` stanza of the
            object. 2. requests to the custom resource `/status` subresource ignore changes to anything other
            than the `status` stanza of the object.

    """

    scale: Optional[CustomResourceSubresourceScale] = None
    status: Optional[JSONObj] = None


@dataclass
class CustomResourceValidation(K8sSpec):
    """CustomResourceValidation is a list of validation methods for CustomResources.

    Attributes:
        openAPIV3Schema: openAPIV3Schema is the OpenAPI v3 schema to use for validation and pruning.

    """

    openAPIV3Schema: Optional[JSONObj] = None


@dataclass
class ExternalDocumentation(K8sSpec):
    """ExternalDocumentation allows referencing an external resource for extended documentation.

    Attributes:
        description: ...
        url: ...

    """

    description: Optional[str] = None
    url: Optional[str] = None


@dataclass
class SelectableField(K8sSpec):
    """SelectableField specifies the JSON path of a field that may be used with field selectors.

    Attributes:
        jsonPath: jsonPath is a simple JSON path which is evaluated against each custom resource to produce a
            field selector value. Only JSON paths without the array notation are allowed. Must point to a
            field of type string, boolean or integer. Types with enum values and strings with formats are
            allowed. If jsonPath refers to absent field in a resource, the jsonPath evaluates to an empty
            string. Must not point to metdata fields. Required.

    """

    jsonPath: str


@dataclass
class ServiceReference(K8sSpec):
    """ServiceReference holds a reference to Service.legacy.k8s.io
    Attributes:
        name: name is the name of the service. Required
        namespace: namespace is the namespace of the service. Required
        path: path is an optional URL path at which the webhook will be contacted.
        port: port is an optional service port at which the webhook will be contacted. `port` should be a
            valid port number (1-65535, inclusive). Defaults to 443 for backward compatibility.

    """

    namespace: str
    name: str
    path: Optional[str] = None
    port: Optional[int] = None


@dataclass
class ValidationRule(K8sSpec):
    """ValidationRule describes a validation rule written in the CEL expression language.

    Attributes:
        fieldPath: fieldPath represents the field path returned when the validation fails. It must be a
            relative JSON path (i.e. with array notation) scoped to the location of this x-kubernetes-
            validations extension in the schema and refer to an existing field. e.g. when validation checks if
            a specific attribute `foo` under a map `testMap`, the fieldPath could be set to `.testMap.foo` If
            the validation checks two lists must have unique attributes, the fieldPath could be set to either
            of the list: e.g. `.testList` It does not support list numeric index. It supports child operation
            to refer to an existing field currently. Refer to [JSONPath support in
            Kubernetes](https://kubernetes.io/docs/reference/kubectl/jsonpath/) for more info. Numeric index
            of array is not supported. For field name which contains special characters, use `['specialName']`
            to refer the field name. e.g. for attribute `foo.34$` appears in a list `testList`, the fieldPath
            could be set to `.testList['foo.34$']`
        message: Message represents the message displayed when validation fails. The message is required if
            the Rule contains line breaks. The message must not contain line breaks. If unset, the message is
            'failed rule: {Rule}'. e.g. 'must be a URL with the host matching spec.host'
        messageExpression: MessageExpression declares a CEL expression that evaluates to the validation
            failure message that is returned when this rule fails. Since messageExpression is used as a
            failure message, it must evaluate to a string. If both message and messageExpression are present
            on a rule, then messageExpression will be used if validation fails. If messageExpression results
            in a runtime error, the runtime error is logged, and the validation failure message is produced as
            if the messageExpression field were unset. If messageExpression evaluates to an empty string, a
            string with only spaces, or a string that contains line breaks, then the validation failure
            message will also be produced as if the messageExpression field were unset, and the fact that
            messageExpression produced an empty string/string with only spaces/string with line breaks will be
            logged. messageExpression has access to all the same variables as the rule; the only difference is
            the return type. Example: 'x must be less than max ('+string(self.max)+')'
        optionalOldSelf: optionalOldSelf is used to opt a transition rule into evaluation even when the object
            is first created, or if the old object is missing the value.  When enabled `oldSelf` will be a CEL
            optional whose value will be `None` if there is no old value, or when the object is initially
            created.  You may check for presence of oldSelf using `oldSelf.hasValue()` and unwrap it after
            checking using `oldSelf.value()`. Check the CEL documentation for Optional types for more
            information: https://pkg.go.dev/github.com/google/cel-go/cel#OptionalTypes  May not be set unless
            `oldSelf` is used in `rule`.
        reason: reason provides a machine-readable validation failure reason that is returned to the caller
            when a request fails this validation rule. The HTTP status code returned to the caller will match
            the reason of the reason of the first failed validation rule. The currently supported reasons are:
            'FieldValueInvalid', 'FieldValueForbidden', 'FieldValueRequired', 'FieldValueDuplicate'. If not
            set, default to use 'FieldValueInvalid'. All future added reasons must be accepted by clients when
            reading this value and unknown reasons should be treated as FieldValueInvalid.
        rule: Rule represents the expression which will be evaluated by CEL. ref:
            https://github.com/google/cel-spec The Rule is scoped to the location of the x-kubernetes-
            validations extension in the schema. The `self` variable in the CEL expression is bound to the
            scoped value. Example: - Rule scoped to the root of a resource with a status subresource: {'rule':
            'self.status.actual <= self.spec.maxDesired'}  If the Rule is scoped to an object with properties,
            the accessible properties of the object are field selectable via `self.field` and field presence
            can be checked via `has(self.field)`. Null valued fields are treated as absent fields in CEL
            expressions. If the Rule is scoped to an object with additionalProperties (i.e. a map) the value
            of the map are accessible via `self[mapKey]`, map containment can be checked via `mapKey in self`
            and all entries of the map are accessible via CEL macros and functions such as `self.all(...)`. If
            the Rule is scoped to an array, the elements of the array are accessible via `self[i]` and also by
            macros and functions. If the Rule is scoped to a scalar, `self` is bound to the scalar value.
            Examples: - Rule scoped to a map of objects: {'rule': 'self.components['Widget'].priority < 10'} -
            Rule scoped to a list of integers: {'rule': 'self.values.all(value, value >= 0 && value < 100)'} -
            Rule scoped to a string value: {'rule': 'self.startsWith('kube')'}  The `apiVersion`, `kind`,
            `metadata.name` and `metadata.generateName` are always accessible from the root of the object and
            from any x-kubernetes-embedded-resource annotated objects. No other metadata properties are
            accessible.  Unknown data preserved in custom resources via x-kubernetes-preserve-unknown-fields
            is not accessible in CEL expressions. This includes: - Unknown field values that are preserved by
            object schemas with x-kubernetes-preserve-unknown-fields. - Object properties where the property
            schema is of an 'unknown type'. An 'unknown type' is recursively defined as:   - A schema with no
            type and x-kubernetes-preserve-unknown-fields set to true   - An array where the items schema is
            of an 'unknown type'   - An object where the additionalProperties schema is of an 'unknown type'
            Only property names of the form `[a-zA-Z_.-/][a-zA-Z0-9_.-/]*` are accessible. Accessible property
            names are escaped according to the following rules when accessed in the expression: - '__' escapes
            to '__underscores__' - '.' escapes to '__dot__' - '-' escapes to '__dash__' - '/' escapes to
            '__slash__' - Property names that exactly match a CEL RESERVED keyword escape to '__{keyword}__'.
            The keywords are:           'true', 'false', 'null', 'in', 'as', 'break', 'const', 'continue',
            'else', 'for', 'function', 'if',           'import', 'let', 'loop', 'package', 'namespace',
            'return'. Examples:   - Rule accessing a property named 'namespace': {'rule': 'self.__namespace__
            > 0'}   - Rule accessing a property named 'x-prop': {'rule': 'self.x__dash__prop > 0'}   - Rule
            accessing a property named 'redact__d': {'rule': 'self.redact__underscores__d > 0'}  Equality on
            arrays with x-kubernetes-list-type of 'set' or 'map' ignores element order, i.e. [1, 2] == [2, 1].
            Concatenation on arrays with x-kubernetes-list-type use the semantics of the list type:   - 'set':
            `X + Y` performs a union where the array positions of all elements in `X` are preserved and
            non-intersecting elements in `Y` are appended, retaining their partial order.   - 'map': `X + Y`
            performs a merge where the array positions of all keys in `X` are preserved but the values     are
            overwritten by values in `Y` when the key sets of `X` and `Y` intersect. Elements in `Y` with
            non-intersecting keys are appended, retaining their partial order.  If `rule` makes use of the
            `oldSelf` variable it is implicitly a `transition rule`.  By default, the `oldSelf` variable is
            the same type as `self`. When `optionalOldSelf` is true, the `oldSelf` variable is a CEL optional
            variable whose value() is the same type as `self`. See the documentation for the `optionalOldSelf`
            field for details.  Transition rules by default are applied only on UPDATE requests and are
            skipped if an old value could not be found. You can opt a transition rule into unconditional
            evaluation by setting `optionalOldSelf` to true.

    """

    rule: str
    fieldPath: Optional[str] = None
    message: Optional[str] = None
    messageExpression: Optional[str] = None
    optionalOldSelf: Optional[bool] = None
    reason: Optional[str] = None


@dataclass
class WebhookClientConfig(K8sSpec):
    """WebhookClientConfig contains the information to make a TLS connection with the webhook.

    Attributes:
        caBundle: caBundle is a PEM encoded CA bundle which will be used to validate the webhook's server
            certificate. If unspecified, system trust roots on the apiserver are used.
        service: service is a reference to the service for this webhook. Either service or url must be
            specified.  If the webhook is running within the cluster, then you should use `service`.
        url: url gives the location of the webhook, in standard URL form (`scheme://host:port/path`). Exactly
            one of `url` or `service` must be specified.  The `host` should not refer to a service running in
            the cluster; use the `service` field instead. The host might be resolved via external DNS in some
            apiservers (e.g., `kube-apiserver` cannot resolve in-cluster DNS as that would be a layering
            violation). `host` may also be an IP address.  Please note that using `localhost` or `127.0.0.1`
            as a `host` is risky unless you take great care to run this webhook on all hosts which run an
            apiserver which might need to make calls to this webhook. Such installs are likely to be non-
            portable, i.e., not easy to turn up in a new cluster.  The scheme must be 'https'; the URL must
            begin with 'https://'.  A path is optional, and if present may be any string permissible in a URL.
            You may use the path to pass an arbitrary string to the webhook, for example, a cluster
            identifier.  Attempting to use a user or basic auth e.g. 'user:password@' is not allowed.
            Fragments ('#...') and query parameters ('?...') are not allowed, either.

    """

    caBundle: Optional[str] = None
    service: Optional[ServiceReference] = None
    url: Optional[str] = None


@dataclass
class WebhookConversion(K8sSpec):
    """WebhookConversion describes how to call a conversion webhook
    Attributes:
        clientConfig: clientConfig is the instructions for how to call the webhook if strategy is `Webhook`.
        conversionReviewVersions: conversionReviewVersions is an ordered list of preferred `ConversionReview`
            versions the Webhook expects. The API server will use the first version in the list which it
            supports. If none of the versions specified in this list are supported by API server, conversion
            will fail for the custom resource. If a persisted Webhook configuration specifies allowed versions
            and does not include any versions known to the API Server, calls to the webhook will fail.

    """

    conversionReviewVersions: List[str]
    clientConfig: Optional[WebhookClientConfig] = None
