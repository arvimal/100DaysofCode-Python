#!/usr/bin/env python3

"""
1.  Use list comprehension to create a list of 100 random numbers
    from the range of 1 to 100, both inclusive.
2. Pick a random value from the list of random numbers.
"""

import random

random_list = []

# List comprehension to create a list of random number from 1 to 100
random_list = [random.randint(1, 101) for num in range(101)]
print(random_list)

# Pick a random number from the random list `random_list`
print("")
print("Randomest randomer: {:<3}".format(random.choice(random_list)))
