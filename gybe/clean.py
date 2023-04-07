from pathlib import Path
import ast
import re


CWD = Path(__file__).parent
PATTERN = r'Model\d*'


def iter_k8s_py():
    return CWD.parent.glob('gybe/kubernetes/**/*.py')


def replace_empty_with_none():
    for path in iter_k8s_py():
        with open(path) as f:
            cleaned = f.read().replace('{},', 'None,')
        with open(path, 'w') as f:
            f.write(cleaned)


def remove_duplicate_classes():
    removed = set()

    for path in iter_k8s_py():
        with open(path, 'r') as f:
            m = ast.parse(f.read())

        nodes = []
        for n in m.body:
            if isinstance(n, ast.ClassDef):
                if re.search(PATTERN, n.name):
                    removed.add(n.name)
                else:
                    nodes.append(n)
            else:
                nodes.append(n)
        
        with open(path, 'w') as f:
            for n in nodes:
                f.write(ast.unparse(n) + '\n')
    
    if len(removed):
        for path in iter_k8s_py():
            with open(path) as f:
                code = f.read()
                for r in reversed(sorted(list(removed))):
                    code = code.replace(r, re.sub(PATTERN, '', r))
            with open(path, 'w') as f:
                f.write(code)


if __name__ == '__main__':
    replace_empty_with_none()
    remove_duplicate_classes()
