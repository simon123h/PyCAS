from mathexpr.expr import Expression


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


class Div(Expression):
    def __str__(self):
        return "/".join([arg.__str__() for arg in self.args[:2]])


class Pow(Expression):
    def __str__(self):
        return "^".join([arg.__str__() for arg in self.args[:2]])
