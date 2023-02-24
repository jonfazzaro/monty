import random


class Project:

    def __init__(self, items, samples):
        self.iterations = []
        self.__run(items, samples)

    def __run(self, items, samples):
        if items != 0 and len(samples) != 0:
            while sum(self.iterations) < items:
                self.iterations.append(random.choice(samples))
