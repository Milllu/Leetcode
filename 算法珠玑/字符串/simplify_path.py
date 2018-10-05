"""

给定一个文档 (Unix-style) 的完全路径，请进行路径简化。

例如，
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"

边界情况:

你是否考虑了 路径 = "/../" 的情况？
在这种情况下，你需返回 "/" 。
此外，路径中也可能包含多个斜杠 '/' ，如 "/home//foo/" 。
在这种情况下，你可忽略多余的斜杠，返回 "/home/foo" 。
"""
class Solution(object):
    def simplifyPath(self, strs):
        # 以'/'为分割分割
        L = strs.split('/')
        path = []
        for l in L:
            # '.'表示当前路径, 不添加到新路径列表L中
            if l in ('.', ''):
                continue
            # '..'表示返回上级路径, 删除L中末尾
            elif l == '..':
                if path:
                    path.pop()
            # 添加路径到L
            else:
                path.append(l)
        # 路径重组
        return '/' + '/'.join(path)
            