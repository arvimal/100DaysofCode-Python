#!/usr/bin/env python3

# Boolean operators : OR, AND, NOT

# The order of priority for boolean opeartors are:
# 1. OR
# 2. AND
# 3. NOT

# 1. OR
# OR means that if any conditional that is `OR`ed together is TRUE
# the statement runs
x, y = 10, 20
if x < 10 or y > 15:
    print("This is true!")

# 2. AND
# AND means that all statements must be True for the statement
# to run.
x, y = 10, 10
if x == 10 and y == 10:
    print("x is {0}, and y is {1}".format(x, y))
else:
    print("Sorry!")

# NOT
# NOT means that if the conditionals are False, the statement runs.
my_list = [1, 2, 3, 4, 5]
x = 10
if x not in my_list:
    print("x is not in {}".format(my_list))

if x != 11:
    print("x is not 11!")
