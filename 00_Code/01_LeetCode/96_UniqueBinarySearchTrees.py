"""
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""


class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """

        stack = [0] * (n + 1)
        for i in range(n + 1):
            if i <= 1:
                stack[i] = 1
            else:
                for j in range(i):
                    stack[i] += stack[j] * stack[i - j - 1]
        return stack[n]