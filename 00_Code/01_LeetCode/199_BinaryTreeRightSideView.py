"""
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        """
        Method 1: BFS

        Same BFS logic as 515, 451, 102


        * Create a result array, res containing the root node value
        * Create a queue with the res node and 'X'

        * While queue: pop the first node
        The first node can either be a node or 'X'
        * IF 'X', then this indicates that we have 
        all the elements in that node of the tree;
        then take the RIGHTmost element i.e. arr[-1]
        to obtain the right side view
        * ELSE append the left and right node elements 
        to the queue

        Your runtime beats 96.51 % of python submissions.
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
                if queue:
                    res.append([ele.val for ele in queue][-1])
                    queue.append('X')

            else:
                # #Left comes before right in level order traversal
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)


                    # print([ele.val if ele != 'X' else ele for ele in queue])

        return res



