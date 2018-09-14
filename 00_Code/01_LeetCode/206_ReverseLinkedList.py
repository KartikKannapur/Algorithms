"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?


"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        """
        Standard Method - Iterative

        * Assign prev_ptr to None
        * Assign current_ptr to head

        * We only care about the current_ptr, therefore
        run a while loop as long as current_ptr exists
        prev_ptr --> current_ptr --> next_ptr

        * next_ptr = current_ptr.next
        * Now, reassign current_ptr to prev_ptr

        * Since we have reversed a subsection of the 
        linked list, we move the pointers by 1
        prev_ptr = current_ptr
        current_ptr = next_ptr

        * At the end of traversing the linked list,
        the prev_ptr has reached the final node OR
        the head node in the reversed order, therefore
        we return the prev_ptr node

        Your runtime beats 99.94 % of python3 submissions.
        """
        prev_ptr = None
        current_ptr = head

        while current_ptr:
            next_ptr = current_ptr.next
            current_ptr.next = prev_ptr
            prev_ptr = current_ptr
            current_ptr = next_ptr

        return prev_ptr

        """
        Method 2 - Recursion

        * Define a custom recursive function
        """

        def reverse(current_ptr, prev_ptr=None):
            if not current_ptr:
                return prev_ptr

            # #Same two lines as in the iterative case
            next_ptr = current_ptr.next
            current_ptr.next = prev_ptr

            # #Same as the two lines in the iterative case
            # #we only move the pointers by calling the
            # #recursive function
            return reverse(next_ptr, current_ptr)

        return reverse(head)

