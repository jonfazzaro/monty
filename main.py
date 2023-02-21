import fire

from monty import Monty


def monty(items, samples, probabilities=None, passes=None):
    return Monty(
            samples=samples,
            probabilities=probabilities,
            passes=passes) \
        .forecast(items=items)


if __name__ == '__main__':
    fire.Fire(monty)
