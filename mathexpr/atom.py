"""
Atomare Bestandteile eines math. Ausdrucks:
Blaetter in der zugehoerigen Baumstruktur
"""

from .expr import Expression


# abstrakte Mutter-Klasse
class Atom(Expression):
    pass


# Integer
class Int(Atom):
    def __init__(self, val):
        self.val = val
        super().__init__(val)

    def __str__(self):
        return str(self.val)

    # Addition
    def __add__(self, other):
        if isinstance(other, Int):
            return Int(self.val + other.val)
        return other.__add__(self)


# Variablen
class Var(Atom):
    def __init__(self, name):
        self.name = str(name)
        super().__init__(name)

    def __str__(self):
        return self.name


# Konstanten
class Constant(Atom):
    def __init__(self, strrep, val):
        Expression.__init__(self, strrep, val)
        self.val = val
        self.strrep = strrep

    def __str__(self):
        return self.strrep


# Wildcards fuer pattern matching
class Wildcard(Atom):
    def __init__(self, name):
        self.name = str(name)
        super().__init__(name)

    def __eq__(self, other):
        return True

    def replace(self, pattern, expr):
        if pattern.isa(Wildcard) and self.name is pattern.name:
            return expr
        return self

    def require(self, other):
        return [(self, other)]

    # @property
    # def args(self):
    #     return []
