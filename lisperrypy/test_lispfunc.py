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


@lisperrypy
def a():
    return '''
        (def x 1)
        (+ x 1)
    '''


def test_lisp_use():
    assert 2 == a()
