from modules.jmath import Matrix
import math

class NeuralNetwork():
    def __init__(self, n_inputs, n_hidden, n_outputs, learning_rate):
        self.inputs_number = n_inputs
        self.hidden_number = n_hidden
        self.outputs_number = n_outputs
        self.learning_rate = learning_rate

        # Initialize weights with random values between -1 and 1
        self.IH_weights = Matrix(rows=n_hidden, cols=n_inputs+1)
        self.IH_weights.rand(-1, 1)
        self.HO_weights = Matrix(rows=n_outputs, cols=n_hidden+1)
        self.HO_weights.rand(-1, 1)

    def guess(self, inputs_array):
        inputs = Matrix(inputs_array + [1], self.inputs_number + 1)
        hidden_non_biased = self.IH_weights*inputs
        hidden_non_biased.apply(NeuralNetwork.sigmoid)
        
        hidden_array = hidden_non_biased.values + [1]
        hidden = Matrix(hidden_array, self.hidden_number + 1)
        outputs = self.HO_weights*hidden
        outputs.apply(NeuralNetwork.sigmoid)
        return outputs, hidden, inputs

    def train(self, data_array, target_array):
        for i in range(0, len(data_array)):
            outputs, hidden, inputs = self.guess(data_array[i])
            target = Matrix(target_array[i], self.outputs_number)
            outputs_error = target - outputs
            HO_weights_transposed = self.HO_weights.getTranspose()
            hidden_error = HO_weights_transposed*outputs_error
            
            outputs.apply(NeuralNetwork.dsigmoid)
            outputs.hadamard(outputs_error)
            outputs *= self.learning_rate
            HO_delta = outputs*hidden.getTranspose()
            self.HO_weights += HO_delta

            hidden.apply(NeuralNetwork.dsigmoid)
            hidden.hadamard(hidden_error)
            hidden *= self.learning_rate
            temporal = Matrix(hidden.values[:(hidden.n_rows-1)*hidden.n_cols], hidden.n_rows-1, hidden.n_cols)
            IH_delta = temporal*inputs.getTranspose()
            self.IH_weights += IH_delta

    # CHANGE TO USE APPLY METHOD IN MATRIX
    @staticmethod
    def sigmoid(x):
        return 1/(1+math.exp(-x))

    @staticmethod
    def dsigmoid(x, n=1):
        if n == 0:
            return NeuralNetwork.sigmoid(x) * (1 - NeuralNetwork.sigmoid(x))
        else:
            return x * (1 - x)

    @staticmethod
    def threshhold(matrix):
        values = []
        for m in matrix.values:
            if m < 0.5: values += [0]
            else: values += [1]
        new_matrix = Matrix(values, matrix.n_rows, matrix.n_cols)
        return new_matrix