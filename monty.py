from numpy import percentile

from project import Project


class Monty:

    def __init__(self, samples, items=None):
        self.items = items
        self.samples = samples
        self.simulated = self.__simulate()

    def forecast(self, probability=85):
        return round(percentile(
            self.simulated,
            probability))

    def __simulate(self):
        if not self.__is_valid():
            return [0]

        return list(map(self.__run_project, range(10000)))

    def __is_valid(self):
        return sum(self.samples) != 0 and self.items != 0

    def __run_project(self, _):
        return len(Project(self.items, self.samples).iterations)
