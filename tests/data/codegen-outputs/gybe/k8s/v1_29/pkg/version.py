"""Models generated from Kubernetes OpenAPI Spec."""
from __future__ import annotations
from typing import List, Optional, Literal
from dataclasses import dataclass
from gybe.k8s.types import JSONObj, JSONDict, K8sSpec, K8sResource

@dataclass
class Info(K8sSpec):
    """
    Info contains versioning information. how we'll want to distribute that information.
    Attributes:
        buildDate: ...
        compiler: ...
        gitCommit: ...
        gitTreeState: ...
        gitVersion: ...
        goVersion: ...
        major: ...
        minor: ...
        platform: ...

"""
    major: str
    minor: str
    gitVersion: str
    gitCommit: str
    gitTreeState: str
    buildDate: str
    goVersion: str
    compiler: str
    platform: str