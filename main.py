from neuralnetwork import NeuralNetwork

nn = NeuralNetwork(2, 2, 1)

inputs = [1, 0]

guess = nn.guess(inputs)

print(guess)