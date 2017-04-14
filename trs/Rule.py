import trs.patterns as patterns


class Rule:
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs

    def invert(self):
        return Rule(self.rhs, self.lhs)

    def apply(self, expr):
        return patterns.replace(expr, self.lhs, self.rhs)


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
    def apply(self, expr, printSteps=False):
        for rule in reversed(self.rules):
            before = expr
            expr = rule.apply(expr)
            if not before == expr:
                print(before)
        return expr

    def __add__(self, other):
        if isinstance(other, RuleSet):
            return RuleSet(*(self.rules + other.rules))
        else:
            raise TypeError("unsupported operand type(s) for +: 'RuleSet' and 'RuleSet'")


class RuleRegistry:
    def __init__(self, ruleSets=[]):
        self.ruleSets = ruleSets

    def addSet(self, set):
        self.ruleSets.append(set)

    def removeSet(self, set):
        self.ruleSets.remove(set)

    def apply(self, expr, printSteps=False):
        for ruleSet in reversed(self.ruleSets):
            expr = ruleSet.apply(expr, printSteps)
        return expr
