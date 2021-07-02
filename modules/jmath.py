import random
from typing import List

def map(v, x1, x2, y1, y2):
    m = (y2 - y1)/(x2 - x1)
    return m*(v - x1) + y1

class Matrix:

    def __init__(self, values=None, rows=0, cols=0):
        if values != None:
            if rows == 0 and cols != 0 and cols != len(values):
                print("MATRIX error on init: cols and values len is not the same")
                return None
            self.n_rows = 1
            self.n_cols = len(values)
            if rows != 0:
                if cols == 0:
                    if rows != 0 and rows != len(values):
                        print("MATRIX error on init: rows and values len is not the same")
                        return None
                    self.n_rows = len(values)
                    self.n_cols = 1
                else:
                    self.n_rows = rows
                    self.n_cols = cols                
            self.n_elements = self.n_rows*self.n_cols
            self.values = values
        elif values == None:
            if rows != 0 and cols != 0:
                self.n_rows = rows
                self.n_cols = cols
                self.n_elements = rows * cols
                values = []
                for i in range(0, self.n_elements):
                    values += [0]
                self.values = values
        else:
            print("MATRIX init: Something went very wrong.")
            return None

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
        self = Matrix(cols, self.cols, self.rows)
    
    def getTranspose(self):
        cols = []
        for i in range(0, self.n_cols):
            col = []
            for j in range(0, self.n_rows):
                col += [self.values[i + j*self.n_cols]]
            cols += col
        return Matrix(cols, self.n_cols, self.n_rows)
    
    def apply(self, func):
        for i in range(0, self.n_elements):
            self.values[i] = func(self.values[i])

    def hadamard(self, v):
        if self.n_rows != v.n_rows or self.n_cols != v.n_cols:
            print("MATRIX error on hadamard: matrix aren't the same size")
        
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

        return Matrix(values, self.n_rows, self.n_cols)

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

        return Matrix(values, self.n_rows, self.n_cols)
        
    
    __rsub__ = __sub__

    def __mul__(self, v):
        if isinstance(v, int) or isinstance(v, float):
            values = self.values.copy()
            for i in range(0, self.n_elements):
                values[i] *= v
            return Matrix(values, self.n_rows, self.n_cols)

        if isinstance(v, Matrix):
            if self.n_cols != v.n_rows:
                print("MATRIX error on mul: matrix aren't the proper size.")
                return self

            elements = self.n_rows*v.n_cols
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
            for i in range(0, elements):
                sum = 0
                i_row = int(i/v.n_cols)
                i_col = int(i%v.n_cols)
                for j in range(0, self.n_cols):
                    sum += rows[i_row][j]*cols[i_col][j]
                values += [sum]
            return Matrix(values, self.n_rows, v.n_cols)

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