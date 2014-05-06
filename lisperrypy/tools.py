# -*- coding: utf-8 -*-
from re import compile, match
from itertools import chain

from .types import Operator, Number, LispType


RE = {
    'NUMBERS': r'((-|\+)?[1-9][0-9]*\.?[0-9]*)',
    'EXPRESSION': r'[^\s\d\(\)\[\]][^\s\(\)\[\]]*',
    'BRACES': r'\(|\)|\[|\]',
    'WHITESPACE': r'\s+'
}


def sum_(*args):
    r = reduce(lambda x, y: x + y, args)
    return r


def sub(*args):
    return reduce(lambda x, y: x - y, args)


def div(*args):
    return reduce(lambda x, y: x / float(y), args)


def mult(*args):
    return reduce(lambda x, y: x * y, args)


def def_(sym, val, env):
    env[sym] = val
    return val


ENV = {'+': sum_, '-': sub, '*': mult, '/': div, 'def': def_}


def tokenize(sources):
    res = []
    r = compile(r'|'.join(RE.values()))
    while len(sources) > 0 :
        pattern = r.match(sources)
        e = pattern.end()
        t = sources[:e]
        if not match(RE['WHITESPACE'], t):
            res.append(t)
        sources = sources[e:]
    return res


def form(t):
    if t == '(' or isinstance(t, list) or isinstance(t, LispType):
        r = t
    elif match(RE['NUMBERS'], t):
        r = Number(t)
    elif match(RE['EXPRESSION'], t):
        r = Operator(t)
    return r


def parse(tokens):
    tree = []
    start = 0
    for i, token in enumerate(tokens):
        if token == '(':
            start = i
        if token != ')':
            tree.append(form(token))
        else:
            l = list(chain(tree[:start],
                           [tree[start + 1:]],
                           tokens[i + 1:]))
            return parse(l)
    return tree


def apply_(op, args):
    return op(*args)


def evalu(form, env):
    integer = r'(-|\+)?[1-9][0-9]*$'
    if isinstance(form, Number):
        if match(integer, form.exp):
            return int(form.exp)
        else:
            return float(form.exp)
    elif isinstance(form, Operator) and form.exp in env:
        return env[form.exp]
    elif isinstance(form, list):
        r = []
        for x in form:
            r.append(evalu(x, env))
        if callable(r[0]):
            if form[0].exp == 'def':
                r.append(env)
            return apply_(r[0], r[1:])
        return r
