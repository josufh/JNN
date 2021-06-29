import random
from perceptron import Perceptron
from point import Point

p = Perceptron(2, 0.001)

points = []
for i in range(0, 8000):
    points += [Point()]

train_x = []
train_y = []
for point in points:
    train_x += [[point.x, point.y]]
    train_y += [point.label]

points = []
for i in range(0, 2000):
    points += [Point()]

test_x = []
test_y = []
for point in points:
    test_x += [[point.x, point.y]]
    test_y += [point.label]

epoch = 500

for j in range(0, epoch):
    for i in range(0, len(points)):
        p.train(train_x[i], train_y[i])
    acc = p.accuracy(test_x, test_y)
    print(j, acc*100, '%')
    if acc == 1.0: break

while True:
    n1 = input('Number     ')
    if n1 == 'c': break
    else:
        n2 = input('Number     ')
        print(p.guess([float(n1), float(n2)]))
