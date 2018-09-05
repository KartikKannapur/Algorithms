"""
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        """
        Method 1:
        Initialize the couters to zero.
        Get the lenghts of the two linked lists - headA and headB

        Depending upon which linked list is longer, move that many
        differences further.

        When tempA == tempB: return tempA

        Your runtime beats 88.65 % of python submissions.

        ----
        Other Approaches:
        1. Use a hash table to store node addresses and check for 
        intersection.
        """
        # #Initialize the couters to zero.
        c1 = c2 = 0

        # #Get the lenghts of the two linked lists - headA and headB
        temp = headA
        while temp:
            c1 += 1
            temp = temp.next

        temp = headB
        while temp:
            c2 += 1
            temp = temp.next

        # #Depending upon which linked list is longer, move that many
        # #differences further.
        tempA = headA
        tempB = headB
        if c1 > c2:
            for i in range(c1 - c2):
                tempA = tempA.next
        elif c2 > c1:
            for i in range(c2 - c1):
                tempB = tempB.next

        # #When tempA == tempB: return tempA
        while tempB != tempA:
            tempB = tempB.next
            tempA = tempA.next
        return tempA