# -*- coding: utf-8 -*-
from re import compile
from itertools import chain

from .types import Operator, Number


WHITESPACE = ' '
LB = '\n'
BRACE = ('(', ')', '[', ']')
RE = {'NUMBERS': compile(r'(-|\+)?[1-9][0-9]*\.?[0-9]*'),
      'OPERATOR': compile(r'[\+\-\*\/]'),
      'INTEGER': compile(r'(-|\+)?[1-9][0-9]*$')}
ENV = {
    '+': lambda x: sum(x),
    '*': lambda x: reduce(lambda z, y: z * y, x),
    '/': lambda x: reduce(lambda z, y: z / float(y), x),
    '-': lambda x: reduce(lambda z, y: z - y, x),
}

def tokenize(sources):
    r = ''
    for x in sources:
        if x == WHITESPACE or x == LB:
            if r:
                yield r
                r = ''
        elif x in BRACE:
            if r:
                yield r
                r = ''
            yield x
        elif RE['NUMBERS'].match(x):
            r += x
        elif RE['OPERATOR'].match(x):
            r += x



def form(tokens):
    for t in tokens[1:]:
        if isinstance(t, list):
            yield t
        elif RE['NUMBERS'].match(t):
            yield Number(t)
        elif RE['OPERATOR']:
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
    if isinstance(form, Number):
        if RE['INTEGER'].match(form.exp):
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
