"""
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
"""


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        """
        Method 1: Standard Solution
        Your runtime beats 83.54 % of python submissions.
        """
        if rowIndex == 0: return [1]

        res = [[1]]

        counter = 0
        while counter < rowIndex:
            temp = [1] + [(res[-1][i] + res[-1][i + 1]) for i in range(len(res[-1]) - 1)] + [1]
            res[0] = temp
            counter += 1

        return res[0]
