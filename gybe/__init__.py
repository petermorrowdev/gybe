"""A simple YAML transpilation tool for rendering kubernetes manifests"""

__version__ = '0.2.2'


from typing import Any, List

from gybe import k8s
from gybe.decorators import transpiler

Manifest = List[Any]

__all__ = ['k8s', 'Manifest', 'transpiler']
