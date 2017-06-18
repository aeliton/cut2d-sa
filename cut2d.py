#!/usr/bin/env python3

from simulated_anealing import SimulatedAnnealing
from plotter import Painter


p = Painter()
s = SimulatedAnnealing()
costs, temperatures = SimulatedAnnealing.execute(s, (0, 0), p.update_line)

p.draw(costs, temperatures)
