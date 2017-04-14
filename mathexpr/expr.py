"""
abstrakte Mutter-Klasse fuer math. Ausdruecke.
Gibt alle notwendigen Methoden fuer Kind-Klassen an.
Implementiert Methoden moeglichst allgemein.
"""

import itertools
import mathexpr


class Expression:
    isAssociative = False
    isCommutative = False

    # Konstruktor
    def __init__(self, *args):
        self._args = list(args)

    # Typ der obersten Operation
    @property
    def type(self):
        return self.__class__.__name__

    # Klasse/Konstruktor der obersten Operation
    @property
    def func(self):
        return self.__class__

    # Argumente
    @property
    def args(self):
        return self._args

    # auf strukturelle Gleichheit zu anderem Ausdruck pruefen
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

    # Ausgabe
    def __str__(self):
        if self.type == "Expression":
            return str(self.args[0])
        return self.__class__.__name__ + "(" + ", ".join([str(arg) for arg in self.args]) + ")"

    # Builtin-Operatoren ueberschreiben
    def __repr__(self):
        return str(self)

    def __ne__(self, other):
        return not self.equals(other)

    def __pos__(self):
        return self

    def __neg__(self):
        return mathexpr.elementary.Mul(mathexpr.atom.Int(-1), self)

    def __add__(self, other):
        return mathexpr.elementary.Add(self, other)

    def __radd__(self, other):
        return mathexpr.elementary.Add(other, self)

    def __sub__(self, other):
        return mathexpr.elementary.Sub(self, other)

    def __rsub__(self, other):
        return mathexpr.elementary.Sub(other, self)

    def __mul__(self, other):
        return mathexpr.elementary.Mul(self, other)

    def __rmul__(self, other):
        return mathexpr.elementary.Mul(other, self)

    def __pow__(self, other):
        return mathexpr.elementary.Pow(self, other)

    def __rpow__(self, other):
        return mathexpr.elementary.Pow(other, self)

    def __xor__(self, other):
        return mathexpr.elementary.Pow(self, other)

    def __truediv__(self, other):
        return mathexpr.elementary.Div(self, other)

    def __rtruediv__(self, other):
        return mathexpr.elementary.Div(other, self)
    __div__ = __truediv__
    __rdiv__ = __rtruediv__

    # return all permutations if the operatand is commutative
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


# from mathexpr.elementary import Add, Mul, Div, Pow
