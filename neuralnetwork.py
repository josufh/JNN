from jmath import Matrix
import math

LR = 0.01

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
        hidden = NeuralNetwork.threshhold(hidden)
        
        hidden.matrix += [1]
        hidden.n_rows += 1
        output_matrix = self.OW*hidden
        output_matrix = NeuralNetwork.threshhold(output_matrix)
        return output_matrix

    @staticmethod
    def sigmoid(matrix):
        values = []
        for m in matrix.matrix:
            values += [1/(1+pow(math.e, -m))]
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