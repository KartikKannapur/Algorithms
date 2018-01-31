"""
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.
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
        """
        Method 1:
        Step 1. Identify the middle node in the linked list
        Step 2. Create two head nodes
        Step 3. Reverse the second half of the linked list
        Step 4. Iterate through both these linked lists alternatively


        Your runtime beats 95.12 % of python submissions.
        """
        if not head:
            return

        # #Step 1. Identify the middle node in the linked list
        slow_ptr = fast_ptr = head
        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        # #Step 2. Create two head nodes
        head1 = head
        head2 = slow_ptr.next

        # #Step 3. Reverse the second half of the linked list
        slow_ptr.next = None
        prev_ptr = None
        current_ptr = head2

        while current_ptr:
            next_ptr = current_ptr.next
            current_ptr.next = prev_ptr
            prev_ptr = current_ptr
            current_ptr = next_ptr

        head2 = prev_ptr

        # #Step 4. Iterate through both these linked lists alternatively
        while head2:
            next1 = head1.next
            next2 = head2.next

            head1.next = head2
            head2.next = next1

            head1 = next1
            head2 = next2

