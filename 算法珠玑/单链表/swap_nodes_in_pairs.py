"""
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

示例:

给定 1->2->3->4, 你应该返回 2->1->4->3.
说明:

你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = new_head = ListNode(0)
        
        while head and head.next:
            # 分别指向当前节点和后一个节点
            next = head.next.next
            pre_node = head
            end_node = head.next
            # 交换前后节点
            end_node.next = pre_node
            new_head.next = end_node
            new_head = pre_node 

            head = next
            
        new_head.next = head if head else None
        return dummy.next