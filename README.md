flake8-mutable
--------------

[![PyPI version](https://img.shields.io/pypi/v/flake8-mutable.svg)](https://pypi.python.org/pypi/flake8-mutable)

#### Motivation

Python's default arguments are evaluated at definition as opposed to when the function is invoked. This leads to unexpected behavior, as mutations persist between calls. For a more detailed explanation, see [The Hitchhiker's Guide to Python](http://docs.python-guide.org/en/latest/writing/gotchas/#mutable-default-arguments).

#### Example

```
def fnc(a, b={}):
    pass

foo.py:2:14: M511 - mutable default arg of type Dict
```

#### Installation

```
pip install flake8-mutable
```

#### Changes

##### [1.1.0] 2016-11-26
- Callables

##### [1.0.6] 2016-11-26
- added MANIFEST.in

#### License

[MIT](https://opensource.org/licenses/MIT)
