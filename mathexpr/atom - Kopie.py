"""
Atomare Bestandteile eines math. Ausdrucks:
Blaetter in der zugehoerigen Baumstruktur
"""


from .expr import Expression


"""abstrakte Mutter-Klasse"""
class Atom(Expression):
	pass
	
"""abstrakte Klasse fuer Numerale"""
class Num(Atom):

	# Klasse vereinfachen, aus Rational(5, 1) wird Integer(5)
	def reduceType(self):
		if self.cls == Complex and self.im == 0:
			return Real(self.re).reduceType()
		elif self.cls == Real:
			max_denom = 10**12
			if self.val*max_denom % 1 == 0:
				return Rational(self.val*max_denom, max_denom).reduceType()
		elif self.cls == Rational:
			if self.q == 1:
				return Integer(self.p)
			elif self.p == 0:
				return Integer(0)
		return self
		

"""Komplexe Zahlen"""
class Complex(Num):
	def __init__(self, re, im):
		Expression.__init__(self, re, im)
		self.re = re
		self.im = im
		self._args = [re, im]
		
	def __str__(self):
		return str(self.re) + " + " + str(self.im) + " * i"
		
	# Addition
	def __add__(self, other):
		return Complex(self.re + other.re, self.im + other.im).reduceType()
	
	# Multiplikation
	def __mul__(self, other):
		return Complex(self.re * other.re - self.im * other.im, self.re * other.im + self.im * other.re).reduceType()
		
	# Division
	def __div__(self, other):
		raise NotImplementedError
	
		
		
		
"""Reelle Zahlen"""
class Real(Num):
	def __init__(self, val):
		Expression.__init__(self, val)
		self.val = val

	def __str__(self):
		return str(self.val)
		
	# Addition
	def __add__(self, other):
		return (self.val * other.val).reduceType()
		
	# Multiplikation
	def __mul__(self, other):
		return Real(self.val * other.val).reduceType()
		
	# Division
	def __div__(self, other):
		return Real(self.val / other.val).reduceType()
	def __rdiv__(self, other):
		return Real(other.val/self.val).reduceType()

"""Rationale Zahlen"""
class Rational(Real):
	def __init__(self, num, denom):
		super().__init__(num/denom)
		p = num
		q = denom
		while q != 0:	# suche ggT von num und denom
			h = p % q
			p = q
			q = h
		self.p = num / p
		self.q = denom / p
		self._args = [self.p, self.q]
			
	def __str__(self):
		if self.q < 10**4 and self.p < 10**4:
			return str(int(self.p)) + "/" + str(int(self.q))
		return str(self.p/self.q)
		
	# Addition
	def __add__(self, other):
		if isinstance(other, Rational):
			return Rational(self.p*other.q + other.p*self.q, self.q*other.q).reduceType()
		return other.reduceType().__add_(self)
		
	# Multiplikation
	def __mul__(self, other):
		if isinstance(other, Rational):
			return Rational(self.p * other.p, self.q * other.q).reduceType()
		return other.reduceType().__mul__(self)
		
	# Division
	def __div__(self, other):
		if isinstance(other, Rational):
			return Rational(self.p * other.q, self.q * other.p).reduceType()
		return other.reduceType().__rdiv__(self)
Frac = Rational
		
"""Ganze Zahlen"""
class Integer(Rational):
	def __init__(self, val):
		super().__init__(val, 1)
		self.val = int(val)
		self._args = [val]

	def __str__(self):
		return str(self.val)

	# Addition
	def __add__(self, other):
		if isinstance(other, Integer):
			return Integer(self.val + other.val)
		return other.reduceType().__add__(self)
	
	# Multiplikation
	def __mul__(self, other):
		if isinstance(other, Integer):
			return Integer(self.val * other.val)
		return other.reduceType().__mul__(self)
		
	# Division
	def __div__(self, other):
		if isinstance(other, Integer):
			if other.val == 0:
				return Infinity
			return Rational(self.val, other.val).reduceType()
		return other.reduceType().__rdiv__(self)
		
Int = Integer
		
		
		


"""Variablen"""		
class Var(Atom):
	def __init__(self, name):
		self.name = str(name)
		super().__init__(name)
		
	def __str__(self):
		return self.name
		
		
	
	
from .elementary import *
from .specialNumbers import *
	
	
	
	
	
	
	
	
	
	
	
	
	