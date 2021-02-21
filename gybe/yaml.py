import yaml


def yaml_dumps(d: dict) -> str:
    return yaml.dump(d, default_flow_style=False)


def yaml_loads(s: str) -> dict:
    return yaml.safe_load(s)
