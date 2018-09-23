"""
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        """
        Method 1: BFS + Queue

        Twisted logic - can clean this code up

        * If a node exists & node.left exists
        and it contains no child nodes i.e 
        node.left.left and node.right.right does not exist
        then we can add it to res

        Your runtime beats 99.62 % of python3 submissions.
        """

        # #Boundary Conditions
        if not root:
            return 0

        res = 0
        queue = [root]

        while queue:
            node = queue.pop(0)

            if node and node.left and not node.left.left and not node.left.right:
                res += node.left.val

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

            # print([ele.val for ele in queue], res)

        return res