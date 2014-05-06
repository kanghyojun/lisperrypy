# -*- coding: utf-8 -*-
from lisperrypy import lisperrypy


@lisperrypy
def lisp_def():
    print 'hi'
    return '''
    (def x 1)
    x
    '''


def test_lisp_def():
    assert 1 == lisp_def()
