# -*- coding: utf-8 -*-
from functools import wraps

from .tools import tokenize, parse, evalu, ENV


def program(source, env={}):
    for k, v in ENV.items():
        env[k] = v
    t = tokenize(source)
    form = parse(t)
    eval_ = evalu(form, env)
    return eval_


def lisperrypy(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        return program(f(*args, **kwargs))
    return wrapper


def lisperrypy_with(env={}):
    def deco(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            return program(f(*args, **kwargs), env)
        return wrapper
    return deco
