from .atom import Atom, Num, Int


class Infinity(Atom):
    def __str__(self):
        return 'oo'

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

One = Int(1)
Zero = Int(0)
# pi = Constant("pi", Num(3.14159265359))
# Phi = Constant("Phi", Num(1.61803398875))
# e = Constant("e", Num(2.71828182846))
