import math
from random import uniform
from guillotine import Guillotine


class SimulatedAnnealing:
    MAX_INTERATIONS = 100  # iterações
    MAX_RANDOMIZE = 1000  # perturbações
    MAX_SUCESS = 500000  # sucessos
    ALPHA = 0.8

    def __init__(self, w, h, rects):
        self.guillotine = Guillotine((w, h), rects)

    def __cut2d(self, cut):
        if cut is not None:
            area = cut[2] * cut[3]
            if cut[4] is not None:
                area = area + self.__cut2d(cut[4])
            if cut[5] is not None:
                area = area + self.__cut2d(cut[5])
            return area

    def __cost(self, solution):
        return self.__cut2d(solution)

    def __diff_solution(self, solutionA, solutionB):
        return self.__cost(solutionA) - self.__cost(solutionB)

    def __randomize(self, solution):
        return self.guillotine.cut()

    def __diff_values(self, solution):
        for i in range(0, 1000):
            initial_solution = solution
            solution = self.__randomize(solution)
            diff_s = self.__diff_solution(initial_solution, solution)

            if diff_s > 0:
                yield diff_s

    def __initial_temperature(self, solution):
        SECRET = 4.48   # DESCRIBE THIS VARIABLE
        diffs = self.__diff_values(solution)
        l = list(diffs)
        return SECRET * (sum(l) / len(l))

    def execute(self, start, painter_callback):
        solution = start
        temperature = self.__initial_temperature(solution)
        success_iterator = 0
        temperatures = []
        costs = []

        for j in range(0, self.MAX_INTERATIONS):
            for i in range(0, self.MAX_RANDOMIZE):
                new_solution = self.__randomize(solution)
                diff_s = self.__diff_solution(new_solution, solution)

                try:
                    if diff_s >= 0 or math.exp(-diff_s / temperature) > uniform(0, 1):
                        solution = new_solution
                        success_iterator = success_iterator + 1
                        # painter_callback(self.__cost(solution), temperature)
                except:
                    pass

                if success_iterator >= self.MAX_SUCESS:  # equilibrium
                    break

            print("%d %f %d" % (j, temperature, self.__cost(solution)))

            temperatures.append(temperature)
            costs.append(self.__cost(solution))

            temperature = self.ALPHA * temperature

            if success_iterator == 0:  # stop condition
                break

        return temperatures, costs, solution
