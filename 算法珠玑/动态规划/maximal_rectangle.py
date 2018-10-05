"""
给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。

示例:

输入:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
输出: 6
"""
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        matrix = [list(map(int, row)) for row in matrix]

        for i in range(len(matrix)-2, -1, -1):
            for j in range(len(matrix[0])):
                if matrix[i][j] and matrix[i+1][j]:
                    matrix[i][j] += matrix[i+1][j]
        rt = 0
        for row in matrix:
            for i in range(len(row)):
                j = i
                while j < len(row) and row[j]:
                    rt = max(rt, (j-i+1)*min(row[i:j+1]))
                    j += 1
        return rt