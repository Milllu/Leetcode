"""
给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在众数。

示例 1:

输入: [3,2,3]
输出: 3
示例 2:

输入: [2,2,1,1,1,2,2]
输出: 2
"""
class Solution(object):
    
    # 方法一, 字典存储元素出现频率, 空间复杂度O(n)
    def majorityElement(self, nums):
        dicti, n = {}, len(nums)//2
        for i in nums:
            dicti[i] = dicti.get(i, 0) + 1
            if dicti[i] > n:
                return i

    # 方法二, 时间复杂度O(nlogn), 排序后计数
    def majorityElement2(self, nums):
        return sorted(nums)[len(nums)//2]

    # 方法三, 时间复杂度O(n), 空间复杂度O(1)
    def majorityElement2(self, nums):
        """
        思路: 不同元素相抵消, 剩下的就是目标元素
        """
        c = 0
        for i in nums:
            if c == 0:
                c += 1
                element = i
            else:
                if element == i:
                    c += 1
                else:
                    c -= 1
        return element