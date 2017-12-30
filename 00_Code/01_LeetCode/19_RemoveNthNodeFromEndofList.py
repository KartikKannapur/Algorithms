# #Given a linked list, remove the nth node from the end of list and return its head.
# #Given linked list: 1->2->3->4->5, and n = 2.
# #After removing the second node from the end, the linked list becomes 1->2->3->5.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # #Defining a starter node
        starter = ListNode(None)
        starter.next = head

        # #Defining a main pointer and a lead pointer
        main_ptr = starter
        lead_ptr = starter

        # #Lead pointer is ahead of the main pointer by n
        for _ in range(0, n):
            if lead_ptr.next:
                lead_ptr = lead_ptr.next
            else:
                return starter.next

        # #When the lead pointer reaches the end,
        # #the main pointer is at end-n
        while lead_ptr.next:
            lead_ptr = lead_ptr.next
            main_ptr = main_ptr.next

        # #Delete the reference to the next node
        main_ptr.next = main_ptr.next.next

        return starter.next