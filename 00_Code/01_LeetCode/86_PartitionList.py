"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """

        """
        Method 1: Two Pointers
        In my opinion, this is one of the most beautiful approaches.

        The key is to maintain two pointers:
        head1 = list1 = ListNode(0)
        head2 = list2 = ListNode(0)

        At each stage check the val of head and assign the pointer

        Your runtime beats 52.99 % of python submissions.
        """

        if not head:
            return []

        head1 = list1 = ListNode(0)
        head2 = list2 = ListNode(0)

        while head:
            if head.val < x:
                list1.next = head
                list1 = list1.next
            else:
                list2.next = head
                list2 = list2.next
            head = head.next

        list2.next = None
        list1.next = head2.next

        return head1.next