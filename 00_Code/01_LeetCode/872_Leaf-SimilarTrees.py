"""
Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.



For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.



Note:

Both of the given trees will have between 1 and 100 nodes.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findleaf_inorder(self, root):
        if root is None:
            return []
        elif (root.left is None) and (root.right is None):
            return [root.val]
        else:
            return self.findleaf_inorder(root.left) + self.findleaf_inorder(root.right)

    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """

        """
        Method 1: Recursion

        * If the node is NULL, then return NULL
        * If the node has a value, but no left or right node
        then it must be the leaf node
        * Append all the leaf nodes to an array from
        both the trees & then compare the trees

        """
        return self.findleaf_inorder(root1) == self.findleaf_inorder(root2)