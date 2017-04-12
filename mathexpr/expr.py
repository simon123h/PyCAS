"""
abstrakte Mutter-Klasse fuer math. Ausdruecke.
Gibt alle notwendigen Methoden fuer Kind-Klassen an.
Implementiert Methoden moeglichst allgemein.
"""

# TODO: muss wahrscheinlich ans Ende:
from .atom import Int
from .elementary import Add, Mul, Div, Pow


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
    def cls(self):
        return self.__class__

    # Klasse/Konstruktor der obersten Operation
    @property
    def func(self):
        return self.__class__

    # Argumente
    @property
    def args(self):
        return self._args

    # auf strukturelle Gleichheit zu anderem Ausdruck pruefen
    def __eq__(self, expr):
        if self.type != expr.type:
            return False
        for i in range(0, len(self.args)):
            if not self.args[i].equals(expr.args[i]):
                return False
        return True

    # Expression var durch Expression val ersetzen
    def set(self, var, val):
        if self.equals(var):
            return val
        else:
            return self     # TODO: rekursiv weitergeben?

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
