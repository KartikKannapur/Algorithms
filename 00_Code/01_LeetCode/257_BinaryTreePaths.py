"""
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        """
        Similar to Q.Path Sum
        DFS + Stack
        """

        # #Boundary Conditions
        if not root:
            return []

        res = []
        res_min_path_sum = []
        stack = [[root, "0"]]

        while stack:
            elem = stack.pop()
            node = elem[0]

            res.append([node.val, elem[1] + "->" + str(node.val)])

            if not node.right and not node.left:
                res_min_path_sum.append(res[-1])

            if node.right:
                stack.append([node.right, elem[1] + "->" + str(node.val)])
            if node.left:
                stack.append([node.left, elem[1] + "->" + str(node.val)])

            # print([stack], res)

        print(res_min_path_sum)

        return [ele[1][3:] for ele in res_min_path_sum]