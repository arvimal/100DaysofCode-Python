#!/usr/bin/env python3

import argparse

# Our parser object
parser = argparse.ArgumentParser(description="Refreshing argparse module")

# Arguments the parser object can expect
parser.add_argument('--git-tag', help="Clone the repo and build from a Git tag")
parser.add_argument('--git-commit', help="Clone the repo and build from a Git commit")

# The arguments and the corresponding values are stored in the namespace `parser.parse_args()`
print(parser.parse_args())

