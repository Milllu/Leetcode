"""

给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:

输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.rt = []
        self.traversal(nums, [])
        return self.rt
    
    def traversal(self, nums, lst):
        
        if len(nums) == 1:
            if lst + nums not in self.rt:
                self.rt.append(lst+nums)
            return 
        
        for i in range(len(nums)):
            self.traversal(nums[:i]+nums[i+1:], lst+[nums[i]])
        