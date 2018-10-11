"""
判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。

上图是一个部分填充的有效的数独。

数独部分空格内已填入了数字，空白格用 '.' 表示。
示例 1:

输入:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
输出: true
"""

class Solution:
    def isValidSudoku(self, board):
        """
        分别进行横向, 纵向, 区块比较,进行判定
        """
        return self.is_row_valid(board) and \
               self.is_col_valid(board) and \
               self.is_board_valid(board)
    
    def is_row_valid(self, board):
        for row in board:
            if not self.is_until_valid(row):
                return False
        return True

    def is_col_valid(self, board):
        for col in zip(*board):
            if not self.is_until_valid(col):
                return False
        return True
    
    def is_board_valid(self, board):
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                seq = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
                if not self.is_until_valid(seq):
                    return False
        return True
    
    def is_until_valid(self, queue):
        seq = [i for i in queue if i != '.']
        return len(seq) == len(set(seq))