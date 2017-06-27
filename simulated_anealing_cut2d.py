import math
from random import uniform, choice
from guillotine import Guillotine
import time


class SimulatedAnnealing:
    MAX_INTERATIONS = 400  # iterações
    MAX_RANDOMIZE = 1000  # perturbações
    MAX_SUCESS = 1000000  # sucessos
    ALPHA = 0.8

    def __init__(self, w, h, rects):
        self.w = w
        self.h = h
        self.rects = rects
        self.guillotine = Guillotine((w, h), rects)

    def __cut2d(self, pieces):
        return sum([x[0]*x[1] for x in pieces])

    def __cost(self, solution):
        return self.__cut2d(solution)

    def __diff_solution(self, solutionA, solutionB):
        return self.__cost(solutionA) - self.__cost(solutionB)

    def __randomize(self, solution):
        return self.guillotine.change(solution)

    def initial_solution(self):
        area = 0
        pieces = []
        while area < self.w * self.h:
            p = choice(self.rects)
            pieces.append(p)
            area += p[0] * p[1]

        cut = self.guillotine.cut(pieces)

        return self.guillotine.pieces(cut)

    def __diff_values(self, solution):
        for i in range(0, 100):
            initial_solution = solution
            solution = self.initial_solution()
            diff_s = self.__diff_solution(initial_solution, solution)

            if diff_s > 0:
                yield diff_s

    def __initial_temperature(self, solution):
        SECRET = 4.48   # DESCRIBE THIS VARIABLE
        diffs = self.__diff_values(solution)
        l = list(diffs)
        return SECRET * (sum(l) / len(l))

    def __waste(self, solution):
        total = self.w * self.h
        return ((total - self.__cost(solution))/total)*100

    def execute(self, start):
        t0 = time.time()
        solution = start
        temperature = self.__initial_temperature(solution)
        success_iterator = 0
        temperatures = []
        costs = []
        solutions = []

        no_change_counter = 0
        for j in range(0, self.MAX_INTERATIONS):
            for i in range(0, self.MAX_RANDOMIZE):
                new_solution = self.__randomize(solution)
                diff_s = self.__diff_solution(new_solution, solution)

                try:
                    if diff_s >= 0 or math.exp(-diff_s / temperature) > uniform(0, 1):
                        solution = new_solution
                        success_iterator = success_iterator + 1

                except:
                    pass

                if success_iterator >= self.MAX_SUCESS:
                    break

            solutions.insert(j, self.__cost(solution))
            if j > 0 and solutions[j] == solutions[j-1]:
                no_change_counter += 1
            else:
                no_change_counter = 0

            temperatures.append(temperature)
            costs.append(self.__cost(solution))

            temperature = self.ALPHA * temperature

            if success_iterator == 0 or 0.2 * self.MAX_INTERATIONS <= no_change_counter:  # stop condition
                break

            average = sum(solutions)/len(solution)

        return temperatures, costs, solution, (self.__waste(solution), len(self.rects), "{0}x{1}".format(self.w, self.h), self.__cost(start), average, self.__cost(solution), time.time() - t0)
