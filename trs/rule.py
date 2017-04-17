"""
A class system to define term rewriting rules,
consisting each of a lhs and a rhs.
The lhs can be matched against Expressions using matching.py
and in case of a match, the rule inserts the rhs in the Expression.
"""

from .matching import replace
from mathexpr.atom import Atom


class Rule:
    # TODO: change order of args? name to front?
    def __init__(self, lhs, rhs, name=None, complexity=1):
        self.name = name
        self.lhs = lhs
        self.rhs = rhs
        self.complexity = complexity

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
    def __init__(self, func, name=None, matchType=None, excludeType=None, complexity=1):
        self.func = func
        self.name = name
        self.matchType = matchType
        self.excludeType = excludeType
        self.complexity = complexity

    # apply rule to expression tree
    def apply(self, expr):
        # if not Atom, pass rule recursively
        if not expr.isa(Atom):
            expr = expr.func(*[self.apply(arg) for arg in expr.args])
        # if matches, apply function
        if self.matchType is None or expr.isa(self.matchType):
            if self.excludeType is None or not expr.isa(self.excludeType):
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

    # apply all matching rules and print steps if rules complexity is higher than printStepsMinComplexity
    def apply(self, expr, printStepsMinComplexity=1, repetitive=True, detectCycles=True):
        changed = True
        history = []
        ruleHistory = []
        while changed:
            changed = False
            for rule in reversed(self.rules):
                before = expr
                expr = rule.apply(expr)
                # if rule caused a change
                if not before == expr:
                    # check for cyclic replacements
                    if detectCycles:
                        if before in history:
                            print(zip(history, ruleHistory))
                            raise CyclicTRException()
                        history.append(before)
                        ruleHistory.append(rule)
                    # print rule replacement steps
                    if rule.complexity >= printStepsMinComplexity:
                        print(before)
                        if rule.name is not None:
                            print(rule.name+":")
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


class CyclicTRException(Exception):
    def __init__(self, message, errors):
        if message is None:
            message = "Cyclic Replacements in pattern, need to adjust rules!"
        super().__init__(message)
