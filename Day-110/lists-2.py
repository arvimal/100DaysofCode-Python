#!/usr/bin/env python3

# Create a function named remove_middle which has three parameters named
# lst, start, and end. The function should return a list where all elements
# in lst with an index between start and end(inclusive) have been removed.

def remove_middle(lst, start, end):
  return lst[:start] + lst[end+1:]

print(remove_middle([9, 7, 3, 10, 2, 4], 1, 2))
