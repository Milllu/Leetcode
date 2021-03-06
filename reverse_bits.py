"""
颠倒给定的 32 位无符号整数的二进制位。

示例:

输入: 43261596
输出: 964176192
解释: 43261596 的二进制表示形式为 00000010100101000001111010011100 ，
     返回 964176192，其二进制表示形式为 00111001011110000010100101000000 。
进阶:
如果多次调用这个函数，你将如何优化你的算法？
"""
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        rt = ''
        while n > 0:
            rt += str(n % 2)
            n = n // 2
        k = 32 - len(rt)
        rt += '0' * (k if k > 0 else 0)
        return int(rt, 2)
