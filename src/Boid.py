import random
import math
import numpy as np

class Boid:
    # ===============================================================================================
    def __init__(self, x = 0, y = 0):
        self.position = Point(x,y)
        self.speed = 1 #scalar value
        self.velocity = np.array([]*3) #vector
        self.neighbours = [] # other boids
    # ===============================================================================================
    # def update(self):
        # self.x += 1
        # self.y += 1

class Point(object):
    # ===============================================================================================
    def __init__(self, x, y):
        self.X = x
        self.Y = y

    # ===============================================================================================
    def move(self, dx, dy):
        self.X = self.X + dx
        self.Y = self.Y + dy

    # ===============================================================================================
    def __str__(self):
        return f"Point({self.x},{self.y})"

    # ===============================================================================================
    def getX(self):
        return self.X

    # ===============================================================================================
    def getY(self):
        return self.Y

    # ===============================================================================================
    def distance(self, p):
        dx = self.X - p.X
        dy = self.Y - p.Y
        return hypot(dx, dy)