"""
动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

示例 1:

输入: [2,3,2]
输出: 3
解释: 你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
示例 2:

输入: [1,2,3,1]
输出: 4
解释: 你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
     偷窃到的最
"""
class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def built(i, j):
            pre = end = 0
            for k in range(i, j):
                pre, end = end, max(end, pre+nums[k])
            return end
        
        n = len(nums)
        if n <= 0:
            return 0
        elif n <= 1:
            return nums[0]
        else:
            return max(built(0, n-1), built(1, n))