







import random
import pygame
from pygame.math import Vector2
import core
from Creep import Creep

core.printMemory()

def setup():

    print("Setup START---------")
    core.fps = 100
    core.WINDOW_SIZE = [1000, 750]

    core.memory("centredecercle", Vector2(500,500))
    core.memory("rayonducercle", 10)
    core.memory("couleurducercle", (255, 0, 0))

    core.memory("direction" ,Vector2(0,0))
    core.memory("lo", 1)
    core.memory("k", 0.00025)
    core.memory("fr", 1)
    core.memory("speed", Vector2(0,0))
    core.memory("PS", Vector2(0,0))
    core.memory("souris", Vector2(0,0))


    core.memory("TableCreep",[])
    for i in range(100) :
        core.memory("TableCreep").append(Creep())

    print("Setup END-----------")


def run(vector2=None):

    core.cleanScreen()
    pygame.draw.circle(core.screen, core.memory("couleurducercle"), core.memory("centredecercle"), core.memory("rayonducercle"))

#Centre du cercle

    if core.getKeyPressList ("r") :
        core.memory("direction", Vector2(0, 0))
    if core.getKeyPressList("z") :
        core.memory("direction", Vector2(core.memory("direction").x, -5))
    if core.getKeyPressList("s") :
        core.memory("direction", Vector2(core.memory("direction").x, 5))
    if core.getKeyPressList("q") :
        core.memory("direction", Vector2(-5,core.memory("direction").y))
    if core.getKeyPressList("d") :
        core.memory("direction", Vector2(5,core.memory("direction").y))
    if core.memory("centredecercle").y  < 0  or core.memory("centredecercle").y > core.WINDOW_SIZE[1] :
        core.memory("direction", Vector2(core.memory("direction").x, core.memory("direction").y*-1))


    if core.memory("centredecercle").x < 0 or core.memory("centredecercle").x > core.WINDOW_SIZE[0]:
        core.memory("direction", Vector2(core.memory("direction").x*-1, core.memory("direction").y ))


    core.memory("centredecercle" , core.memory("direction")+core.memory("centredecercle"))



#Contrôle_Souris

    if core.getMouseLeftClick() is not None :

        core.memory("souris",core.getMouseLeftClick())
        core.memory("PS", core.memory("souris")-core.memory("centredecercle"))
        core.memory("l", core.memory("PS").length())
        core.memory("u", core.memory("PS").normalize())
        core.memory("fr", core.memory("k") * ((core.memory("lo") - core.memory("l"))*core.memory("u")))

        core.memory("speed", core.memory("speed") - core.memory("fr"))
        core.memory("centredecercle", core.memory("centredecercle") + core.memory("speed"))



    print(core.memory("souris"))

 #CREEP_Apparition

    for i in core.memory("TableCreep"):
        pygame.draw.circle(core.screen, i.couleur, i.position, i.rayon)

        print(Creep().position)





core.main(setup, run)