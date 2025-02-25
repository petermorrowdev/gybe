import ast
import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent
PATTERN = r'Model\d*'


def iter_k8s_py():
    return PROJECT_ROOT.parent.glob('gybe/k8s/**/*.py')


def test_no_duplicate_models():
    duplicates = {}
    for path in iter_k8s_py():
        with open(path) as f:
            tree = ast.parse(f.read())

        for node in tree.body:
            if isinstance(node, ast.ClassDef):
                has_duplicate = re.search(PATTERN, node.name)
                if has_duplicate:
                    clean_name = re.sub(PATTERN, '', node.name)
                    duplicates[clean_name] = duplicates.get(clean_name, 0) + 1

    count = sum([v for v in duplicates.values()])
    top_five = '\n\t'.join([f'{k}: {v}' for k, v in sorted(duplicates.items(), key=lambda i: -i[1])][:5])
    assert not count, f'Found {count} duplicates: \n\t{top_five}\n\t...{count - 5} more'
