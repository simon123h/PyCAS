from .expr import Expression
from .atom import Int


class Add(Expression):
    isAssociative = True
    isCommutative = True

    def __str__(self):
        return "+".join([arg.__str__() for arg in self.args])


class Sub(Expression):

    def __str__(self):
        return "-".join([arg.__str__() for arg in self.args])


class Mul(Expression):
    isAssociative = True
    isCommutative = True

    def __str__(self):
        return "*".join([arg.__str__() for arg in self.args])

    # hardcoded multiplication rules, axiomatic for int arithmetics
    def eval(self):
        print("evald mul")
        if all(arg.isa(Int) for arg in self.args):
            result = 1
            for arg in self.args:
                result *= arg.val
            return Int(result)
        return super().eval()


class Div(Expression):
    def __str__(self):
        return "/".join([arg.__str__() for arg in self.args[:2]])


class Pow(Expression):
    def __str__(self):
        return "^".join([arg.__str__() for arg in self.args[:2]])
