# -*- coding: utf-8 -*-
from lisperrypy.tools import tokenize, parse, apply_, evalu, ENV
from lisperrypy.types import Operator, Number


def test_tokenize():
    source = '(+ 1 2)'
    assert ['(', '+', '1', '2', ')'] == tokenize(source)
    source = '(* (+ 2 3) 4 2)'
    x = ['(', '*', '(', '+', '2', '3', ')', '4', '2', ')']
    assert x == tokenize(source)


def test_string_tokenize():
    source = '(+ "123" "123")'
    assert ['(', '+', '"123"', '"123"', ')'] == tokenize(source)
    source = '(+ "1\'23" "123")'
    assert ['(', '+', '"1\'23"', '"123"', ')'] == tokenize(source)


def test_large_number_tokenize():
    source = '(+ 123123 123123)'
    assert ['(', '+', '123123', '123123', ')'] == tokenize(source)


def test_float_number_tokenize():
    source = '(+ 12.3123 123123)'
    assert ['(', '+', '12.3123', '123123', ')'] == tokenize(source)


def test_symbol_tokenize():
    source = '(plus maybe 123123)'
    assert ['(', 'plus', 'maybe', '123123', ')'] == tokenize(source)
    source = '(plus maybe? 123123)'
    assert ['(', 'plus', 'maybe?', '123123', ')'] == tokenize(source)
    source = '(< 1 1.2)'
    assert ['(', '<', '1', '1.2', ')'] == tokenize(source)


def test_new_parse():
    source = '(* (+ 1 2) 5 2)'
    t = tokenize(source)
    form = parse(t)
    print(form)
    assert form
    assert isinstance(form, list)
    assert '*' == form[0].exp
    assert isinstance(form[1], list)
    assert isinstance(form[1][0], Operator)
    assert '+' == form[1][0].exp
    assert '1' == form[1][1].exp
    assert '2' == form[1][2].exp
    assert '5' == form[2].exp
    assert '2' == form[3].exp


def test_parse_complex():
    source = '(* (+ 1 (- 2 3)) (- 5 2)'
    form = parse(tokenize(source))
    assert form
    assert isinstance(form, list)
    assert '*' == form[0].exp
    assert isinstance(form[1], list)
    assert isinstance(form[1][0], Operator)
    assert '+' == form[1][0].exp
    assert '1' == form[1][1].exp
    assert isinstance(form[1][2], list)
    assert '-' == form[1][2][0].exp
    assert '2' == form[1][2][1].exp
    assert '3' == form[1][2][2].exp
    assert isinstance(form[2], list)
    assert '-' == form[2][0].exp
    assert '5' == form[2][1].exp
    assert '2' == form[2][2].exp


def test_apply():
    assert 3 == apply_(ENV['+'], [1, 2])


def test_eval():
    tree = [Operator('*'), [Operator('+'), Number('1'), Number('2')],
            Number('3')]
    assert 9 == evalu(tree, ENV)
