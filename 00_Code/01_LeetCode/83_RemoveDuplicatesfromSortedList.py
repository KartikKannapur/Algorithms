"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.

Your runtime beats 67.55 % of python submissions.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        """
        * Initialized the current_ptr to head
        * If the current_ptr and current_ptr.next have the same value
        then move the pointer by one more

        Your runtime beats 90.02 % of python3 submissions.
        """

        current_ptr = head

        while current_ptr:
            while current_ptr.next and (current_ptr.val == current_ptr.next.val):
                current_ptr.next = current_ptr.next.next
            current_ptr = current_ptr.next

        return head
