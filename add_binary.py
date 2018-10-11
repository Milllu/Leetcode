"""

给定两个二进制字符串，返回他们的和（用二进制表示）。

输入为非空字符串且只包含数字 1 和 0。

示例 1:

输入: a = "11", b = "1"
输出: "100"
示例 2:

输入: a = "1010", b = "1011"
输出: "10101"
"""
class Solution(object):
    def addBinary(self, a, b):
        # a为空返回b, b同
        if not a:
            return b
        if not b:
            return a
        # 倒序遍历, 余值保留, 商值进位
        na, nb = len(a) - 1, len(b) - 1
        val = 0; res = ''
        while na >= 0 or nb >= 0:
            if na >= 0:
                val += int(a[na])
            if nb >= 0:
                val += int(b[nb])
            res = str(val%2) + res
            val = val // 2
            na, nb = na - 1, nb - 1
           
        res = str(val) + res
        return str(int(res))
                