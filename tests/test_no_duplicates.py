from pathlib import Path
from typing import Iterator, Union
import ast
import re

from gybe.clean import PATTERN, iter_k8s_py


def test_no_duplicate_models():
    for path in iter_k8s_py():
        with open(path) as f:
            tree = ast.parse(f.read())
        
        for node in tree.body:
            if isinstance(node, ast.ClassDef):
                has_duplicate = re.search(PATTERN, node.name)
                assert not has_duplicate, f'Duplicate Found: {node.name}'


def get_classes_from_ast(node):
    classes = [n.name for n in ast.walk(node) if isinstance(n, ast.ClassDef)]
    return classes


def walk_module(m: Union[ast.Module, ast.ClassDef]) -> Iterator[ast.AST]:
    for tree in m.body:
        if isinstance(tree, (ast.Module, ast.ClassDef)):
            yield tree
            for tree in walk_module(tree):
                yield tree
        else:
            yield tree
