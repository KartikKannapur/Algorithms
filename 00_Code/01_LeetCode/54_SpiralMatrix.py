"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
"""


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        """
        Method 1
        Your runtime beats 37.38 % of python submissions
        """
        if matrix == []:
            return matrix

        left = 0
        right = len(matrix[0]) - 1
        top = 0
        bottom = len(matrix) - 1

        res = []
        while left < right and top < bottom:
            # #Top Row
            for i in range(left, right):
                res.append(matrix[top][i])

            # #Right Column
            for i in range(top, bottom):
                res.append(matrix[i][right])

                # #Bottom Row
            for i in range(right, left, -1):
                res.append(matrix[bottom][i])

                # #Left Column
            for i in range(bottom, top, -1):
                res.append(matrix[i][left])

            left += 1
            right -= 1

            top += 1
            bottom -= 1

        # #Perfect Square Matrix
        if left == right and top == bottom:
            res.append(matrix[top][left])

        # #Column Vector
        elif left == right:
            for i in range(top, bottom + 1):
                res.append(matrix[i][left])

        # #Row Vector
        elif top == bottom:
            for i in range(left, right + 1):
                res.append(matrix[top][i])

        return res