"""
Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

For example, given a 3-ary tree:





We should return its max depth, which is 3.
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """

        """
        Method 1: Recursion

        """
        #         if not root:
        #             return 0
        #         if not root.children:
        #             return 1

        #         return max(self.maxDepth(node) for node in root.children) + 1


        """
        Method 2: BFS
        """
        if not root:
            return 0
        if not root.children:
            return 1

        max_depth = 0
        queue = [root, 'X']

        while queue:
            node = queue.pop(0)

            if node == 'X':
                max_depth += 1
                if queue:
                    queue.append('X')

            elif node and node.children:
                for ele in node.children:
                    queue.append(ele)

            # print([ele.val if ele != 'X' else ele for ele in queue])

        return max_depth


