"""
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.

Example:

Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
Example 2:

Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        """
        Similar to Q.Path Sum
        DFS + Stack

        Your runtime beats 68.68 % of python submissions.
        """

        # #Boundary Conditions
        if not root:
            return 0

        res = []
        res_min_path_sum = []
        stack = [[root, "0"]]

        while stack:
            elem = stack.pop()
            node = elem[0]

            res.append([node.val, elem[1] + str(node.val)])

            if not node.right and not node.left:
                res_min_path_sum.append(res[-1])

            if node.right:
                stack.append([node.right, elem[1] + str(node.val)])
            if node.left:
                stack.append([node.left, elem[1] + str(node.val)])

            # print([stack], res)

        # print(res_min_path_sum)

        return sum([int(ele[1]) for ele in res_min_path_sum])