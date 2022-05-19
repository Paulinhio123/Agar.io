import random
from pygame.math import Vector2
import core


#Structure Joueur
class Joueur :

    def __init__(self):
        self.rayon = 10
        self.posx = 250
        self.posy = 350
        self.couleur = [0,255,0]

    def show(self):
        core.Draw.circle(self.couleur, [self.posx, self.posy], self.rayon)

    def mourir(self):
        pass

    def move(self):
        # if core.getKeyPressList("r"):
        #     core.memory("joueur", Vector2(0, 0))
        if core.getKeyPressList("z"):
            core.memory("joueur", Vector2(core.memory("joueur").posx, -2))
        if core.getKeyPressList("s"):
            core.memory("joueur", Vector2(core.memory("joueur").posx, 2))
        if core.getKeyPressList("q"):
            core.memory("joueur", Vector2(-2, core.memory("joueur").posy))
        if core.getKeyPressList("d"):
            core.memory("joueur", Vector2(2, core.memory("joueur").posy))

        self.limit()

    def limit(self):
        if core.memory("centredecercle").y < 0 or core.memory("centredecercle").y > core.WINDOW_SIZE[1]:
            core.memory("direction", Vector2(core.memory("direction").x, core.memory("direction").y * -1))

        if core.memory("centredecercle").x < 0 or core.memory("centredecercle").x > core.WINDOW_SIZE[0]:
            core.memory("direction", Vector2(core.memory("direction").x * -1, core.memory("direction").y))
        core.memory("centredecercle", core.memory("direction") + core.memory("centredecercle"))

