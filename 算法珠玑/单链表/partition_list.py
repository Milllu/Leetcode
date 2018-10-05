"""

给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。

你应当保留两个分区中每个节点的初始相对位置。

示例:

输入: head = 1->4->3->2->5->2, x = 3
输出: 1->2->2->4->3->5
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        chain_lt1 = chain_lt2 = ListNode(0)
        chain_rt1 = chain_rt2 = ListNode(0)
        
        while head:
            # 小于x链接左链条, 反之链接右链条
            if head.val < x:
                chain_lt2.next = head
                chain_lt2 = chain_lt2.next
            else:
                chain_rt2.next = head
                chain_rt2 = chain_rt2.next
            head = head.next
        # 左链条尾部链接右链条头部
        chain_lt2.next = chain_rt1.next
        chain_rt2.next = None
        return chain_lt1.next