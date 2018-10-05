"""

给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

返回符合要求的最少分割次数。

示例:

输入: "aab"
输出: 1
解释: 进行一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。
"""
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == s[::-1]:
            return 0
        
        for i in range(len(s)):
            if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
                return 1
            
        ispal = [[False for j in range(len(s))] for i in range(len(s))]
        dp = list(range(len(s))) + [-1]
        for i in range(len(s)):
            for j in range(i, -1, -1):
                if s[i] == s[j] and (i-j <= 1 or ispal[i-1][j+1]):
                    ispal[i][j] = True
                    dp[i] = min(dp[i], dp[j-1]+1)
        return dp[len(s)-1]