"""Models generated from Kubernetes OpenAPI Spec."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Literal, Optional

import gybe.k8s.v1_37.meta.v1 as _meta_v1
from gybe.k8s.types import JSONDict, K8sResource, K8sSpec


@dataclass
class CertificateSigningRequest(K8sResource):
    """CertificateSigningRequest objects provide a mechanism to obtain x509 certificates by submitting a
    certificate signing request, and having it asynchronously approved and issued.  Kubelets use this API
    to obtain:  1. client certificates to authenticate to kube-apiserver (with the 'kubernetes.io/kube-
    apiserver-client-kubelet' signerName).  2. serving certificates for TLS endpoints kube-apiserver can
    connect to securely (with the 'kubernetes.io/kubelet-serving' signerName).  This API can be used to
    request client certificates to authenticate to kube-apiserver (with the 'kubernetes.io/kube-apiserver-
    client' signerName), or to obtain certificates from custom non-Kubernetes signers.

    Attributes:
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
    apiVersion: Literal['certificates.k8s.io/v1'] = 'certificates.k8s.io/v1'
    kind: Literal['CertificateSigningRequest'] = 'CertificateSigningRequest'
    metadata: Optional[_meta_v1.ObjectMeta] = None
    status: Optional[CertificateSigningRequestStatus] = None


@dataclass
class CertificateSigningRequestCondition(K8sSpec):
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
class CertificateSigningRequestSpec(K8sSpec):
    """CertificateSigningRequestSpec contains the certificate request.

    Attributes:
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
class CertificateSigningRequestStatus(K8sSpec):
    """CertificateSigningRequestStatus contains conditions used to indicate approved/denied/failed status of
    the request, and the issued certificate.

    Attributes:
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


@dataclass
class ClusterTrustBundle(K8sResource):
    """ClusterTrustBundle is a cluster-scoped container for X.509 trust anchors (root certificates).
    ClusterTrustBundle objects are considered to be readable by any authenticated user in the cluster,
    because they can be mounted by pods using the `clusterTrustBundle` projection.  All service accounts
    have read access to ClusterTrustBundles by default.  Users who only have namespace-level access to a
    cluster can read ClusterTrustBundles by impersonating a serviceaccount that they have access to.  It
    can be optionally associated with a particular signer, in which case it contains one valid set of
    trust anchors for that signer. Signers may have multiple associated ClusterTrustBundles; each is an
    independent set of trust anchors for that signer. Admission control is used to enforce that only users
    with permissions on the signer can create or modify the corresponding bundle.

    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: metadata contains the object metadata.
        spec: spec contains the signer (if any) and trust anchors.

    """

    spec: ClusterTrustBundleSpec
    apiVersion: Literal['certificates.k8s.io/v1'] = 'certificates.k8s.io/v1'
    kind: Literal['ClusterTrustBundle'] = 'ClusterTrustBundle'
    metadata: Optional[_meta_v1.ObjectMeta] = None


@dataclass
class ClusterTrustBundleSpec(K8sSpec):
    """ClusterTrustBundleSpec contains the signer and trust anchors.

    Attributes:
        signerName: signerName indicates the associated signer, if any.  In order to create or update a
            ClusterTrustBundle that sets signerName, you must have the following cluster-scoped permission:
            group=certificates.k8s.io resource=signers resourceName=<the signer name> verb=attest.  If
            signerName is not empty, then the ClusterTrustBundle object must be named with the signer name as
            a prefix (translating slashes to colons). For example, for the signer name `example.com/foo`,
            valid ClusterTrustBundle object names include `example.com:foo:abc` and `example.com:foo:v1`.  If
            signerName is empty, then the ClusterTrustBundle object's name must not have such a prefix.
            List/watch requests for ClusterTrustBundles can filter on this field using a
            `spec.signerName=NAME` field selector.
        trustBundle: trustBundle contains the individual X.509 trust anchors for this bundle, as PEM bundle of
            PEM-wrapped, DER-formatted X.509 certificates.  The data must consist only of PEM certificate
            blocks that parse as valid X.509 certificates.  Each certificate must include a basic constraints
            extension with the CA bit set.  The API server will reject objects that contain duplicate
            certificates, or that use PEM block headers.  Users of ClusterTrustBundles, including Kubelet, are
            free to reorder and deduplicate certificate blocks in this file according to their own logic, as
            well as to drop PEM block headers and inter-block data.

    """

    trustBundle: str
    signerName: Optional[str] = None


@dataclass
class PodCertificateRequest(K8sResource):
    """PodCertificateRequest encodes a pod requesting a certificate from a given signer.  Kubelets use this
    API to implement podCertificate projected volumes
    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata: metadata contains the object metadata.
        spec: spec contains the details about the certificate being requested.
        status: status contains the issued certificate, and a standard set of conditions.

    """

    spec: PodCertificateRequestSpec
    apiVersion: Literal['certificates.k8s.io/v1'] = 'certificates.k8s.io/v1'
    kind: Literal['PodCertificateRequest'] = 'PodCertificateRequest'
    metadata: Optional[_meta_v1.ObjectMeta] = None
    status: Optional[PodCertificateRequestStatus] = None


@dataclass
class PodCertificateRequestSpec(K8sSpec):
    """PodCertificateRequestSpec describes the certificate request.  All fields are immutable after creation.

    Attributes:
        maxExpirationSeconds: maxExpirationSeconds is the maximum lifetime permitted for the certificate.  If
            omitted, kube-apiserver will set it to 86400(24 hours). kube-apiserver will reject values shorter
            than 3600 (1 hour).  The maximum allowable value is 7862400 (91 days).  The signer implementation
            is then free to issue a certificate with any lifetime *shorter* than MaxExpirationSeconds, but no
            shorter than 3600 seconds (1 hour).  This constraint is enforced by kube-apiserver.
            `kubernetes.io` signers will never issue certificates with a lifetime longer than 24 hours.
        nodeName: nodeName is the name of the node the pod is assigned to.
        nodeUID: nodeUID is the UID of the node the pod is assigned to.
        podName: podName is the name of the pod into which the certificate will be mounted.
        podUID: podUID is the UID of the pod into which the certificate will be mounted.
        serviceAccountName: serviceAccountName is the name of the service account the pod is running as.
        serviceAccountUID: serviceAccountUID is the UID of the service account the pod is running as.
        signerName: signerName indicates the requested signer.  All signer names beginning with
            `kubernetes.io` are reserved for use by the Kubernetes project.  There is currently one well-known
            signer documented by the Kubernetes project, `kubernetes.io/kube-apiserver-client-pod`, which will
            issue client certificates understood by kube-apiserver.  It is currently unimplemented.
        stubPKCS10Request: A PKCS#10 certificate signing request (DER-serialized) generated by Kubelet using
            the subject private key.  Most signer implementations will ignore the contents of the CSR except
            to extract the subject public key. The API server automatically verifies the CSR signature during
            admission, so the signer does not need to repeat the verification.  CSRs generated by kubelet are
            completely empty.  The subject public key must be one of RSA3072, RSA4096, ECDSAP256, ECDSAP384,
            ECDSAP521, or ED25519. Note that this list may be expanded in the future.  Signer implementations
            do not need to support all key types supported by kube-apiserver and kubelet.  If a signer does
            not support the key type used for a given PodCertificateRequest, it must deny the request by
            setting a status.conditions entry with a type of 'Denied' and a reason of 'UnsupportedKeyType'. It
            may also suggest a key type that it does support in the message field.
        unverifiedUserAnnotations: unverifiedUserAnnotations allow pod authors to pass additional information
            to the signer implementation.  Kubernetes does not restrict or validate this metadata in any way.
            Entries are subject to the same validation as object metadata annotations, with the addition that
            all keys must be domain-prefixed. No restrictions are placed on values, except an overall size
            limitation on the entire field.  Signers should document the keys and values they support.
            Signers should deny requests that contain keys they do not recognize.

    """

    signerName: str
    podName: str
    podUID: str
    serviceAccountName: str
    serviceAccountUID: str
    nodeName: str
    nodeUID: str
    stubPKCS10Request: str
    maxExpirationSeconds: Optional[int] = None
    unverifiedUserAnnotations: Optional[JSONDict] = None


@dataclass
class PodCertificateRequestStatus(K8sSpec):
    """PodCertificateRequestStatus describes the status of the request, and holds the certificate data if the
    request is issued.

    Attributes:
        beginRefreshAt: beginRefreshAt is the time at which the kubelet should begin trying to refresh the
            certificate.  This field is set via the /status subresource, and must be set at the same time as
            certificateChain.  Once populated, this field is immutable.  This field is only a hint.  Kubelet
            may start refreshing before or after this time if necessary.
        certificateChain: certificateChain is populated with an issued certificate by the signer. This field
            is set via the /status subresource. Once populated, this field is immutable.  If the certificate
            signing request is denied, a condition of type 'Denied' is added and this field remains empty. If
            the signer cannot issue the certificate, a condition of type 'Failed' is added and this field
            remains empty.  Validation requirements:  1. certificateChain must consist of one or more PEM-
            formatted certificates.  2. Each entry must be a valid PEM-wrapped, DER-encoded ASN.1 Certificate
            as     described in section 4 of RFC5280.  If more than one block is present, and the definition
            of the requested spec.signerName does not indicate otherwise, the first block is the issued
            certificate, and subsequent blocks should be treated as intermediate certificates and presented in
            TLS handshakes.  When projecting the chain into a pod volume, kubelet will drop any data in-
            between the PEM blocks, as well as any PEM block headers.
        conditions: conditions applied to the request.  The types 'Issued', 'Denied', and 'Failed' have
            special handling.  At most one of these conditions may be present, and they must have status
            'True'.  If the request is denied with `Reason=UnsupportedKeyType`, the signer may suggest a key
            type that will work in the message field.
        notAfter: notAfter is the time at which the certificate expires.  The value must be the same as the
            notAfter value in the leaf certificate in certificateChain.  This field is set via the /status
            subresource.  Once populated, it is immutable.  The signer must set this field at the same time it
            sets certificateChain.
        notBefore: notBefore is the time at which the certificate becomes valid.  The value must be the same
            as the notBefore value in the leaf certificate in certificateChain.  This field is set via the
            /status subresource.  Once populated, it is immutable. The signer must set this field at the same
            time it sets certificateChain.

    """

    beginRefreshAt: Optional[str] = None
    certificateChain: Optional[str] = None
    conditions: Optional[List[_meta_v1.Condition]] = None
    notAfter: Optional[str] = None
    notBefore: Optional[str] = None
