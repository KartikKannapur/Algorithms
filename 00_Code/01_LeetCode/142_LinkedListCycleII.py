# #Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
# #Note: Do not modify the linked list.
# #Your runtime beats 67.82 % of python submissions.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # #Method 1
        dict_nodes = {}
        var_node = head

        while var_node:
            if var_node in dict_nodes:
                return var_node
            else:
                dict_nodes[var_node] = var_node.val
                var_node = var_node.next

        return None
