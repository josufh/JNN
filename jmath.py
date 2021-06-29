class Matrix:

    def __init__(self, rows, cols):
        self.n_rows = rows
        self.n_cols = cols
        self.matrix = []

        for i in range(0, rows*cols):
            self.matrix += [0]

    def initValues(self, matrix):
        length = len(matrix)
        if length != self.n_rows*self.n_cols:
            print("MATRIX error on initValues: matrix aren't the same size.")
            return
        
        self.matrix = matrix
    
    def __str__(self):
        s = '\n' + str(self.n_rows) + 'x' + str(self.n_cols) + ' matrix\n'
        for i in range(0, self.n_rows):
            s += '  '
            for j in range(0, self.n_cols):
                s += str(self.matrix[j + i*self.n_cols])
                s += ' '
            s += '\n'
        return s