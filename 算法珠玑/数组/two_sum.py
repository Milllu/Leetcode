"""
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。

你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""
class Solution:
    def twoSum(self, nums, target):
        """
        O(n**2)会超时,选择哈希表
        """
        d = {}
        for k, v in enumerate(nums):
            # 有相同元素则和target进行判定
            if v in d and v*2 == target:
                return [d[v], k]
            else:
                d[v] = k

        # 遍历每一元素进行判定     
        for i in d:
            if target-i in d:
                return [d[i], d[target-i]]
        return []
            