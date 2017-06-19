#!/usr/bin/env python3

import random
from functools import cmp_to_key


class Guillotine:
    def __init__(self, rect, rects):
        self.cuts = []
        self.rect = rect
        self.rects = sorted(rects, key=cmp_to_key(self.__cmp))

    def cut(self):
        cut = self.__cut(0, 0, self.rect[0], self.rect[1])
        self.cuts.append(cut)
        return cut

    def __cut(self, x0, y0, x1, y1):
        w, h = x1 - x0, y1 - y0
        rects = [x for x in self.rects if x[0] * x[1] <= w * h]

        for pw, ph in random.sample(rects, min(len(rects), 3)):
            pw, ph = random.choice(rects)
            if pw <= w and ph <= h:
                above_cuts = self.__cut(x0, y0+ph, x1, y1)
                right_cuts = self.__cut(x0+pw, y0, x1, y0 + ph)
                return (x0, y0, pw, ph, right_cuts, above_cuts)
            aux = pw
            pw = ph
            ph = aux
            if pw <= w and ph <= h:
                above_cuts = self.__cut(x0, y0+ph, x1, y1)
                right_cuts = self.__cut(x0+pw, y0, x1, y0 + ph)
                return (x0, y0, pw, ph, right_cuts, above_cuts)

        for pw, ph in rects[::-1]:
            if pw <= w and ph <= h:
                above_cuts = self.__cut(x0, y0+ph, x1, y1)
                right_cuts = self.__cut(x0+pw, y0, x1, y0 + ph)
                return (x0, y0, pw, ph, right_cuts, above_cuts)
            aux = pw
            pw = ph
            ph = aux
            if pw <= w and ph <= h:
                above_cuts = self.__cut(x0, y0+ph, x1, y1)
                right_cuts = self.__cut(x0+pw, y0, x1, y0 + ph)
                return (x0, y0, pw, ph, right_cuts, above_cuts)

    def __cmp(self, a, b):
        return a[0] * a[1] - b[0] * b[1]
