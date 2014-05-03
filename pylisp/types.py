class Operator(object):

    def __init__(self, exp):
        self.exp = exp

    def __repr__(self):
        return 'Op(%s)' % self.exp
