import gybe


def create_standard_container(image: str, command: list[str]):
    return gybe.k8s.Container(image=image, command=command, name='standard-server')


@gybe.transpiler
def two_pods(image: str, command: list[str]) -> gybe.Manifest:
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


def test_two_pods_chart_transpiles_with_valid_yaml(run_cli):
    result = run_cli(two_pods, VALID_TWO_POD_YAML)
    assert result.exit_code == 0
    assert result.stdout.strip() == EXPECTED_TWO_POD_MANIFEST.strip()


EXPECTED_EMPTY_YAML_VALIDATION_ERROR = """
validation errors:
- required field missing @ $.image
- required field missing @ $.command
"""


def test_two_pods_chart_fails_with_empty_yaml(run_cli):
    result = run_cli(two_pods, '')
    assert result.exit_code == -1
    assert result.stdout.strip() == EXPECTED_EMPTY_YAML_VALIDATION_ERROR.strip()


INVALID_TWO_POD_YAML = """
image: python:3
command: false
"""

EXPECTED_INVALID_TWO_POD_YAML = """
validation errors:
- invalid value for type, expected list @ $.command
"""


def test_two_pods_chart_fails_with_invalid_yaml(run_cli):
    result = run_cli(two_pods, INVALID_TWO_POD_YAML)
    assert result.exit_code == -1
    assert result.stdout.strip() == EXPECTED_INVALID_TWO_POD_YAML.strip()
