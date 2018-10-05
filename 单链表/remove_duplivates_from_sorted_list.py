"""
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

示例 1:

输入: 1->1->2
输出: 1->2
示例 2:

输入: 1->1->2->3->3
输出: 1->2->3
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return 
        pre = head
        cur = head.next
        # 当前节点与前节点比较
        while cur:
            # 节点值相同则删除
            if cur.val == pre.val:
                pre.next = cur.next
            # 节点值不相同, 则前节点变为前节点的下一个节点
            else:
                pre = pre.next
            cur = cur.next
        return head