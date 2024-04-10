"""Models generated from Kubernetes OpenAPI Spec."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

import gybe.k8s.v1_27.meta.v1
from gybe.k8s.types import JSONDict, JSONObj


@dataclass
class CertificateSigningRequest:
    """CertificateSigningRequest objects provide a mechanism to obtain x509 certificates by submitting a
    certificate signing request, and having it asynchronously approved and issued.  Kubelets use this API
    to obtain:  1. client certificates to authenticate to kube-apiserver (with the 'kubernetes.io/kube-
    apiserver-client-kubelet' signerName).  2. serving certificates for TLS endpoints kube-apiserver can
    connect to securely (with the 'kubernetes.io/kubelet-serving' signerName).  This API can be used to
    request client certificates to authenticate to kube-apiserver (with the 'kubernetes.io/kube-apiserver-
    client' signerName), or to obtain certificates from custom non-Kubernetes signers.

    Attributes
    ----------
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: ...
        spec: spec contains the certificate request, and is immutable after creation. Only the request,
            signerName, expirationSeconds, and usages fields can be set on creation. Other fields are derived
            by Kubernetes and cannot be modified by users.
        status: status contains information about whether the request is approved or denied, and the
            certificate issued by the signer, or the failure condition indicating signer failure.

    """

    spec: CertificateSigningRequestSpec
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[gybe.k8s.v1_27.meta.v1.ObjectMeta] = None
    status: Optional[CertificateSigningRequestStatus] = None


@dataclass
class CertificateSigningRequestCondition:
    """CertificateSigningRequestCondition describes a condition of a CertificateSigningRequest object
    Attributes:
        lastTransitionTime: lastTransitionTime is the time the condition last transitioned from one status to
            another. If unset, when a new condition type is added or an existing condition's status is
            changed, the server defaults this to the current time.
        lastUpdateTime: lastUpdateTime is the time of the last update to this condition
        message: message contains a human readable message with details about the request state
        reason: reason indicates a brief reason for the request state
        status: status of the condition, one of True, False, Unknown. Approved, Denied, and Failed conditions
            may not be 'False' or 'Unknown'.
        type: type of the condition. Known conditions are 'Approved', 'Denied', and 'Failed'.  An 'Approved'
            condition is added via the /approval subresource, indicating the request was approved and should
            be issued by the signer.  A 'Denied' condition is added via the /approval subresource, indicating
            the request was denied and should not be issued by the signer.  A 'Failed' condition is added via
            the /status subresource, indicating the signer failed to issue the certificate.  Approved and
            Denied conditions are mutually exclusive. Approved, Denied, and Failed conditions cannot be
            removed once added.  Only one condition of a given type is allowed.

    """

    type: str
    status: str
    lastTransitionTime: Optional[str] = None
    lastUpdateTime: Optional[str] = None
    message: Optional[str] = None
    reason: Optional[str] = None


@dataclass
class CertificateSigningRequestList:
    """CertificateSigningRequestList is a collection of CertificateSigningRequest objects
    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        items: items is a collection of CertificateSigningRequest objects
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: ...

    """

    items: List[CertificateSigningRequest]
    apiVersion: Optional[str] = None
    kind: Optional[str] = None
    metadata: Optional[JSONObj] = None


@dataclass
class CertificateSigningRequestSpec:
    """CertificateSigningRequestSpec contains the certificate request.

    Attributes
    ----------
        expirationSeconds: expirationSeconds is the requested duration of validity of the issued certificate.
            The certificate signer may issue a certificate with a different validity duration so a client must
            check the delta between the notBefore and and notAfter fields in the issued certificate to
            determine the actual duration.  The v1.22+ in-tree implementations of the well-known Kubernetes
            signers will honor this field as long as the requested duration is not greater than the maximum
            duration they will honor per the --cluster-signing-duration CLI flag to the Kubernetes controller
            manager.  Certificate signers may not honor this field for various reasons:    1. Old signer that
            is unaware of the field (such as the in-tree      implementations prior to v1.22)   2. Signer
            whose configured maximum is shorter than the requested duration   3. Signer whose configured
            minimum is longer than the requested duration  The minimum valid value for expirationSeconds is
            600, i.e. 10 minutes.
        extra: extra contains extra attributes of the user that created the CertificateSigningRequest.
            Populated by the API server on creation and immutable.
        groups: groups contains group membership of the user that created the CertificateSigningRequest.
            Populated by the API server on creation and immutable.
        request: request contains an x509 certificate signing request encoded in a 'CERTIFICATE REQUEST' PEM
            block. When serialized as JSON or YAML, the data is additionally base64-encoded.
        signerName: signerName indicates the requested signer, and is a qualified name.  List/watch requests
            for CertificateSigningRequests can filter on this field using a 'spec.signerName=NAME'
            fieldSelector.  Well-known Kubernetes signers are:  1. 'kubernetes.io/kube-apiserver-client':
            issues client certificates that can be used to authenticate to kube-apiserver.   Requests for this
            signer are never auto-approved by kube-controller-manager, can be issued by the 'csrsigning'
            controller in kube-controller-manager.  2. 'kubernetes.io/kube-apiserver-client-kubelet': issues
            client certificates that kubelets use to authenticate to kube-apiserver.   Requests for this
            signer can be auto-approved by the 'csrapproving' controller in kube-controller-manager, and can
            be issued by the 'csrsigning' controller in kube-controller-manager.  3. 'kubernetes.io/kubelet-
            serving' issues serving certificates that kubelets use to serve TLS endpoints, which kube-
            apiserver can connect to securely.   Requests for this signer are never auto-approved by kube-
            controller-manager, and can be issued by the 'csrsigning' controller in kube-controller-manager.
            More details are available at https://k8s.io/docs/reference/access-authn-authz/certificate-
            signing-requests/#kubernetes-signers  Custom signerNames can also be specified. The signer
            defines:  1. Trust distribution: how trust (CA bundles) are distributed.  2. Permitted subjects:
            and behavior when a disallowed subject is requested.  3. Required, permitted, or forbidden x509
            extensions in the request (including whether subjectAltNames are allowed, which types,
            restrictions on allowed values) and behavior when a disallowed extension is requested.  4.
            Required, permitted, or forbidden key usages / extended key usages.  5. Expiration/certificate
            lifetime: whether it is fixed by the signer, configurable by the admin.  6. Whether or not
            requests for CA certificates are allowed.
        uid: uid contains the uid of the user that created the CertificateSigningRequest. Populated by the API
            server on creation and immutable.
        usages: usages specifies a set of key usages requested in the issued certificate.  Requests for TLS
            client certificates typically request: 'digital signature', 'key encipherment', 'client auth'.
            Requests for TLS serving certificates typically request: 'key encipherment', 'digital signature',
            'server auth'.  Valid values are:  'signing', 'digital signature', 'content commitment',  'key
            encipherment', 'key agreement', 'data encipherment',  'cert sign', 'crl sign', 'encipher only',
            'decipher only', 'any',  'server auth', 'client auth',  'code signing', 'email protection',
            's/mime',  'ipsec end system', 'ipsec tunnel', 'ipsec user',  'timestamping', 'ocsp signing',
            'microsoft sgc', 'netscape sgc'
        username: username contains the name of the user that created the CertificateSigningRequest. Populated
            by the API server on creation and immutable.

    """

    request: str
    signerName: str
    expirationSeconds: Optional[int] = None
    extra: Optional[JSONDict] = None
    groups: Optional[List[str]] = None
    uid: Optional[str] = None
    usages: Optional[List[str]] = None
    username: Optional[str] = None


@dataclass
class CertificateSigningRequestStatus:
    """CertificateSigningRequestStatus contains conditions used to indicate approved/denied/failed status of
    the request, and the issued certificate.

    Attributes
    ----------
        certificate: certificate is populated with an issued certificate by the signer after an Approved
            condition is present. This field is set via the /status subresource. Once populated, this field is
            immutable.  If the certificate signing request is denied, a condition of type 'Denied' is added
            and this field remains empty. If the signer cannot issue the certificate, a condition of type
            'Failed' is added and this field remains empty.  Validation requirements:  1. certificate must
            contain one or more PEM blocks.  2. All PEM blocks must have the 'CERTIFICATE' label, contain no
            headers, and the encoded data   must be a BER-encoded ASN.1 Certificate structure as described in
            section 4 of RFC5280.  3. Non-PEM content may appear before or after the 'CERTIFICATE' PEM blocks
            and is unvalidated,   to allow for explanatory text as described in section 5.2 of RFC7468.  If
            more than one PEM block is present, and the definition of the requested spec.signerName does not
            indicate otherwise, the first block is the issued certificate, and subsequent blocks should be
            treated as intermediate certificates and presented in TLS handshakes.  The certificate is encoded
            in PEM format.  When serialized as JSON or YAML, the data is additionally base64-encoded, so it
            consists of:      base64(     -----BEGIN CERTIFICATE-----     ...     -----END CERTIFICATE-----
            )
        conditions: conditions applied to the request. Known conditions are 'Approved', 'Denied', and
            'Failed'.

    """

    certificate: Optional[str] = None
    conditions: Optional[List[CertificateSigningRequestCondition]] = None
