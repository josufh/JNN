from neuralnetwork import NeuralNetwork
from jmath import Matrix

nn = NeuralNetwork(2, 2, 1)

m = Matrix(2, 3)
n = Matrix(3, 2)

matrix = [1, 2, 3, 4, 5, 6]
natrix = [1, 2, 3, 4, 5, 6]

m.initValues(matrix)
n.initValues(natrix)

print(m, n)

m  = n * m

print(m)