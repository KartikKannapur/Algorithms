"""
Print a binary tree in an m*n 2D string array following these rules:

The row number m should be equal to the height of the given binary tree.
The column number n should always be an odd number.
The root node's value (in string format) should be put in the exactly middle of the first row it can be put. The column and the row where the root node belongs will separate the rest space into two parts (left-bottom part and right-bottom part). You should print the left subtree in the left-bottom part and print the right subtree in the right-bottom part. The left-bottom part and the right-bottom part should have the same size. Even if one subtree is none while the other is not, you don't need to print anything for the none subtree but still need to leave the space as large as that for the other subtree. However, if two subtrees are none, then you don't need to leave space for both of them.
Each unused space should contain an empty string "".
Print the subtrees following the same rules.
Example 1:
Input:
     1
    /
   2
Output:
[["", "1", ""],
 ["2", "", ""]]
Example 2:
Input:
     1
    / \
   2   3
    \
     4
Output:
[["", "", "", "1", "", "", ""],
 ["", "2", "", "", "", "3", ""],
 ["", "", "4", "", "", "", ""]]
Example 3:
Input:
      1
     / \
    2   5
   /
  3
 /
4
Output:

[["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""]
 ["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""]
 ["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]
 ["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]]
Note: The height of binary tree is in the range of [1, 10].
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """

        """
        Method: Reference from https://leetcode.com/problems/print-binary-tree/discuss/106273/Simple-Python-with-thorough-explanation

        Given a Binary Tree of height H:

        The maximum total number of nodes is = 2^H - 1
        Number of nodes at each level, L (0-indexed) = 2^L
        We can view the final output as a 2-D matrix, 
        where the number of rows is the height of the 
        tree and the number of columns will be the 2^H - 1.

        The height is 4 and based on our calculations, 
        the number of rows = 4, number of cols = 2^4 - 1 = 15. 
        So we can directly initialize a 2-D matrix of size 4 x 15. 
        We can observe that for each row, the first node has a left 
        padding = 2^(H-L-1) - 1 and the space between each node is 2^(H-L) - 1.
        """

        def get_height(node):
            if not node:
                return 0
            return 1 + max(get_height(node.left), get_height(node.right))

        rows = get_height(root)
        cols = 2 ** rows - 1
        res = [['' for _ in range(cols)] for _ in range(rows)]

        def traverse(node, level, pos):
            if not node:
                return
            left_padding, spacing = 2 ** (rows - level - 1) - 1, 2 ** (rows - level) - 1
            index = left_padding + pos * (spacing + 1)
            print(level, index, node.val)
            res[level][index] = str(node.val)
            traverse(node.left, level + 1, pos << 1)
            traverse(node.right, level + 1, (pos << 1) + 1)

        traverse(root, 0, 0)
        return res
