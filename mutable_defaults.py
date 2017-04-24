# -*- coding: utf-8 -*-
import ast


__version__ = '1.2.0'


mutable_types = [
    ast.Call,
    ast.Dict,
    ast.List,
    ast.Set,
]


class MutableDefaultChecker(object):
    """Mutable default argument checker.

    Flake8 extension that alerts when a mutable type is used
    as an argument's default value.
    """
    name = 'flake-mutable'
    version = __version__
    _error_tmpl = '{} - mutable default arg of type {}'
    _code = 'M511'

    def __init__(self, tree, filename):
        self.tree = tree

    def run(self):
        for node in ast.walk(self.tree):
            if isinstance(node, ast.FunctionDef):
                for default in node.args.defaults:
                    if any([
                        isinstance(default, mutable_type)
                        for mutable_type in mutable_types
                    ]):
                        error_msg = self._error_tmpl.format(
                            self._code, type(default).__name__
                        )
                        yield (default.lineno, default.col_offset,
                               error_msg, type(self))
