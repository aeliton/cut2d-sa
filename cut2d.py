#!/usr/bin/env python3

from meta_heuristic import SimulatedAnnealing
from plotter import Painter


p = Painter()
s = SimulatedAnnealing()
costs, temperatures = SimulatedAnnealing.execute(s, (0,0), p.update_line)
#p.drawOne(temperatures)
#p.drawOne(costs)
p.draw(costs, temperatures)

