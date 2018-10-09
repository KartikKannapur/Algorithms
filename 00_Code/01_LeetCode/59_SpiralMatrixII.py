"""
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

"""


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        matrix = [[0 for _ in range(n)] for _ in range(n)]

        left = 0
        right = n - 1
        top = 0
        bottom = n - 1

        counter = 1

        while left <= right and top <= bottom:
            # #Top Row
            for i in range(left, right + 1):
                matrix[top][i] = counter
                print(matrix[top][i], top, i)
                counter += 1

            top += 1
            # #Right Column
            for i in range(top, bottom + 1):
                matrix[i][right] = counter
                print(matrix[i][right], i, right)
                counter += 1

            right -= 1
            # #Bottom Row
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = counter
                print(matrix[bottom][i], bottom, i)
                counter += 1

            bottom -= 1
            # #Left Column
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = counter
                print(matrix[i][left], i, left)
                counter += 1
            left += 1

        return matrix

