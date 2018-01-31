"""
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        """
        Method 1:
        Your runtime beats 29.21 % of python submissions
        """
        def reverseLinkedList(head):
            prev_ptr = None
            current_ptr = head

            while current_ptr:
                next_ptr = current_ptr.next
                current_ptr.next = prev_ptr

                prev_ptr = current_ptr
                current_ptr = next_ptr

            head = prev_ptr
            return prev_ptr

        # #MAIN
        head = my_ptr_1 = reverseLinkedList(l1)
        my_ptr_2 = reverseLinkedList(l2)

        carry = 0
        dummy = current_ptr = ListNode(None)
        while my_ptr_1 or my_ptr_2 or carry:
            v1 = v2 = 0
            if my_ptr_1:
                v1 = my_ptr_1.val
                my_ptr_1 = my_ptr_1.next
            if my_ptr_2:
                v2 = my_ptr_2.val
                my_ptr_2 = my_ptr_2.next

            carry, val = divmod(v1 + v2 + carry, 10)
            current_ptr.next = ListNode(val)
            current_ptr = current_ptr.next
        return reverseLinkedList(dummy.next)

