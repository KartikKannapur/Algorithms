"""
Given a binary tree, find the leftmost value in the last row of the tree.

Example 1:
Input:

    2
   / \
  1   3

Output:
1
Example 2:
Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7
Note: You may assume the tree (i.e., the given root node) is not NULL.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        """
        Algorithm: BFS 

        * Use BFS + Queue
        * Each time we encounter an 'X', we only
        consider the leftmost element in the queue
        and update res

        Your runtime beats 99.83 % of python submissions
        """

        queue = [root, 'X']
        res = root
        while queue:
            node = queue.pop(0)

            if node == 'X':
                if queue:
                    queue.append('X')
                    res = queue[0]

            elif node and (node.left or node.right):
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # print([ele.val if ele != 'X' else ele for ele in queue], res.val)

        return res.val