"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        """
        Method 2: BFS + Queue

        Same BFS logic as 515, 451
        Your runtime beats 100.00 % of python submissions.
        """
        # #Boundary conditions
        if not root:
            return []
        if root and ((not root.left) and (not root.right)):
            return [[root.val]]

        res = [[root.val]]
        queue = [root, 'X']

        while queue:
            node = queue.pop(0)

            if queue and node == 'X':
                res.append([ele.val for ele in queue])
                queue.append('X')

            elif queue:
                # #Left comes before right in level order traversal
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return res
