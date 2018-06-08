#!/usr/bin/env python3

# Generate a tic-tac-toe board using dicts.

theBoard = {"top-L": " ", "top-M": " ", "top-R": " ",
            "mid-L": " ", "mid-M": " ", "mid-R": " ",
            "low-L": " ", "low-M": " ", "low-R": " "}


def printBoard(board):
    """Print the latest state"""

    print("\n      - TIC TAC TOE - ")
    print("\n")
    print("\t{}".format("-" * 9))
    print("\t{} | {} | {}".format(
        board["top-L"], board["top-M"], board["top-R"]))
    print("\t{}".format("-" * 9))
    print("\t{} | {} | {}".format(
        board["mid-L"], board["mid-M"], board["mid-R"]))
    print("\t{}".format("-" * 9))
    print("\t{} | {} | {}".format(
        board["low-L"], board["low-M"], board["low-R"]))
    print("\t{}".format("-" * 9))
    print("\n")


# Get the current status of our tic-tac-toe board
printBoard(theBoard)
