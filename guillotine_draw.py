#!/usr/bin/env python3

import pygame


class PainterGui:
    def __init__(self):
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.gray = (211, 211, 211)

        self.H = 100
        self.W = 100

        pygame.init()
        self.font = pygame.font.SysFont('Arial', 11)
        pygame.display.set_caption('Box Test')
        self.screen = pygame.display.set_mode((700, 700), 0, 32)
        self.screen.fill(self.white)
        pygame.display.update()

    def end(self):
        pygame.quit()

    def clear(self):
        self.screen.fill(self.white)
        pygame.display.update()

    def save(self, file_path):
        pygame.image.save(self.screen, file_path)

    def drawRect(self, x0, y0, x1, y1, text):
        pygame.draw.rect(self.screen, self.black, (self.f(x0), self.f(y0), self.f(x1), self.f(y1)), 1)
        pygame.display.update()
        self.screen.blit(self.font.render(text, True, (255, 0, 0)), (self.f(x0) + 1, self.f(y0) + 1))
        pygame.display.update()

    def f(self, x):
        return x * 600 // ((self.W + self.H) // 2)

    def drawGuillotine(self, g):
        self.screen.fill(self.white)
        self.drawRect(0, 0, self.W, self.H, '')
        self.__drawGuillotine(g)

    def __drawGuillotine(self, g):
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
