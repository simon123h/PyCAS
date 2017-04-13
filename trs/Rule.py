

class Rule():
    def __init__(self, lhs, rhs, definition=False):
        self.lhs = lhs
        self.rhs = rhs
        self.definition = definition

    def invert(self):
        return Rule(self.rhs, self.lhs)

    def apply(self, expr):
        return expr.replace(self.lhs, self.rhs)


# a set of rules to be applied at once
class RuleSet():
    def __init__(self, *rules):
        self.rules = list(rules)

    # add one or more rules to the set
    def add(self, *rules):
        self.rules += list(rules)

    # apply all matching rules
    def apply(self, expr):
        for rule in self.rules:
            expr = rule.apply(expr)
        return expr


from .mathexpr.atom import Wildcard, Atom
