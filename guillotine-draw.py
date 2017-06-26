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


class GuilhotinePainter:

    def __init__(self, instance):
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.gray = (211, 211, 211)

        self.cuts = []

        pygame.init()
        self.font = pygame.font.SysFont('Arial', 11)
        pygame.display.set_caption('Box Test')
        self.screen = pygame.display.set_mode((700, 700), 0, 32)
        self.screen.fill(self.white)
        pygame.display.update()

        file_lines = [line.rstrip('\n') for line in open(instance)]
        self.rects = list(map(lambda line: (int(line.split()[0]), int(line.split()[1])), file_lines[1:]))

        self.W, self.H = self.rects[2][0], self.rects[2][1]
        self.guilhotine = Guillotine((self.W, self.H), self.rects)
        self.painter = Painter()
        self.simulated_annealing = SimulatedAnnealing(self.W, self.H, self.rects)

        self.cut = self.cut()
        self.cuts.append(self.cut)

        print(self.cut)
        self.drawGuillotine(self.cut)
        print(self.area(self.cut))

    def cut(self):
        return self.guilhotine.cut()

    def draw(self):
        cut_pos = 0

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        cut_pos += 1
                        if cut_pos == len(self.cuts):
                            self.cut = self.guilhotine.change(self.cut)
                            self.cuts.append(self.cut)
                        else:
                            self.cut = self.cuts[cut_pos]
                        print("%d %s" % (cut_pos, self.cut))
                        self.drawGuillotine(self.cut)
                    elif event.key == pygame.K_LEFT:
                        cut_pos = cut_pos - 1 if cut_pos > 0 else len(self.cuts) - 1
                        self.cut = self.cuts[cut_pos]
                        print("%d %s" % (cut_pos, self.cut))
                        self.drawGuillotine(self.cut)

    def f(self, x):
        return x * 600 // ((self.W + self.H) // 2)

    def drawRect(self, x0, y0, x1, y1, text):
        pygame.draw.rect(self.screen, self.black, (self.f(x0), self.f(y0), self.f(x1), self.f(y1)), 1)
        pygame.display.update()
        self.screen.blit(self.font.render(text, True, (255, 0, 0)), (self.f(x0) + 1, self.f(y0) + 1))
        pygame.display.update()

    def drawGuillotine(self, g):
        self.screen.fill(self.white)
        self.__drawGuillotine(g)

    def __drawGuillotine(self, g):
        self.drawRect(0, 0, self.W, self.H, '')
        if g is not None:
            x, y, w, h, q, g1, g2 = g
            for i in range(q):
                self.drawRect(i * w + x, y, w, h, str((w, h)))
            self.__drawGuillotine(g1)
            self.__drawGuillotine(g2)

    def area(self, cut):
        if cut is not None:
            x, y, w, h, q, g1, g2 = cut
            a = q * w * h
            if g1 is not None:
                a = a + self.area(g1)
            if g2 is not None:
                a = a + self.area(g2)
            return a

gui = GuilhotinePainter('input/cut1.txt')
gui.draw()

