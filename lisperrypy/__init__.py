# -*- coding: utf-8 -*-
from functools import wraps

from .tools import tokenize, parse, evalu, ENV


def program(source):
    t = tokenize(source)
    form = parse(t)
    eval_ = evalu(form, ENV)
    return eval_


def lisperrypy(f):
    @wraps(f)
    def deco(*args, **kwargs):
        return program(f(*args, **kwargs))
    return deco
