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

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        """
        Method 1: Recursive approach

        * Check if the root nodes are equal
        * Then recursively call the isSameTree() method on
        the left and right nodes

        Your runtime beats 94.40 % of python3 submissions
        """

        # #To handle None cases
        if not p and not q:
            return True

        # #Then recursively call the isSameTree() method on he left and right nodes
        if p and q:
            return ((p.val == q.val) and (self.isSameTree(p.left, q.left)) and (self.isSameTree(p.right, q.right)))

        return False