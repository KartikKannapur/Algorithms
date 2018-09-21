"""

Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        """
        Method 1: BFS

        Same as Q 102, 103
        where in I get the results in level order and then
        reverse it

        Your runtime beats 94.08 % of python submissions.
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

            if node == 'X':
                if queue:
                    res.append([ele.val for ele in queue])
                    queue.append('X')

            else:
                # #Left comes before right in level order traversal
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)


                    # print([ele.val if ele != 'X' else ele for ele in queue])

        return res[::-1]



