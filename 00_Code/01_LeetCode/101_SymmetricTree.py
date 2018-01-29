"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        """
        Method 1 - Recursive - isMirror function()

        isMirror(left, right)
        IF left.val == right.val:
            isMirror(left.left, right.right)
            and
            isMirror(left.right, right.left)

        Your runtime beats 41.15 % of python submissions.

        If we are running this iteratively, then we must use a stack
        """

        def isMirror(left, right):
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False

            if left.val == right.val:
                outPair = isMirror(left.left, right.right)
                inPair = isMirror(left.right, right.left)
                return outPair and inPair
            else:
                return False

        # #MAIN
        if root is None:
            return True
        else:
            return isMirror(root.left, root.right)
