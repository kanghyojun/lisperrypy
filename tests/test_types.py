# -*- coding: utf-8 -*-
from pylisp.tools import evalu, RE
from pylisp.types import Number


def test_float():
    assert 1.2 == evalu(Number('1.2'), {})


def test_negative():
    assert -1 == evalu(Number('-1'), {})
    assert -2.2 == evalu(Number('-2.2'), {})


def test_postive():
    assert 1 == evalu(Number('+1'), {})
    assert 2.2 == evalu(Number('+2.2'), {})
