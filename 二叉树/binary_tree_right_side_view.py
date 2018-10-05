"""

给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

示例:

输入: [1,2,3,null,5,null,4]
输出: [1, 3, 4]
解释:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        rt = []
        queue = [root]
        while queue:
            queue, rt_level = self.getNextLevel(queue, [], [])
            rt.append(rt_level[-1]) if rt_level else None 
        return rt
    
    def getNextLevel(self, queue, next_queue, rt_level):
        
        while queue:
            node = queue.pop(0)
            if node:
                rt_level.append(node.val)
                next_queue.append(node.left)
                next_queue.append(node.right)
                
        return next_queue, rt_level  