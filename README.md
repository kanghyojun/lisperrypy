lisperrypy
---------
[![Build Status](https://travis-ci.org/admire93/lisperrypy.svg?branch=master)](https://travis-ci.org/admire93/lisperrypy)

Mixing python and lisp!


Usage
========



```python
from lisperrypy import lisperrypy


@lisperrypy
def lisp_sum(x, y)
    return '(+ %s %s)' % (x, y)


assert 3 == lisp_sum(1, 2)
```
