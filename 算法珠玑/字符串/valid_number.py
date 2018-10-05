"""
验证给定的字符串是否为数字。

例如:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true

说明: 我们有意将问题陈述地比较模糊。在实现代码之前，你应当事先思考所有可能的情况。

更新于 2015-02-10:
C++函数的形式已经更新了。如果你仍然看见你的函数接收 const char * 类型的参数，请点击重载按钮重置你的代码。
"""
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        state = [
            {},
            {'blank': 1, 'sign': 2, 'digit': 3, '.': 4},  # 1.开始
            {'digit': 3, '.': 4},                         # 2.加减号后跟数字或小数点
            {'digit': 3, '.': 5, 'e': 6, 'blank': 9},     # 3.数字后面跟数字/小数点/自然数e/空
            {'digit': 5},                                 # 4.第一位为小数点,后跟数字
            {'digit': 5, 'e': 6, 'blank': 9},             # 5.前为 数字-小数点, 后跟数字/自然数e/空
            {'sign': 7, 'digit': 8},     # 6.前为 自然数e, 后跟数字
            {'digit': 8},       # 7.前为 自然数e后的sign, 后跟数字
            {'digit': 8, 'blank': 9},       # 8.前为 数字/e/数字, 后跟数字或空
            {'blank': 9}        # 9.空
        ]
        currentState = 1
        for c in s:
            if c >= '0' and c <= '9':
                c = 'digit'
            if c == ' ':
                c = 'blank'
            if c in ['+', '-']:
                c = 'sign'
            if c not in state[currentState].keys():
                return False
            currentState = state[currentState][c]
        if currentState not in [3,5,8,9]:
            return False
        return True