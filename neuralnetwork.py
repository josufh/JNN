from perceptron import Perceptron
LR = 0.01

class NeuralNetwork():


    def __init__(self, n_inputs, n_hidden, n_outputs):
        self.n_i = n_inputs
        self.n_h = n_hidden
        self.n_o = n_outputs
        
        self.h_nodes = []
        for i in range(0, self.n_h):
            self.h_nodes += [Perceptron(self.n_i, LR)]

        self.o_nodes = []
        for i in range(0, self.n_o):
            self.o_nodes += [Perceptron(self.n_h, LR)]
