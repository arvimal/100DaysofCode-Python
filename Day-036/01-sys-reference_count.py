#!/usr/bin/env python3

# The `sys.getrefcount()` method counts the number of
# references to an object, in the current namespace.
# Once the reference count reaches zero, the object
# can be scheduled for garbage collection.

import sys

print("\nCreating a new list, `list_1`")
list_1 = list(range(1, 10))
print(f"list_1: {list_1}")
# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print(f"Reference count of `list_1`: {sys.getrefcount(list_1)}")

print("\nAssigning a new reference (list_2) to `list_1`")
list_2 = list_1
print(f"Reference count of `list_1`: {sys.getrefcount(list_1)}")

print("\nAssigning a new reference (list_3) to `list_1`")
list_3 = list_1
print(f"Reference count of `list_1`: {sys.getrefcount(list_1)}")

print("\nDeleting reference lists, list_2 and list_3")
del list_2
del list_3

print(f"Reference count of `list_1`: {sys.getrefcount(list_1)}")
