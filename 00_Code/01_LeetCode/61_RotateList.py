"""
Given a list, rotate the list to the right by k places, where k is non-negative.


Example:

Given 1->2->3->4->5->NULL and k = 2,

return 4->5->1->2->3->NULL.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        """
        Method 1: Iterative Function
        def rotateList logic works well
        Could be used for reference
        """
        #         if not head:
        #             return []

        #         if not head.next:
        #             return head

        #         def rotateList(head):
        #             dummy = current_ptr = ListNode(None)
        #             dummy.next = head
        #             current_ptr.next = head


        #             while current_ptr.next.next != None:
        #                 current_ptr = current_ptr.next

        #             last_ptr = current_ptr.next


        #             last_ptr.next = head
        #             current_ptr.next = None
        #             dummy.next = last_ptr
        #             return dummy.next

        #         for _ in range(k):
        #             head = rotateList(head)

        #         return head

        """
        Method 2: Iterative Function
        Works on the same logic as Method 1 with rotateTimes = k%length
        Your runtime beats 5.10 % of python submissions.
        """
        if not head:
            return []

        if not head.next:
            return head

        pointer = head
        length = 1

        while pointer.next:
            pointer = pointer.next
            length += 1

        rotateTimes = k % length

        if k == 0 or rotateTimes == 0:
            return head

        def rotateList(head):
            dummy = current_ptr = ListNode(None)
            dummy.next = head
            current_ptr.next = head

            while current_ptr.next.next != None:
                current_ptr = current_ptr.next

            last_ptr = current_ptr.next

            last_ptr.next = head
            current_ptr.next = None
            dummy.next = last_ptr
            return dummy.next

        for _ in range(rotateTimes):
            head = rotateList(head)

        return head