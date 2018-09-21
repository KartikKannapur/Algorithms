"""

Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
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
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        """
        Method 1: BFS

        Same as Q 102
        where in I get the results in level order and then
        perform the zig-zag operation

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

        res_res = []
        for index, ele in enumerate(res):
            if index % 2 == 0:
                res_res.append(ele)
            else:
                res_res.append(ele[::-1])

        return res_res



