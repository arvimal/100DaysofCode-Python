
"""
* Initial submssion

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        num_list = []
        for num in str(n):
            num_list.append(int(num))
        sum_num = sum(num_list)
        prod_num = 1
        for i in num_list:
            prod_num = prod_num * i
        print(prod_num - sum_num)
        return prod_num - sum_num
"""

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        num_list = [int(num) for num in str(n)]
        sum_num = sum(num_list)
        prod_num = 1
        for i in num_list:
            prod_num *= i
        return prod_num - sum_num

Test = Solution()
Test.subtractProductAndSum(124)
Test.subtractProductAndSum(234)
Test.subtractProductAndSum(590)
