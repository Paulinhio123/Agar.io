import pygame
import core

def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = (400, 800)
    core.memory("centreducercle", pygame.Vector2(200, 200))
    core.memory("rayonducercle", 100)
    core.memory("couleurducercle", (150, 200, 3))

    core.memory("gravity", 1)
    print("Setup END---------")

def run():

    core.cleanScreen()
    pygame.draw.circle(core.screen, core.memory("couleurducercle"), core.memory("centreducercle"), core.memory("rayonducercle"))
    core.memory("centreducercle", pygame.Vector2(core.memory("centreducercle").x, core.memory("centreducercle").y+core.memory("gravity")))
    if core.memory("centreducercle").y+core.memory("rayonducercle")>core.WINDOW_SIZE[1]:
        core.memory("gravity", core.memory("gravity") * -1)

    if core.memory("centreducercle").y - core.memory("rayonducercle") < 0 :
        core.memory("gravity", core.memory("gravity")* -1)




core.main(setup, run)
