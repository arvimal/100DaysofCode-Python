#!/usr/bin/env python3

import os

print("Some use cases of the `os` module.\n")

print("Operating System type: {}".format(os.name))
print("Environment variables: {}".format(os.environ))
print("\nos.envrion returns a dict")
print("Hence, it is possible to retreive a specific value")
print("Calling os.environ['USER'] : {}".format(os.environ["USER"]))
print("os.environ(<KEY>) will error if KEY is not present")
print("Use os.printenv(KEY) in such cases")
print("Calling os.getenv('USER'): {}".format(os.getenv("USER")))
print("Get the current working directory, and change to another")
print("Current Working Directory: {}".format(os.getcwd()))
print("Changing workding directory, with os.chdir('<path>')")
os.chdir("/tmp/")
print("Current working directory: {}".format(os.getcwd()))
print("Create a single directory using os.mkdir(<path>)")
os.removedirs("/tmp/new_dir")
print("Creating /tmp/new_dir/")
os.mkdir("/tmp/new_dir")
print("Changing to the new dir")
os.chdir("/tmp/new_dir")
print("Where are we?: {}".format(os.getcwd()))
print("Creating multiple directory hierarchy using os.makedirs(<path/to/)")
print("Creating /tmp/new_dir/dir1/dir2/")
os.makedirs("/tmp/new_dir/dir1/dir2")
os.chdir("/tmp/new_dir/dir1/dir2")
print("Where are we?: {}".format(os.getcwd()))

