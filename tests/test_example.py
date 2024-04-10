import gybe


def create_standard_container(image: str, command: list[str]):
    return gybe.k8s.Container(image=image, command=command, name='standard-server')


@gybe.transpiler
def two_pods(image: str, command: list[str], port: int = 8080) -> gybe.Manifest:
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
image: python:3
command:
  - python
  - -m
  - http.server
"""

EXPECTED_TWO_POD_MANIFEST = """
apiVersion: v1
kind: Pod
metadata:
  name: pod-1
spec:
  containers:
  - command:
    - python
    - -m
    - http.server
    image: python:3
    name: standard-server
---
apiVersion: v1
kind: Pod
metadata:
  name: pod-2
spec:
  containers:
  - command:
    - python
    - -m
    - http.server
    image: python:3
    name: standard-server
"""

INVALID_VALID_TWO_POD_YAML = """
image: python:3
command: false
"""


def test_two_pods_chart_transpiles_with_valid_yaml(run_cli):
    result = run_cli(two_pods, VALID_TWO_POD_YAML)
    assert result.exit_code == 0
    assert result.stdout.strip() == EXPECTED_TWO_POD_MANIFEST.strip()


def test_two_pods_chart_fails_with_invalid_yaml(run_cli):
    result = run_cli(two_pods, INVALID_VALID_TWO_POD_YAML)
    assert result.exit_code == -1
