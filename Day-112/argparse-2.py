#!/usr/bin/env python3

import argparse

def get_args():
    parser = argparse.ArgumentParser(description="A test argument parser")
    parser.add_argument('-a', action="store_true", default=False)
    parser.add_argument('-b', action="store", dest="b")
    parser.add_argument('-c', action="store", dest="c",
                        type=int, required=True)
    return parser.print_help()



if __name__ == '__main__':
    get_args()

