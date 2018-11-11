#!/usr/bin/env python3

"""
Split the sentence based on new lines,
and join them back with a pipe (|) in between
"""

message = """Hello world!
We hope that you are learning a lot of Python.
Have fun with our Bites of Py.
Keep calm and code in Python!
Become a PyBites ninja!"""


def split_in_columns(message=message):
    """Split the message by newline (\n)
    and join it together on '|' (pipe),
    return the obtained output"""
    words = message.split("\n")
    print("|".join(words))

split_in_columns(message)