"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true
"""
class Solution(object):
    def isValid(self, s):
        
        dic = {')': '(', ']': '[', '}': '{'}
        stack = []
    
        for i in s:
            # 右括号时取栈顶对比, 栈为空或栈顶值与右括号不匹配, 返回False
            if i in {'}', ']', ')'}:
                if not stack or stack.pop() != dic[i]:
                    return False
            # 左括号是存入栈
            else:
                stack.append(i)
        # 栈为空则全部匹配, 返回True, 反之亦然
        return False if stack else True
