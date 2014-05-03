pylisp
---------
[![Build Status](https://travis-ci.org/admire93/pylisp.svg?branch=master)](https://travis-ci.org/admire93/pylisp)

Mixing python and lisp!


Usage
========



```python
from pylisp import pylisp


@pylisp
def lisp_sum(x, y)
    return '(+ %s %s)' % (x, y)


assert 3 == lisp_sum(1, 2)
```

