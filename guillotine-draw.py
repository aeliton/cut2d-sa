#!/usr/bin/env python3

# import numpy as np
from simulated_anealing_cut2d import SimulatedAnnealing
from guillotine import Guillotine
from plotter import Painter
# from functools import cmp_to_key

# start - drawing stuff to be removed
import pygame
import sys
# from pygame.locals import *
# end - drawing stuff to be removed

# W, H = 10, 10
# xs = np.random.random_integers(1, W//3, 30)
# ys = np.random.random_integers(1, H//3, 30)
# rects = [(xs[i], ys[i]) for i in range(len(xs))]

W, H, n, a, b, c, d, e = [int(s) for s in input().split(" ")]

rects = []

for i in range(0, int(n)):
    w, h, a, b, c = [int(s) for s in input().split(" ")]
    rects.append((w, h))

print(rects)
print("------------------------")

g = Guillotine((W, H), rects)
p = Painter()
s = SimulatedAnnealing(W, H, rects)
pieces = s.initial_solution()
cut = g.cut(pieces)
# costs, temperatures, cut = SimulatedAnnealing.execute(s, g.cut(), p.update_line)

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
    screen.fill((white))
    drawRect(0, 0, W, H, '')
    __drawGuillotine(g)


def __drawGuillotine(g):
    if g is not None:
        x, y, w, h, q, g1, g2 = g
        for i in range(q):
            drawRect(i*w + x, y, w, h, str((w, h)))
        __drawGuillotine(g1)
        __drawGuillotine(g2)


def area(cut):
    if cut is not None:
        x, y, w, h, q, g1, g2 = cut
        a = q * w * h
        if g1 is not None:
            a = a + area(g1)
        if g2 is not None:
            a = a + area(g2)
        return a


cuts = []

cuts.append(cut)
cut_pos = 0

print(cut)
drawGuillotine(cut)
print(area(cut))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                cut_pos += 1
                if cut_pos == len(cuts):
                    cut = g.change_cut(cut)
                    cuts.append(cut)
                else:
                    cut = cuts[cut_pos]
                print("%d %s" % (cut_pos, cut))
                drawGuillotine(cut)
            elif event.key == pygame.K_LEFT:
                cut_pos = cut_pos - 1 if cut_pos > 0 else len(cuts) - 1
                cut = cuts[cut_pos]
                print("%d %s" % (cut_pos, cut))
                drawGuillotine(cut)

# end - drawing stuff to be removed
