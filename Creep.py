import random
from pygame.math import Vector2



#Structure du CREEP

class Creep :
    def __init__(self, largeur=400, hauteur=400) :
        self.rayon = 3
        self.position = Vector2(random.randint(0,1000),random.randint(0,750))
        self.couleur = (random.randint(50,230), random.randint(50,230), random.randint(50,230))
        self.nom : str("Creep1")

    #def reset(self):

    def mourir(self):
        pass


