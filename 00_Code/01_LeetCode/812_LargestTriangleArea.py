"""
You have a list of points in the plane. Return the area of the largest triangle that can be formed by any 3 of the points.

Example:
Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output: 2
Explanation:
The five points are show in the figure below. The red triangle is the largest.
"""


class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        # #Method 1: Brute Force
        """
        57 / 57 test cases passed.
        Status: Accepted
        Runtime: 448 ms
        """

        import math
        def distanceEuclidean(x, y):
            return math.sqrt((y[0] - x[0]) ** 2 + (y[1] - x[1]) ** 2)

        def areaHeronFormula(var_triangle):
            A = distanceEuclidean(var_triangle[0], var_triangle[1])
            B = distanceEuclidean(var_triangle[0], var_triangle[2])
            C = distanceEuclidean(var_triangle[1], var_triangle[2])

            # #Without adding this condition the traiangle would not
            # #be valid, and it would result in a math domain error
            if A + B <= C or B + C <= A or A + C <= B:
                # print('Triangle cannot be formed')
                return float('-Inf')
            else:
                S = (A + B + C) / 2
                return math.sqrt(S * (S - A) * (S - B) * (S - C))

        max_area = float('-Inf')
        for triangle in itertools.combinations(points, 3):
            # print(triangle, areaHeronFormula(triangle))
            temp_area = areaHeronFormula(triangle)
            if temp_area > max_area:
                max_area = temp_area

        return max_area