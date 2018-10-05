"""
给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回锯齿形层次遍历如下：

[
  [3],
  [20,9],
  [15,7]
]
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        i, rt, queue = 1, [], [root]
        
        while queue:
            queue, rt_level = self.nextLevel(queue, [], [])
            rt.append(rt_level if i%2 else rt_level[::-1]) if rt_level else None
            i += 1
        return rt 
            
    def nextLevel(self, queue, next_queue, rt_level):
        
        while queue:
            node = queue.pop(0)
            if node:
                next_queue.append(node.left)
                next_queue.append(node.right)
                rt_level.append(node.val)
                
        return next_queue, rt_level