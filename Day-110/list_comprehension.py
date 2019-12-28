#!/usr/bin/env python3

# Return a list
# The element at the index should be multiplied by 2
# Rest of the elements should be the same.


def double_index(lst, index):
  if index > len(lst):
    return lst
  else:
    return([n for n in lst[:index]] + [2 * lst[index]] + [n for n in lst[index + 1:]])


print(double_index([3, 8, -10, 12], 2))

