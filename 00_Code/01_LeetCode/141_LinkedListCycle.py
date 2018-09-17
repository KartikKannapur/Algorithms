""""
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        """
        Method 1: Using a hash set

        * As we traverse over each item in a linked list,
        we add that to a set.
        * Each time, we check if the item is already present
        in the set or not. If it is then we can safely
        say that a loop exists in the Linked List.

        Your runtime beats 35.51 % of python submissions
        """
        #         s = set()
        #         current_ptr = head

        #         while current_ptr:
        #             if current_ptr in s:
        #                 return True
        #             else:
        #                 s.add(current_ptr)
        #                 current_ptr = current_ptr.next
        #         return False


        """
        Method 2:
        Using a fast and slow pointer
        If a cycle exists, then the fast and slow pointer
        will eventually meet

        Your runtime beats 97.46 % of python submissions.
        """
        slow_ptr = head
        fast_ptr = head

        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

            if slow_ptr == fast_ptr:
                return True

        return False

