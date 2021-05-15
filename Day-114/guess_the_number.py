#!/usr/bin/env python3

import random
import sys

def guessing_game():
    while True:
        num = random.randint(0, 101)
        guess = int(input("Guess the number: "))
        if guess < num:
            print("Too low")
        elif guess > num:
            print("Too high")
        elif guess == num:
            print("Just right")
            sys.exit()

if __name__ == "__main__":
    guessing_game()
