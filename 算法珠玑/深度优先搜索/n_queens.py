"""
给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。

每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

示例:

输入: 4
输出: [
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]
解释: 4 皇后问题存在两个不同的解法。
"""
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.result = []
        self.dfs(n, [])
        return [['.'*i + 'Q' + '.'*(n-i-1) for i in queens] for queens in self.result]
        
    def dfs(self, n, queens):

        if len(queens) == n:
            self.result.append(queens)
            return

        for i in range(n):
            if self.judement(queens, i):
                self.dfs(n, queens+[i])
                
    def judement(self, queens, x):
        
        y = len(queens)
        for y0 in range(len(queens)):
            if y == y0 or x == queens[y0] or abs(y-y0) == abs(x-queens[y0]):
                return False
        return True