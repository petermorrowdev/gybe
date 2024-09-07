# Gybe

![PyPI Package](https://img.shields.io/pypi/v/gybe?color=%2334D058&label=PyPI%20Package)

Transpile Kubernetes manifests with your simple values.yaml files using python type-hints.
Gybe is a simple, declarative, and more pythonic alternative to [helm](https://helm.sh/)
that makes it easier to develop modest kubernetes deployments.

## Reqiurements

Python 3.10+

## Install

```bash
pip install gybe
```

## Example

Create a `values.yaml` file:

```yaml
image: python:3
command:
  - python
  - -m
  - http.server
```

Create a `chart.py` file:

```python
import gybe


def create_standard_container(image: str, command: list[str]):
    return gybe.k8s.Container(image=image, command=command, name='my-python-server')


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
    image: python:3
    name: my-python-server
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
    name: my-python-server
```

If you're feeling lucky, you can pipe that into `kubectl`:

```bash
python chart.py values.yaml | kubectl apply -f -
```

```
pod/pod-1 created
pod/pod-2 created
```


```bash
kubectl get pods
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
