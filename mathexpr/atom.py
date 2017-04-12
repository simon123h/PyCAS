"""
Atomare Bestandteile eines math. Ausdrucks:
Blaetter in der zugehoerigen Baumstruktur
"""


from .expr import Expression


"""abstrakte Mutter-Klasse"""


class Atom(Expression):
    pass


"""abstrakte Klasse fuer Numerale"""


class Number(Atom):

    isRational = False
    isInteger = False

    # Return a Number (Rational or Real) from input decimal (or fraction)
    @staticmethod
    def make(val, denom=1):
        # Check for Infinity
        if denom == 0:
            return Infinity if val > 0 else NegativeInfinity
        # Check for Integer input
        if float(val).is_integer() and float(denom).is_integer():
            return Rational(val, denom)
        # Check for Integer ratio
        if float(val / denom).is_integer():
            return Rational(val / denom, 1)
        # Try brute-forcing Ratio with a Stern-Brocot-Tree
        else:
            val = val / denom
            sB = Number.sternBrocot(val)
            if sB[2] == 0:
                return Rational(sB[0], sB[1])
            # Check for simple ratios
            if float(val / denom * 20922789888000).is_integer():		# multiply with 16!
                return Rational(val * 10**12, denom * 10**12)
            else:
                return Real(val)

    # decimal to fraction via Stern-Brocot-Tree
    @staticmethod
    def sternBrocot(val, minError=10**-32, maxIter=10**5):
        if val == 0:
            return 0, 1, 0
        isNegative = False if val > 0 else True
        val = abs(val)
        if val > 1:
            pl = int(val)
            ql = 1
            pr = int(val) + 1
            qr = 1
        else:
            pl = 0
            ql = 1
            pr = 1
            qr = 0
        error = 1
        i = 0
        while not (error < minError or i > maxIter):
            pMed = pl + pr
            qMed = ql + qr
            med = pMed / qMed
            if val < med:
                pr = pMed
                qr = qMed
            else:
                pl = pMed
                ql = qMed
            error = abs(val - med)
            i += 1
        if isNegative:
            return -pMed, qMed
        return pMed, qMed, error, i


Num = Number.make


"""Reelle Zahlen"""


class Real(Number):

    def __init__(self, val):
        Expression.__init__(self, val)
        self.val = val
        print("Fell back to REAL:", val)

    def __str__(self):
        return str(self.val)

    # Addition
    def __add__(self, other):
        if isinstance(other, Real):
            return Num(self.val + other.val)
        return other.__add__(self)

    # Multiplikation
    def __mul__(self, other):
        if isinstance(other, Real):
            return Num(self.val * other.val)
        return other.__mul__(self)

    # Division
    def __truediv__(self, other):
        if isinstance(other, Real):
            return Num(self.val / other.val)
        return other.__truediv__(self)

    def __rtruediv__(self, other):
        if isinstance(other, Real):
            return Num(other.val / self.val)
        return other.__truediv__(self)

    # Equals
    def __eq__(self, other):
        return self.val == other.val


"""Rationale Zahlen"""


class Rational(Real):

    @staticmethod
    def ggt(p, q):
        while q != 0:  # suche ggT von num und denom
            h = p % q
            p = q
            q = h
        return p

    isRational = True

    def __init__(self, num, denom=1, strrep=None):
        p = num if denom > 0 else -num
        q = abs(denom)
        if q == 0:
            raise ZeroDivisionError(
                'Tried to set zero as fraction denominator')
        while q != 0:  # suche ggT von num und denom
            h = p % q
            p = q
            q = h
        self.p = int(num / p)
        self.q = int(denom / p)
        self.val = num / denom
        #Real.__init__(self, self.p/self.q)
        Expression.__init__(self, self.p, self.q)

    def __str__(self):
        if self.isInteger:
            return str(int(self.p))
        if self.q < 10**4 and self.p < 10**4:
            return str(int(self.p)) + "/" + str(int(self.q))
        return str(self.val)

    # Addition
    def __add__(self, other):
        if other.isRational:
            return Rational(self.p * other.q + other.p * self.q, self.q * other.q)
        return other.__add_(self)

    # Subtraktion
    def __sub__(self, other):
        if other.isRational:
            return Rational(self.p * other.q - other.p * self.q, self.q * other.q)
        return other.__sub_(self)

    # Multiplikation
    def __mul__(self, other):
        if other.isRational:
            return Rational(self.p * other.p, self.q * other.q)
        return other.__mul__(self)

    # Division
    def __truediv__(self, other):
        if other.isRational:
            return Rational(self.p * other.q, self.q * other.p)
        return other.__rtruediv__(self)

    # is Integer?
    @property
    def isInteger(self):
        return self.q == 1 and float(self.p).is_integer()


class Constant(Atom):
    def __init__(self, strrep, num):
        self.strrep = strrep
        self.num = num
        self.val = num.val

    def __str__():
        return self.strrep


class Complex(Number):
    def __init__(self, re, im=Num(0)):
        self.re = re
        self.im = im

        def __str__(self):
            if self.isReal:
                return str(self.re)
            if self.re == Zero:
                return str(self.im) + "i"
            return str(self.re) + str(self.im) + "i"

    # Addition
    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(self.re + other.re, self.im * other.im)
            if isinstance(other, Number):
                return Complex(self.re + other, self.im)
        return other.__add_(self)

    # Subtraktion
    def __sub__(self, other):
        if other.isRational:
            return Rational(self.p * other.q - other.p * self.q, self.q * other.q)
        return other.__sub_(self)

    # Multiplikation
    def __mul__(self, other):
        if other.isRational:
            return Rational(self.p * other.p, self.q * other.q)
        return other.__mul__(self)

    # Division
    def __truediv__(self, other):
        if other.isRational:
            return Rational(self.p * other.q, self.q * other.p)
        return other.__rtruediv__(self)

    # is Real?
    @property
    def isReal(self):
        return self.im == Zero


"""Konstanten"""


class Constant(Atom):
    def __init__(self, strrep, num):
        Number.__init__(self, strrep, num)
        self.num = num

    def __str__(self):
        return strrep


"""Variablen"""


class Var(Atom):
    def __init__(self, name):
        self.name = str(name)
        super().__init__(name)

    def __str__(self):
        return self.name


from .elementary import *
from .specialNumbers import Zero
