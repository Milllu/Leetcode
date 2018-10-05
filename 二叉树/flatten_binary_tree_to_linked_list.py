"""
给定一个二叉树，原地将它展开为链表。

例如，给定二叉树

    1
   / \
  2   5
 / \   \
3   4   6
将其展开为：

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return root
        dummy = TreeNode(0)
        for i in self.inorder(root, []):
            dummy.right = i
            dummy = dummy.right
            dummy.left = None
        return dummy.right
        
        
    def inorder(self, root, lst):
        if not root:
            return
        lst.append(root)
        self.inorder(root.left, lst)
        self.inorder(root.right, lst)
        return lst