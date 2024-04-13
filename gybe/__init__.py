"""A simple YAML transpilation tool for rendering kubernetes manifests"""

__version__ = '0.3.0'


from typing import List

from gybe import k8s
from gybe.decorators import transpiler

Manifest = List[k8s.K8sSpec]

__all__ = ['k8s', 'Manifest', 'transpiler']
