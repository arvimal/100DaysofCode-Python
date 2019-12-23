#!/usr/bin/env python3

"""
Given a non-empty array of digits, find the occurrence of each digit.

Example 1:
Input: [1, 2, 3, 2, 3, 5]
Output: {1: 1, 2: 2, 3: 2, 5: 1}
"""

def find_dupes(digits):
    num_dict = {}
    if len(digits) == 0:
        print("No data to work on.")
        exit()
    else:
        for num in digits:
            if num in digits.keys():


find_dupes([1,2,2,2,3,4,5])

