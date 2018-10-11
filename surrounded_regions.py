"""

给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。

找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。

示例:

X X X X
X O O X
X X O X
X O X X
运行你的函数后，矩阵变为：

X X X X
X X X X
X X X X
X O X X
解释:

被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
"""
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m = len(board)
        if not m:
            return 
        n = len(board[0])
        if not n:
            return 
        save = [(i, j) for i in range(m) for j in range(n) if i in (0, m-1) or j in (0, n-1)]
   
        while save:
            i, j = save.pop(0)
            if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                board[i][j] = 'V'
                save += [(i-1, j), (i+1, j), (i, j+1), (i, j-1)]

        for row in board:
            for k, v in enumerate(row):
                if v == 'V':
                    row[k] = 'O'
                else:
                    row[k] = 'X'
  