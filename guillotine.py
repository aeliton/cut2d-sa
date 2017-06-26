#!/usr/bin/env python3

import random
from functools import cmp_to_key


class Guillotine:
    def __init__(self, rect, rects):
        self.cuts = []
        self.w, self.h = rect
        rects = rects + [(x[1], x[0]) for x in rects if x[0] != x[1]]
        self.rects = sorted(rects, key=cmp_to_key(self.__cmp))

    def cut(self):
        # cut = self.__cut(0, 0, self.rect[0], self.rect[1])
        cut = self.__naive_cut(0, 0, self.w, self.h)
        self.cuts.append(cut)
        return cut

    # def __cut(self, x0, y0, x1, y1):
        # w, h = x1 - x0, y1 - y0
        # rects = map(lambda r: (r, random.randint(0, min(w//r[0], h//r[1]))), rects)

    def change(self, cut):
        x, y, w, h, q, gr, gu = cut
        pieces = self.__position_slack(cut)
        change_index = random.randint(0, len(pieces)-1)

        pos, slack = pieces[change_index]

        new, q = random.choice(self.__pieces(slack[0], slack[1]))

        cut = self.__change_pos(cut, pos[0], pos[1], new)
        return cut

    def __change_pos(self, cut, x0, y0, piece):
        x, y, w, h, q, gr, gu = cut

        if x == x0 and y == y0:
            if gr is not None:
                grx, gry, grw, grh, grq, grgr, grgu = gr
                gr = grx - (w - grx), gry, grw, grh, grq, grgr, grgu
            return (x, y, piece[0], piece[1], 1, gr, gu)
        if gr is not None:
            gr = self.__change_pos(gr, x0, y0, piece)
        if gu is not None:
            gu = self.__change_pos(gu, x0, y0, piece)
        return (x, y, w, h, q, gr, gu)

    def __position_slack(self, cut):
        x, y, w, h, q, gr, gu = cut
        sw, sh = w, h
        pieces = []
        if gr is not None:
            pieces += self.__position_slack(gr)
        else:
            sw += self.w - (x+w)

        if gu is not None:
            pieces += self.__position_slack(gu)
        else:
            sh += self.h - (y+h)

        return [((x, y), (sw, sh))] + pieces

    def __naive_cut(self, x0, y0, x1, y1):
        w, h = x1 - x0, y1 - y0

        p, q = random.choice(self.__pieces(w, h))
        pw, ph = p
        if pw <= w and ph <= h:
            above_cuts = self.__cut(x0, y0+ph, x1, y1)
            right_cuts = self.__cut(x0+pw, y0, x1, y0 + ph)
            return (x0, y0, pw, ph, 1, right_cuts, above_cuts)
        return None

    def __cut(self, x0, y0, x1, y1):
        w, h = x1 - x0, y1 - y0
        pieces = self.__pieces(w, h)
        if len(pieces) > 0:
            piece, max_quantity = random.choice(pieces)
            # get only a certain number of pieces that can fill the current line
            # rand_quantity = random.randint(1, max_quantity)
            rand_quantity = max_quantity
            pw, ph = piece
            above_cuts = self.__cut(x0, y0+ph, x1, y1)
            right_cuts = self.__cut(x0+pw * rand_quantity, y0, x1, y0 + ph)
            return (x0, y0, piece[0], piece[1], rand_quantity, right_cuts, above_cuts)
        return None

    """
    Return the all the pieces and their quantities that fits the area w x h

    returns a tuple:
    ((piece_w, piece_h), quantity)
    """
    def __pieces(self, w, h):
        rects = [x for x in self.rects if x[0] <= w and x[1] <= h]
        rects = list(map(lambda r: (r, w//r[0]), rects))
        if len(rects) > 0:
            rects = list(filter(lambda r: r[1] > 0, rects))
            return rects
        return []

    def __heuristic_cut(self, x0, y0, x1, y1):
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

# import numpy as np

# xs = np.random.random_integers(1, 10, 10)
# ys = np.random.random_integers(1, 10, 10)
# rects = [(xs[i], ys[i]) for i in range(len(xs))]

# g = Guillotine((20, 20), rects)
# cut = g.cut()
# g.change(cut)
