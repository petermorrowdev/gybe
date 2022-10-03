from typing import List
from pathlib import Path

from gybe.favorites.kubernetes import Pod, PodSpec, Container
import gybe


def create_standard_container(image: str, command: str):
    return Container(image=image, command=command, name='standard-server')


@gybe.transpiler
def two_pods(image: str, command: List[str], port: int=8080) -> gybe.Manifest:
    pod_spec = PodSpec(
        containers=[
            create_standard_container(image=image, command=command)
        ],
        ports=[dict(port=port)]
    )
    return [
        Pod(
            kind='Pod',
            apiVersion='v1',
            metadata=dict(name='pod-1'),
            spec=pod_spec,
        ),
        Pod(
            kind='Pod',
            apiVersion='v1',
            metadata=dict(name='pod-2'),
            spec=pod_spec,
        ),
    ]


VALID_TWO_POD_YAML = """
image: python:3.9
command:
  - python
  - -m
  - http.server
"""


INVALID_VALID_TWO_POD_YAML = """
image: python:3.9
# Expects list of strings so this should fail
command: python -m http.server
"""


def test_two_pods_chart_transpiles_with_valid_yaml(run_cli):
    result = run_cli(two_pods, VALID_TWO_POD_YAML)
    assert result.exit_code == 0


def test_two_pods_chart_fails_with_invalid_yaml(run_cli):
    result = run_cli(two_pods, INVALID_VALID_TWO_POD_YAML)
    assert result.exit_code == -1
