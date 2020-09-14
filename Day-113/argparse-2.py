#!/usr/bin/env python3

import argparse

# Our parser object
parser = argparse.ArgumentParser(description="Refreshing argparse module")

# Arguments the parser object can expect
parser.add_argument('--git-tag', help="Clone the repo and build from a Git tag")
parser.add_argument('--git-commit', help="Clone the repo and build from a Git commit")

# The arguments and the corresponding values are stored in the namespace `parser.parse_args()`
print("-- 1. This will print the arguments defined and expected by the parser object")
print(parser.parse_args())

# The argument switches and the values are expected as a list
print(parser.parse_args(['--git-tag', 'dfsfds', '--git-commit', '123']))
print("")

# This will error out since the argument `--git-fds` is not defined with `add_argument()`
print("-- This will error out and show a usage help")
print(parser.parse_args(['--git-fds', 'dfsfds', '--git-commit', '123']))
