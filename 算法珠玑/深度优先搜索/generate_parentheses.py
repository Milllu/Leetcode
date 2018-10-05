"""
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def dfs(dic, str, n, l):
            
            if l < 0:
                return 
            
            if len(str) == n*2:
                if str not in result:
                    result.append(str)
                return 
        
            for p in dic:
                if dic[p] <= 0:
                    continue
                dic[p] -= 1
                dfs(dic, str+p, n, l-1 if p == ')' else l+1)
                dic[p] += 1
        
        
        dic = {'(': n-1, ')': n}
        result = []
        dfs(dic, '(', n, 1)
        return result