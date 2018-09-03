"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        """
        Method 1: Using divmod()

        Your runtime beats 54.97 % of python submissions.
        """

        carry = 0
        dummy = new_list = ListNode(0)

        while l1 or l2 or carry:
            value1 = value2 = 0  # #To make sure there is no spill over
            if l1:
                value1 = l1.val
                l1 = l1.next
            if l2:
                value2 = l2.val
                l2 = l2.next

            carry, value_res = divmod(value1 + value2 + carry, 10)

            # #Creating a new Linked List in the reverse order
            new_list.next = ListNode(value_res)
            new_list = new_list.next
        return dummy.next