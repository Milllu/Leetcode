"""

给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: [1,2,2]
输出:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        self.rt = []
        self.traversal(nums, 0, len(nums), [])
        return self.rt
        
    def traversal(self, nums, i, j, res):
        if res not in self.rt:
            self.rt.append(res)
        if i >= j:
            return 

        for k in range(i, j):
            self.traversal(nums, k+1, j, res+[nums[k]])
            