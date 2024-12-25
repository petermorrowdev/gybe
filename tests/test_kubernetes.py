"""Tests model definition code generated from codegen/k8s import-able

List of actively maintained k8s versions here:
https://k8s.io/releases/
"""


def test_import_default_kuberentes():
    """Tests default k8s module imports"""
    from gybe import k8s

    assert k8s


def test_import_k8s_1_29():
    """Tests k8s 1.29 module imports"""
    from gybe.k8s.v1_29.apps import v1

    assert v1
    from gybe.k8s.v1_29.batch import v1

    assert v1
    from gybe.k8s.v1_29.core import v1

    assert v1


def test_import_k8s_1_30():
    """Tests k8s 1.30 module imports"""
    from gybe.k8s.v1_30.apps import v1

    assert v1
    from gybe.k8s.v1_30.batch import v1

    assert v1
    from gybe.k8s.v1_30.core import v1

    assert v1


def test_import_k8s_1_31():
    """Tests k8s 1.31 module imports"""
    from gybe.k8s.v1_31.apps import v1

    assert v1
    from gybe.k8s.v1_31.batch import v1

    assert v1
    from gybe.k8s.v1_31.core import v1

    assert v1


def test_import_k8s_1_32():
    """Tests k8s 1.32 module imports"""
    from gybe.k8s.v1_32.apps import v1

    assert v1
    from gybe.k8s.v1_32.batch import v1

    assert v1
    from gybe.k8s.v1_32.core import v1

    assert v1
