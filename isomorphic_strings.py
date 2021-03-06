"""
给定两个字符串 s 和 t，判断它们是否是同构的。

如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。

所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。

示例 1:

输入: s = "egg", t = "add"
输出: true
示例 2:

输入: s = "foo", t = "bar"
输出: false
"""
class Solution(object):
    def isIsomorphic(self, s1, s2):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return map(s1.find, s1) == map(s2.find, s2)
        
        
        
        
        