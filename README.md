# Gybe

![PyPI Package](https://img.shields.io/pypi/v/gybe?color=%2334D058&label=PyPI%20Package)
![codecov.io](https://codecov.io/github/petermorrow/gybe/coverage.svg?branch=main)

Transpile Kubernetes manifests with your simple values.yaml files using python type-hints.
Gybe is a simple, declarative, and more pythonic alternative to [helm](https://helm.sh/)
that makes it easier to develop modest kubernetes deployments.

## Reqiurements

Python 3.7+

Gybe uses [pydantic](https://github.com/samuelcolvin/pydantic) for type-hint
validation and [click](https://github.com/pallets/click) for the CLI.

## Install

```
pip install gybe
```

## Example

Create a simple `values.yaml` file:

```yaml
image: python:3.9
command:
  - python
  - -m
  - http.server
```

Create a `chart.py` file:

```python
from typing import List

from gybe.kubernetes.favorites import Pod, PodSpec, Container
import gybe


def create_standard_container(image: str, command: List[str]):
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


if __name__ == '__main__':
    two_pods()
```

Now run your transpiler with your values file:

```bash
python chart.py values.yaml
```

```yaml
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
    image: python:3.9
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
    image: python:3.9
    name: standard-server
```

If you're feeling lucky, you can pipe that into `kubectl`:

```bash
python chart.py values.yaml | kubectl apply -f -
```

```
pod/pod-1 created
pod/pod-2 created
```bash
$ kubectl get pods
```

```
NAME    READY   STATUS    RESTARTS   AGE
pod-1   1/1     Running   0          5s
pod-2   1/1     Running   0          5s
```

```bash
python chart.py values.yaml | kubectl delete -f -
```

```
pod "pod-1" deleted
pod "pod-2" deleted
```
