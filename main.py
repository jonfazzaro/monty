import fire

from monty import Monty


def monty(items, samples, probabilities=None, passes=None):
    simulation = Monty(samples=samples, items=items, passes=passes or 10000)
    return list(map(
        lambda p: f"{round(simulation.forecast(p))} iterations (a {p}% chance)",
        probabilities or [75, 85, 95]))


if __name__ == '__main__':
    fire.Fire(monty)
