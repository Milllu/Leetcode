"""
输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
说明：

所有输入均为小写字母。
不考虑答案输出的顺序。
"""
class Solution(object):
    def groupAnagrams(self, strs):
        dic = {}
        # 排序元素作为key, 如果元素排序后与存在字典中, 则作为value存入
        for str in strs:
            temp = ''.join(sorted(str))
            dic[temp] = dic.get(temp, []) + [str]
            
        return list(dic.values())