#!/usr/bin/env python3

# Generate a tic-tac-toe board using dicts.


theBoard = {"top-L": " ", "top-M": " ", "top-R": " ",
            "mid-L": " ", "mid-M": " ", "mid-R": " ",
            "low-L": " ", "low-M": " ", "low-R": " "}
"""

theBoard = [
    {"top-L": " ", "top-M": " ", "top-R": " "},
    {"mid-L": " ", "mid-M": " ", "mid-R": " ", },
    {"low-L": " ", "low-M": " ", "low-R": " "}
]
"""

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


def check_win(theBoard):
    """
    Check for a win
    """
    vals = ["X", "O"]
    #import pdb
    # pdb.set_trace()
    for i in vals:

        if (theBoard["top-L"] and theBoard["top-M"] and theBoard["top-R"]) is i:
            print("Player {} is the new Winner".format(i))
        elif (theBoard["mid-L"] and theBoard["mid-M"] and theBoard["mid-R"]) is i:
            print("Player {} is the new Winner".format(i))
        elif (theBoard["low-L"] and theBoard["low-M"] and theBoard["low-R"]) is i:
            print("Player {} is the new Winner".format(i))
        else:
            pass


def play_loop():
    player = 'X'
    for i in range(9):
        printBoard(theBoard)
        move_location = input(
            "Player ** {} **, enter location: ".format(player))
        if move_location not in theBoard.keys():
            print("  \nLocation {} not valid. Try again!".format(move_location))
            play_loop()
        # Set the move location to the user's input.
        theBoard[move_location] = player
        # Check if we've met a win condition
        check_win(theBoard)
        if player == "X":
            player = "O"
        else:
            player = "X"
    printBoard(theBoard)


if __name__ == "__main__":
    # There are two players in tic-tac-toe, "X" and "O".
    # Both the player and their move is denoted by "X" and "O".
    play_loop()

print("Trying the test board!")