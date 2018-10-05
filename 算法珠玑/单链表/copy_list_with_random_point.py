"""

给定一个链表，每个节点包含一个额外增加的随机指针，该指针可以指向链表中的任何节点或空节点。

要求返回这个链表的深度拷贝。
"""
# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        dummy = dummy2 = RandomListNode(0)
        
        while head:
            val = head.random 
            # 复制node.labe 和 node.random
            node = RandomListNode(head.label)
            node.random = RandomListNode(val.label) if val is not None else None
            
            dummy2.next = node
            dummy2 = node
            head = head.next
        return dummy.next