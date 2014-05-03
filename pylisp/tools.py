# -*- coding: utf-8 -*-
from re import compile
from itertools import chain

from .types import Operator


WHITESPACE = ' '
BRACE = ('(', ')', '[', ']')
RE = {'NUMBERS': compile(r'[0-9]+\.?[0-9]*'),
      'OPERATOR': compile(r'[\+\-\*\/]')}

def tokenize(sources):
    r = ''
    for x in sources:
        if x == WHITESPACE:
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
    number = lambda x: int(x)
    for t in tokens[1:]:
        if isinstance(t, list):
            yield t
        elif RE['NUMBERS'].match(t):
            yield number(t)
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
