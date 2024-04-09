from typing import List

import gybe


def create_standard_container(image: str, command: List[str]):
    return gybe.k8s.Container(image=image, command=command, name='standard-server')


@gybe.transpiler
def two_pods(image: str, command: List[str], port: int = 8080) -> gybe.Manifest:
    pod_spec = gybe.k8s.PodSpec(
        containers=[create_standard_container(image=image, command=command)],
    )
    return [
        gybe.k8s.Pod(
            kind='Pod',
            apiVersion='v1',
            metadata=gybe.k8s.ObjectMeta(name='pod-1'),
            spec=pod_spec,
        ),
        gybe.k8s.Pod(
            kind='Pod',
            apiVersion='v1',
            metadata=gybe.k8s.ObjectMeta(name='pod-2'),
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
