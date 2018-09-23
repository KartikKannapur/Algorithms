"""
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        """
        Method 1: Iterative Solution DFS + Stack

        Same logic as  589
        Rather than travesing a N-ary tree there, we
        would traverse a Binary tree here

        Note: For Preorder traversal - Stack works well

        Your runtime beats 100.00 % of python submissions.
        """

        # #Boundary Conditions
        if not root:
            return []

        res = []
        stack = [root]

        while stack:
            node = stack.pop()

            res.append(node.val)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

                # print([ele.val for ele in stack], res)

        return res