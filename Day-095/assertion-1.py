#!/usr/bin/env python3

"""
Write an assert statement that triggers an AssertionError
if the variables `eggs` and `bacon` contain strings that are the same as each other,
even if their cases are different.
(that is, 'hello' and 'hello' are considered the same,
and 'goodbye' and 'GOODbye' are also considered the same).
"""


def assert_test(eggs=None, bacon=None):
    first_word = eggs.lower()
    sec_word = bacon.lower()
    # 1. Raise AssertionError, if eggs NOT in bacon, or bacon NOT in eggs.
    assert (first_word in sec_word) or (sec_word in first_word), "Words not equal"


# First test - eggs IN bacon
assert_test("hello", "hello how are you?")

# Second test - eggs NOT in bacon
assert_test("who", "How are you?")
