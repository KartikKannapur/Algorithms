"""
Given a non-negative number represented as a singly linked list of digits, plus one to the number.
The digits are stored such that the most significant digit is at the head of the list.
Example:
Input:
1->2->3

Output:
1->2->4
"""


class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        def reverseLinkedList(head):
            prev_ptr = None
            current_ptr = head

            while current_ptr:
                next_ptr = current_ptr.next
                current_ptr.next = prev_ptr

                prev_ptr = current_ptr
                current_ptr = next_ptr

            head = prev_ptr

            return prev_ptr


        # #MAIN
        head = my_ptr = reverseLinkedList(head)

        carry = 1
        while my_ptr:
            carry, my_ptr.val = divmod(my_ptr.val + carry, 10)
            my_ptr = my_ptr.next

        head = reverseLinkedList(head)
        return head