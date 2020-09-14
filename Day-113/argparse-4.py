#!/usr/bin/env python3

import argparse

arg_parser = argparse.ArgumentParser(
    description="Checkout Git repos based on branch, tag, or commit id")

arg_parser.add_argument('--git-repo', help="Checkout the Git repo",
                        default="https://github.com/arvimal/Daisho")

git_group = arg_parser.add_mutually_exclusive_group(required=True)
git_group.add_argument(
    '--git-tag', help='Fetch a git repo based on tag or branch', dest="da_tag")
git_group.add_argument(
    '--git-commit', help="Checkout a git repo based on commit id", dest="da_commit")

# First test
argument_namespace = arg_parser.parse_args(['--git-tag', '2bd5s8r'])
print("First namespace: {}\n".format(argument_namespace))

# Second test
argument_namespace = arg_parser.parse_args(['--git-commit', 'RHEL82_v0.1'])
print("Second namespace: {}\n".format(argument_namespace))


if argument_namespace.da_commit:
    print("The commit ID: {}\n".format(argument_namespace.da_commit))
elif argument_namespace.da_tag:
    print("The repo tag: {}\n".format(argument_namespace.da_tag))
