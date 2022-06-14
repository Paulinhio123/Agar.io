###############################################
# Créateur : PETIT, HAMADOUCHE                #
# Date : 08/06/2022                           #
# Définition de notre classe Joueur           #
# Version : V0.1                              #
###############################################
import random
from pygame.math import Vector2
import pygame
import core


#Structure Joueur
class Player :

    def __init__(self):
        self.rayon = 10
        self.rayon2 = self.rayon * 1.5
        self.rayonmax = 500
        self.x = random.randint(0,650)
        self.y = random.randint(0,650)
        self.pos = Vector2(self.x, self.y)
        self.couleur = [255,0,0]
        self.couleur2 = [random.randint(0, 200),random.randint(0, 200),random.randint(0, 200)]

    # Variables mouvement sourie # pas fonctionnelle
        self.k = 0.5
        self.speed = 1
        self.maxspeed = 5
        self.direction = Vector2(0, 0)
        self.u = Vector2(0, 0)
        self.l = 0
        self.l0 = 10
        self.L = 0
        self.fr = 0

    def show(self):
        core.Draw.circle(self.couleur2, self.pos, self.rayon2)
        core.Draw.circle(self.couleur, self.pos, self.rayon)

    def moveClavier(self):
        self.limite()
        if core.getKeyPressList("z"):
            self.pos.y = self.pos.y - 2
        if core.getKeyPressList("s"):
            self.pos.y = self.pos.y + 2

        if core.getKeyPressList("d"):
            self.pos.x = self.pos.x + 2
        if core.getKeyPressList("q"):
            self.pos.x = self.pos.x - 2


    def moveCursor(self, clic = core.getMouseRightClick()):
        self.limite()
        if clic is not None:
            self.u = clic - self.pos
            self.l = self.u.length()
            self.u = self.u.normalize()
            self.l = abs(self.l - self.l0)

            self.fr = self.k * self.L * self.u
            self.direction = self.direction + self.fr
        else:
            self.u = Vector2(0, 0)
        if self.direction.length() > self.maxspeed and self.direction.length() != 0:
            self.direction.normalize()
            self.direction.scale_to_length(self.maxspeed)
        self.pos = self.direction + self.pos

    def limite(self):
        if self.x - self.rayon <= 0:
            self.x = self.rayon
        if self.x + self.rayon >= core.WINDOW_SIZE[0]:
            self.x = core.WINDOW_SIZE[0] - self.rayon

        if self.y - self.rayon <= 0:
            self.y = self.rayon
        if self.y + self.rayon >= core.WINDOW_SIZE[0]:
            self.y = core.WINDOW_SIZE[0] - self.rayon

    def grow(self):
        if self.rayon < self.rayonmax:
            self.rayon += 1
            self.maxspeed = self.maxspeed * 0.95

    def mourir(self):
        pass



