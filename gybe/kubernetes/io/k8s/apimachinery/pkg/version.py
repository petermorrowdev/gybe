from __future__ import annotations
from pydantic import BaseModel


class Info(BaseModel):
    buildDate: str
    compiler: str
    gitCommit: str
    gitTreeState: str
    gitVersion: str
    goVersion: str
    major: str
    minor: str
    platform: str
