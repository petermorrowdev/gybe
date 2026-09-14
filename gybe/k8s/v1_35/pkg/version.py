"""Models generated from Kubernetes OpenAPI Spec."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from gybe.k8s.types import K8sSpec


@dataclass
class Info(K8sSpec):
    """Info contains versioning information. how we'll want to distribute that information.

    Attributes:
        buildDate: ...
        compiler: ...
        emulationMajor: EmulationMajor is the major version of the emulation version
        emulationMinor: EmulationMinor is the minor version of the emulation version
        gitCommit: ...
        gitTreeState: ...
        gitVersion: ...
        goVersion: ...
        major: Major is the major version of the binary version
        minCompatibilityMajor: MinCompatibilityMajor is the major version of the minimum compatibility version
        minCompatibilityMinor: MinCompatibilityMinor is the minor version of the minimum compatibility version
        minor: Minor is the minor version of the binary version
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
    emulationMajor: Optional[str] = None
    emulationMinor: Optional[str] = None
    minCompatibilityMajor: Optional[str] = None
    minCompatibilityMinor: Optional[str] = None
