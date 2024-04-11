"""Tests model definition code generated from codegen/k8s import-able

List of actively maintained k8s versions here:
https://k8s.io/releases/
"""


def test_import_default_kuberentes():
    """Tests default k8s module imports"""
    from gybe import k8s

    assert k8s


def test_import_k8s_1_26():
    """Tests k8s 1.26 module imports"""
    from gybe.k8s.v1_26.apps import v1

    assert v1
    from gybe.k8s.v1_26.batch import v1

    assert v1
    from gybe.k8s.v1_26.core import v1

    assert v1


def test_import_k8s_1_27():
    """Tests k8s 1.27 module imports"""
    from gybe.k8s.v1_27.apps import v1

    assert v1
    from gybe.k8s.v1_27.batch import v1

    assert v1
    from gybe.k8s.v1_27.core import v1

    assert v1


def test_import_k8s_1_28():
    """Tests k8s 1.28 module imports"""
    from gybe.k8s.v1_28.apps import v1

    assert v1
    from gybe.k8s.v1_28.batch import v1

    assert v1
    from gybe.k8s.v1_28.core import v1

    assert v1


def test_import_k8s_1_29():
    """Tests k8s 1.29 module imports"""
    from gybe.k8s.v1_29.apps import v1

    assert v1
    from gybe.k8s.v1_29.batch import v1

    assert v1
    from gybe.k8s.v1_29.core import v1

    assert v1
