import random


class Project:

    def __init__(self, items, samples):
        self.iterations = []
        if len(samples) == 0:
            return

        while sum(self.iterations) < items:
            self.iterations.append(random.choice(samples))