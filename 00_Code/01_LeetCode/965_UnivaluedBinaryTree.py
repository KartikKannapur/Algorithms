"""
A binary tree is univalued if every node in the tree has the same value.

Return true if and only if the given tree is univalued.



Example 1:


Input: [1,1,1,1,1,null,1]
Output: true
Example 2:


Input: [2,2,2,5,2]
Output: false
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        """
        Method 1: BFS

        Your runtime beats 82.98 % of python3 submissions.
        """
        #         if not root:
        #             return False

        #         res = set([root.val])
        #         queue = [root, 'X']

        #         while queue:
        #             node = queue.pop(0)

        #             if queue and node == 'X':
        #                 for ele in queue:
        #                     res.add(ele.val)
        #                 queue.append('X')

        #             elif queue:
        #                 if node.left:
        #                     queue.append(node.left)
        #                 if node.right:
        #                     queue.append(node.right)

        #         if len(res) <= 1:
        #             return True
        #         return False

        """
        Method 2: Recursion

        * In the recursive solution make sure that
        if the root node is not present then the
        return value must be True
        * If the right and/or left nodes are present
        then check if the values are the same as
        that of the root node.
        * Recursively call the left and right nodes
        at each level

        Your runtime beats 82.98 % of python3 submissions.
        """
        if not root:
            return True

        if (root.right) and (root.right.val != root.val):
            return False

        if (root.left) and (root.left.val != root.val):
            return False

        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)