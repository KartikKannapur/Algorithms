"""

Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.


Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false

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