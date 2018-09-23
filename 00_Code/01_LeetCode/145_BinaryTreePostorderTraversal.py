"""
Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        """
        Method 1: BFS + Stack + Return in Reverse Order

        Same logic as 590.
        Can't believe that it worked for this hard problem

        Your runtime beats 100.00 % of python submissions.
        """
        # #Boundary Conditions:
        if not root:
            return []

        res = []
        stack = [root]

        while stack:
            node = stack.pop()

            if node.left:
                stack.append(node.left)

            if node.right:
                stack.append(node.right)

            res += [node.val]

        return res[::-1]