#!/usr/bin/env python3

import sys


def calculator(action=None, *args):
    if action not in ["add", "mult"]:
        print("The calculator takes in an action, either `add` or `mult`.")
        sys.exit()
    elif action == "add":
        print(sum(args))
    elif action == "mult":
        product = 1
        for i in args:
            product *= i
        print(product)


calculator("add", 10, 2)
calculator("mult", 20, 20)
