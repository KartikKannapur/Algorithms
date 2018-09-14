"""
Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node with value 3, the linked list should become 1 -> 2 -> 4 after calling your function.

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        """
        Method 1:

        * Traverse through the LinkedList, by constantly
        checking the value of the next element.
        * If the next element is equal to the value of
        the node given, double jump the pointer
        * Assign the val and node to the next.next pointer

        Your runtime beats 94.15 % of python3 submissions.
        """
        node.val = node.next.val
        node.next = node.next.next