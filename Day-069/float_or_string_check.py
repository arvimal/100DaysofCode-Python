#!/usr/bin/env python3

# Write a function that verifies if a given input is a float or not.
# Do not use the float() builtin anywhere.


def isfloat(x):
    """
    Function to check if the input is a float or not

    -----
    Possible inputs:
        a) A proper integer [1]
        b) A float [10.2]
        c) An integer as a string ["1"]
        d) A float as a string ["10.2"]
        e) A mixed string ["10.a"]

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


#
isfloat(1)
isfloat("1")
# --
isfloat(1.5)
isfloat("1.5")
# --
isfloat("a.2")
