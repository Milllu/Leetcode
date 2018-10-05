"""

给定一个二叉树，返回它的 后序 遍历。

示例:

输入: [1,null,2,3]  
   1
    \
     2
    /
   3 

输出: [3,2,1]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        rt = [] 
        queue = [[root, 0]]
        while queue:
            node = queue.pop()
            if node[0]:
                if node[1] == 1:
                    rt.append(node[0].val)
                else:
                    queue.append([node[0], node[1]+1])
                    queue.append([node[0].right, 0])    
                    queue.append([node[0].left, 0])
        return rt