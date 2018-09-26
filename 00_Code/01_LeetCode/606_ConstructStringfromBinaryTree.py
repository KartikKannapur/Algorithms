"""
You need to construct a string consists of parenthesis and integers from a binary tree with the preorder traversing way.

The null node needs to be represented by empty parenthesis pair "()". And you need to omit all the empty parenthesis pairs that don't affect the one-to-one mapping relationship between the string and the original binary tree.

Example 1:
Input: Binary tree: [1,2,3,4]
       1
     /   \
    2     3
   /
  4

Output: "1(2(4))(3)"

Explanation: Originallay it needs to be "1(2(4)())(3()())",
but you need to omit all the unnecessary empty parenthesis pairs.
And it will be "1(2(4))(3)".
Example 2:
Input: Binary tree: [1,2,3,null,4]
       1
     /   \
    2     3
     \
      4

Output: "1(2()(4))(3)"

Explanation: Almost the same as the first example,
except we can't omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.

"""


class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """

        """
        Method 0: Recursive
        if(t.right==null)
            return t.val+"("+tree2str(t.left)+")";
        return t.val+"("+tree2str(t.left)+")("+tree2str(t.right)+")";   

        """

        """
        Method 1: DFS + Stack
        """
        root = t

        # #Boundary Conditions
        if not root:
            return ""
        if root and ((not root.left) and (not root.right)):
            return str(root.val)

        res = ""
        stack = [root]

        while stack:
            node = stack.pop()

            if node == ")":
                res += ")"
                continue

            res += "(" + str(node.val)

            if not node.left and node.right:
                res += "()"

            if node and (node.left or node.right):

                if node.right:
                    stack.append(")")
                    stack.append(node.right)

                if node.left:
                    stack.append(")")
                    stack.append(node.left)

        return res[1:]

