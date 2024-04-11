"""Models generated from Kubernetes OpenAPI Spec."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Info:
    """Info contains versioning information. how we'll want to distribute that information.

    Attributes
    ----------
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
