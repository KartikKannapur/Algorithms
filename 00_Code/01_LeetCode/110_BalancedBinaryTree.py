"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        if not root:
            return True

        return abs(self.getHeight(root.left) - self.getHeight(root.right)) < 2 and self.isBalanced(
            root.left) and self.isBalanced(root.right)

    def getHeight(self, root):
        if not root:
            return 0

        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))

#         """
#         DFS + Stack
#         """
#         # #Boundary conditions
#         if not root:
#             return []

#         res = []
#         stack = [[root, 0]]

#         while stack:
#             elem = stack.pop()
#             node = elem[0]
#             res.append([node.val, elem[1]])

#             # #Left comes before right in level order traversal
#             if node.left:
#                 stack.append([node.left, elem[1]+1])
#             if node.right:
#                 stack.append([node.right, elem[1]+1])

#             print(res)
#         return res
