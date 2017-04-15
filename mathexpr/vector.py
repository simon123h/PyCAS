# TODO: implement vector class

from .expr import Expression


class Matrix(Expression):
    def __init__(self, data):
        # a two-dimensional list
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])
        Expression.__init__(self, data)

    def __add__(self, other):
        if self.rows == other.rows and self.cols == other.cols:
            return Matrix([[value[0] + value[1] for value in zip(row[0], row[1])] for row in zip(self.data, other.data)])
        else:
            raise ValueError('Given Matrices do not have the same dimensions')

    def __str__(self):
        data = [", ".join([str(x) for x in row]) for row in self.data]
        return "{{" + "}{".join(data) + "}}"


class Vector(Matrix):
    def __init__(self, data):
        Expression.__init__(data)
        Matrix.__([[x] for x in data])


class Tensor(Expression):
    pass
