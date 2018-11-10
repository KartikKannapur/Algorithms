"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """

        """
        Method 1: DFS + Stack

        Similar to other Tree based DFS + Stack problems
        Addition is the schema in the result array and stack
        Rather than only considering the node, we also
        factor in the value.

        Your runtime beats 94.92 % of python submissions.
        """
        # #Boundary Conditions
        if not root:
            return False

        res = []
        res_min_path_sum = []
        stack = [[root, 0]]

        while stack:
            elem = stack.pop()
            node = elem[0]

            res.append([node.val, elem[1] + node.val])

            if not node.right and not node.left:
                res_min_path_sum.append(res[-1])

            if node.right:
                stack.append([node.right, elem[1] + node.val])
            if node.left:
                stack.append([node.left, elem[1] + node.val])

            # print([stack], res)

        # print(res_min_path_sum)
        return sum in [ele[1] for ele in res_min_path_sum]