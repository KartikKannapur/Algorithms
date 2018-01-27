"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        """
        Method 1: Standard Method
        Your runtime beats 84.97 % of python submissions.

        Note: We use the same logic to find the Maximum Depth
        of a Binary Tree.
        The only difference is while comparing l_depth > r_depth
        we return the value that is smaller value + 1
        """
        if not root:
            return 0

        l_depth = self.maxDepth(root.left)
        r_depth = self.maxDepth(root.right)

        if l_depth > r_depth:
            return l_depth + 1
        else:
            return r_depth + 1
