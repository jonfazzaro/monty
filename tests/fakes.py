class FakeRandom:
    def __init__(self):
        self.call_count = 0

    def choice(self, samples):
        self.call_count += 1
        index = round(self.call_count / 10) % len(samples)
        return samples[index]
