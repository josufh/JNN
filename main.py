from neuralnetwork import NeuralNetwork

nn = NeuralNetwork(2, 2, 1)

train_x = [[0, 0], [1, 0], [0, 1], [1, 1]]
train_y = [[0], [1], [1], [0]]

nn.train(train_x, train_y)
