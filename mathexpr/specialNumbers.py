"""
Numbers that have special behavior (e.g. Infinity),
a special name (e.g. constants) or just deserve a
separate variable reference (e.g. 0, 1)
"""

from .atom import Atom, Int


# Infinity
class Infinity(Atom):
    def __str__(self):
        return 'oo'

    # TODO: these are rules! make up InfinityRules
    def __add__(self, other):
        return self

    def __sub__(self, other):
        return self

    def __truediv__(self, other):
        return self

    def __rtruediv__(self, other):
        return Zero

    def __eq__(self, other):
        return False


Infinity = Infinity()


# Negative Infinity
class NegativeInfinity(Atom):
    def __str__(self):
        return '-oo'

    def __add__(self, other):
        return self

    def __sub__(self, other):
        return self

    def __truediv__(self, other):
        return self

    def __rtruediv__(self, other):
        return Zero

    def __eq__(self, other):
        return False


NegativeInfinity = NegativeInfinity()

# for ease of use
One = Int(1)
Zero = Int(0)

# important constants
# pi = Constant("pi", Num(3.14159265359))
# Phi = Constant("Phi", Num(1.61803398875))
# e = Constant("e", Num(2.71828182846))
