import random, math
from neuralnetwork import NeuralNetwork

nn = NeuralNetwork(2, 4, 2)

train_x = [[0, 0], [1, 0], [0, 1], [1, 1]]
train_y = [[0, 1], [1, 0], [1, 0], [0, 1]]

data_x = []
data_y = []
for i in range(0, 10000):
    r = math.floor(random.uniform(0, 4))
    data_x += [train_x[r]]
    data_y += [train_y[r]]


nn.train(data_x, data_y)

print(nn.guess([0,0])[0])
print(nn.guess([0,1])[0])
print(nn.guess([1,0])[0])
print(nn.guess([1,1])[0])