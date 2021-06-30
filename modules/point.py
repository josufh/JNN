import random

class Point:
    x = 0
    y = 0
    label = 0

    def __init__(self):
        self.x = random.random()
        self.y = random.random()
        if self.y > self.x:
            self.label = 1
        else:
            self.label = -1
