#!/usr/bin/env python3

"""
Cleanup the given list of strings, and print each string in
its own line
"""

love_maybe_lines = [
    "Always    ",
    "     in the middle of our bloodiest battles  ",
    "you lay down your arms",
    "           like flowering mines    ",
    "\n",
    "   to conquer me home.    ",
]

love_maybe_lines_stripped = []
for line in love_maybe_lines:
    new_line = line.strip()
    # If you need to remove the newline (\n) element
    # in the original list, use the following `if` statement.
    # if new_line != "":
    love_maybe_lines_stripped.append(new_line)

love_maybe_full = "\n".join(love_maybe_lines_stripped)
print(love_maybe_full)
