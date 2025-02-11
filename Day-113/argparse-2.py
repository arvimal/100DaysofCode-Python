#!/usr/bin/env python3

import argparse

# Our parser object
parser = argparse.ArgumentParser(description="Refreshing argparse module")

# Arguments the parser object can expect
parser.add_argument("--git-tag", help="Clone the repo and build from a Git tag")
parser.add_argument("--git-commit", help="Clone the repo and build from a Git commit")

# The arguments and the corresponding values are stored in the namespace `parser.parse_args()`
print("-- 1. This will print the arguments defined and expected by the parser object")
print(
    "NOTE: Calling the `parse_args()` method on the parser object to access the argument namespace"
)
print(parser.parse_args())
print()

# The argument switches and the values are expected as a list
print(
    "-- 2. This will print the arguments in the order they're defined via `add_argument`"
)
print(parser.parse_args(["--git-tag", "dfsfds", "--git-commit", "123"]))
print(parser.parse_args(["--git-commit", "34324324324", "--git-tag", "dfsdsfd"]))
print("")

# This will error out since the argument `--git-fds` is not defined with `add_argument()`
print("-- 3. This will error out and show a usage help")
print(parser.parse_args(["--git-fds", "dfsfds", "--git-commit", "123"]))
