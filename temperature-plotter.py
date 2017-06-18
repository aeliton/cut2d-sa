#!/usr/bin/env python3
import sys
import matplotlib.pyplot as plt

x = []
y = []

for line in sys.stdin:
    line = line.split(" ")
    (i, t, f, a, b) = [float(s) for s in line]
    x.append(i)
    y.append(f)

# Scatter plot on top of lines
plt.plot(x, y, 'r', zorder=1, lw=1)
plt.scatter(x, y, s=1, zorder=2)
plt.title('Cost X Iteration')

plt.show()
