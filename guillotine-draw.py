#!/usr/bin/env python3

import numpy as np
from simulated_anealing_cut2d import SimulatedAnnealing
from guillotine import Guillotine
from plotter import Painter
# from functools import cmp_to_key

# start - drawing stuff to be removed
import pygame
import sys
# from pygame.locals import *
# end - drawing stuff to be removed

xs = np.random.random_integers(1, 10, 10)
ys = np.random.random_integers(1, 10, 10)
rects = [(xs[i], ys[i]) for i in range(len(xs))]

g = Guillotine((60, 60), rects)
p = Painter()
s = SimulatedAnnealing(60, 60, rects)
costs, temperatures, cut = SimulatedAnnealing.execute(s, g.cut(), p.update_line)

print(cut)

# start - drawing stuff to be removed

white = (255, 255, 255)
black = (0, 0, 0)
gray = (211, 211, 211)

pygame.init()
font = pygame.font.SysFont('Arial', 11)
pygame.display.set_caption('Box Test')
screen = pygame.display.set_mode((700, 700), 0, 32)
screen.fill((gray))
pygame.display.update()


def f(x):
    return x * 10


def drawRect(x0, y0, x1, y1, text):
    pygame.draw.rect(screen, (black), (f(x0), f(y0), f(x1), f(y1)), 1)
    pygame.display.update()
    screen.blit(font.render(text, True, (255, 0, 0)), (f(x0) + 1, f(y0) + 1))
    pygame.display.update()


def drawGuillotine(g):
    if g is not None:
        drawRect(g[0], g[1], g[2], g[3], str((g[2], g[3])))
        drawGuillotine(g[4])
        drawGuillotine(g[5])


def area(cut):
    if cut is not None:
        print(cut)
        a = cut[2] * cut[3]
        if cut[4] is not None:
            a = a + area(cut[4])
        if cut[5] is not None:
            a = a + area(cut[5])
        return a


drawRect(0, 0, 60, 60, '')
drawGuillotine(cut)

print(area(cut))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
# end - drawing stuff to be removed
