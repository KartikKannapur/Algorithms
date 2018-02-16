"""
Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:
Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5
Example 2:
Input: 3
Output: False

Your runtime beats 80.45 % of python submissions.
"""


class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        """
        Method 1: Two Pointers

        Your runtime beats 80.45 % of python submissions.
        """
        low = 0
        high = int(c ** 0.5) + 1

        while low <= high:
            if ((low * low) + (high * high)) == c:
                return True
            elif ((low * low) + (high * high)) > c:
                high -= 1
            else:
                low += 1

        return False