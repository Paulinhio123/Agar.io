###############################################
# Créateur : PETIT, HAMADOUCHE                #
# Date : 08/06/2022                           #
# Définition de notre classe Ennemi           #
# Version : V0.1                              #
###############################################
import random
from pygame.math import Vector2
import core

#Structure Ennemie

class Ennemi :

    def __init__(self):
        self.rayon = 10
        self.x = random.randint(0, core.WINDOW_SIZE[0]-self.rayon)
        self.y = random.randint(0, core.WINDOW_SIZE[1]-self.rayon)
        self.couleur = (255, 0, 255)
        self.acc = Vector2(0,0)
        self.vel = [0,0]
        self.maxVel = 1

    def randMove(self):

        self.acc = Vector2(random.uniform(-400, 600), random.uniform(-50, 500))

        self.vel = self.vel + self.acc

        if self.vel.length() > self.maxVel:
            self.vel.scale_to_length(self.maxVel)

        self.y = self.vel.y + self.y
        self.x = self.vel.x + self.x

        self.limite()

    def showEnnemi(self):
        core.Draw.circle(self.couleur, [self.x, self.y], self.rayon)

    def limite(self):
        if self.x - self.rayon <= 0:
            self.x = self.rayon
        if self.x + self.rayon >= core.WINDOW_SIZE[0]:
            self.x = core.WINDOW_SIZE[0] - self.rayon

        if self.y - self.rayon <= 0:
            self.y = self.rayon
        if self.y + self.rayon >= core.WINDOW_SIZE[0]:
            self.y = core.WINDOW_SIZE[0] - self.rayon







