from neuralnetwork import NeuralNetwork
from jmath import Matrix

nn = NeuralNetwork(2, 2, 1)

m = Matrix(2, 3)

matrix = [2, 3, 4, 5, 6]
m.initValues(matrix)
print(m)