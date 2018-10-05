"""

根据百度百科，生命游戏，简称为生命，是英国数学家约翰·何顿·康威在1970年发明的细胞自动机。

给定一个包含 m × n 个格子的面板，每一个格子都可以看成是一个细胞。每个细胞具有一个初始状态 live（1）即为活细胞， 或 dead（0）即为死细胞。每个细胞与其八个相邻位置（水平，垂直，对角线）的细胞都遵循以下四条生存定律：

如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；
如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活；
如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
如果死细胞周围正好有三个活细胞，则该位置死细胞复活；
根据当前状态，写一个函数来计算面板上细胞的下一个（一次更新后的）状态。下一个状态是通过将上述规则同时应用于当前状态下的每个细胞所形成的，其中细胞的出生和死亡是同时发生的。

示例:

输入: 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
输出: 
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
进阶:

你可以使用原地算法解决本题吗？请注意，面板上所有格子需要同时被更新：你不能先更新某些格子，然后使用它们的更新后的值再更新其他格子。
本题中，我们使用二维数组来表示面板。原则上，面板是无限的，但当活细胞侵占了面板边界时会造成问题。你将如何解决这些问题？
"""

class Solution(object):
    def gameOfLife(self, matrix):
        """
        第一次遍历将符合改变的细胞换一种编码, 本身1死亡 -> 'd; 本身0复活 -> 'r'
        """
        self.m, self.n = len(matrix), len(matrix[0])
        for y in range(self.m):
            for x in range(self.n):
                a = self.is_survive(matrix, x, y)
                cur = matrix[y][x]
                if cur == 1 and (a < 2 or a > 3):
                    matrix[y][x] = 'd'
                if cur == 0 and a == 3:
                    matrix[y][x] = 'r'

        for y in range(self.m):
            for x in range(self.n):
                if matrix[y][x] == 'd':
                    matrix[y][x] = 0
                if matrix[y][x] == 'r':
                    matrix[y][x] = 1
        
    def is_survive(self, matrix, x, y):
        a = 0
        for m in [y-1, y, y+1]:
            for n in [x-1, x, x+1]:
                if m >= 0 and n >= 0 and m < self.m and n < self.n and (m, n) != (y, x):
                    if matrix[m][n] == 1 or matrix[m][n] == 'd':
                        a += 1
        return a