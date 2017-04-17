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
        return (" + ".join([arg.__str__() for arg in self.args]))


# Subtraction
class Sub(Expression):
    def __str__(self):
        result = []
        i = 0
        for arg in self.args:
            if i != 0 and arg.isa((Sub, Add)):
                result.append("(" + arg.__str__() + ")")
            else:
                result.append(arg.__str__())
            i += 1
        return " - ".join(result)


# Multiplication
class Mul(Expression):
    isAssociative = True
    isCommutative = True

    def __str__(self):
        return (" * ".join(["(" + arg.__str__() + ")" if arg.isa((Add, Sub)) else arg.__str__() for arg in self.args]))


# Division
class Div(Expression):
    def __str__(self):
        result = []
        i = 0
        for arg in self.args:
            if i != 0 and arg.isa((Mul, Div)) or arg.isa((Sub, Add)):
                result.append("(" + arg.__str__() + ")")
            else:
                result.append(arg.__str__())
            i += 1
        return " / ".join(result)


# Exponentiation
class Pow(Expression):
    def __str__(self):
        return "(" + ("^".join(["(" + arg.__str__() + ")" if arg.isa((Add, Sub, Div, Mul)) else arg.__str__() for arg in self.args])) + ")"
