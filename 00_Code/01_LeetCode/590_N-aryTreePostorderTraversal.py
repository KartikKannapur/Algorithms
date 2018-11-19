"""
Given an n-ary tree, return the postorder traversal of its nodes' values.


For example, given a 3-ary tree:




Return its postorder traversal as: [5,6,3,2,4,1].
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """

        """
        Method 1: BFS + Stack + Return in Reverse Order

        Your runtime beats 81.43 % of python submissions.
        """
        # #Boundary Conditions:
        if not root:
            return []

        res = []
        stack = [root]

        while stack:
            node = stack.pop()

            for ele in node.children:
                stack.append(ele)

            res += [node.val]

        return res[::-1]