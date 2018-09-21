"""

Given an n-ary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example, given a 3-ary tree:





We should return its level order traversal:





[
     [1],
     [3,2,4],
     [5,6]
]

"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """

        """
        Method 1: BFS

        Same BFS logic as 515

        * Create a result array, res containing the root node value
        * Create a queue with the res node and 'X'

        * While queue: pop the first node
        The first node can either be a node or 'X'
        * IF 'X', then this indicates that we have 
        all the elements in that node of the tree;
        then take the max of the numbers
        * ELSE append the left and right node elements 
        to the queue

        Your runtime beats 95.67 % of python submissions.
        """

        # #Boundary Conditions
        if not root:
            return []
        if root and (not root.children):
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
                if node.children:
                    for ele in node.children:
                        queue.append(ele)

        return res


