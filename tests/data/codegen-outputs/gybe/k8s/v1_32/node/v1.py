"""Models generated from Kubernetes OpenAPI Spec."""
from __future__ import annotations
from typing import List, Optional, Literal
from dataclasses import dataclass
from gybe.k8s.types import JSONObj, JSONDict, K8sSpec, K8sResource
import gybe.k8s.v1_32.core.v1
import gybe.k8s.v1_32.meta.v1

@dataclass
class Overhead(K8sSpec):
    """
    Overhead structure represents the resource overhead associated with running a pod.
    Attributes:
        podFixed: podFixed represents the fixed resource overhead associated with running a pod.

"""
    podFixed: Optional[JSONDict] = None

@dataclass
class RuntimeClass(K8sResource):
    """
    RuntimeClass defines a class of container runtime supported in the cluster. The RuntimeClass is used
    to determine which container runtime is used to run all containers in a pod. RuntimeClasses are
    manually defined by a user or cluster provisioner, and referenced in the PodSpec. The Kubelet is
    responsible for resolving the RuntimeClassName reference before running the pod.  For more details,
    see https://kubernetes.io/docs/concepts/containers/runtime-class/
    Attributes:
        apiVersion: APIVersion defines the versioned schema of this representation of an object. Servers
            should convert recognized schemas to the latest internal value, and may reject unrecognized
            values.
        handler: handler specifies the underlying runtime and configuration that the CRI implementation will
            use to handle pods of this class. The possible values are specific to the node & CRI
            configuration.  It is assumed that all handlers are available on every node, and handlers of the
            same name are equivalent on every node. For example, a handler called 'runc' might specify that
            the runc OCI runtime (using native Linux containers) will be used to run the containers in a pod.
            The Handler must be lowercase, conform to the DNS Label (RFC 1123) requirements, and is immutable.
        kind: Kind is a string value representing the REST resource this object represents. Servers may infer
            this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.
        metadata:
        overhead: overhead represents the resource overhead associated with running a pod for a given
            RuntimeClass. For more details, see  https://kubernetes.io/docs/concepts/scheduling-eviction/pod-
            overhead/
        scheduling: scheduling holds the scheduling constraints to ensure that pods running with this
            RuntimeClass are scheduled to nodes that support it. If scheduling is nil, this RuntimeClass is
            assumed to be supported by all nodes.

"""
    handler: str
    apiVersion: Literal['node.k8s.io/v1'] = 'node.k8s.io/v1'
    kind: Literal['RuntimeClass'] = 'RuntimeClass'
    metadata: Optional[gybe.k8s.v1_32.meta.v1.ObjectMeta] = None
    overhead: Optional[Overhead] = None
    scheduling: Optional[Scheduling] = None

@dataclass
class Scheduling(K8sSpec):
    """
    Scheduling specifies the scheduling constraints for nodes supporting a RuntimeClass.
    Attributes:
        nodeSelector: nodeSelector lists labels that must be present on nodes that support this RuntimeClass.
            Pods using this RuntimeClass can only be scheduled to a node matched by this selector. The
            RuntimeClass nodeSelector is merged with a pod's existing nodeSelector. Any conflicts will cause
            the pod to be rejected in admission.
        tolerations: tolerations are appended (excluding duplicates) to pods running with this RuntimeClass
            during admission, effectively unioning the set of nodes tolerated by the pod and the RuntimeClass.

"""
    nodeSelector: Optional[JSONDict] = None
    tolerations: Optional[List[gybe.k8s.v1_32.core.v1.Toleration]] = None