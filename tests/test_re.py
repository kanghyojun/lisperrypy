from lisperrypy.tools import RE
from re import match


def test_symbol():
    assert match(RE['SYMBOL'], 'a-d')
    assert not match(RE['SYMBOL'], '0a-d')
    assert not match(RE['SYMBOL'], '(a-d')
    assert match(RE['SYMBOL'], '-ad')
    assert match(RE['SYMBOL'], '+')
    assert not match(RE['SYMBOL'], ' +')
