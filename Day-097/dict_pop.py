#!/usr/bin/env python3

"""
Add a value to a variable `health_points` from the
dictionary `available_items`, and delete the key
from the dictionary.

The operation has to be done in a single line of code.
"""

# The dictionary
available_items = {
    "health potion": 10,
    "cake of the cure": 5,
    "green elixir": 20,
    "strength sandwich": 25,
    "stamina grains": 15,
    "power stew": 30
    }

# The variable to add the points to
health_points = 20

print("Starting ..")
print("{:<20}: {}, {:<20}: {}".format("Available items", available_items, "Health points", health_points))
# Answer: The operation

## A. Add the value of the key `stamina grains` to `health_points`
## and delete `stamina grains` from `health_points`.
print("Adding `stamina grains` to Available item list.")
health_points += available_items.pop("stamina grains", 0)
print("{:<20}: {}, {:<20}: {}".format("Available items", available_items, "Health points", health_points))

## B. Add the value of the key `power stew` to `health_points`
## and delete `power stew` from `health_points`.
print("Adding `power stew` to Available item list.")
health_points += available_items.pop("power stew", 0)
print("{:<20}: {}, {:<20}: {}".format("Available items", available_items, "Health points", health_points))

## C. Add the value of the key `mystic bread` to `health_points`
## and delete `mystic bread` from `health_points`.
print("Adding `mystic bread` to Available item list.")
health_points += available_items.pop("mystic bread", 0)
print("{:<20}: {}, {:<20}: {}".format("Available items", available_items, "Health points", health_points))

#print(available_items)
#print(health_points)