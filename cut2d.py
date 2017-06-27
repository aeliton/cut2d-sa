#!/usr/bin/env python3

from guillotine import Guillotine
from simulated_anealing_cut2d import SimulatedAnnealing
from plotter import Painter
import numpy as np

W, H, n, a, b, c, d, e = [int(s) for s in input().split(" ")]

rects = []

for i in range(0, int(n)):
    w, h, a, b, c = [int(s) for s in input().split(" ")]
    rects.append((w, h))

g = Guillotine((W, H), rects)
p = Painter()
s = SimulatedAnnealing(W, H, rects)
initial = s.initial_solution()
costs, temperatures, cut = SimulatedAnnealing.execute(s, initial, p.update_line)

p.draw(costs, temperatures)
