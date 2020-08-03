from Boid import Boid

class Model:
    # ===============================================================================================
    def __init__(self):
        self.worldSettings = WorldSettings()
        self.boidSettings = BoidSettings()
        self.boids = [Boid(1)] * self.worldSettings.initialPopulation #boids objects
# ===============================================================================================
class BoidSettings:
    # ===============================================================================================
    def __init__(self):
        self.sight = 50 #sight radius in <units>
        self.maxSpeed = 20 #maximum speed allowed

# ===============================================================================================
class WorldSettings:
    def __init__(self):
        self.width = 2048
        self.height = 1024
        self.wind = [] #vector of wind
        self.wrapAround = True
        self.initialPopulation = 128

