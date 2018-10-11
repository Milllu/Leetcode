"""
给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

示例 1:

输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]
示例 2:

输入:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
输出: [1,2,3,4,8,12,11,10,9,5,6,7]
"""

class Solution(object):
    """
    取矩阵第一行，矩阵一行以外作为新矩阵, 
    在左旋转90度，循环直至矩阵为空
    """
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        while matrix and matrix[0]:
            result, matrix = self.delline(matrix, result)
            if matrix and matrix[0]:
                matrix = self.overturn(matrix)
        return result

    def delline(self, matrix, result):
        result.extend(matrix[0])
        matrix = matrix[1:]
        return result, matrix

    def overturn(self, matrix):
        m, n = len(matrix), len(matrix[0])
        new_matrix = [[0 for j in range(m)] for i in range(n)]
        
        for i in range(m):
            for j in range(n):
                new_matrix[j][i] = matrix[i][j]

        return new_matrix[::-1]


if __name__ == '__main__':
    matrix = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]

    s = Solution()
    print(s.spiralOrder(matrix))



