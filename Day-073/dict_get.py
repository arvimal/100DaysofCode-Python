#!/usr/bin/env python3

"""
The get() method for a dict is used to:
    * Check if a key exist in dict.
    * If the key does not exist, return a predefined value.
    * If a predefined value is not set by us, or if the key
    does not exist, do not error out with a KeyError.

NOTE: Without using the `get()` method, calling a inexistent dict key
      will error out with `KeyError`.
"""

birthdays = {
    "Alice": "April 1",
    "Bob": "December 12",
    "Carol": "March 4"
}

# We try to list a key which is present, but not.

# 1. Key does exist in the birthdays dict
# If the key does exist, it returns the actual value for the key.
print("{}`s birthday is on {}".format(
    "Alice", birthdays.get("Alice", "Oct 10")))


# 2. Key does not exist in the birthdays dict
# If the key does not exist, it returns the predefined value set in the get()
# method.
print("{}`s birthday is on {}".format(
    "Vimal", birthdays.get("Vimal", "Oct 15")))
