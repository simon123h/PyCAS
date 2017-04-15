"""
A class system to define term rewriting rules,
consisting each of a lhs and a rhs.
The lhs can be matched against Expressions using matching.py
and in case of a match, the rule inserts the rhs in the Expression.
"""

from .matching import replace


class Rule:
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs

    def invert(self):
        return Rule(self.rhs, self.lhs)

    # check if lhs matches expr
    # if they match, insert rhs with corresponding Wildcard substitutions
    # this is all handled in matching.py's replace method
    def apply(self, expr):
        return replace(expr, self.lhs, self.rhs)


# DeepRules give deeper Expression manipulation functionality,
# as they are simply given a function to be applied to the expression.
# Use DeepRules, whenever regular TRS with the given Wildcard matching
# functionality is not sufficient.
class DeepRule(Rule):
    # pass a function that is applied to an expression when applying the rule
    def __init__(self, func, matchType=None):
        self.func = func
        self.matchType = matchType

    def apply(self, expr):
        if self.matchType is None or expr.isa(self.matchType):
            return self.func(expr)
        return expr


# a set of rules to be applied at once
class RuleSet:
    def __init__(self, *rules):
        self.rules = list(rules)
        self.order = 0

    # add one or more rules to the set
    def add(self, *rules):
        self.rules += list(rules)

    # apply all matching rules
    def apply(self, expr, printSteps=False, repetitive=False):
        changed = True
        while changed:
            changed = False
            for rule in reversed(self.rules):
                before = expr
                expr = rule.apply(expr)
                if not before == expr:
                    if printSteps:
                        print(before)
                    if repetitive:
                        changed = True
        return expr

    def __add__(self, other):
        if isinstance(other, RuleSet):
            return RuleSet(*(self.rules + other.rules))
        else:
            raise TypeError("unsupported operand type(s) for +: 'RuleSet' and 'RuleSet'")


# TODO: something between Rule and DeepRule: I need to first match with
# a pattern, and then return func(expr) where func knows the wildcard
# substitutions or something
