"""
Given the coordinates of four points in 2D space, return whether the four points could construct a square.

The coordinate (x,y) of a point is represented by an integer array with two integers.

Example:
Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: True
Note:

All the input integers are in the range [-10000, 10000].
A valid square has four equal sides with positive length and four equal angles (90-degree angles).
Input points have no order.
"""


class Solution:
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """

        """
        Method 1: 

        In order for 4 points to be a square:
        i. the distance between ab, bc, cd, da should be equal
        ii. the distance between ab, ad and ac = (x, x, sqrt(2).x)
        similarly with b, c and d

        """
        import math

        def calculateEuclideanDistance(x, y):
            return math.sqrt((y[0] - x[0]) ** 2 + (y[1] - x[1]) ** 2)

        # def check_equalSides_Diagonal(temp_arr):
        #     a, b, c = temp_arr[0], temp_arr[1], temp_arr[2]
        #     set_res = [calculateEuclideanDistance(a, b), calculateEuclideanDistance(b, c), calculateEuclideanDistance(a, c)]
        #     min_set_res = min(set_res)
        #     set_res = set(sorted([ele/min_set_res for ele in set_res]))
        #    return set_res == set([1, 1, math.sqrt(2)])



        if p1 == p2 == p3 == p4:
            return False

        arr = [calculateEuclideanDistance(p1, p2), calculateEuclideanDistance(p1, p3), \
               calculateEuclideanDistance(p1, p4), calculateEuclideanDistance(p2, p3), \
               calculateEuclideanDistance(p2, p4), calculateEuclideanDistance(p3, p4)]

        arr.sort()
        if (arr[0] == arr[1] == arr[2] == arr[3]) and (arr[4] == arr[5]):
            return True
        return False