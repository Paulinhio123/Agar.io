import random
from pygame.math import Vector2


class Ennemie :

    def __init__(self):
        self.size(10)
        self.position = Vector2(random.randint(0, 500), random.randint(0, 500))
        self.couleur = (255,0,0)
        self.couleur = random.randstr(0,26)
