







import random
import pygame
from pygame.math import Vector2
import core
from Creep import Creep
from Ennemie import Ennemie

core.printMemory()

def setup():

    print("Setup START---------")
    core.fps = 50
    core.WINDOW_SIZE = [1000, 750]

    core.memory("centredecercle", Vector2(500,500))
    core.memory("rayonducercle", 10)
    core.memory("couleurducercle", (255, 0, 0))

    core.memory("direction", Vector2(0,0))
    core.memory("lo", 1)
    core.memory("k", 0.00025)
    core.memory("fr", 0.01)
    core.memory("speed", Vector2(0,0))
    core.memory("PS", Vector2(0,0))
    core.memory("souris", Vector2(0,0))


    core.memory("TableCreep",[])
    for c in range(100) :
        core.memory("TableCreep").append(Creep())

    core.memory("TableEnnemie", [])
    for e in range(random.randint(4,15)) :
        core.memory("TableEnnemie").append(Ennemie())

    print("Setup END-----------")


def run(vector2=None):


    core.cleanScreen()
    # CREEP_Apparition

    for c in core.memory("TableCreep"):
        pygame.draw.circle(core.screen, c.couleur, c.position, c.rayon)

        print(Creep().position)

    # Ennemies Aparition

    for e in core.memory("TableEnnemie"):
        pygame.draw.circle(core.screen, e.couleur, e.position, e.rayon)

        print(Ennemie().position)

    pygame.draw.circle(core.screen, core.memory("couleurducercle"), core.memory("centredecercle"), core.memory("rayonducercle"))

#Contrôle Clavier

    if core.getKeyPressList ("r") :
        core.memory("direction", Vector2(0, 0))
    if core.getKeyPressList("z") :
        core.memory("direction", Vector2(core.memory("direction").x, -2))
    if core.getKeyPressList("s") :
        core.memory("direction", Vector2(core.memory("direction").x, 2))
    if core.getKeyPressList("q") :
        core.memory("direction", Vector2(-2,core.memory("direction").y))
    if core.getKeyPressList("d") :
        core.memory("direction", Vector2(2,core.memory("direction").y))

    if core.memory("centredecercle").y < 0 or core.memory("centredecercle").y > core.WINDOW_SIZE[1]:
        core.memory("direction", Vector2(core.memory("direction").x, core.memory("direction").y * -1))

    if core.memory("centredecercle").x < 0 or core.memory("centredecercle").x > core.WINDOW_SIZE[0]:
        core.memory("direction", Vector2(core.memory("direction").x * -1, core.memory("direction").y))
    core.memory("centredecercle", core.memory("direction") + core.memory("centredecercle"))


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

    font1 = pygame.font.SysFont('Comic Sans MS', 72)
    text = font1.render('BIEN JOUER', False, (255, 0, 0))
    core.screen.blit(text, (core.WINDOW_SIZE[0] / 2 - 250, core.WINDOW_SIZE[1] / 2 - 50))








core.main(setup, run)