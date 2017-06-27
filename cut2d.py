#!/usr/bin/env python3

from guillotine import Guillotine
from simulated_anealing_cut2d import SimulatedAnnealing
from plotter import Painter
from guillotine_draw import PainterGui

cut_file_path = 'cut.png'
plot_file_path = 'plot.png'

W, H, n, a, b, c, d, e = [int(s) for s in input().split(" ")]


rects = []

for i in range(0, int(n)):
    w, h, a, b, c = [int(s) for s in input().split(" ")]
    rects.append((w, h))

g = Guillotine((W, H), rects)
p = Painter()
s = SimulatedAnnealing(W, H, rects)
initial = s.initial_solution()
costs, temperatures, solution, stats = SimulatedAnnealing.execute(s, initial)

#stats: (self.__waste(solution), len(self.rects), WxH, self.__cost(start), average, self.__cost(solution))
cut = g.cut(solution)

gui = PainterGui(W, H)
gui.drawGuillotine(cut)
gui.save(cut_file_path)
gui.end()

p.draw(costs, temperatures, plot_file_path)

print("%.2f\\%% %d %s %d %d %d %f" % stats)
