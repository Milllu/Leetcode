"""

实现一个二叉搜索树迭代器。你将使用二叉搜索树的根节点初始化迭代器。

调用 next() 将返回二叉搜索树中的下一个最小的数。

注意: next() 和hasNext() 操作的时间复杂度是O(1)，并使用 O(h) 内存，其中 h 是树的高度。

您是否在真实的面试环节中遇到过这道题目呢？  
"""
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = []
        self.inorder(root)
        self.i = 0
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.i < len(self.root)

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            self.i += 1
            return self.root[self.i-1]
        
    
    def inorder(self, nodes):
        if not nodes:
            return 
        self.inorder(nodes.left)
        self.root.append(nodes.val)
        self.inorder(nodes.right)

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())