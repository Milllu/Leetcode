"""
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:

输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.rt = []
        self.traversal(list(range(1, n+1)),0, k, [])
        return self.rt
        
    def traversal(self, nums, i, k, lst):
        if k == 0:
            self.rt.append(lst)
            return 
        
        for j in range(i, len(nums)):
            self.traversal(nums, j+1, k-1, lst+[nums[j]])