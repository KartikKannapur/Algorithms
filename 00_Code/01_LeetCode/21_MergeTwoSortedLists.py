"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

Your runtime beats 55.16 % of python submissions.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        """
        Method 1: Merge the LinkedLists Iteratively using
        a dummy variable
        We create a variable:
        dummy = current = ListNode(0)

        We start at the beginning of both the linked lists
        and compare the values. At each stage we alter the 
        pointer of l1, l2, current
        Your runtime beats 55.16 % of python submissions.
        """
        dummy = current = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        current.next = l1 or l2
        return dummy.next
