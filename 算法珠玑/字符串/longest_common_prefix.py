"""

编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
"""
class Solution(object):
    def longestCommonPrefix(self, s):
        """
        从位置零遍历, 直到各个元素的索引值不同, 返回res
        """
        res = ''
        for i in zip(*s):
            str = ''.join(i)
            if str == len(str) * str[0]:
                res += str[0]
            else:
                break
        return res