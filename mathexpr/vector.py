"""
Class for Vectors, Matrices and Tensors inheriting from each other.
"""

from .expr import Expression


class Tensor(Expression):
    def __init__(self, *data):
        self.rank = 0 if data == [] else 1
        d = data
        self.dimensions = [len(d)]
        while(isinstance(d[0], list)):
            self.rank += 1
            self.dimensions.append(len(d[0]))
            d = d[0]
        super().__init__(data)


class Matrix(Tensor):
    def __init__(self, data):
        # a two-dimensional list
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])
        for row in data:
            if len(row) != self.cols:
                raise ValueError("Given data has no valid matrix form! Row lengths must be equal")
        super().__init__(data)

    def matAdd(self, other):
        if self.rows == other.rows and self.cols == other.cols:
            return Matrix([[value[0] + value[1] for value in zip(row[0], row[1])] for row in zip(self.data, other.data)])
        else:
            raise ValueError('Given matrices do not have the same dimensions')

    # TODO: matmul implementieren
    def matMul(self, other):
        pass

    def __str__(self):
        data = [", ".join([str(x) for x in row]) for row in self.data]
        return "{{" + "}{".join(data) + "}}"


class Vector(Matrix):
    def __init__(self, data):
        self.data = list(data)
        self.dimension = len(list(data))
        super(Matrix, self).__init__([[x] for x in list(data)])

    def __str__(self):
        return "{" + ", ".join([str(d) for d in self.data]) + "}^T"

    def dotProd(self, other):
        pass

    def crossP(self, other):
        pass
