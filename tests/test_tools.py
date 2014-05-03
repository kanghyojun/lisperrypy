# -*- coding: utf-8 -*-
from pylisp.tools import tokenize, parse, apply_, evalu, ENV
from pylisp.types import Operator, Number


def test_tokenize():
    source = '(+ 1 2)'
    assert ['(', '+', '1', '2', ')'] == list(tokenize(source))
    source = '(* (+ 1 2) 5 2)'
    x = ['(', '*', '(', '+', '1', '2', ')', '5', '2', ')']
    assert x == list(tokenize(source))


def test_parse():
    source = '(* (+ 1 2) 5 2)'
    t = list(tokenize(source))
    form = parse(t)
    assert form
    assert isinstance(form[0], Operator)
    assert '*' == form[0].exp
    assert isinstance(form[1], list)
    assert isinstance(form[1][0], Operator)
    assert '+' == form[1][0].exp
    assert '1' == form[1][1].exp
    assert '2' == form[1][2].exp
    assert '5' == form[2].exp
    assert '2' == form[3].exp


def test_apply():
    assert 3 == apply_(ENV['+'], [1, 2])


def test_eval():
    tree = [Operator('*'), [Operator('+'), Number('1'), Number('2')],
            Number('3')]
    assert 9 == evalu(tree, ENV)
