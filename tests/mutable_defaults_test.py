import ast
import pytest

from mutable_defaults import MutableDefaultChecker


@pytest.mark.parametrize('code,error_count', [
    ('def foo(bar={}): pass', 1),
    ('def foo(bar=[]): pass', 1),
    ('def foo(): pass', 0),
    ('def foo(a, b, c=False): pass', 0),
    (
        '\n'.join([
            'def foo():',
            '    def bar(a={}):',
            '        pass',
            '    pass',
        ]),
        1
    ),
    ('def foo(bar=[], baz={}): pass', 2),
    ('def foo(bar=range(10)): pass', 1),
    ('def foo(bar=set()): pass', 1),
    (
        '\n'.join([
            'def foo():',
            '    return True',
            'def bar(a=foo()):',
            '    pass',
        ]),
        1
    ),
    ('', 0),
], ids=(
    'dict',
    'list',
    'empty_arg_list',
    'valid_args_and_kwargs',
    'nested_function',
    'multiple_mutable_defaults',
    'builtin_callable_with_value',
    'builtin_callable_without_value',
    'user_defined_callable',
    'empty_tree',
))
def test_mutable_defaults(code, error_count):
    tree = ast.parse(code)
    assert (
        len(list(MutableDefaultChecker(tree, 'filename').run())) ==
        error_count
    )
