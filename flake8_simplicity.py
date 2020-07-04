import ast


__version__ = '0.0.1'


FORBIDDEN = {
    # ast.AnnAssign is captured by presence of annotation.
    ast.AsyncFunctionDef: 100,
    ast.AsyncFor: 101,
    ast.With: 102,
    ast.AsyncWith: 103,
    ast.IfExp: 104,
    ast.Set: 105,
    ast.ListComp: 106,
    ast.SetComp: 107,
    ast.DictComp: 108,
    ast.GeneratorExp: 109,
    ast.Await: 110,
    ast.Yield: 111,
    ast.YieldFrom: 112,
    getattr(ast, 'NamedExpr', None): 113,  # walrus
}


def make_error(node, number, name):
    return (node.lineno, node.col_offset,
            f'SPL{number:0>3d} {name} is not simple', checker)


def checker(tree):
    for node in ast.walk(tree):
        for decorator in getattr(node, 'decorator_list', []):
            yield make_error(decorator, 900, 'decorator')  # noqa

        if getattr(node, 'annotation', None):
            yield make_error(node, 901, 'annotation')  # noqa

        cls = node.__class__
        err_no = FORBIDDEN.get(cls)
        if err_no:
            yield make_error(node, err_no, cls.__name__)  # noqa


checker.name = 'flake8-simplicity'
checker.version = __version__
