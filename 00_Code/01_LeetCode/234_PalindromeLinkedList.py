# #Given a singly linked list, determine if it is a palindrome.

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

        main_ptr = head
        lead_ptr = head

        # #Finding the middle node
        while lead_ptr != None and lead_ptr.next != None:
            main_ptr = main_ptr.next
            lead_ptr = lead_ptr.next.next

        new_ptr = None

        # #Reverse the linked list
        while main_ptr != None:
            next_ptr = main_ptr.next
            main_ptr.next = new_ptr
            new_ptr = main_ptr
            main_ptr = next_ptr

        # #Compare
        while new_ptr:
            if new_ptr.val != head.val:
                return False
            new_ptr = new_ptr.next
            head = head.next
        return True

