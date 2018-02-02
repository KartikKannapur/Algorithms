"""
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        """
        Method 1: Standard Solution
        Your runtime beats 54.22 % of python submissions.
        """
        if numRows == 0: return []

        res = [[1]]

        while len(res) < numRows:
            temp = [1] + [(res[-1][i] + res[-1][i + 1]) for i in range(len(res[-1]) - 1)] + [1]
            res.append(temp)

        return res