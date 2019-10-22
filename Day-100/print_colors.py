#!/usr/bin/env python3

VALID_COLORS = ["blue", "yellow", "red"]


def print_colors():
    """Ask for color, lowercase it, check if 'quit' is entered, if so print
       'bye' and break, next check if given color is in VALID_COLORS, if not,
       continue, finally if that check passes, print the color"""
    while True:
        my_color = input("Enter a color:- ")
        if my_color.lower() == "quit":
            print("bye")
            break
        elif my_color.lower() in VALID_COLORS:
            print("{}".format(my_color.lower()))
        else:
            print("Not a valid color")
            pass


print_colors()
