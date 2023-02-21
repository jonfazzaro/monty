from random import choice
from numpy import percentile


class Monty:

    def __init__(self,
                 samples,
                 probabilities=None,
                 passes=None,
                 choose=None):
        self.samples = samples
        self.probabilities = probabilities or [75, 85, 95]
        self.passes = passes or 10000
        self.choose = choose or choice

    def forecast(self, items):
        return self.__report(
            self.__simulate(items))

    def __report(self, simulated):
        def show(probability):
            return probability, round(percentile(simulated, probability))

        return list(map(show, self.probabilities))

    def __simulate(self, items):
        def iterations(i):
            count = done = 0
            if sum(self.samples) > 0:
                while done < items:
                    count += 1
                    done += self.choose(self.samples)
            return count

        return list(map(iterations, range(self.passes)))
