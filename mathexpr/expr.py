"""
Abstract parent class for all mathematical Expressions.
Defines all necessary member methods for children classes.
Implements methods in general ways, if possible.
"""

import itertools


class Expression:
    isAssociative = False
    isCommutative = False

    # constructor
    def __init__(self, *args):
        self._args = list(args)

    # type of current node
    @property
    def type(self):
        return self.__class__.__name__

    # class/Constructor of current node
    @property
    def func(self):
        return self.__class__

    # arguments (usually: children) of node
    @property
    def args(self):
        return self._args

    # test if Expression tree is structually equal to other Expression tree
    def __eq__(self, other):
        if not isinstance(other, Expression):
            return False
        if self.type != other.type:
            return False
        if len(self.args) is not len(other.args):
            return False
        for arg1, arg2 in zip(self.args, other.args):
            if not arg1 == arg2:
                return False
        return True

    # return if self is instance of cls
    def isa(self, cls):
        return isinstance(self, cls)

    # print the Expression tree as a string
    def __str__(self):
        if self.type == "Expression":
            return str(self.args[0])
        return self.__class__.__name__ + "(" + ", ".join([str(arg) for arg in self.args]) + ")"

    # override builtin operations
    def __repr__(self):
        return str(self)

    def __ne__(self, other):
        return not self.equals(other)

    def __pos__(self):
        return self

    def __neg__(self):
        return Mul(Int(-1), self)

    def __add__(self, other):
        return Add(self, other)

    def __radd__(self, other):
        return Add(other, self)

    def __sub__(self, other):
        return Sub(self, other)

    def __rsub__(self, other):
        return Sub(other, self)

    def __mul__(self, other):
        return Mul(self, other)

    def __rmul__(self, other):
        return Mul(other, self)

    def __pow__(self, other):
        return Pow(self, other)

    def __rpow__(self, other):
        return Pow(other, self)

    def __xor__(self, other):
        return Pow(self, other)

    def __truediv__(self, other):
        return Div(self, other)

    def __rtruediv__(self, other):
        return Div(other, self)
    __div__ = __truediv__
    __rdiv__ = __rtruediv__

    # return all permutations if the operand is commutative
    def perms(self):
        if self.isCommutative:
            return [self.func(*ls) for ls in itertools.permutations(self.args)]
        return [self]

    # recursively replace var by val
    def set(self, var, val):
        if self == var:
            return val
        args = [arg.set(var, val) for arg in self.args]
        return self.func(*args)

    # get all nodes of the Expression tree matching class cls
    def getNodes(self, cls=None):
        if cls is None:
            cls = Expression
        result = [self] if self.isa(cls) else []
        for arg in self.args:
            if isinstance(arg, Expression):
                result += arg.getNodes(cls)
        return result


# bottom imports to solve circular dependencies
from .elementary import Add, Sub, Mul, Div, Pow  # noqa
from .atom import Int  # noqa
