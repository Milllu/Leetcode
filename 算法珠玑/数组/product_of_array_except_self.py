"""
给定长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。

示例:

输入: [1,2,3,4]
输出: [24,12,8,6]
说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。
"""

from functools import reduce
class Solution(object):
    def productExceptSelf(self, nums):
        """
        思路: 当前元素左右乘积和相乘, 得到除当前元素的乘积和
        """
        l1, l2 = [1], [1]
        pro = lambda a, b: a * b
        for i in range(1, len(nums)):
            j = -i - 1
            l1.append(l1[-1]*nums[i-1])
            l2.append(l2[-1]*nums[j+1])
            
        l = []
        for x, y in zip(l1, l2[::-1]):
            l.append(x*y)
        return l
            