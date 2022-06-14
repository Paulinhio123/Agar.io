###############################################
# Créateur : PETIT, HAMADOUCHE                #
# Date : 08/06/2022                           #
# Programme de lancement de notre application #
# Version : V0.1                              #
###############################################
import random
import pygame
from pygame.math import Vector2
import core
from Creep import Creep
from Ennemi import Ennemi
from Joueur import Player



def setup():

    core.fps = 60
    core.WINDOW_SIZE = [750, 750]
    core.bgColor = (255,255,255)

    j = Player()
    core.memory("player", j)

    core.memory("TableCreep",[])
    nbCreep = random.randint(60, 100)
    for i in range(nbCreep) :
        c = Creep()
        core.memory("TableCreep").append(c)

    core.memory("tableEnnemi", [])
    nbEnnemi = random.randint(5, 10)
    for e in range(nbEnnemi):
        e = Ennemi()
        core.memory("tableEnnemi").append(e)

def run(vector2=None):
    core.cleanScreen()

    # CREEP_Action
    for creep in core.memory("TableCreep"):
        creep.showCreep()

    for c in core.memory("TableCreep"):
        if c.pos.distance_to(core.memory("player").pos) < (core.memory("player").rayon + c.rayon):
            c.mourir()
            c.respawn()
            core.memory("player").grow()

    # Joueur
    core.memory("player").show()
    core.memory("player").moveClavier()
    # core.memory("player").grow()

    #Ennemi_action
    for ennemi in core.memory("tableEnnemi"):
        ennemi.showEnnemi()
        ennemi.randMove()


#Contrôle_Souris

    # if core.getMouseLeftClick() is not None :
    #     core.memory("souris",core.getMouseLeftClick())
    #     core.memory("PS", core.memory("souris")-core.memory("centredecercle"))
    #     core.memory("l", core.memory("PS").length())
    #     core.memory("u", core.memory("PS").normalize())
    #     core.memory("fr", core.memory("k") * ((core.memory("lo") - core.memory("l"))*core.memory("u")))

    #     core.memory("speed", core.memory("speed") - core.memory("fr"))
    #     core.memory("centredecercle", core.memory("centredecercle") + core.memory("speed"))

    #print(core.memory("souris"))

    # font1 = pygame.font.SysFont('Comic Sans MS', 72)
    # text = font1.render('BIEN JOUER', False, (255, 0, 0))
    # core.screen.blit(text, (core.WINDOW_SIZE[0] / 2 - 250, core.WINDOW_SIZE[1] / 2 - 50))

if __name__ == '__main__':
    core.main(setup, run)