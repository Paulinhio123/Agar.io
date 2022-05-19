import random
from pygame.math import Vector2

#Structure Ennemie
class Ennemie :

    def __init__(self):
        self.rayon = 10
        self.position = Vector2(random.randint(0, 1000), random.randint(0, 750))
        self.couleur = (255, 255, 255)
        self.v = Vector2(0,0)

    def move(self):
        pass

    def show(self):
        pass



