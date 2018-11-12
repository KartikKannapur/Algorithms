    """
Given a binary tree, return the tilt of the whole tree.

The tilt of a tree node is defined as the absolute difference between the sum of all left subtree node values and the sum of all right subtree node values. Null node has tilt 0.

The tilt of the whole tree is defined as the sum of all nodes' tilt.

Example:
Input:
         1
       /   \
      2     3
Output: 1
Explanation:
Tilt of node 2 : 0
Tilt of node 3 : 0
Tilt of node 1 : |2-3| = 1
Tilt of binary tree : 0 + 0 + 1 = 1
Note:

The sum of node values in any subtree won't exceed the range of 32-bit integer.
All the tilt values won't exceed the range of 32-bit integer.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        """
        Algorithm: Recursion

        * This can be divided into a two step problem.
        * 1. At each node, the result is equal to the
        sum of the abs difference between the left subtree
        and the right subtree
        * 2. At each node we can also return the subtree
        sum as node.val + node.left.val + node.right.val


        Your runtime beats 100.00 % of python submissions
        """

        self.res = 0

        def subtreeSum(node):
            if not node:
                return 0

            left = subtreeSum(node.left)
            right = subtreeSum(node.right)

            # print(left, right, abs(left-right))
            self.res += abs(left - right)
            return node.val + left + right

        subtreeSum(root)
        return self.res