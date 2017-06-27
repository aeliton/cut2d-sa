#!/usr/bin/env python3

from guillotine import Guillotine
from simulated_anealing_cut2d import SimulatedAnnealing
from plotter import Painter
from guillotine_draw import PainterGui

file = '/Users/thalita/Alano/Workspace/images/result_teste'
cut = '/cut.png'
plot = '/plot.png'

W, H, n, a, b, c, d, e = [int(s) for s in input().split(" ")]


rects = []

for i in range(0, int(n)):
    w, h, a, b, c = [int(s) for s in input().split(" ")]
    rects.append((w, h))

g = Guillotine((W, H), rects)
p = Painter()
s = SimulatedAnnealing(W, H, rects)
initial = s.initial_solution()
costs, temperatures, solution = SimulatedAnnealing.execute(s, initial, p.update_line)

cut = g.cut(solution)

gui = PainterGui()
gui.drawGuillotine(cut)
gui.save('/Users/thalita/Alano/Workspace/images/result_teste.png')

p.draw(costs, temperatures, '/Users/thalita/Alano/Workspace/images/result_plot.png')
