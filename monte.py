import random
from numpy import percentile


class Monte:
    PASSES = 10000
    PROBABILITY = 85

    def __init__(self, items, samples, passes=PASSES):
        self.simulations = []
        self.__simulate(items, samples, passes)

    def forecast(self, probability=PROBABILITY):
        return round(percentile(self.simulations, probability))

    def __simulate(self, items, samples, passes):
        if 0 < items and any(samples):
            for i in range(passes):
                self.simulations.append(
                    self.__simulation(items, samples))

    @staticmethod
    def __simulation(items, samples):
        iterations = []
        while sum(iterations) < items:
            iterations.append(random.choice(samples))
        return len(iterations)
