# #Given a linked list, determine if it has a cycle in it.
# #Your runtime beats 95.57 % of python submissions.

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
        # #Method 1
        dict_nodes = {}
        var_node = head

        while var_node:
            if var_node in dict_nodes:
                return True
            else:
                dict_nodes[var_node] = var_node.val
                var_node = var_node.next

        return False

        # #Method 2
        try:
            slow_ptr = head
            fast_ptr = head.next
            while slow_ptr is not fast_ptr:
                slow_ptr = slow_ptr.next
                fast_ptr = fast_ptr.next.next
            return True
        except:
            return False