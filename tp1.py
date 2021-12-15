from locale import normalize

import pygame
from pygame.math import Vector2

import core


def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = (400, 800)
    core.memory("centreducercle", pygame.Vector2(200, 200))
    core.memory("rayonducercle", 20)
    core.memory("couleurducercle", (150, 200, 3))

    print("Setup END---------")


def self():
    pass


def run():

    core.cleanScreen()
    pygame.draw.circle(core.screen, core.memory("couleurducercle"), core.memory("centreducercle"), core.memory("rayonducercle"))


    if core.getKeyPressList(pygame.K_z):
        core.memory("centreducercle", Vector2(core.memory("centreducercle").x, core.memory("centreducercle").y-5))

    if core.getKeyPressList(pygame.K_s):
        core.memory("centreducercle", Vector2(core.memory("centreducercle").x, core.memory("centreducercle").y+5))

    if core.getKeyPressList(pygame.K_q):
        core.memory("centreducercle", Vector2(core.memory("centreducercle").x-5, core.memory("centreducercle").y))

    if core.getKeyPressList(pygame.K_d):
        core.memory("centreducercle", Vector2(core.memory("centreducercle").x+5, core.memory("centreducercle").y))

    if core.memory("centreducercle").y + core.memory("rayonducercle") > core.WINDOW_SIZE[1] :
        core.memory("centreducercle", Vector2(core.memory("centreducercle").x, core.memory("centreducercle").y + 5))

    normalize(self)






core.main(setup, run)
