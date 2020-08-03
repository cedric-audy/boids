import random

class Boid:
    # ===============================================================================================
    def __init__(self, x):
        self.x = x
        self.y = 0
        self.speed = 1 #scalar value
        self.velocity = [] #vector
        self.neighbours = [] # other boids
    # ===============================================================================================
    def update(self):
        self.x += 1
        self.y += 1
