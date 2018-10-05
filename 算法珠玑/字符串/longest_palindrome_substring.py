"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba"也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"
"""
class Solution(object):
    def longestPalindrome(self, s):
        longest = ''
        for i in range(len(s)):
            # 奇数长度的回文字符串
            tmp = self.palinds(s, i, i)
            longest = tmp if len(tmp) > len(longest) else longest
            # 偶数长度的回文字符串
            tmp = self.palinds(s, i, i+1)
            longest = tmp if len(tmp) > len(longest) else longest
        return longest
    
    def palinds(self, s, i, j):
        # 向左右扫描, 返回回文区间
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        return s[i+1:j]
        