import math
from random import uniform, choice


class SimulatedAnnealing:
    MAX_INTERATIONS = 100  # iterações
    MAX_RANDOMIZE = 10000  # perturbações
    MAX_SUCESS = 1500000  # sucessos
    ALPHA = 0.8

    @staticmethod
    def __himmelblau(x, y):
        return (x * x + y - 11) * (x * x + y - 11) + (x + y * y - 7) * (x + y * y - 7)

    def __cost(self, solution):
        return self.__himmelblau(solution[0], solution[1])

    def __diff_solution(self, solutionA, solutionB):
        return self.__cost(solutionA) - self.__cost(solutionB)

    @staticmethod
    def __randomize(solution):
        random_value = uniform(-6, 6)
        return (solution[0], random_value) if choice([True, False]) else (random_value, solution[1])

    def __diff_values(self, solution):
        for i in range(0, 100):
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

                if diff_s <= 0 or math.exp(-diff_s / temperature) > uniform(0, 1):
                    solution = new_solution
                    success_iterator = success_iterator + 1
                    # painter_callback(self.__cost(solution), temperature)
                    temperatures.append(temperature)
                    costs.append(self.__cost(solution))

                if success_iterator >= self.MAX_SUCESS:  # equilibrium
                    break

            print("%d %f %f %f %f" % (j, temperature, self.__cost(solution), solution[0], solution[1]))

            temperature = self.ALPHA * temperature

            if success_iterator == 0:  # stop condition
                break

        return temperatures, costs
