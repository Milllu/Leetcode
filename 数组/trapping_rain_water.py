

"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。

示例:

输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6
"""
class Solution:
    def trap(self, height):
        """
        思路: 找到两遍柱子最高的,改柱子容纳雨水面积 -> min(max_left, max_right) - height
        """
        l1 = [0]
        l2 = [0]
        for i in range(1, len(height)):
            j = len(height) - 1 - i
            l1.append(max(l1[-1], height[i-1]))
            l2.append(max(l2[-1], height[j+1]))
        suml = 0
        for x, y, z in zip(l1, l2[::-1], height):
            suml += max(min(x, y) - z, 0)
        return suml