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
	
	# Klasse der obersten Operation
	@property
	def cls(self):
		return self.__class__
		
	# Argumente des Operators/Ausdrucks ausgeben
	@property
	def args(self):
		return self._args
		
	# auf strukturelle Gleichheit zu anderem Ausdruck pruefen
	def equals(self, expr):
		if self.type != expr.type: return False
		for i in range(0, len(self.args)):
			if not self.args[i].equals(expr.args[i]): return False
		return True

	# Ausdruck in math. Schreibweise ausgeben
	def toString(self):
		if self.type == "Expression": return self.args[0].toString()
		return self.__class__.__name__ + "(" + ", ".join([arg.toString() for arg in self.args]) + ")" 
		
	# Variable varName durch Ausdruck expr ersetzen
	def set(self, varName, expr):
		return self.func(*[arg.set(varName, expr) for arg in self.args])
		
	# Ausdruck durch anderen Ausdruck substituieren
	def subs(self, oldExpr, newExpr):
		if self.equals(oldExpr):
			return newExpr
		return self.func(*[arg.subs(oldExpr, newExpr) for arg in self.args])
	
	# prueft, ob Ausdruck expr im Baum vorkommt
	def has(self, expr):
		if self.equals(expr):
			return True
		return any(arg.has(expr) for arg in self.args)

	# Kopie des Objekts
	def copy(self):
		return self.func(*self.args)
		
	# Ausdruck elementar auswerten
	#def eval(self):
	#	return self.func(*[arg.eval() for arg in self.args])
		
	# Builtin-Operatoren ueberschreiben
	def __eq__(self, other): return self.equals(other)
	def __ne__(self, other): return not self.equals(other)
	def __pos__(self): return self
	def __neg__(self): return Mul(Num(-1), self)
	def __add__(self, other): return Add(self, other)
	def __radd__(self, other): return Add(other, self)
	def __sub__(self, other): return Add(self, -other)
	def __rsub__(self, other): return Add(other, -self)
	def __mul__(self, other): return Mul(self, other)
	def __rmul__(self, other): return Mul(other, self)
	def __pow__(self, other): return Pow(self, other)
	def __rpow__(self, other): return Pow(other, self)
	def __xor__(self, other): return Pow(self, other)
	def __div__(self, other): return Div(self, other)
	def __rdiv__(self, other): return Mul(other, Pow(self, Num(-1)))
	__truediv__ = __div__
	__rtruediv__ = __rdiv__
	def __str__(self): return self.toString()
	def __repr__(self): return str(self)			# TODO nur zum debuggen
		
	
from .atom import Num, Var
from .elementary import Add, Sub, Mul, Pow, Div
