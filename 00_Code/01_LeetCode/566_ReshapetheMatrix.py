"""
In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.

You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

Your runtime beats 46.02 % of python submissions.
"""


class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        """
        Method 1:
        Your runtime beats 46.02 % of python submissions.
        """
        if len(nums) * len(nums[0]) != (r * c):
            return nums

        result = []
        temp = []
        count = 0
        for i in range(len(nums)):
            for j in range(len(nums[0])):

                temp.append(nums[i][j])
                count += 1
                if count == c:
                    result.append(temp)
                    temp = []
                    count = 0

        return result