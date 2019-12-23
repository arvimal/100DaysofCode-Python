#!/usr/bin/env python3

# Leetcode problem 66: https://leetcode.com/problems/plus-one/

"""
66. Plus One
    Given a non-empty array of digits representing a non-negative integer,
    plus one to the integer.

    The digits are stored such that the most significant digit is at the head of the list,
    and each element in the array contain a single digit.

    You may assume the integer does not contain any leading zero, except the number 0 itself.

    Example 1:

    Input: [1,2,3]
    Output: [1,2,4]
    Explanation: The array represents the integer 123.
    Example 2:

    Input: [4,3,2,1]
    Output: [4,3,2,2]
    Explanation: The array represents the integer 4321.
    """

class Solution:


    def plusOne(self, digits):
        whole_num = ""
        new_list = []
        if len(digits) == 0:
            pass
        else:
            for i in digits:
                whole_num += str(i)
            new_num = int(whole_num) + 1
            # print(list((str(new_num))))
            for i in list(str(new_num)):
                new_list.append(int(i))
            print(new_list)
            return new_list



Test = Solution()
Test.plusOne([1,2,3])