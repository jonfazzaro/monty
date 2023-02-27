import numpy

from project import Project


class Monty:

    def __init__(self, items, samples, passes=10000):
        self.runs = []
        for i in range(passes):
            self.runs.append(Project(items, samples))

    def forecast(self, probability=85):
        results = list(map(lambda r: len(r.iterations), self.runs))
        return numpy.percentile(results, probability)