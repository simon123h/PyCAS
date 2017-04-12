

class Rule():
    def __init__(self, lhs, rhs, definition=False):
        self.lhs = lhs
        self.rhs = rhs
        self.definition = definition

    def invert(self):
        return Rule(self.rhs, self.lhs)

    def apply(self, expr):
        return expr.
