"""Read and write YAML."""

from typing import Any

import yaml


def yaml_dumps(d: dict[str, Any]) -> str:
    """Write dict to YAML str"""
    return yaml.dump(d, default_flow_style=False)


def yaml_loads(s: str) -> dict[str, Any]:
    """Read dict from YAML str"""
    return yaml.safe_load(s)
