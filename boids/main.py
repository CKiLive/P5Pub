import random
import pygame
from pygame.math import Vector2
import core
from boids.boid import Boid


def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [800, 800]

    core.memory("boids", [])
    core.memory("boidsNb",100)

    for i in range(0,core.memory("boidsNb")):
        core.memory("boids").append(Boid(random.randint(0,0)))



    print("Setup END-----------")


def reset():
    core.memory("boids", [])
    for i in range(0,core.memory("boidsNb")):
        core.memory("boids").append(Boid(random.randint(0,2)))


def run():
    core.cleanScreen()
    if core.getKeyPressList(pygame.K_r):
        reset()

    for b in core.memory("boids"):
        if core.getMouseLeftClick():
           b.fear(core.getMouseLeftClick())
        b.flock(core.memory("boids"))
        b.update()
        b.show(core.screen)
        b.edge(core.WINDOW_SIZE)

core.main(setup, run)