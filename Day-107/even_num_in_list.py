#!/usr/bin/env python3
# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/submissions/

"""
1295. Find Numbers with Even Number of Digits - Easy

# Given an array nums of integers, return how many of them contain an even number of digits.

# Example 1:

Input: nums = [12,345,2,6,7896]
Output: 2
# Explanation:
    12 contains 2 digits (even number of digits).
    345 contains 3 digits (odd number of digits).
    2 contains 1 digit (odd number of digits).
    6 contains 1 digit (odd number of digits).
    7896 contains 4 digits (even number of digits).
    Therefore only 12 and 7896 contain an even number of digits.
# Example 2:

Input: nums = [555,901,482,1771]
Output: 1
# Explanation:
Only 1771 contains an even number of digits.

#Constraints:

1 <= nums.length <= 500
1 <= nums[i] <= 10^5
"""

class Solution:
    def findNumbers(self, nums):
        even_num = []
        if len(nums) < 1 and len(nums) >= 500:
            print("The list does not meet the constraints!")
        else:
            for i in nums:
                if len(str(i)) % 2 == 0:
                    even_num.append(i)
                else:
                    pass
        print(even_num)
        return len(even_num)


test = Solution()
test.findNumbers([12, 345, 2, 6, 7896])
