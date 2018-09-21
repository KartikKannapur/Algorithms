"""
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
Note:
The range of node's value is in the range of 32-bit signed integer.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """

        """
        Method 1: BFS

        Same logic as 515, 102, 103, 107, 199

        Rathe than returning the max or the entire array
        we return the mean

        * Create a result array, res containing the root node value
        * Create a queue with the res node and 'X'

        * While queue: pop the first node
        The first node can either be a node or 'X'
        * IF 'X', then this indicates that we have 
        all the elements in that node of the tree;
        then take the max of the numbers
        * ELSE append the left and right node elements 
        to the queue


        Your runtime beats 64.78 % of python3 submissions.
        """
        # #Boundary conditions
        if not root:
            return []
        if root and ((not root.left) and (not root.right)):
            return [root.val]

        res = [float(root.val)]
        queue = [root, 'X']

        while queue:
            node = queue.pop(0)

            if node == 'X':

                if queue:  # #Logic to handle the infinite loop pop and append condition
                    arr = [ele.val for ele in queue]
                    res.append(sum(arr) / float(len(arr)))
                    queue.append('X')

            else:
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)

                    # print([ele.val if ele != 'X' else ele for ele in queue])

        return res
