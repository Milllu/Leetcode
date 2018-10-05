"""

找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。

说明：

所有数字都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: k = 3, n = 7
输出: [[1,2,4]]
示例 2:

输入: k = 3, n = 9
输出: [[1,2,6], [1,3,5], [2,3,4]]
"""
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def dfs(dic, target, lst, suml, k):
            
            if suml == target and len(lst) == k:
                result.append(lst)
                return
            if suml >= target:
                return
                
            for key in dic:
                if dic[key] > 0 and (not lst or lst and key > lst[-1]):
                    dic[key] -= 1
                    dfs(dic, target, lst+[key], suml+key, k)
                    dic[key] += 1
                
        dic = {i: 1 for i in range(1, 10)}          
        result = []
        dfs(dic, n, [], 0, k)
        return result
        