from re import compile, match
from itertools import chain
from functools import reduce
from string import whitespace

from .types import Operator, Number, LispType


RE = {
    'NUMBERS': r'((-|\+)?[1-9][0-9]*\.?[0-9]*)',
    'SYMBOL': r'[^\s\d\(\)\[\]][^\s\(\)\[\]]*',
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


def defn(sym_form, param, body, env):
    return def_(sym_form.exp, lambda_(param, body, env), env)


def lambda_(sym, body, env):
    def f(*args):
        sub_env = env.copy()
        for arg_name, value in zip(sym, args):
            sub_env[arg_name.exp] = value
        return evalu(body, sub_env)
    return f


ENV = {'+': sum_, '-': sub, '*': mult, '/': div, 'print': print}
numbers = ''.join([str(x) for x in range(0,9)]) + '.'
symbols = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*+_-=<>/?'
braces = ['[', ']', '(', ')', '{', '}']


def tokenize(sources):
    i = 0
    state = False
    b = ''
    while i < len(sources) - 1:
        t = sources[i]
        r = None
        if t in braces or t == '`':
             r = [t]
        elif t in whitespace:
            i += 1
            continue
        elif t == '"' or t == "'":
            return tokenize_when(sources[i:], when=lambda x: x != t, padd=1)
        elif t in numbers:
            return tokenize_when(sources[i:], when=lambda x: x in numbers)
        elif t in symbols:
            return tokenize_when(sources[i:], when=lambda x: x in symbols)
        if r is not None:
            return r + tokenize(sources[i+1:])
        i += 1
    return [sources]


def tokenize_when(source, when, padd=0):
    b = ''
    i = 0 + padd
    while when(source[i]):
        b += source[i]
        i += 1
    if padd != 0:
        r = ['{}{}{}'.format(source[:padd], b, source[i:i+padd])]
    else:
        r = [b]
    return r + tokenize(source[i+padd:])


def parse(tokens):
    tree = []
    parser = Parser(tokens)
    while parser:
        tree.append(parser.parse())
    return tree


class Parser(list):
    def form(self, t):
        if t == ')':
            r = t
        elif match(RE['NUMBERS'], t):
            r = Number(t)
        elif match(RE['SYMBOL'], t):
            r = Operator(t)
        return r

    def parse(self):
        token = self.pop(0) if self else None
        if token == '(':
            return self.parse_list()
        else:
            return self.form(token)

    def parse_list(self):
        token = ''
        l = []
        while token != ')' and self:
            token = self.parse()
            if token != ')':
                l.append(token)
        return l


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
        if isinstance(form[0], Operator):
            if form[0].exp == 'def':
                def_(form[1].exp, evalu(form[2], env), env)
            elif form[0].exp == 'defn':
                return defn(form[1], form[2], form[3], env)
            elif form[0].exp == 'lambda':
                return lambda_(form[1], form[2], env)
        for x in form:
            r.append(evalu(x, env))
        if callable(r[0]):
            return apply_(r[0], r[1:])
        return r
