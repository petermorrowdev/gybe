from dataclasses import dataclass, field

import pytest

import gybe
from gybe.decorators import set_nested_arg


def test_set_nested_arg_list_path():
    data = [[1, 2], {'a': 1}]
    set_nested_arg('0.1', 3, data)
    assert data == [[1, 3], {'a': 1}]


def test_set_nested_arg_dict_then_list_path():
    data = {'a': [1, 2]}
    set_nested_arg('a.1', 3, data)
    assert data == {'a': [1, 3]}


def test_set_nested_arg_dict_then_list_path_wrong_type_fails():
    data = {'a': [1, 2]}
    with pytest.raises(ValueError):
        set_nested_arg('a.b', 3, data)


def test_set_nested_arg_list_then_dict_path():
    data = [[1, 2], {'a': 1}]
    set_nested_arg('1.a', 3, data)
    assert data == [[1, 2], {'a': 3}]


def test_set_nested_arg_dict_then_list_deep_path():
    data = {'a': [1, {'b': 2}]}
    set_nested_arg('a.1.b', 3, data)
    assert data == {'a': [1, {'b': 3}]}


def test_two_pod_example_path():
    path = 'pod_one.command.1'
    value = 'http.server'
    data = {
        'pod_one': {'name': 'pod-1', 'image': 'python:3', 'command': ['python', 'server.py']},
        'pod_two': {'name': 'pod-2', 'image': 'python:3', 'command': ['python', 'server.py']},
    }
    set_nested_arg(path, value, data)
    assert data['pod_one']['command'][1] == 'http.server'


@dataclass
class PodConfig:
    name: str
    image: str = 'python:3'
    command: list[str] = field(default_factory=lambda: ['python', 'server.py'])


def create_standard_container(image: str, command: list[str] | None = None):
    return gybe.k8s.Container(image=image, command=command, name='standard-server')


@gybe.transpiler
def two_pods_nested(pod_one: PodConfig, pod_two: PodConfig) -> gybe.Manifest:
    return [
        gybe.k8s.Pod(
            kind='Pod',
            apiVersion='v1',
            metadata=gybe.k8s.ObjectMeta(name='pod-1'),
            spec=gybe.k8s.PodSpec(
                containers=[create_standard_container(image=pod_one.image, command=pod_one.command)],
            ),
        ),
        gybe.k8s.Pod(
            kind='Pod',
            apiVersion='v1',
            metadata=gybe.k8s.ObjectMeta(name='pod-2'),
            spec=gybe.k8s.PodSpec(
                containers=[create_standard_container(image=pod_two.image, command=pod_two.command)],
            ),
        ),
    ]


VALID_YAML = """
pod_one:
  name: pod-1
pod_two:
  name: pod-2
"""


def test_two_pods_nested_set_image(run_cli):
    result = run_cli(two_pods_nested, VALID_YAML, '--set', 'pod_one.image=python:3.14')
    assert result.exit_code == 0, result.stdout.strip()


def test_two_pods_nested_set_command(run_cli):
    result = run_cli(two_pods_nested, VALID_YAML, '--set', 'pod_one.command.1=http.server')
    assert result.exit_code == 0, result.stdout.strip()
