"""Tests model definition code generated from codegen/kubernetes import-able

List of actively maintained kubernetes versions here:
https://kubernetes.io/releases/
"""


def test_import_default_kuberentes():
    """Tests default kubernetes module imports"""
    from gybe import kubernetes
    assert kubernetes


def test_import_kubernetes_1_26():
    """Tests kubernetes 1.26 module imports"""
    from gybe.kubernetes.v1_26.io.k8s.api.apps import v1
    assert v1
    from gybe.kubernetes.v1_26.io.k8s.api.batch import v1
    assert v1
    from gybe.kubernetes.v1_26.io.k8s.api.core import v1
    assert v1


def test_import_kubernetes_1_27():
    """Tests kubernetes 1.27 module imports"""
    from gybe.kubernetes.v1_27.io.k8s.api.apps import v1
    assert v1
    from gybe.kubernetes.v1_27.io.k8s.api.batch import v1
    assert v1
    from gybe.kubernetes.v1_27.io.k8s.api.core import v1
    assert v1


def test_import_kubernetes_1_28():
    """Tests kubernetes 1.28 module imports"""
    from gybe.kubernetes.v1_28.io.k8s.api.apps import v1
    assert v1
    from gybe.kubernetes.v1_28.io.k8s.api.batch import v1
    assert v1
    from gybe.kubernetes.v1_28.io.k8s.api.core import v1
    assert v1


def test_import_kubernetes_1_29():
    """Tests kubernetes 1.29 module imports"""
    from gybe.kubernetes.v1_29.io.k8s.api.apps import v1
    assert v1
    from gybe.kubernetes.v1_29.io.k8s.api.batch import v1
    assert v1
    from gybe.kubernetes.v1_29.io.k8s.api.core import v1
    assert v1
