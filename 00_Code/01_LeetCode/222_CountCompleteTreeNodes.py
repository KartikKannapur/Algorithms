"""
Given a complete binary tree, count the number of nodes.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        """
        Method 1: Recursive Solution
        Algorithm works well, but TLE
        Good for Interviews
        15 / 18 test cases passed.
        """
        if not root:
            return 0

        if root.left and root.right:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        elif root.left:
            return 1 + self.countNodes(root.left)
        elif root.right:
            return 1 + self.countNodes(root.right)
        else:
            return 1

        """
        Method 2:
        Your runtime beats 65.97 % of python submissions
        """
        if not root:
            return 0

        counter1 = 0
        counter2 = 0

        node = root
        while node:
            counter1 += 1
            node = node.left

        node = root
        while node:
            counter2 += 1
            node = node.right

        if counter1 == counter2:
            return 2 ** counter1 - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)