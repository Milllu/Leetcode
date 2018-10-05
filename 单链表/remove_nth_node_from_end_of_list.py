# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。

进阶：

你能尝试使用一趟扫描实现吗？
"""
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        两个指针, 当i大于n时, 有一个指针开始移动
        """
        i, cur, cur2 = 0, head, head
        while cur:
            i += 1
            if i > n:
                pre, cur2 = cur2, cur2.next
            cur = cur.next
            
        if i == n:
            return head.next
        pre.next = cur2.next
        return head