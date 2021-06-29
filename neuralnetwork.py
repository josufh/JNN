from jmath import Matrix
import math

LR = 0.001

class NeuralNetwork():


    def __init__(self, n_inputs, n_hidden, n_outputs):
        self.n_i = n_inputs
        self.n_h = n_hidden
        self.n_o = n_outputs

        self.HW = Matrix(n_hidden, n_inputs+1)
        self.HW.rand(-1, 1)

        self.OW = Matrix(n_outputs, n_hidden+1)
        self.OW.rand(-1, 1)

    def guess(self, inputs):
        inputs += [1]
        input_matrix = Matrix(self.n_i+1, 1)
        input_matrix.initValues(inputs)
        hidden = self.HW*input_matrix
        hidden = NeuralNetwork.sigmoid(hidden)
        
        hidden.matrix += [1]
        hidden.n_rows += 1
        output_matrix = self.OW*hidden
        output_matrix = NeuralNetwork.sigmoid(output_matrix)
        return output_matrix

    def train(self, x, y):
        for i in range(0, len(x)):
            guess = self.guess(x[i])
            y_m = Matrix(len(y[i]), 1)
            y_m.initValues(y[i])
            guess_error = y_m - guess
            OW_t = self.OW.getTranspose()
            hidden_error = OW_t*guess_error
            print(hidden_error)          

    # CHANGE TO USE MAP METHOD IN MATRIX
    @staticmethod
    def sigmoid(matrix):
        values = []
        for m in matrix.matrix:
            values += [1/(1+math.exp(-m))]
        new_matrix = Matrix(matrix.n_rows, matrix.n_cols)
        new_matrix.initValues(values)
        return new_matrix

    @staticmethod
    def threshhold(matrix):
        values = []
        for m in matrix.matrix:
            if m < 0: values += [0]
            else: values += [1]
        new_matrix = Matrix(matrix.n_rows, matrix.n_cols)
        new_matrix.initValues(values)
        return new_matrix