"""
Atomic components of a mathematical Expression.
Leafs of the corresponding tree structure.
Includes, Numerals, Variables and Wildcards
"""

from .expr import Expression


# abstract parent class for all atomic Expressions
class Atom(Expression):
    def set(self, var, val):
        if self == var:
            return val
        return self


# abstract parent class for Numerals
class Num(Atom):
    pass


# Integers
class Int(Num):
    def __init__(self, val):
        self.val = val
        super().__init__(val)

    def __str__(self):
        return str(self.val)


# Variables
class Var(Atom):
    def __init__(self, name):
        self.name = str(name)
        super().__init__(name)

    def __str__(self):
        return self.name


# Constants have a special representation and tend to remain unchanged
class Constant(Num):
    def __init__(self, strrep, val):
        Expression.__init__(self, strrep, val)
        self.val = val
        self.strrep = strrep

    def __str__(self):
        return self.strrep


# Wildcards for pattern matching
class Wildcard(Atom):
    def __init__(self, name="", matchType=None, matchFunc=None):
        self.name = str(name)
        self.matchType = matchType
        self.matchFunc = matchFunc   # a function: matches if func(expr) == True
        super().__init__(name, matchType)

    # A Wildcard matches every expression (restricted by matchType)
    # if any requirements have been made in require, compare to them as well
    def matches(self, expr):
        if expr.isa(Expression):
            return ((self.matchType is None or expr.isa(self.matchType)) and
                    (self.matchFunc is None or self.matchFunc(expr)))
        return False
