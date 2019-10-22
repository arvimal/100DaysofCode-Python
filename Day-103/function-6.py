#!/usr/bin/env python3

# Return your age in dog years :)
# Assuming a human year is equivalent to seven dog years.


def dog_years(name, age):
    return "{}, you are {} years old in dog years".format(name, age * 7)


print(dog_years("Lola", 16))
print(dog_years("Baby", 0))
