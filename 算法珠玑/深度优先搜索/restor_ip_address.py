"""

给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

示例:

输入: "25525511135"
输出: ["255.255.11.135", "255.255.111.35"]
"""
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) > 12:
            return []
        self.result = []
        self.dfs(s, [], 0)
        return map(lambda lst: '.'.join(lst), self.result)
    
        
    def dfs(self, s, queue, n):
        
        if s == '':
            if len(queue) == 4 and queue not in self.result:
                self.result.append(queue)
            return 
             
        for i in range(3):
            l, r = s[:i+1], s[i+1:]
            if int(l) > 255 or (len(l) > 1 and l[0] == '0'):
                continue
            self.dfs(r, queue+[l], n+len(l))

            