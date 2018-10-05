"""
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]
示例 2:

输入: [-1,-100,3,99] 和 k = 2
输出: [3,99,-1,-100]
解释: 
向右旋转 1 步: [99,-1,-100,3]
向右旋转 2 步: [3,99,-1,-100]
"""
class Solution(object):
    def rotate(self, nums, k):
        """
        时间复杂度O(n), 空间复杂度O(1);
        整体反转后分为两段, 分别反转
        """
        if k == 0 or k % len(nums) == 0:
            return 
        k = k % len(nums)
        nums.reverse()
        self._run(nums, 0, k-1)
        self._run(nums, k, len(nums)-1)
        
    def _run(self, nums, l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1