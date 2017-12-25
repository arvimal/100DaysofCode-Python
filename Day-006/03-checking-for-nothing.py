#!/usr/bin/env python3

# In certain conditions, we may need to evaluate to False.
# Python has the keyword `False` for this.

# Empty data sets also amount to False
# Example : Empty string, empty dicts, empty lists etc.

empty_list = []
empty_dict = {}
empty_string = ""
nothing = None

# IMPORTANT NOTE:
# If you just use "if empty_list" or any other from the
# above, it will always amount to True
# This is because, in such a case, the `if` condition
# only tests for the existence of such a name in the namespace.

# Even if there is no string in `empty_string`,
# this will not print anything, since this is just a
# check if the name `empty_string` exits.
if empty_string:
    print("Empty string")

# This is an explicit check for an empty list, rather than
# the existence of a name called `empty_list`.
if empty_list == []:
    print("Empty list")

# This is an existence check, and not a content check.
if empty_dict:
    print("Empty dict")

