#!/usr/bin/env python3

from guillotine import Guillotine
from simulated_anealing_cut2d import SimulatedAnnealing
from plotter import Painter
import numpy as np


xs = np.random.random_integers(1, 10, 10)
ys = np.random.random_integers(1, 10, 10)
rects = [(xs[i], ys[i]) for i in range(len(xs))]

g = Guillotine((60, 60), rects)
p = Painter()
s = SimulatedAnnealing(60, 60, rects)
costs, temperatures, cut = SimulatedAnnealing.execute(s, g.cut(), p.update_line)

p.draw(costs, temperatures)
