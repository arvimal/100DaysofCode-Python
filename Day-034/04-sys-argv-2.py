#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    for i in sys.argv:
        print(f"{sys.argv.index(i) + 1} arg: {i}")
    print(f"List of arguments: {sys.argv[:]}")
