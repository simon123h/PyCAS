"""
abstrakte Mutter-Klasse fuer math. Ausdruecke.
Gibt alle notwendigen Methoden fuer Kind-Klassen an.
Implementiert Methoden moeglichst allgemein.
"""


class Expression:

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
        if isinstance(other, Wildcard):
            return other == self
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
    def __ne__(self, other): return not self.equals(other)

    def __pos__(self): return self

    def __neg__(self): return Mul(Int(-1), self)

    def __add__(self, other): return Add(self, other)

    def __radd__(self, other): return Add(other, self)

    def __sub__(self, other): return Add(self, -other)

    def __rsub__(self, other): return Add(other, -self)

    def __mul__(self, other): return Mul(self, other)

    def __rmul__(self, other): return Mul(other, self)

    def __pow__(self, other): return Pow(self, other)

    def __rpow__(self, other): return Pow(other, self)

    def __xor__(self, other): return Pow(self, other)

    def __truediv__(self, other): return Div(self, other)

    def __rtruediv__(self, other): return Mul(other, Pow(self, Int(-1)))
    __div__ = __truediv__
    __rdiv__ = __rtruediv__

    def __repr__(self):
        return str(self)

    # Rekursiv pattern durch expr val ersetzen
    def replace(self, pattern, expr):
        if self == pattern and not pattern.isa(Wildcard):
            wildcardSubs = self.require(pattern)
            for wc, sub in wildcardSubs:
                expr = expr.replace(wc, sub)
            return expr
        if self.isa(Atom):
            return self
        args = [arg.replace(pattern, expr) for arg in self._args]
        return self.func(*args)

    # return list of all required wildcard substitutions for two equal expressions
    def require(self, pattern):
        if pattern.isa(Wildcard):
            return pattern.require(self)
        if self.isa(Atom) or pattern.isa(Atom):
            return []
        result = []
        for a1, a2 in zip(self.args, pattern.args):
            result += a1.require(a2)
        return result


from .atom import Atom, Int, Wildcard
from .elementary import Add, Mul, Div, Pow
