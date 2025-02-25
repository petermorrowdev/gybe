from pathlib import Path
from tempfile import TemporaryDirectory

import pytest

from gybe.codegen.k8s_modules import write_module

base_test_spec_dir = Path(__file__).parent / 'data/k8s-api-specs'
base_codegen_out_dir = Path(__file__).parent / 'data/codegen-outputs'
k8s_module_dir = base_codegen_out_dir / 'gybe/k8s'


@pytest.mark.parametrize(
    'version,version_module',
    [
        ('v1.29.13', 'v1_29'),
        ('v1.30.9', 'v1_30'),
        ('v1.31.5', 'v1_31'),
        ('v1.32.1', 'v1_32'),
    ],
)
def test_codegen_write_module(version, version_module):
    base_version_dir = base_test_spec_dir / version
    base_api_version_dir = base_version_dir / 'api/'

    assert base_api_version_dir.exists()

    k8s_openapi_dir = base_api_version_dir / 'openapi-spec/v3'

    with TemporaryDirectory() as tdir:
        temp_k8s_module_dir = Path(tdir) / 'gybe/k8s'
        (temp_k8s_module_dir / version_module).mkdir(parents=True)
        write_module(
            k8s_version_module=version_module,
            k8s_module_dir=temp_k8s_module_dir,
            k8s_openapi_dir=k8s_openapi_dir,
        )


def test_cli_importable():
    from gybe.codegen import __main__, cli

    _ = cli, __main__
