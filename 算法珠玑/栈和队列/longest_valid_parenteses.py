"""
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:

输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"
示例 2:

输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"
"""
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack, longest = [0], 0
        
        for e in s:
            if e == '(':
                stack.append(0)  
            else:
                if len(stack) >= 2:
                    v = stack.pop()
                    stack[-1] += v + 2
                    longest = max(longest, stack[-1])
                else:
                    stack = [0]
        return longest
                    