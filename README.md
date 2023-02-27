# Monty

Simple Monte Carlo forecasting in your terminal.

    monty --items 120 --samples "[8, 19, 12, 13, 3, 15, 6, 6, 7]"
    
        # parameters
        items               The number of work items to be done.
        samples             An array of the number of items completed per iteration, historically.
        probabilities       An array of probabilities at which to forecast. Defaults to [75, 85, 95].
        passes              How many passes to use in Monte Carlo simulation. Defaults to 10000.

        # sample output
        14 iterations (a 75% chance)
        14 iterations (a 85% chance)
        16 iterations (a 95% chance)


Written in Python, for reasons.

![](https://upload.wikimedia.org/wikipedia/en/c/cb/Flyingcircus_2.jpg)
