#!/usr/bin/env python3

"""
The `import` statement is just a call to the
`__import__()` function.
"""

print("1. Importing `itertools` using the import statement!")
import itertools
print(itertools.__doc__)

print("\nDeleting `itertools` from the namespace!")
del itertools

print("\nImporting `itertools` using `__import__()`")
itertools = __import__("itertools")
print(itertools.__doc__)

