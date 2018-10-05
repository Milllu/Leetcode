"""

合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from functools import reduce
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) < 1:
            return []
        if len(lists) < 2:
            return lists[0]
        
        return reduce(self.mergeTwoSortedLists, lists)
        
        
    def mergeTwoSortedLists(self, l1, l2):
        dummy = dummy2 = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                dummy2.next = l1
                dummy2 = dummy2.next
                l1 = l1.next
            else:
                dummy2.next = l2
                dummy2 = dummy2.next
                l2 = l2.next
        dummy2.next = l1 or l2
        return dummy.next