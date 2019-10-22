#!/usr/bin/env python3

# Exceptions and handling them

# 1. Catching a ZeroDivisionError with try/except
try:
    1 / 0
except ZeroDivisionError:
    print("Zero division not possible!")

# 2. KeyError
my_dict = {"A": 1, "B": 2, "C": 3}
try:
    value = my_dict["D"]
except KeyError as err:
    print("\nThe key does not exist - {0}".format(err))

# 3. IndexError
my_list = [1, 2, 3, 43, 45, 55]
try:
    my_list[6]
except IndexError:
    print("\nThe index is not in the list.")

# 4. Using `finally`
# The clause under `finally` runs no matter what
# ie. if the try clauses runs or not.
# `finally` is good to clean out stuff before exiting the loop,
# if needed.
my_dict_1 = {"A": 1, "B": 2, "C": 3}
try:
    value = my_dict_1["D"]
except KeyError:
    print("\nA keyerror occurred")
finally:
    print("This will run no matter what!\n")

# 5. try/except/else
# The try/except statement can also have an `else` statement.
# This gets executed only if the `try` statement is a success.
# ie. no errors are hit.
my_dict_2 = {"A": 1, "B": 2, "C": 3}
try:
    value = my_dict_2["D"]
except KeyError:
    print("No such key in the dictionary.")
else:
    print("This is an `else` clause, this won't run here!")

my_dict_3 = {"A": 1, "B": 2, "C": 3}
try:
    value = my_dict_3["B"]
except KeyError:
    print("Hit a keyerror")
else:
    print("This will run, since there are no errors in this test\n")

    # Using both `finally` and `else` with `try/except`.
my_dict_4 = {"A": 1, "B": 2, "C": 3}
try:
    value = my_dict_4["A"]
except KeyError:
    print("Hit a KeyError.")
else:
    print("I will run if there are no Exceptions in this code")
finally:
    print("I am the one who will always execute! (for cleanup)")
