# -*- coding: utf-8 -*-
from pylisp.tools import tokenize, parse, apply_, evalu, ENV
from pylisp.types import Operator


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
    assert 1 == form[1][1]
    assert 2 == form[1][2]
    assert 5 == form[2]
    assert 2 == form[3]


def test_apply():
    assert 3 == apply_(ENV['+'], [1, 2])


def test_eval():
    tree = [Operator('*'), [Operator('+'), 1, 2], 3]
    assert 9 == evalu(tree, ENV)
