"""

给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

返回 s 所有可能的分割方案。

示例:

输入: "aab"
输出:
[
  ["aa","b"],
  ["a","a","b"]
]
"""
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.rt = []
        self.dfs(s, [])
        return self.rt 
    
    def dfs(self, str, lst):
        
        if len(str) == 0:
            self.rt.append(lst)
            return 
        
        for i in range(len(str)):
            if str[:i+1] == str[:i+1][::-1]:
                self.dfs(str[i+1:], lst+[str[:i+1]])
            
