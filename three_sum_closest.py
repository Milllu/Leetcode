"""

给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
"""
class Solution:
    def threeSumClosest(self, nums, target):
        """
        时间复杂度O(n**2), 排序后左右加相比较,
        返回与目标值差值最小的值
        """
        if len(nums) < 3:
            return 
        anum = sum(nums[:3])
        diff = abs(target - anum)
        nums.sort()
        for i in range(len(nums)-2):
            # 去重
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                suml = nums[i] + nums[l] + nums[r]
                if suml == target:
                    return suml
                elif suml > target:
                    if suml - target < diff:
                        diff = suml - target
                        anum = suml
                    r -= 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                else:
                    if target - suml < diff:
                        diff = target - suml
                        anum = suml
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return anum