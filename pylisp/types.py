class LispType(object):

    def __init__(self, exp):
        self.exp = exp

class Operator(LispType):

    def __repr__(self):
        return 'Operator(%s)' % self.exp


class Number(LispType):

    def __repr__(self):
        return 'Number(%s)' % self.exp
