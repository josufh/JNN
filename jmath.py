import random

class Matrix:

    def __init__(self, rows, cols):
        self.n_rows = rows
        self.n_cols = cols
        self.n_elements = rows*cols
        self.matrix = []

        for i in range(0, rows*cols):
            self.matrix += [0]

    def initValues(self, matrix):
        length = len(matrix)
        if length != self.n_elements:
            print("MATRIX error on initValues: matrix aren't the same size.")
            return
        
        self.matrix = matrix

    def rand(self, min=0, max=1):
        for i in range(0, self.n_elements):
            self.matrix[i] = random.uniform(min, max)

    def __add__(self, v):
        if isinstance(v, int) or isinstance(v, float):
            for i in range(0, self.n_elements):
                self.matrix[i] += v
        if isinstance(v, Matrix):
            if self.n_rows != v.n_rows or self.n_cols != v.n_cols:
                print("MATRIX error on add: matrix aren't the same size.")
                return self
            for i in range(0, self.n_elements):
                self.matrix[i] += v.matrix[i]

        new_matrix = Matrix(self.n_rows, self.n_cols)
        new_matrix.initValues(self.matrix)
        return new_matrix

    __radd__ = __add__

    def __mul__(self, v):
        if isinstance(v, int) or isinstance(v, float):
            for i in range(0, self.n_elements):
                self.matrix[i] *= v
        
        new_matrix = Matrix(self.n_rows, self.n_cols)
        new_matrix.initValues(self.matrix)
        return new_matrix

    __rmul__ = __mul__

    def __str__(self):
        s = '\n' + str(self.n_rows) + 'x' + str(self.n_cols) + ' matrix\n'
        for i in range(0, self.n_rows):
            s += '  '
            for j in range(0, self.n_cols):
                s += str(self.matrix[j + i*self.n_cols])
                s += ' '
            s += '\n'
        return s