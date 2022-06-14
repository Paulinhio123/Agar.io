###############################################
# Créateur : PETIT, HAMADOUCHE                #
# Date : 08/06/2022                           #
# Définition de notre classe Creep            #
# Version : V0.1                              #
###############################################
import random
from pygame.math import Vector2
import pygame
import core
from Joueur import Player

#Structure du CREEP



class Creep :
    def __init__(self, largeur=400, hauteur=400) :
        self.rayon = 3
        self.pos = Vector2(random.randint(0 - core.WINDOW_SIZE[0], core.WINDOW_SIZE[0] ),
                           random.randint(0 - core.WINDOW_SIZE[1], core.WINDOW_SIZE[1] ))
        self.couleur = (random.randint(50,230), random.randint(50,230), random.randint(50,230))


    def showCreep(self):
        core.Draw.circle(self.couleur, self.pos, self.rayon)

    def mourir(self):
        self.Couleur = core.bgColor
        self.Pos = Vector2(random.randint(0 - core.WINDOW_SIZE[0], core.WINDOW_SIZE[0]),
                           random.randint(0 - core.WINDOW_SIZE[1], core.WINDOW_SIZE[1]))
        #self.respawn()
        self.couleur = (random.randint(50,230), random.randint(50,230), random.randint(50,230))

    def respawn(self, posj = Player()):

        if self.pos.x < posj.x:
            self.mourir()

        if self.pos.y < posj.y:
            self.mourir()

        if self.pos.x > posj.x:
            self.mourir()

        if self.pos.y > posj.y:
            self.mourir()


