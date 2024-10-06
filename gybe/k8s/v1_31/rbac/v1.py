"""Models generated from Kubernetes OpenAPI Spec."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

import gybe.k8s.v1_31.meta.v1
from gybe.k8s.types import JSONObj, K8sSpec


@dataclass
class AggregationRule(K8sSpec):
    """AggregationRule describes how to locate ClusterRoles to aggregate into the ClusterRole
    Attributes:
        clusterRoleSelectors: ClusterRoleSelectors holds a list of selectors which will be used to find
            ClusterRoles and create the rules. If any of the selectors match, then the ClusterRole's
            permissions will be added

    """

    clusterRoleSelectors: Optional[List[gybe.k8s.v1_31.meta.v1.LabelSelector]] = None


@dataclass
class ClusterRole(K8sSpec):
    """ClusterRole is a cluster level, logical grouping of PolicyRules that can be referenced as a unit by a
    RoleBinding or ClusterRoleBinding.

    Attributes:
        aggregationRule: AggregationRule is an optional field that describes how to build the Rules for this
            ClusterRole. If AggregationRule is set, then the Rules are controller managed and direct changes
            to Rules will be stomped by the controller.
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object's metadata.
        rules: Rules holds all the PolicyRules for this ClusterRole

    """

    aggregationRule: Optional[AggregationRule] = None
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[gybe.k8s.v1_31.meta.v1.ObjectMeta] = None
    rules: Optional[List[PolicyRule]] = None


@dataclass
class ClusterRoleBinding(K8sSpec):
    """ClusterRoleBinding references a ClusterRole, but not contain it.  It can reference a ClusterRole in
    the global namespace, and adds who information via Subject.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object's metadata.
        roleRef: RoleRef can only reference a ClusterRole in the global namespace. If the RoleRef cannot be
            resolved, the Authorizer must return an error. This field is immutable.
        subjects: Subjects holds references to the objects the role applies to.

    """

    roleRef: RoleRef
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[gybe.k8s.v1_31.meta.v1.ObjectMeta] = None
    subjects: Optional[List[Subject]] = None


@dataclass
class ClusterRoleBindingList(K8sSpec):
    """ClusterRoleBindingList is a collection of ClusterRoleBindings
    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        items: Items is a list of ClusterRoleBindings
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object's metadata.

    """

    items: List[ClusterRoleBinding]
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[JSONObj] = None


@dataclass
class ClusterRoleList(K8sSpec):
    """ClusterRoleList is a collection of ClusterRoles
    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        items: Items is a list of ClusterRoles
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object's metadata.

    """

    items: List[ClusterRole]
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[JSONObj] = None


@dataclass
class PolicyRule(K8sSpec):
    """PolicyRule holds information that describes a policy rule, but does not contain information about who
    the rule applies to or which namespace the rule applies to.

    Attributes:
        apiGroups: APIGroups is the name of the APIGroup that contains the resources.  If multiple API groups
            are specified, any action requested against one of the enumerated resources in any API group will
            be allowed. '' represents the core API group and '*' represents all API groups.
        nonResourceURLs: NonResourceURLs is a set of partial urls that a user should have access to.  *s are
            allowed, but only as the full, final step in the path Since non-resource URLs are not namespaced,
            this field is only applicable for ClusterRoles referenced from a ClusterRoleBinding. Rules can
            either apply to API resources (such as 'pods' or 'secrets') or non-resource URL paths (such as
            '/api'),  but not both.
        resourceNames: ResourceNames is an optional white list of names that the rule applies to.  An empty
            set means that everything is allowed.
        resources: Resources is a list of resources this rule applies to. '*' represents all resources.
        verbs: Verbs is a list of Verbs that apply to ALL the ResourceKinds contained in this rule. '*'
            represents all verbs.

    """

    verbs: List[str]
    apiGroups: Optional[List[str]] = None
    nonResourceURLs: Optional[List[str]] = None
    resourceNames: Optional[List[str]] = None
    resources: Optional[List[str]] = None


@dataclass
class Role(K8sSpec):
    """Role is a namespaced, logical grouping of PolicyRules that can be referenced as a unit by a
    RoleBinding.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object's metadata.
        rules: Rules holds all the PolicyRules for this Role

    """

    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[gybe.k8s.v1_31.meta.v1.ObjectMeta] = None
    rules: Optional[List[PolicyRule]] = None


@dataclass
class RoleBinding(K8sSpec):
    """RoleBinding references a role, but does not contain it.  It can reference a Role in the same namespace
    or a ClusterRole in the global namespace. It adds who information via Subjects and namespace
    information by which namespace it exists in.  RoleBindings in a given namespace only have effect in
    that namespace.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object's metadata.
        roleRef: RoleRef can reference a Role in the current namespace or a ClusterRole in the global
            namespace. If the RoleRef cannot be resolved, the Authorizer must return an error. This field is
            immutable.
        subjects: Subjects holds references to the objects the role applies to.

    """

    roleRef: RoleRef
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[gybe.k8s.v1_31.meta.v1.ObjectMeta] = None
    subjects: Optional[List[Subject]] = None


@dataclass
class RoleBindingList(K8sSpec):
    """RoleBindingList is a collection of RoleBindings
    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        items: Items is a list of RoleBindings
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object's metadata.

    """

    items: List[RoleBinding]
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[JSONObj] = None


@dataclass
class RoleList(K8sSpec):
    """RoleList is a collection of Roles
    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        items: Items is a list of Roles
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object's metadata.

    """

    items: List[Role]
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[JSONObj] = None


@dataclass
class RoleRef(K8sSpec):
    """RoleRef contains information that points to the role being used
    Attributes:
        apiGroup: APIGroup is the group for the resource being referenced
        kind: Kind is the type of resource being referenced
        name: Name is the name of resource being referenced

    """

    apiGroup: str
    kind: str
    name: str


@dataclass
class Subject(K8sSpec):
    """Subject contains a reference to the object or user identities a role binding applies to.  This can
    either hold a direct API object reference, or a value for non-objects such as user and group names.

    Attributes:
        apiGroup: APIGroup holds the API group of the referenced subject. Defaults to '' for ServiceAccount
            subjects. Defaults to 'rbac.authorization.k8s.io' for User and Group subjects.
        kind: Kind of object being referenced. Values defined by this API group are 'User', 'Group', and
            'ServiceAccount'. If the Authorizer does not recognized the kind value, the Authorizer should
            report an error.
        name: Name of the object being referenced.
        namespace: Namespace of the referenced object.  If the object kind is non-namespace, such as 'User' or
            'Group', and this value is not empty the Authorizer should report an error.

    """

    kind: str
    name: str
    apiGroup: Optional[str] = None
    namespace: Optional[str] = None
