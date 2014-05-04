from lisperrypy.tools import RE
from re import match


def test_expression():
    assert match(RE['EXPRESSION'], 'a-d')
    assert not match(RE['EXPRESSION'], '0a-d')
    assert not match(RE['EXPRESSION'], '(a-d')
    assert match(RE['EXPRESSION'], '-ad')
    assert match(RE['EXPRESSION'], '+')
    assert not match(RE['EXPRESSION'], ' +')
