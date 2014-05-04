# -*- coding: utf-8 -*-
from re import compile, match
from itertools import chain

from .types import Operator, Number


WHITESPACE = ' '
LB = '\n'
BRACE = ('(', ')', '[', ']')
RE = {
    'NUMBERS': r'((-|\+)?[1-9][0-9]*\.?[0-9]*)',
    'EXPRESSION': r'[^\s\d\(\)\[\]][^\s\(\)\[\]]*',
    'BRACES': r'\(|\)|\[|\]',
    'WHITESPACE': r'\s+'
}
ENV = {
    '+': lambda x: sum(x),
    '*': lambda x: reduce(lambda z, y: z * y, x),
    '/': lambda x: reduce(lambda z, y: z / float(y), x),
    '-': lambda x: reduce(lambda z, y: z - y, x),
}


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


def form(tokens):
    for t in tokens[1:]:
        if isinstance(t, list):
            yield t
        elif match(RE['NUMBERS'], t):
            yield Number(t)
        elif match(RE['EXPRESSION'], t):
            yield Operator(t)


def parse(tokens):
    tree = []
    start = 0
    for i, token in enumerate(tokens):
        if token != ')':
            tree.append(token)
        else:
            l = list(chain(tokens[:start],
                           [list(form(tree[start:]))],
                           tokens[i + 1:]))
            return parse(l)
        if token == '(':
            start = i
    return tokens[0]


def apply_(op, args):
    return op(args)


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
            return apply_(r[0], r[1:])
        return r
