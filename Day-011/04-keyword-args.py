#!/usr/bin/env python3

# Keyword arguments help functions accept any number
# of arguments

# The name `args` does not matter, it's the number of
# asterisks that matter
# One Asterisk takes all the arguments and creates a list
# Two Asterisk takes in key value pairs and creates a dict.
# 1. *args


def hello(*args):
    print(args)
    print("First element : {}".format(args[0]))
    print("Second element : {}\n".format(args[1]))

hello("hello", "how", "are", "you?")
hello(1, 2, 3)
hello([1,2], ["a", "b"])


# 2. **kwargs
def keyargs(**kwargs):
    print(kwargs)
keyargs(name="Tulip", job="SDE")

def testing(*args, **kwargs):
    print(args)
    print(kwargs)

testing(1, 2, numbers="One and Two", name="numerals")