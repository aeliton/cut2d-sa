#!/usr/bin/env python3

import random
import numpy as np
# from functools import cmp_to_key

# start - drawing stuff to be removed
import pygame
import sys
# from pygame.locals import *
# end - drawing stuff to be removed


class Guillotine:
    def __init__(self, rect, rects):
        self.cuts = []
        self.rect = rect
        self.rects = rects
        # self.rects = sorted(rects, key=cmp_to_key(self.__cmp))

    def cut(self):
        cut = self.__cut(0, 0, self.rect[0], self.rect[1])
        self.cuts.append(cut)
        return cut

    def __cut(self, x0, y0, x1, y1):
        w, h = x1 - x0, y1 - y0
        pw, ph = random.choice(self.rects)
        if pw <= w and ph <= h:
            above_cuts = self.__cut(x0, y0+ph, x1, y1)
            right_cuts = self.__cut(x0+pw, y0, x1, y0 + ph)
            return (x0, y0, pw, ph, right_cuts, above_cuts)

    def __cmp(a, b):
        return a[0] * a[1] - b[0] * b[1]


xs = np.random.random_integers(1, 20, 10)
ys = np.random.random_integers(1, 20, 10)
rects = [(xs[i], ys[i]) for i in range(len(xs))]

print(rects)

g = Guillotine((60, 60), rects)
print(g.cut())

# start - drawing stuff to be removed

white = (255, 255, 255)
black = (0, 0, 0)

pygame.init()
font = pygame.font.SysFont('Arial', 11)
pygame.display.set_caption('Box Test')
screen = pygame.display.set_mode((700, 700), 0, 32)
screen.fill((white))
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


drawGuillotine(g.cut())


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
# end - drawing stuff to be removed
