"""
给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例 1:

给定链表 1->2->3->4, 重新排列为 1->4->2->3.
示例 2:

给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return 
        fast = slow = head
        while fast and fast.next:
            fast = fast.next
            fast = fast.next
            pre_ = slow
            slow = slow.next
        pre_.next = None

        cur = None
        while slow:
            slow_next = slow.next
            slow.next = cur
            cur = slow
            slow = slow_next
        
        res = head
        while res:
            res_next = res.next
            cur_next = cur.next

            res.next = cur
            res = res.next
            res.next = res_next
            pre = res
            res = res.next
            cur = cur_next
        if cur is not None:
            pre.next = cur
