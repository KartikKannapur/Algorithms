"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:

Input:
    2
   / \
  1   3
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6
Output: false
Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
             is 5 but its right child's value is 4.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        """
        Method 1: Recursive

        Your runtime beats 100 % of python submissions.
        """

        def check_bst(node, left, right):
            if not node:
                return True

            if not (left < node.val < right):
                return False

            return (check_bst(node.left, left, node.val)
                    and check_bst(node.right, node.val, right))

        return check_bst(root, float("-inf"), float("inf"))

