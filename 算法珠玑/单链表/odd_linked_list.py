"""
给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。

请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。

示例 1:

输入: 1->2->3->4->5->NULL
输出: 1->3->5->2->4->NULL
示例 2:

输入: 2->1->3->5->6->4->7->NULL 
输出: 2->3->6->7->1->5->4->NULL
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = odd = ListNode(0)
        even_head = even_tail = ListNode(0)
        while head:
            # 奇偶链条连接各自奇点, 偶点
            odd.next = head
            even_tail.next = head.next
            # 链条调整至末尾
            odd = odd.next
            even_tail = even_tail.next
            
            head = head.next.next if even_tail else None
        odd.next = even_head.next
        return dummy.next
            