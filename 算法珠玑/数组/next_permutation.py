"""

实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须原地修改，只允许使用额外常数空间。

以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""
class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        non_increase = len(nums) - 1
        # 找到最长的非增长后缀
        while nums[non_increase] <= nums[non_increase-1] and non_increase-1 >= 0:
            non_increase -= 1
        # non_increase = 0则nums整体为非增长的
        if non_increase == 0:
            return self._reverse(nums, 0, len(nums)-1)
        # 寻找替换元素
        swap_a = non_increase - 1
        swap_b = 0
        for i in range(len(nums)-1, swap_a, -1):
            if nums[i] > nums[swap_a]:
                swap_b = i
                break
        # 交换swap_a和swap_b
        nums[swap_a], nums[swap_b] = nums[swap_b], nums[swap_a]
        # 反转非增长后缀
        self._reverse(nums, swap_a+1, len(nums)-1)

    def _reverse(self, nums, l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1