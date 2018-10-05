"""
报数序列是指一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 被读作  "one 1"  ("一个一") , 即 11。
11 被读作 "two 1s" ("两个一"）, 即 21。
21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。

给定一个正整数 n ，输出报数序列的第 n 项。

注意：整数顺序将表示为一个字符串。

示例 1:

输入: 1
输出: "1"
示例 2:

输入: 4
输出: "1211"
"""
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        rt = '1'
        # n-1次for循环得到n的报数序列
        for i in range(n-1):
            l = [rt[0]]
            # 获得当前整数的报数数据
            for r in rt[1:]:
                if r == l[-1][0]:
                    l[-1] += r
                else:
                    l.append(r)
            # 报数数据整合成整数序列,供下一个for循环使用
            rt = ''
            for v in l:
                rt += str(len(v)) + v[0]
        return rt
        