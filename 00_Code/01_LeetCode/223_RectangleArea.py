"""
Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Rectangle Area

Example:

Input: A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2
Output: 45
Note:

Assume that the total area is never beyond the maximum possible value of int.
"""


class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """

        """
        Method:

        * Similar to Q 836 - Draw out all the 4 cases of the
        two rectangles intersecting each other
        * Find the points of intersection/overlap by
        empirical methods
        * Calculate the area of overlap
        * Total area = area of the two rects. - area of overlap
        
        Your runtime beats 62.97 % of python submissions.
        """
        # #Find the points of intersection/overlap by empirical methods
        x1 = max(A, E)
        y1 = max(B, F)

        x2 = min(C, G)
        y2 = min(D, H)

        overlap = max(x2 - x1, 0) * max(y2 - y1, 0)

        return (A - C) * (B - D) + (E - G) * (F - H) - overlap