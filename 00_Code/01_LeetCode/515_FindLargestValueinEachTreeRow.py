"""
You need to find the largest value in each row of a binary tree.

Example:
Input:

          1
         / \
        3   2
       / \   \
      5   3   9

Output: [1, 3, 9]
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        """
        Method 1: BFS

        * Create a result array, res containing the root node value
        * Create a queue with the res node and 'X'

        * While queue: pop the first node
        The first node can either be a node or 'X'
        * IF 'X', then this indicates that we have 
        all the elements in that node of the tree;
        then take the max of the numbers
        * ELSE append the left and right node elements 
        to the queue


        Your runtime beats 99.71 % of python3 submissions.
        """
        # #Boundary conditions
        if not root:
            return []
        if root and ((not root.left) and (not root.right)):
            return [root.val]

        res = [root.val]
        queue = [root, 'X']

        while queue:
            node = queue.pop(0)

            if node == 'X':

                if queue:  # #Logic to handle the infinite loop pop and append condition
                    res.append(max([ele.val for ele in queue]))
                    queue.append('X')

            else:
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)

                    # print([ele.val if ele != 'X' else ele for ele in queue])

        return res