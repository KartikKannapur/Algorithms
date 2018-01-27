"""
Reverse a singly linked list.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        """
        Standard Method
        Your runtime beats 72.22 % of python submissions
        """
        prev_ptr = None
        current_ptr = head

        while current_ptr:
            next_ptr = current_ptr.next
            current_ptr.next = prev_ptr
            prev_ptr = current_ptr
            current_ptr = next_ptr

        head = prev_ptr

        return prev_ptr


