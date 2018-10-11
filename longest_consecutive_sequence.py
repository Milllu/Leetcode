"""
给定一个未排序的整数数组，找出最长连续序列的长度。

要求算法的时间复杂度为 O(n)。

示例:
输入: [100, 4, 200, 1, 3, 2]
输出: 4
解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。
"""

class Solution:
    def longestConsecutive(self, nums):
        """
        要求时间复杂度O(n), 选择哈希;
        对x - 1不存在的进行操作, 则元素总体只进行了一次检查, 时间复杂度O(n)
        """
        nums = set(nums)  # 剔除重复元素
        longest = 0
        for num in nums:
            if num - 1 not in nums:
                y = num + 1
                while y in nums:
                    y += 1
                longest = max(longest, y-num)
        return longest