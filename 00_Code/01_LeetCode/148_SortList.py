"""
Sort a linked list in O(n log n) time using constant space complexity.


"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        """
        Method 1: Merge Sort
        """

        def merge(h1, h2):
            dummy = tail = ListNode(None)
            while h1 and h2:
                if h1.val < h2.val:
                    tail.next = h1
                    tail = h1
                    h1 = h1.next
                else:
                    tail.next = h2
                    tail = h2
                    h2 = h2.next

            tail.next = h1 or h2
            return dummy.next

        # #IF there are no elements in the Linked List
        if not head or not head.next:
            return head

        pre = None
        slow = head
        fast = head

        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        pre.next = None

        return merge(self.sortList(head), self.sortList(slow))