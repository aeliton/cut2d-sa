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

W, H = 60, 60

xs = np.random.random_integers(1, W//2, 10)
ys = np.random.random_integers(1, H//2, 10)
rects = [(xs[i], ys[i]) for i in range(len(xs))]

g = Guillotine((W, H), rects)
p = Painter()
s = SimulatedAnnealing(W, H, rects)
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
screen.fill((white))
pygame.display.update()


def f(x):
    return x * 600//((W+H)//2)


def drawRect(x0, y0, x1, y1, text):
    pygame.draw.rect(screen, (black), (f(x0), f(y0), f(x1), f(y1)), 1)
    pygame.display.update()
    screen.blit(font.render(text, True, (255, 0, 0)), (f(x0) + 1, f(y0) + 1))
    pygame.display.update()


def drawGuillotine(g):
    if g is not None:
        x, y, w, h, q, g1, g2 = g
        for i in range(q):
            drawRect(i*w + x, y, w, h, str((w, h)))
        drawGuillotine(g1)
        drawGuillotine(g2)


def area(cut):
    if cut is not None:
        x, y, w, h, q, g1, g2 = cut
        a = q * w * h
        if g1 is not None:
            a = a + area(g1)
        if g2 is not None:
            a = a + area(g2)
        return a


drawRect(0, 0, W, H, '')
drawGuillotine(cut)

print(area(cut))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
# end - drawing stuff to be removed
