"""gybe.k8s codegen cli"""

import argparse

from gybe.codegen.k8s_modules import write_module


def main():
    """Run gybe.k8s code generator cli"""
    parser = argparse.ArgumentParser()
    parser.add_argument('k8s_version_module')
    args = parser.parse_args()
    write_module(args.k8s_version_module)
