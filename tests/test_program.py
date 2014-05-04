# -*- coding: utf-8 -*-
from lisperrypy import program, lisperrypy


def test_program():
    source = '(* (+ 1 2) 3)'
    assert 9 == program(source)
    source = '(* (+ 1 2) 3 (- 6 4))'
    assert 18 == program(source)
    source = '(* 2 (+ 1 2) 3 (- 6 4))'
    assert 36 == program(source)
    source = '(/ (* 2 (+ 1 2) 3 (- 6 4)) 2)'
    assert 18 == program(source)


@pylisp
def lisp_sum(x, y):
    return '(+ %s %s)' % (x, y)


@pylisp
def lisp_mixing(x, y):
    return '''
    (*
      (+ %s %s)
      2)
    ''' % (x, y)


def test_pylisp_func():
    assert 3 == lisp_sum(1, 2)
    assert 6 == lisp_mixing(1, 2)
