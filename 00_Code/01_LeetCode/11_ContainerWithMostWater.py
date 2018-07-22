"""

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.


"""


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        """
        Method 1: Two Pointer
        Your runtime beats 37.22 % of python submissions.
        """
        start_ptr = 0
        end_ptr = len(height) - 1
        res_area = 0

        while start_ptr < end_ptr:
            temp_area = (end_ptr - start_ptr) * min(height[start_ptr], height[end_ptr])
            # print(start_ptr, end_ptr, temp_area)

            res_area = max(res_area, temp_area)

            # #Note - Condition to increment/decrement
            if height[start_ptr] < height[end_ptr]:
                start_ptr += 1
            else:
                end_ptr -= 1

        return res_area
