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
        print(self.HW)

        self.OW = Matrix(n_outputs, n_hidden+1)
        self.OW.rand(-1, 1)
        print(self.OW)

    def guess(self, inputs):
        pass

    @staticmethod
    def sigmoid(x):
        return 1/(1+pow(math.e, -x))