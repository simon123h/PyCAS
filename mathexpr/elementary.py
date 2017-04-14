from .expr import Expression
from .atom import Int


class Add(Expression):
    def __str__(self):
        return "+".join([arg.__str__() for arg in self.args])

    # hardcoded addition rules, axiomatic for int arithmetics
    def eval(self):
        print("evald add")
        if all(arg.isa(Int) for arg in self.args):
            return Int(sum([arg.val for arg in self.args]))
        return super().eval()


class Sub(Expression):
    def __str__(self):
        return "-".join([arg.__str__() for arg in self.args])


class Mul(Expression):
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
