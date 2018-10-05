"""
给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的绝对值最大为 k。

示例 1:

输入: nums = [1,2,3,1], k = 3
输出: true
示例 2:

输入: nums = [1,0,1,1], k = 1
输出: true
示例 3:

输入: nums = [1,2,3,1,2,3], k = 2
输出: false
"""
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        字典存储元素和索引, 遍历元素进行判断
        """
        d = {}
        for i, v in enumerate(nums):
            if v not in d:
                d[v] = i
            else:
                a = abs(d[v] - i)
                # 元素相等, 索引差符合则返回True
                if a <= k:
                    return True
                # 索引差大于k, 替换d[v]值
                else:
                    d[v] = i
        return False