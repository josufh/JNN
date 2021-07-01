import random

def map(v, x1, x2, y1, y2):
    m = (y2 - y1)/(x2 - x1)
    return m*(v - x1) + y1

class Matrix:

    def __init__(self, rows, cols):
        self.n_rows = rows
        self.n_cols = cols
        self.n_elements = rows*cols
        self.values = []

        for i in range(0, rows*cols):
            self.values += [0]

    def initValues(self, matrix):
        length = len(matrix)
        if length != self.n_elements:
            print("MATRIX error on initValues: matrix aren't the same size.")
            return
        
        self.values = matrix

    def rand(self, min=0, max=1):
        for i in range(0, self.n_elements):
            self.values[i] = random.uniform(min, max)

    def transpose(self):
        cols = []
        for i in range(0, self.n_cols):
            col = []
            for j in range(0, self.n_rows):
                col += [self.values[i + j*self.n_cols]]
            cols += col
        temp = self.n_cols
        self.n_cols = self.n_rows
        self.n_rows = temp
        self.initValues(cols)
    
    def getTranspose(self):
        cols = []
        for i in range(0, self.n_cols):
            col = []
            for j in range(0, self.n_rows):
                col += [self.values[i + j*self.n_cols]]
            cols += col
        new_matrix = Matrix(self.n_cols, self.n_rows)
        new_matrix.initValues(cols)
        return new_matrix
    
    def apply(self, func):
        for i in range(0, self.n_elements):
            self.values[i] = func(self.values[i])

    # CHECK IF MATRIX ARE THE SAME SIZE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    def hadamard(self, v):
        for i in range(0, self.n_elements):
            self.values[i] *= v.values[i]

    def __add__(self, v):
        if isinstance(v, int) or isinstance(v, float):
            values = self.values.copy()
            for i in range(0, self.n_elements):
                values[i] += v
        if isinstance(v, Matrix):
            if self.n_rows != v.n_rows or self.n_cols != v.n_cols:
                print("MATRIX error on add: matrix aren't the same size.")
                return self
            values = self.values.copy()
            for i in range(0, self.n_elements):
                values[i] += v.values[i]

        new_matrix = Matrix(self.n_rows, self.n_cols)
        new_matrix.initValues(values)
        return new_matrix

    __radd__ = __add__

    def __sub__(self, v):
        if isinstance(v, int) or isinstance(v, float):
            values = self.values.copy()
            for i in range(0, self.n_elements):
                values[i] -= v
        if isinstance(v, Matrix):
            if self.n_rows != v.n_rows or self.n_cols != v.n_cols:
                print("MATRIX error on add: matrix aren't the same size.")
                return self
            values = self.values.copy()
            for i in range(0, self.n_elements):
                values[i] -= v.values[i]

        new_matrix = Matrix(self.n_rows, self.n_cols)
        new_matrix.initValues(values)
        return new_matrix
    
    __rsub__ = __sub__

    def __mul__(self, v):
        if isinstance(v, int) or isinstance(v, float):
            values = self.values.copy()
            for i in range(0, self.n_elements):
                values[i] *= v
            new_matrix = Matrix(self.n_rows, self.n_cols)
            new_matrix.initValues(values)
            return new_matrix

        if isinstance(v, Matrix):
            if self.n_cols != v.n_rows:
                print("MATRIX error on mul: matrix aren't the proper size.")
                return self

            new_matrix = Matrix(self.n_rows, v.n_cols)
            rows = []
            for i in range(0, self.n_rows):
                row = []
                for j in range(0, self.n_cols):
                    row += [self.values[j + i*self.n_cols]]
                rows += [row]
            cols = []
            for i in range(0, v.n_cols):
                col = []
                for j in range(0, v.n_rows):
                    col += [v.values[i + j*v.n_cols]]
                cols += [col]
            values = []
            for i in range(0, new_matrix.n_elements):
                sum = 0
                i_row = int(i/v.n_cols)
                i_col = int(i%v.n_cols)
                for j in range(0, self.n_cols):
                    sum += rows[i_row][j]*cols[i_col][j]
                values += [sum]
            new_matrix.initValues(values)
            return new_matrix
        return self

    __rmul__ = __mul__

    def __str__(self):

        s = '\n' + str(self.n_rows) + 'x' + str(self.n_cols) + ' matrix\n'
        for i in range(0, self.n_rows):
            s += '  '
            for j in range(0, self.n_cols):
                s += str(self.values[j + i*self.n_cols])
                s += ' '
            s += '\n'
        return s
