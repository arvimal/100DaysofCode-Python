#!/usr/bin/env python3
# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/submissions/

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
