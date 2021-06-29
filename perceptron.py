import random

def sign(n):
    if n >= 0:
        return 1
    else:
        return -1

class Perceptron:
    weights = []

    def __init__(self, n, lr):
        for i in range(0, n):
            self.weights += [random.uniform(-1, 1)]
        self.lr = lr

    def guess(self, inputs):
        sum = 1
        for i in range(0, len(self.weights)):
            sum += inputs[i] * self.weights[i]
        output = sign(sum)
        return output

    def correct(self, error, input_):
        for i in range(0, len(self.weights)):
            self.weights[i] += error * input_[i] * self.lr

    def train(self, input_, target):
        guess = self.guess(input_)
        error = target - guess
        self.correct(error, input_)            

    def accuracy(self, inputs, targets):
        total = len(targets)
        wrong = 0
        for i in range(0, total):
            guess = self.guess(inputs[i])
            if guess != targets[i]:
                wrong += 1
        return (total-wrong)/total
