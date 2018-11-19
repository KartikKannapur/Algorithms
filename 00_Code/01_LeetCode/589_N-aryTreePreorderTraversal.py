"""
Given an n-ary tree, return the preorder traversal of its nodes' values.


For example, given a 3-ary tree:




Return its preorder traversal as: [1,3,5,6,2,4].


Note: Recursive solution is trivial, could you do it iteratively?
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """

        """
        Method 1: Iterative Solution DFS + Stack

        * Initialization: empty res array & stack with root node
        * WHILE stack
        pop the element on the top of the stack

        * IF this is a valid node, append it to the res #used to handle boundary conditions
        * IF the node has children, push them in 
        reverse order into the stack i.e. RIGHT -> LEFT
        since they want the results from LEFT to RIGHT and we 
        can pop elements in the stack accordingly

        Your runtime beats 82.63 % of python submissions.
        """

        # #Boundary Conditions
        if not root:
            return []
        if root and not root.children:
            return [root.val]

        res = []
        stack = [root]

        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)

            if node.children:
                for ele in node.children[::-1]:
                    stack.append(ele)

                    # print([ele.val for ele in stack], res)

        return res