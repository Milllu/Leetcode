"""
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。
示例:

输入: [2,1,5,6,2,3]
输出: 10
"""
class Solution(object):
    def largestRectangleArea(self, height):
        """
        :type heights: List[int]
        :rtype: int
        """           
        if not height:
            return 0
        if len(height) == 1:
            return height[0]
        stack = []  # The bottom element in the stack is the lowest
        max_area = 0
        n = len(height)
        for i in range(n + 1):
            while stack and (i == n or height[stack[-1]] > height[i]):
                h = height[stack.pop()]
                if stack:
                    w = i - stack[-1] - 1
                else:
                    w = i
                max_area = max(max_area, int(h) * w)
            stack.append(i)
        return max_area
        