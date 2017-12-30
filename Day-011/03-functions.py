#!/usr/bin/env python3

# Functions

# 1. Passing arguments to a function
def my_func(name):
    print("Hello, {0}".format(name))
my_func("vimal")

def my_func_2(a, b):
    return a + b
add(10, 20)

# 2. Empty functions or Stubs
# pass is a null operation, and does nothing but
# terminates the function without errors
def my_empty_func():
    pass

# 3. Return values
# If not specifically mentioned, a function returns None.
def test(A, B):
    return A * B


