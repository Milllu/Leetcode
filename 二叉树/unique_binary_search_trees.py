"""
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

示例:

输入: 3
输出: 5
解释:
给定 n = 3, 一共有 5 种不同结构的二叉搜索树:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

"""
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.dic = {0:1, 1:1, 2:2}
        return self._numTrees(n)
        
    def _numTrees(self, n):
        
        if n not in self.dic:
            self.dic[n] = sum(self._numTrees(i-1)*self._numTrees(n-i) for i in range(1, n+1))

        return self.dic[n]
        