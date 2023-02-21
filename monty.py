from random import choice
from numpy import percentile


class Monty:

    def __init__(self,
                 historical_items_per_iteration,
                 probabilities=[75, 85, 95],
                 passes=10000,
                 choose=choice):
        self.choose = choose
        self.passes = passes
        self.probabilities = probabilities
        self.historical_items_per_iteration = historical_items_per_iteration

    def historical_data_is_valid(self):
        return sum(self.historical_items_per_iteration) > 0

    def forecast(self, items):
        def iterations(i):
            count = done = 0
            if self.historical_data_is_valid():
                while done < items:
                    count += 1
                    done += self.choose(self.historical_items_per_iteration)
            return count

        data = list(map(iterations, range(self.passes)))
        return list(map(
            lambda p: (p, round(percentile(data, p))),
            self.probabilities))