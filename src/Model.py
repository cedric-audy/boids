import numpy as np

from Boid import Boid

class Model:
    # ===============================================================================================
    def __init__(self):
        self.worldSettings = WorldSettings()
        self.boidSettings = BoidSettings()
        self.boids = [Boid(1)] * self.worldSettings.initialPopulation #boids objects
    
    # ===============================================================================================
    # @staticmethod
    def rule1(self):
        #cohesion
        #c = (b1.position + b2.position + ... + bN.position) / N
        centerOfMass = 0
        for b in self.boids:
            centerOfMass += b.position
        
        return (centerOfMass / len(boids) - 1) / factor

    # ===============================================================================================
    # @staticmethod
    def rule2(self):
        #separation
        x = 1
    # ===============================================================================================
    # @staticmethod
    def rule3(self):
        #alignment
        x = 1

# ===============================================================================================
class BoidSettings:
    # ===============================================================================================
    def __init__(self):
        self.sight = 50 #sight radius in <units>
        self.maxSpeed = 20 #maximum speed allowed
        self.cohesionFactor = 100

# ===============================================================================================
class WorldSettings:
    # ===============================================================================================
    def __init__(self):
        self.width = 2048
        self.height = 1024
        self.wind = [] #vector of wind
        self.wrapAround = True
        self.initialPopulation = 128

