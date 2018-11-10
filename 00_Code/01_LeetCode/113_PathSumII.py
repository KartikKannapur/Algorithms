"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, summ):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        """
        DFS + Stack
        """

        # #Boundary Conditions
        if not root:
            return []

        res = []
        res_min_path_sum = []
        stack = [[root, [0]]]

        while stack:
            elem = stack.pop()
            node = elem[0]

            res.append([node.val, elem[1] + [node.val]])

            if not node.right and not node.left:
                res_min_path_sum.append(res[-1])

            if node.right:
                stack.append([node.right, elem[1] + [node.val]])
            if node.left:
                stack.append([node.left, elem[1] + [node.val]])

            # print([stack], res)

        # print(res_min_path_sum)
        return [ele[1][1:] for ele in res_min_path_sum if sum(ele[1]) == summ]