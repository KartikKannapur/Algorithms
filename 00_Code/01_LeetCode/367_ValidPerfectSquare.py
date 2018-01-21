"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Returns: True
Example 2:

Input: 14
Returns: False

Your runtime beats 72.24 % of python submissions.
"""


class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # #Method 1 - Your runtime beats 6.94 % of python submissions.
        i = 1
        while i**2 <= num:
            if i**2 == num: return True
            i += 1
        return False

        # #Method 2 - Newton's Method
        # #Your runtime beats 72.24 % of python submissions.
        if num == 1: return True

        low = 1
        high = num
        while low <= high:
            mid = (low + high) // 2
            if mid ** 2 == num:
                return True

            if mid ** 2 > num:
                high = mid - 1
            else:
                low = mid + 1

        return False