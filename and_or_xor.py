import random, math, pygame
from modules.neuralnetwork import NeuralNetwork as NN
from pygame import Color
from modules.jmath import map

xor = NN(2, 2, 1, 0.05)
a = NN(2, 1, 1, 0.05)
o = NN(2, 1, 1, 0.05)

xor_x = [[0, 0], [1, 0], [0, 1], [1, 1]]
xor_y = [[0], [1], [1], [0]]

and_x = [[0, 0], [1, 0], [0, 1], [1, 1]]
and_y = [[0], [0], [0], [1]]

or_x = [[0, 0], [1, 0], [0, 1], [1, 1]]
or_y = [[0], [1], [1], [1]]

def next_data(train_x, train_y):
    r = math.floor(random.uniform(0, 4))
    data_x = [train_x[r]]
    data_y = [train_y[r]]
    return data_x, data_y

def set_colors(row, col):
    colors = []
    for i in range(0, row*col):
        x = map((i%col)*side, 0, width, 0, 1)
        y = map(int(i/row)*side, 0, height, 0, 1)
        r = xor.guess([x, y])[0].values[0]
        g = a.guess([x, y])[0].values[0]
        b = o.guess([x, y])[0].values[0]
        r, g, b = math.floor(r*255), math.floor(g*255), math.floor(b*255)
        colors += [Color(r, g, b)]

    return colors


pygame.init()

width = 500
height = 500
screen = pygame.display.set_mode([width, height])

side = 20
rectangles = []
rects_row = int(width/side)
rects_col = int(height/side)
rects_total = rects_row * rects_col

for i in range(0, rects_total):
    x = (i%rects_col)*side
    y = int(i/rects_row)*side
    r = pygame.Rect(x, y, side, side)
    rectangles += [r]
colors = set_colors(rects_row, rects_col)


done = False
while not done:
    screen.fill([255, 255, 255])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            pass
    for i in range(0, 300):
        data = next_data(xor_x, xor_y)
        xor.train(data[0], data[1])

        data = next_data(and_x, and_y)
        a.train(data[0], data[1])

        data = next_data(or_x, or_y)
        o.train(data[0], data[1])
    colors = set_colors(rects_row, rects_col)

    for i in range(0, len(rectangles)):
        pygame.draw.rect(screen, colors[i], rectangles[i])
    
    pygame.display.flip()