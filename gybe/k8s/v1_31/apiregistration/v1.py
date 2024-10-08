"""Models generated from Kubernetes OpenAPI Spec."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Literal, Optional

import gybe.k8s.v1_31.meta.v1
from gybe.k8s.types import JSONObj, K8sResource, K8sSpec


@dataclass
class APIService(K8sResource):
    """APIService represents a server for a particular GroupVersion. Name must be 'version.group'.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object's metadata.
        spec: Spec contains information for locating and communicating with a server
        status: Status contains derived information about an API server

    """

    apiVersion: Literal['apiregistration.k8s.io/v1'] = 'apiregistration.k8s.io/v1'
    kind: Literal['APIService'] = 'APIService'
    metadata: Optional[gybe.k8s.v1_31.meta.v1.ObjectMeta] = None
    spec: Optional[APIServiceSpec] = None
    status: Optional[APIServiceStatus] = None


@dataclass
class APIServiceCondition(K8sSpec):
    """APIServiceCondition describes the state of an APIService at a particular point
    Attributes:
        lastTransitionTime: Last time the condition transitioned from one status to another.
        message: Human-readable message indicating details about last transition.
        reason: Unique, one-word, CamelCase reason for the condition's last transition.
        status: Status is the status of the condition. Can be True, False, Unknown.
        type: Type is the type of the condition.

    """

    type: str
    status: str
    lastTransitionTime: Optional[str] = None
    message: Optional[str] = None
    reason: Optional[str] = None


@dataclass
class APIServiceList(K8sSpec):
    """APIServiceList is a list of APIService objects.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        items: Items is the list of APIService
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard list metadata

    """

    items: List[APIService]
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[JSONObj] = None


@dataclass
class APIServiceSpec(K8sSpec):
    """APIServiceSpec contains information for locating and communicating with a server. Only https is
    supported, though you are able to disable certificate verification.

    Attributes:
        caBundle: CABundle is a PEM encoded CA bundle which will be used to validate an API server's serving
            certificate. If unspecified, system trust roots on the apiserver are used.
        group: Group is the API group name this server hosts
        groupPriorityMinimum: GroupPriorityMinimum is the priority this group should have at least. Higher
            priority means that the group is preferred by clients over lower priority ones. Note that other
            versions of this group might specify even higher GroupPriorityMinimum values such that the whole
            group gets a higher priority. The primary sort is based on GroupPriorityMinimum, ordered highest
            number to lowest (20 before 10). The secondary sort is based on the alphabetical comparison of the
            name of the object.  (v1.bar before v1.foo) We'd recommend something like: *.k8s.io (except
            extensions) at 18000 and PaaSes (OpenShift, Deis) are recommended to be in the 2000s
        insecureSkipTLSVerify: InsecureSkipTLSVerify disables TLS certificate verification when communicating
            with this server. This is strongly discouraged.  You should use the CABundle instead.
        service: Service is a reference to the service for this API server.  It must communicate on port 443.
            If the Service is nil, that means the handling for the API groupversion is handled locally on this
            server. The call will simply delegate to the normal handler chain to be fulfilled.
        version: Version is the API version this server hosts.  For example, 'v1'
        versionPriority: VersionPriority controls the ordering of this API version inside of its group.  Must
            be greater than zero. The primary sort is based on VersionPriority, ordered highest to lowest (20
            before 10). Since it's inside of a group, the number can be small, probably in the 10s. In case of
            equal version priorities, the version string will be used to compute the order inside a group. If
            the version string is 'kube-like', it will sort above non 'kube-like' version strings, which are
            ordered lexicographically. 'Kube-like' versions start with a 'v', then are followed by a number
            (the major version), then optionally the string 'alpha' or 'beta' and another number (the minor
            version). These are sorted first by GA > beta > alpha (where GA is a version with no suffix such
            as beta or alpha), and then by comparing major version, then minor version. An example sorted list
            of versions: v10, v2, v1, v11beta2, v10beta3, v3beta1, v12alpha1, v11alpha2, foo1, foo10.

    """

    groupPriorityMinimum: int
    versionPriority: int
    caBundle: Optional[str] = None
    group: Optional[str] = None
    insecureSkipTLSVerify: Optional[bool] = None
    service: Optional[ServiceReference] = None
    version: Optional[str] = None


@dataclass
class APIServiceStatus(K8sSpec):
    """APIServiceStatus contains derived information about an API server
    Attributes:
        conditions: Current service state of apiService.

    """

    conditions: Optional[List[APIServiceCondition]] = None


@dataclass
class ServiceReference(K8sSpec):
    """ServiceReference holds a reference to Service.legacy.k8s.io
    Attributes:
        name: Name is the name of the service
        namespace: Namespace is the namespace of the service
        port: If specified, the port on the service that hosting webhook. Default to 443 for backward
            compatibility. `port` should be a valid port number (1-65535, inclusive).

    """

    name: Optional[str] = None
    namespace: Optional[str] = None
    port: Optional[int] = None
