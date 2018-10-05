"""
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:

输入: "race a car"
输出: false
"""
class Solution(object):
    def isPalindrome(self, s):
        """
        设置左右指针, 进行比较
        """
        if not s:
            return True
        
        l, r = 0, len(s) - 1
        while l < r:
            # 值非数字或字母则移动
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue
            # 值为字母则转变成同一大小格式
            v1 = s[l].upper() if not s[l].isdigit() else s[l]
            v2 = s[r].upper() if not s[r].isdigit() else s[r]
            
            if v1 != v2:
                return False
            l, r = l + 1, r - 1
        return True