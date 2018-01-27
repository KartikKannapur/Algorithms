"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        """
        Method 1: Standard Method
        Your runtime beats 59.75 % of python submissions.

        Note: We use the same logic to find the Maximum Depth
        of a Binary Tree.
        The only difference is while comparing l_depth > r_depth
        we return the value that is greater value + 1
        """
        if not root:
            return 0

        l_depth = self.minDepth(root.left)
        r_depth = self.minDepth(root.right)

        # #Handle the situation when we have only a left node or
        # #a right node.
        if not r_depth:
            return l_depth + 1
        elif not l_depth:
            return r_depth + 1

        if l_depth > r_depth:
            return r_depth + 1
        else:
            return l_depth + 1

