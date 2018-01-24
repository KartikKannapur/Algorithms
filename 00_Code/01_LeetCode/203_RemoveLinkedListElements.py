"""
Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5

Your runtime beats 70.63 % of python submissions.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        """
        Method 1:
        Your runtime beats 70.63 % of python submissions.

        starter.next = head
        var_node = starter

        while var_node
        """
        starter = ListNode(None)
        starter.next = head
        var_node = starter

        while var_node.next:
            if var_node.next.val == val:
                var_node.next = var_node.next.next
            else:
                var_node = var_node.next

        return starter.next
