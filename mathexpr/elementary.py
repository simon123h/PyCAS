"""
Elementary arithmetic operators.
Includes Addition, Subtraction, Multiplication, Division and Exponentiation
"""

from .expr import Expression


# Addition
class Add(Expression):
    isAssociative = True
    isCommutative = True

    def __str__(self):
        return "("+("+".join([arg.__str__() for arg in self.args]))+")"


# Subtraction
class Sub(Expression):

    def __str__(self):
        return "-".join([arg.__str__() for arg in self.args])


# Multiplication
class Mul(Expression):
    isAssociative = True
    isCommutative = True

    def __str__(self):
        return "("+("*".join([arg.__str__() for arg in self.args]))+")"


# Division
class Div(Expression):
    def __str__(self):
        return "("+("/".join([arg.__str__() for arg in self.args]))+")"


# Exponentiation
class Pow(Expression):
    def __str__(self):
        return "("+("^".join([arg.__str__() for arg in self.args]))+")"
