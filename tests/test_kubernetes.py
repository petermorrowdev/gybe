"""Tests model definition code generated from codegen/k8s import-able

List of actively maintained k8s versions here:
https://k8s.io/releases/
"""


def test_import_default_kuberentes():
    """Tests default k8s module imports"""
    from gybe import k8s

    assert k8s


def test_import_k8s_1_34():
    """Tests k8s 1.31 module imports"""
    from gybe.k8s.v1_34.apps import v1

    assert v1
    from gybe.k8s.v1_34.batch import v1

    assert v1
    from gybe.k8s.v1_34.core import v1

    assert v1


def test_import_k8s_1_35():
    """Tests k8s 1.32 module imports"""
    from gybe.k8s.v1_35.apps import v1

    assert v1
    from gybe.k8s.v1_35.batch import v1

    assert v1
    from gybe.k8s.v1_35.core import v1

    assert v1


def test_import_k8s_1_36():
    """Tests k8s 1.33 module imports"""
    from gybe.k8s.v1_36.apps import v1

    assert v1
    from gybe.k8s.v1_36.batch import v1

    assert v1
    from gybe.k8s.v1_36.core import v1

    assert v1


def test_import_k8s_1_37():
    """Tests k8s 1.34 module imports"""
    from gybe.k8s.v1_37.apps import v1

    assert v1
    from gybe.k8s.v1_37.batch import v1

    assert v1
    from gybe.k8s.v1_37.core import v1

    assert v1
