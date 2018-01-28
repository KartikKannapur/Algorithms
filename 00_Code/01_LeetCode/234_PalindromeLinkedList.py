"""
Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        """
        Method 1:
        Using Stacks - O(n) compute O(n) size

        Add each element to the stack.
        Then compare head.val == stack.pop()
        IF the elements are unequal, then return False
        """

        """
        Method 2:
        Reverse hald the Linked List

        1. Finding the middle node
        2. Reverse the linked list
        3. Compare head and middle pointer

        Your runtime beats 81.07 % of python submissions.
        """

        main_ptr = head
        lead_ptr = head

        # #Finding the middle node
        while lead_ptr and lead_ptr.next:
            main_ptr = main_ptr.next
            lead_ptr = lead_ptr.next.next

        prev_ptr = None

        # #Reverse the linked list
        while main_ptr:
            next_ptr = main_ptr.next
            main_ptr.next = prev_ptr
            prev_ptr = main_ptr
            main_ptr = next_ptr

        # #NOW, prev_ptr is at the middle of the Linked List
        # #Compare
        while prev_ptr:
            if prev_ptr.val != head.val:
                return False
            prev_ptr = prev_ptr.next
            head = head.next
        return True

