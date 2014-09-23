# -*- coding: utf-8 -*-
from lisperrypy import program, lisperrypy, lisperrypy_with


def test_program():
    source = '(* (+ 1 2) 3)'
    assert 9 == program(source)
    source = '(* (+ 1 2) 3 (- 6 4))'
    assert 18 == program(source)
    source = '(* 2 (+ 1 2) 3 (- 6 4))'
    assert 36 == program(source)
    source = '(/ (* 2 (+ 1 2) 3 (- 6 4)) 2)'
    assert 18 == program(source)
    source = '(def a (lambda (f) (lambda (g) (lambda (h) (add f g h))))) (def add (lambda (x y z) (+ x y z))) (((a 1) 1) 1)'
    assert 3 == program(source)


@lisperrypy
def lisp_sum(x, y):
    return '(+ %s %s)' % (x, y)


@lisperrypy
def lisp_mixing(x, y):
    return '''
    (*
      (+ %s %s)
      2)
    ''' % (x, y)


def test_pylisp_func():
    assert 3 == lisp_sum(1, 2)
    assert 6 == lisp_mixing(1, 2)


def abc(x, y, z):
    return x + y + z


@lisperrypy_with(env=globals())
def lisp_py_abc():
    return '(abc 1 2 3)'


def test_lisp_py_abc():
    assert 6 == lisp_py_abc()


@lisperrypy
def lisp_int():
    return '1'


def test_lisp_int():
    assert 1 == lisp_int()
