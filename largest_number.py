"""

给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。

示例 1:

输入: [10,2]
输出: 210
示例 2:

输入: [3,30,34,5,9]
输出: 9534330
说明: 输出结果可能非常大，所以你需要返回一个字符串而不是整数。
"""
class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
    
        for i in range(len(nums)-1, -1, -1):
            
            mini = 0
            for j in range(1, i+1):
                mini = self.judgment(nums[mini], nums[j], mini, j)
            nums[mini], nums[i] = nums[i], nums[mini]
       
        return str(int(''.join(map(str, nums))))
        
        
    def judgment(self, a, b, i, j):
        a, b = str(a), str(b)
        if int(a+b) >= int(b+a):
            return j
        else:
            return i
