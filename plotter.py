import matplotlib.pyplot as plt
import matplotlib.animation as anim
import numpy


class Painter:

    def __init__(self):
        self.temperatures = []
        self.func_obj = []
        self.hl, = plt.plot([], [])

    def update_line(self, temperature, cost):
        self.temperatures.append(temperature)
        self.func_obj.append(cost)
        self.hl.set_xdata(numpy.append(self.hl.get_xdata(), self.temperatures))
        self.hl.set_ydata(numpy.append(self.hl.get_ydata(), self.func_obj))
        plt.draw()
        plt.show()
        print(temperature, ': ', cost)

    def redraw(self, temperature, cost):
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        self.temperatures.append(temperature)
        self.func_obj.append(cost)

        def update(i):

            ax.clear()
            ax.plot(temperature, cost)
            print(temperature, ': ', cost)

        anim.FuncAnimation(fig, update, frames=100, repeat=False)
        plt.show()

    def drawOne(self, unit):
        counter = list(range(0, len(unit)))

        plt.plot(counter, unit, 'r', zorder=1, lw=1)
        plt.scatter(counter, unit, s=1, zorder=2)
        plt.title('Temperature')

        plt.show()

    def draw(self, costs, temperatures, file_path):
        # Scatter plot on top of lines
        plt.figure(1)

        plt.subplot(211)
        counter_costs = list(range(0, len(costs)))
        plt.plot(counter_costs, costs, 'r', zorder=1, lw=1)
        plt.scatter(counter_costs, costs, s=1, zorder=2)
        plt.title('Temperature')

        plt.subplot(212)
        counter_temperatures = list(range(0, len(temperatures)))
        plt.plot(counter_temperatures, temperatures, 'r', zorder=1, lw=1)
        plt.scatter(counter_temperatures, temperatures, s=1, zorder=2)
        plt.tight_layout(h_pad=2)
        plt.title('Costs')

        #plt.show()
        plt.savefig(file_path)


