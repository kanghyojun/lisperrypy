# -*- coding: utf-8 -*-
from pylisp.tools import tokenize, parse

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
