#!/usr/bin/env python3

import argparse

arg_parser = argparse.ArgumentParser(
    description="Checkout Git repos based on branch, tag, or commit id"
)

arg_parser.add_argument(
    "--git-repo",
    help="Checkout the Git repo",
    default="https://github.com/arvimal/Daisho",
)

# First mutually exclusive group (Required)
group_one = arg_parser.add_mutually_exclusive_group(required=True)
group_one.add_argument(
    "--git-tag", help="Fetch a git repo based on tag or branch", dest="da_tag"
)
group_one.add_argument(
    "--git-commit", help="Checkout a git repo based on commit id", dest="da_commit"
)

# Second mutually exclusive group ()
group_two = arg_parser.add_mutually_exclusive_group()
group_two.add_argument(
    "--deploy-vm",
    help="Build a virtual machine, from a filesystem tarball available locally",
    nargs="?",
)
group_two.add_argument(
    "--deploy-vm-remote",
    help="Build a virtual machine, from a tarball hosted on Artifactory",
    nargs="?",
)
group_two.add_argument("--delete-vm", help="Delete a deployed VM", nargs="?")
group_two.add_argument("--delete-vm-host", help="Delete a deployed VM", nargs="?")
group_two.add_argument(
    "--upload", help="Upload the archive file to Artifactory", action="store_true"
)
group_two.add_argument(
    "--generate-test-rpm", help="Build and upload the test rpm", action="store_true"
)

# Optional arguments
arg_parser.add_argument(
    "--verbose",
    help="Add verbosity to the ansible playbook execution",
    action="store_true",
)
arg_parser.add_argument(
    "--debug", help='Do not skip tasks tagged with "debug"', action="store_true"
)
arg_parser.add_argument(
    "--pause", help='Do not skip tasks tagged with "pause"', action="store_true"
)
arg_parser.add_argument(
    "--cleanup", help='Only run tasks tagged with "cleanup"', action="store_true"
)
arg_parser.add_argument(
    "--tags", help="Space separated list of tags to run", nargs="+", default=[]
)
arg_parser.add_argument(
    "--skip-tags", help="Space separated list of tags to skip", nargs="+", default=[]
)
arg_parser.add_argument(
    "--build-id",
    help="Add a build ID to the archive when triggered by a build system",
    required=True,
    nargs="?",
)


arguments = arg_parser.parse_args()

print("\nNewly defined namespace: {}\n".format(arg_parser.parse_args()))

if arguments.da_commit:
    print("The commit ID: {}\n".format(arguments.da_commit))
    # git clone -n repo
    # git checkout <commit_id>
elif arguments.da_tag:
    print("The repo tag: {}\n".format(arguments.da_tag))
    # git clone repo:branch

# cd repo
#
