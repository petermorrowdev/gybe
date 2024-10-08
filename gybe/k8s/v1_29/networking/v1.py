"""Models generated from Kubernetes OpenAPI Spec."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Literal, Optional

import gybe.k8s.v1_29.core.v1
import gybe.k8s.v1_29.meta.v1
from gybe.k8s.types import JSONObj, K8sResource, K8sSpec


@dataclass
class HTTPIngressPath(K8sSpec):
    """HTTPIngressPath associates a path with a backend. Incoming urls matching the path are forwarded to the
    backend.

    Attributes:
        backend: backend defines the referenced service endpoint to which the traffic will be forwarded to.
        path: path is matched against the path of an incoming request. Currently it can contain characters
            disallowed from the conventional 'path' part of a URL as defined by RFC 3986. Paths must begin
            with a '/' and must be present when using PathType with value 'Exact' or 'Prefix'.
        pathType: pathType determines the interpretation of the path matching. PathType can be one of the
            following values: * Exact: Matches the URL path exactly. * Prefix: Matches based on a URL path
            prefix split by '/'. Matching is   done on a path element by element basis. A path element refers
            is the   list of labels in the path split by the '/' separator. A request is a   match for path p
            if every p is an element-wise prefix of p of the   request path. Note that if the last element of
            the path is a substring   of the last element in request path, it is not a match (e.g. /foo/bar
            matches /foo/bar/baz, but does not match /foo/barbaz). * ImplementationSpecific: Interpretation of
            the Path matching is up to   the IngressClass. Implementations can treat this as a separate
            PathType   or treat it identically to Prefix or Exact path types. Implementations are required to
            support all path types.

    """

    pathType: str
    backend: IngressBackend
    path: Optional[str] = None


@dataclass
class HTTPIngressRuleValue(K8sSpec):
    """HTTPIngressRuleValue is a list of http selectors pointing to backends. In the example:
    http://<host>/<path>?<searchpart> -> backend where where parts of the url correspond to RFC 3986, this
    resource will be used to match against everything after the last '/' and before the first '?' or '#'.

    Attributes:
        paths: paths is a collection of paths that map requests to backends.

    """

    paths: List[HTTPIngressPath]


@dataclass
class Ingress(K8sResource):
    """Ingress is a collection of rules that allow inbound connections to reach the endpoints defined by a
    backend. An Ingress can be configured to give services externally-reachable urls, load balance
    traffic, terminate SSL, offer name based virtual hosting etc.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object's metadata.
        spec: spec is the desired state of the Ingress.
        status: status is the current state of the Ingress.

    """

    apiVersion: Literal['networking.k8s.io/v1'] = 'networking.k8s.io/v1'
    kind: Literal['Ingress'] = 'Ingress'
    metadata: Optional[gybe.k8s.v1_29.meta.v1.ObjectMeta] = None
    spec: Optional[IngressSpec] = None
    status: Optional[IngressStatus] = None


@dataclass
class IngressBackend(K8sSpec):
    """IngressBackend describes all endpoints for a given service and port.

    Attributes:
        resource: resource is an ObjectRef to another Kubernetes resource in the namespace of the Ingress
            object. If resource is specified, a service.Name and service.Port must not be specified. This is a
            mutually exclusive setting with 'Service'.
        service: service references a service as a backend. This is a mutually exclusive setting with
            'Resource'.

    """

    resource: Optional[gybe.k8s.v1_29.core.v1.TypedLocalObjectReference] = None
    service: Optional[IngressServiceBackend] = None


@dataclass
class IngressClass(K8sSpec):
    """IngressClass represents the class of the Ingress, referenced by the Ingress Spec. The
    `ingressclass.kubernetes.io/is-default-class` annotation can be used to indicate that an IngressClass
    should be considered default. When a single IngressClass resource has this annotation set to true, new
    Ingress resources without a class specified will be assigned this default class.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object's metadata.
        spec: spec is the desired state of the IngressClass.

    """

    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[gybe.k8s.v1_29.meta.v1.ObjectMeta] = None
    spec: Optional[IngressClassSpec] = None


@dataclass
class IngressClassList(K8sSpec):
    """IngressClassList is a collection of IngressClasses.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        items: items is the list of IngressClasses.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard list metadata.

    """

    items: List[IngressClass]
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[JSONObj] = None


@dataclass
class IngressClassParametersReference(K8sSpec):
    """IngressClassParametersReference identifies an API object. This can be used to specify a cluster or
    namespace-scoped resource.

    Attributes:
        apiGroup: apiGroup is the group for the resource being referenced. If APIGroup is not specified, the
            specified Kind must be in the core API group. For any other third-party types, APIGroup is
            required.
        kind: kind is the type of resource being referenced.
        name: name is the name of resource being referenced.
        namespace: namespace is the namespace of the resource being referenced. This field is required when
            scope is set to 'Namespace' and must be unset when scope is set to 'Cluster'.
        scope: scope represents if this refers to a cluster or namespace scoped resource. This may be set to
            'Cluster' (default) or 'Namespace'.

    """

    kind: str
    name: str
    apiGroup: Optional[str] = None
    namespace: Optional[str] = None
    scope: Optional[str] = None


@dataclass
class IngressClassSpec(K8sSpec):
    """IngressClassSpec provides information about the class of an Ingress.

    Attributes:
        controller: controller refers to the name of the controller that should handle this class. This allows
            for different 'flavors' that are controlled by the same controller. For example, you may have
            different parameters for the same implementing controller. This should be specified as a domain-
            prefixed path no more than 250 characters in length, e.g. 'acme.io/ingress-controller'. This field
            is immutable.
        parameters: parameters is a link to a custom resource containing additional configuration for the
            controller. This is optional if the controller does not require extra parameters.

    """

    controller: Optional[str] = None
    parameters: Optional[IngressClassParametersReference] = None


@dataclass
class IngressList(K8sSpec):
    """IngressList is a collection of Ingress.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        items: items is the list of Ingress.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object's metadata.

    """

    items: List[Ingress]
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[JSONObj] = None


@dataclass
class IngressLoadBalancerIngress(K8sSpec):
    """IngressLoadBalancerIngress represents the status of a load-balancer ingress point.

    Attributes:
        hostname: hostname is set for load-balancer ingress points that are DNS based.
        ip: ip is set for load-balancer ingress points that are IP based.
        ports: ports provides information about the ports exposed by this LoadBalancer.

    """

    hostname: Optional[str] = None
    ip: Optional[str] = None
    ports: Optional[List[IngressPortStatus]] = None


@dataclass
class IngressLoadBalancerStatus(K8sSpec):
    """IngressLoadBalancerStatus represents the status of a load-balancer.

    Attributes:
        ingress: ingress is a list containing ingress points for the load-balancer.

    """

    ingress: Optional[List[IngressLoadBalancerIngress]] = None


@dataclass
class IngressPortStatus(K8sSpec):
    """IngressPortStatus represents the error condition of a service port
    Attributes:
        error: error is to record the problem with the service port The format of the error shall comply with
            the following rules: - built-in error values shall be specified in this file and those shall use
            CamelCase names - cloud provider specific error values must have names that comply with the
            format foo.example.com/CamelCase.
        port: port is the port number of the ingress port.
        protocol: protocol is the protocol of the ingress port. The supported values are: 'TCP', 'UDP', 'SCTP'

    """

    port: int
    protocol: str
    error: Optional[str] = None


@dataclass
class IngressRule(K8sSpec):
    """IngressRule represents the rules mapping the paths under a specified host to the related backend
    services. Incoming requests are first evaluated for a host match, then routed to the backend
    associated with the matching IngressRuleValue.

    Attributes:
        host: host is the fully qualified domain name of a network host, as defined by RFC 3986. Note the
            following deviations from the 'host' part of the URI as defined in RFC 3986: 1. IPs are not
            allowed. Currently an IngressRuleValue can only apply to    the IP in the Spec of the parent
            Ingress. 2. The `:` delimiter is not respected because ports are not allowed.           Currently
            the port of an Ingress is implicitly :80 for http and           :443 for https. Both these may
            change in the future. Incoming requests are matched against the host before the IngressRuleValue.
            If the host is unspecified, the Ingress routes all traffic based on the specified
            IngressRuleValue.  host can be 'precise' which is a domain name without the terminating dot of a
            network host (e.g. 'foo.bar.com') or 'wildcard', which is a domain name prefixed with a single
            wildcard label (e.g. '*.foo.com'). The wildcard character '*' must appear by itself as the first
            DNS label and matches only a single label. You cannot have a wildcard label by itself (e.g. Host
            == '*'). Requests will be matched against the Host field in the following way: 1. If host is
            precise, the request matches this rule if the http host header is equal to Host. 2. If host is a
            wildcard, then the request matches this rule if the http host header is to equal to the suffix
            (removing the first label) of the wildcard rule.
        http: ...

    """

    host: Optional[str] = None
    http: Optional[HTTPIngressRuleValue] = None


@dataclass
class IngressServiceBackend(K8sSpec):
    """IngressServiceBackend references a Kubernetes Service as a Backend.

    Attributes:
        name: name is the referenced service. The service must exist in the same namespace as the Ingress
            object.
        port: port of the referenced service. A port name or port number is required for a
            IngressServiceBackend.

    """

    name: str
    port: Optional[ServiceBackendPort] = None


@dataclass
class IngressSpec(K8sSpec):
    """IngressSpec describes the Ingress the user wishes to exist.

    Attributes:
        defaultBackend: defaultBackend is the backend that should handle requests that don't match any rule.
            If Rules are not specified, DefaultBackend must be specified. If DefaultBackend is not set, the
            handling of requests that do not match any of the rules will be up to the Ingress controller.
        ingressClassName: ingressClassName is the name of an IngressClass cluster resource. Ingress controller
            implementations use this field to know whether they should be serving this Ingress resource, by a
            transitive connection (controller -> IngressClass -> Ingress resource). Although the
            `kubernetes.io/ingress.class` annotation (simple constant name) was never formally defined, it was
            widely supported by Ingress controllers to create a direct binding between Ingress controller and
            Ingress resources. Newly created Ingress resources should prefer using the field. However, even
            though the annotation is officially deprecated, for backwards compatibility reasons, ingress
            controllers should still honor that annotation if present.
        rules: rules is a list of host rules used to configure the Ingress. If unspecified, or no rule
            matches, all traffic is sent to the default backend.
        tls: tls represents the TLS configuration. Currently the Ingress only supports a single TLS port, 443.
            If multiple members of this list specify different hosts, they will be multiplexed on the same
            port according to the hostname specified through the SNI TLS extension, if the ingress controller
            fulfilling the ingress supports SNI.

    """

    defaultBackend: Optional[IngressBackend] = None
    ingressClassName: Optional[str] = None
    rules: Optional[List[IngressRule]] = None
    tls: Optional[List[IngressTLS]] = None


@dataclass
class IngressStatus(K8sSpec):
    """IngressStatus describe the current state of the Ingress.

    Attributes:
        loadBalancer: loadBalancer contains the current status of the load-balancer.

    """

    loadBalancer: Optional[IngressLoadBalancerStatus] = None


@dataclass
class IngressTLS(K8sSpec):
    """IngressTLS describes the transport layer security associated with an ingress.

    Attributes:
        hosts: hosts is a list of hosts included in the TLS certificate. The values in this list must match
            the name/s used in the tlsSecret. Defaults to the wildcard host setting for the loadbalancer
            controller fulfilling this Ingress, if left unspecified.
        secretName: secretName is the name of the secret used to terminate TLS traffic on port 443. Field is
            left optional to allow TLS routing based on SNI hostname alone. If the SNI host in a listener
            conflicts with the 'Host' header field used by an IngressRule, the SNI host is used for
            termination and value of the 'Host' header is used for routing.

    """

    hosts: Optional[List[str]] = None
    secretName: Optional[str] = None


@dataclass
class NetworkPolicy(K8sSpec):
    """NetworkPolicy describes what network traffic is allowed for a set of Pods
    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object's metadata.
        spec: spec represents the specification of the desired behavior for this NetworkPolicy.

    """

    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[gybe.k8s.v1_29.meta.v1.ObjectMeta] = None
    spec: Optional[NetworkPolicySpec] = None


@dataclass
class NetworkPolicyEgressRule(K8sSpec):
    """NetworkPolicyEgressRule describes a particular set of traffic that is allowed out of pods matched by a
    NetworkPolicySpec's podSelector. The traffic must match both ports and to. This type is beta-level in
    1.8
    Attributes:
        ports: ports is a list of destination ports for outgoing traffic. Each item in this list is combined
            using a logical OR. If this field is empty or missing, this rule matches all ports (traffic not
            restricted by port). If this field is present and contains at least one item, then this rule
            allows traffic only if the traffic matches at least one port in the list.
        to: to is a list of destinations for outgoing traffic of pods selected for this rule. Items in this
            list are combined using a logical OR operation. If this field is empty or missing, this rule
            matches all destinations (traffic not restricted by destination). If this field is present and
            contains at least one item, this rule allows traffic only if the traffic matches at least one item
            in the to list.

    """

    ports: Optional[List[NetworkPolicyPort]] = None
    to: Optional[List[NetworkPolicyPeer]] = None


@dataclass
class NetworkPolicyList(K8sSpec):
    """NetworkPolicyList is a list of NetworkPolicy objects.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        items: items is a list of schema objects.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard list metadata.

    """

    items: List[NetworkPolicy]
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[JSONObj] = None


@dataclass
class NetworkPolicyPeer(K8sSpec):
    """NetworkPolicyPeer describes a peer to allow traffic to/from. Only certain combinations of fields are
    allowed
    Attributes:
        ipBlock: ipBlock defines policy on a particular IPBlock. If this field is set then neither of the
            other fields can be.
        namespaceSelector: namespaceSelector selects namespaces using cluster-scoped labels. This field
            follows standard label selector semantics; if present but empty, it selects all namespaces.  If
            podSelector is also set, then the NetworkPolicyPeer as a whole selects the pods matching
            podSelector in the namespaces selected by namespaceSelector. Otherwise it selects all pods in the
            namespaces selected by namespaceSelector.
        podSelector: podSelector is a label selector which selects pods. This field follows standard label
            selector semantics; if present but empty, it selects all pods.  If namespaceSelector is also set,
            then the NetworkPolicyPeer as a whole selects the pods matching podSelector in the Namespaces
            selected by NamespaceSelector. Otherwise it selects the pods matching podSelector in the policy's
            own namespace.

    """

    ipBlock: Optional[JSONObj] = None
    namespaceSelector: Optional[gybe.k8s.v1_29.meta.v1.LabelSelector] = None
    podSelector: Optional[gybe.k8s.v1_29.meta.v1.LabelSelector] = None


@dataclass
class NetworkPolicyPort(K8sSpec):
    """NetworkPolicyPort describes a port to allow traffic on
    Attributes:
        endPort: endPort indicates that the range of ports from port to endPort if set, inclusive, should be
            allowed by the policy. This field cannot be defined if the port field is not defined or if the
            port field is defined as a named (string) port. The endPort must be equal or greater than port.
        port: port represents the port on the given protocol. This can either be a numerical or named port on
            a pod. If this field is not provided, this matches all port names and numbers. If present, only
            traffic on the specified protocol AND port will be matched.
        protocol: protocol represents the protocol (TCP, UDP, or SCTP) which traffic must match. If not
            specified, this field defaults to TCP.

    """

    endPort: Optional[int] = None
    port: Optional[str] = None
    protocol: Optional[str] = None


@dataclass
class NetworkPolicySpec(K8sSpec):
    """NetworkPolicySpec provides the specification of a NetworkPolicy
    Attributes:
        egress: egress is a list of egress rules to be applied to the selected pods. Outgoing traffic is
            allowed if there are no NetworkPolicies selecting the pod (and cluster policy otherwise allows the
            traffic), OR if the traffic matches at least one egress rule across all of the NetworkPolicy
            objects whose podSelector matches the pod. If this field is empty then this NetworkPolicy limits
            all outgoing traffic (and serves solely to ensure that the pods it selects are isolated by
            default). This field is beta-level in 1.8
        ingress: ingress is a list of ingress rules to be applied to the selected pods. Traffic is allowed to
            a pod if there are no NetworkPolicies selecting the pod (and cluster policy otherwise allows the
            traffic), OR if the traffic source is the pod's local node, OR if the traffic matches at least one
            ingress rule across all of the NetworkPolicy objects whose podSelector matches the pod. If this
            field is empty then this NetworkPolicy does not allow any traffic (and serves solely to ensure
            that the pods it selects are isolated by default)
        podSelector: podSelector selects the pods to which this NetworkPolicy object applies. The array of
            ingress rules is applied to any pods selected by this field. Multiple network policies can select
            the same set of pods. In this case, the ingress rules for each are combined additively. This field
            is NOT optional and follows standard label selector semantics. An empty podSelector matches all
            pods in this namespace.
        policyTypes: policyTypes is a list of rule types that the NetworkPolicy relates to. Valid options are
            ['Ingress'], ['Egress'], or ['Ingress', 'Egress']. If this field is not specified, it will default
            based on the existence of ingress or egress rules; policies that contain an egress section are
            assumed to affect egress, and all policies (whether or not they contain an ingress section) are
            assumed to affect ingress. If you want to write an egress-only policy, you must explicitly specify
            policyTypes [ 'Egress' ]. Likewise, if you want to write a policy that specifies that no egress is
            allowed, you must specify a policyTypes value that include 'Egress' (since such a policy would not
            include an egress section and would otherwise default to just [ 'Ingress' ]). This field is beta-
            level in 1.8

    """

    podSelector: gybe.k8s.v1_29.meta.v1.LabelSelector
    egress: Optional[List[NetworkPolicyEgressRule]] = None
    ingress: Optional[List[JSONObj]] = None
    policyTypes: Optional[List[str]] = None


@dataclass
class ServiceBackendPort(K8sSpec):
    """ServiceBackendPort is the service port being referenced.

    Attributes:
        name: name is the name of the port on the Service. This is a mutually exclusive setting with 'Number'.
        number: number is the numerical port number (e.g. 80) on the Service. This is a mutually exclusive
            setting with 'Name'.

    """

    name: Optional[str] = None
    number: Optional[int] = None
