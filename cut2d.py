#!/usr/bin/env python3

from guillotine import Guillotine
from simulated_anealing_cut2d import SimulatedAnnealing
from plotter import Painter
import numpy as np
from guillotine_draw import PainterGui

file = '/Users/thalita/Alano/Workspace/images/result_teste'
cut = '/cut.png'
plot = '/plot.png'

xs = np.random.random_integers(1, 10, 10)
ys = np.random.random_integers(1, 10, 10)
rects = [(xs[i], ys[i]) for i in range(len(xs))]

g = Guillotine((60, 60), rects)
p = Painter()
s = SimulatedAnnealing(60, 60, rects)
initial = s.initial_solution()
costs, temperatures, solution = SimulatedAnnealing.execute(s, initial, p.update_line)

cut = g.cut(solution)

gui = PainterGui()
gui.drawGuillotine(cut)
gui.save('/Users/thalita/Alano/Workspace/images/result_teste.png')

p.draw(costs, temperatures, '/Users/thalita/Alano/Workspace/images/result_plot.png')
