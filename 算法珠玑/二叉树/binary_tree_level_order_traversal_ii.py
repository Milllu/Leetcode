"""
给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        rt = []
        queue = [root]
        while queue:
            queue, rt_level = self.getNextLevel(queue, [], [])
            rt.append(rt_level) if rt_level else None 
        return rt[::-1]
    
    def getNextLevel(self, queue, next_queue, rt_level):
        
        while queue:
            node = queue.pop(0)
            if node:
                rt_level.append(node.val)
                next_queue.append(node.left)
                next_queue.append(node.right)
                
        return next_queue, rt_level
            
            