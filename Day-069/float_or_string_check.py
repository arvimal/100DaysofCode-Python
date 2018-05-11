#!/usr/bin/env python3

# Write a function that verifies if a given input is a float or not.
# Do not use the float() builtin anywhere.

# The theme is to build a feature similar to the `is*` methods
# available for the `str` class.
# In [14]: [i for i in dir(str) if i.startswith("is")]
# Out[14]:
# ['isalnum',
# 'isalpha',
# 'isdecimal',
# 'isdigit',
# 'isidentifier',
# 'islower',
# 'isnumeric',
# 'isprintable',
# 'isspace',
# 'istitle',
# 'isupper']


def isfloat(x):
    """
    Function to check if the input is a float or not.
    Even if the input is a string in the form of an int/float,
    they should be treated as int/float respectively.

    -----
    Possible inputs:
        a) A proper integer [1], should return int
        b) A float [10.2], should return float
        c) An integer as a string ["1"], should return int
        d) A float as a string ["10.2"], should return float
        e) A mixed string ["10.a"], should return string

    Idea:
        1. Convert the input to a string.
        2. Split the string on the delimiter ".", to a list
        3. If the list contains one element,
            * Try converting it into an integer
                * Success = input is an integer
                * Not Success = input is a string
        4. If the list contains two elements
            * Try converting each element into integers
                * Both succeed = Input is a float
                * Any one fail = Input is a string
        5. If the list contains more than two elements
            * The input is a string
    """

    # 1, 1.0, and "1", "1.0"

    x = str(x)
    x_list = x.split(".")

    if len(x_list) == 1:
        # x = 1, or x = "1"
        try:
            a = int(x_list[0])
            print("{} is an integer.".format(a))
        except ValueError:
            print("{} is {}".format(a, type(a)))
    #----
    elif len(x_list) == 2:
        try:
            a, b = x_list[0], x_list[1]
            a, b = int(x_list[0]), int(x_list[1])
            print("{} is a float.".format(str(a) + "." + str(b)))
        except ValueError:
            print("{} is a string.".format(str(a) + "." + str(b)))

    else:
        print("{} is a string".format(x))
#
isfloat(1)
isfloat("1")
# --
isfloat(1.5)
isfloat("1.5")
# --
isfloat("a.2")
# --
isfloat("1.2.4")