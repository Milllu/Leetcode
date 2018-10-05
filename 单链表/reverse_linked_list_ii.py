"""

反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤ m ≤ n ≤ 链表长度。

示例:

输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        
        for i in range(m-1):
            pre = pre.next
        
        # 反转[m, n]区间的节点
        reverse = None
        cur = pre.next
        for i in range(n-m+1):
            next_node = cur.next
            cur.next = reverse
            reverse = cur
            cur = next_node
        pre.next.next = cur
        pre.next = reverse
        return dummy.next