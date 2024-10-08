"""Models generated from Kubernetes OpenAPI Spec."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

import gybe.k8s.v1_30.core.v1
import gybe.k8s.v1_30.meta.v1
from gybe.k8s.types import JSONDict, JSONObj, K8sSpec


@dataclass
class Endpoint(K8sSpec):
    """Endpoint represents a single logical 'backend' implementing a service.

    Attributes:
        addresses: addresses of this endpoint. The contents of this field are interpreted according to the
            corresponding EndpointSlice addressType field. Consumers must handle different types of addresses
            in the context of their own capabilities. This must contain at least one address but no more than
            100. These are all assumed to be fungible and clients may choose to only use the first element.
            Refer to: https://issue.k8s.io/106267
        conditions: conditions contains information about the current status of the endpoint.
        deprecatedTopology: deprecatedTopology contains topology information part of the v1beta1 API. This
            field is deprecated, and will be removed when the v1beta1 API is removed (no sooner than
            kubernetes v1.24).  While this field can hold values, it is not writable through the v1 API, and
            any attempts to write to it will be silently ignored. Topology information can be found in the
            zone and nodeName fields instead.
        hints: hints contains information associated with how an endpoint should be consumed.
        hostname: hostname of this endpoint. This field may be used by consumers of endpoints to distinguish
            endpoints from each other (e.g. in DNS names). Multiple endpoints which use the same hostname
            should be considered fungible (e.g. multiple A values in DNS). Must be lowercase and pass DNS
            Label (RFC 1123) validation.
        nodeName: nodeName represents the name of the Node hosting this endpoint. This can be used to
            determine endpoints local to a Node.
        targetRef: targetRef is a reference to a Kubernetes object that represents this endpoint.
        zone: zone is the name of the Zone this endpoint exists in.

    """

    addresses: List[str]
    conditions: Optional[EndpointConditions] = None
    deprecatedTopology: Optional[JSONDict] = None
    hints: Optional[EndpointHints] = None
    hostname: Optional[str] = None
    nodeName: Optional[str] = None
    targetRef: Optional[gybe.k8s.v1_30.core.v1.ObjectReference] = None
    zone: Optional[str] = None


@dataclass
class EndpointConditions(K8sSpec):
    """EndpointConditions represents the current condition of an endpoint.

    Attributes:
        ready: ready indicates that this endpoint is prepared to receive traffic, according to whatever system
            is managing the endpoint. A nil value indicates an unknown state. In most cases consumers should
            interpret this unknown state as ready. For compatibility reasons, ready should never be 'true' for
            terminating endpoints, except when the normal readiness behavior is being explicitly overridden,
            for example when the associated Service has set the publishNotReadyAddresses flag.
        serving: serving is identical to ready except that it is set regardless of the terminating state of
            endpoints. This condition should be set to true for a ready endpoint that is terminating. If nil,
            consumers should defer to the ready condition.
        terminating: terminating indicates that this endpoint is terminating. A nil value indicates an unknown
            state. Consumers should interpret this unknown state to mean that the endpoint is not terminating.

    """

    ready: Optional[bool] = None
    serving: Optional[bool] = None
    terminating: Optional[bool] = None


@dataclass
class EndpointHints(K8sSpec):
    """EndpointHints provides hints describing how an endpoint should be consumed.

    Attributes:
        forZones: forZones indicates the zone(s) this endpoint should be consumed by to enable topology aware
            routing.

    """

    forZones: Optional[List[ForZone]] = None


@dataclass
class EndpointPort(K8sSpec):
    """EndpointPort represents a Port used by an EndpointSlice
    Attributes:
        appProtocol: The application protocol for this port. This is used as a hint for implementations to
            offer richer behavior for protocols that they understand. This field follows standard Kubernetes
            label syntax. Valid values are either:  * Un-prefixed protocol names - reserved for IANA standard
            service names (as per RFC-6335 and https://www.iana.org/assignments/service-names).  * Kubernetes-
            defined prefixed names:   * 'kubernetes.io/h2c' - HTTP/2 prior knowledge over cleartext as
            described in https://www.rfc-editor.org/rfc/rfc9113.html#name-starting-http-2-with-prior-   *
            'kubernetes.io/ws'  - WebSocket over cleartext as described in https://www.rfc-
            editor.org/rfc/rfc6455   * 'kubernetes.io/wss' - WebSocket over TLS as described in
            https://www.rfc-editor.org/rfc/rfc6455  * Other protocols should use implementation-defined
            prefixed names such as mycompany.com/my-custom-protocol.
        name: name represents the name of this port. All ports in an EndpointSlice must have a unique name. If
            the EndpointSlice is derived from a Kubernetes service, this corresponds to the
            Service.ports[].name. Name must either be an empty string or pass DNS_LABEL validation: * must be
            no more than 63 characters long. * must consist of lower case alphanumeric characters or '-'. *
            must start and end with an alphanumeric character. Default is empty string.
        port: port represents the port number of the endpoint. If this is not specified, ports are not
            restricted and must be interpreted in the context of the specific consumer.
        protocol: protocol represents the IP protocol for this port. Must be UDP, TCP, or SCTP. Default is
            TCP.

    """

    appProtocol: Optional[str] = None
    name: Optional[str] = None
    port: Optional[int] = None
    protocol: Optional[str] = None


@dataclass
class EndpointSlice(K8sSpec):
    """EndpointSlice represents a subset of the endpoints that implement a service. For a given service there
    may be multiple EndpointSlice objects, selected by labels, which must be joined to produce the full
    set of endpoints.

    Attributes:
        addressType: addressType specifies the type of address carried by this EndpointSlice. All addresses in
            this slice must be the same type. This field is immutable after creation. The following address
            types are currently supported: * IPv4: Represents an IPv4 Address. * IPv6: Represents an IPv6
            Address. * FQDN: Represents a Fully Qualified Domain Name.
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        endpoints: endpoints is a list of unique endpoints in this slice. Each slice may include a maximum of
            1000 endpoints.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard object's metadata.
        ports: ports specifies the list of network ports exposed by each endpoint in this slice. Each port
            must have a unique name. When ports is empty, it indicates that there are no defined ports. When a
            port is defined with a nil port value, it indicates 'all ports'. Each slice may include a maximum
            of 100 ports.

    """

    addressType: str
    endpoints: List[Endpoint]
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[gybe.k8s.v1_30.meta.v1.ObjectMeta] = None
    ports: Optional[List[EndpointPort]] = None


@dataclass
class EndpointSliceList(K8sSpec):
    """EndpointSliceList represents a list of endpoint slices
    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        items: items is the list of endpoint slices
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: Standard list metadata.

    """

    items: List[EndpointSlice]
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[JSONObj] = None


@dataclass
class ForZone(K8sSpec):
    """ForZone provides information about which zones should consume this endpoint.

    Attributes:
        name: name represents the name of the zone.

    """

    name: str
