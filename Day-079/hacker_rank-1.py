#!/usr/bin/env python3

if __name__ == "__main__":
    N = int(input())
    if N % 2 != 0:
        print("Weird")
    elif N % 2 == 0 and N in range(2, 6):
        print("Not Weird")
    elif N % 2 == 0 and N in range(6, 21):
        print("Weird")
    elif N % 2 == 0 and N > 20:
        print("Not Weird")
