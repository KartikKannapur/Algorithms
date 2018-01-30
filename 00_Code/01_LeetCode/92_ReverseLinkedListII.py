"""
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.
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

        """
        Method 1
        Your runtime beats 58.95 % of python submissions.
        """

        dummy = prev_ptr = ListNode(0)
        dummy.next = head

        for _ in range(m - 1):
            prev_ptr = prev_ptr.next

        current_ptr = prev_ptr.next

        prevv_ptr = None
        for _ in range(n - m + 1):
            next_ptr = current_ptr.next
            current_ptr.next = prevv_ptr
            prevv_ptr = current_ptr
            current_ptr = next_ptr

        prev_ptr.next.next = current_ptr
        prev_ptr.next = prevv_ptr
        return dummy.next
