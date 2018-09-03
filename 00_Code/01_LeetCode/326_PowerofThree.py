"""
Given an integer, write a function to determine if it is a power of three.

Example 1:

Input: 27
Output: true
Example 2:

Input: 0
Output: false
Example 3:

Input: 9
Output: true
Example 4:

Input: 45
Output: false
"""


class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """

        """
        Method 1: WHILE Loop

        * WHILE loop - repeatedly divide n by 3
        * At the end if the number is 1, them return True
        Otherwise, False

        Your runtime beats 31.70 % of python3 submissions.
        """
        # #Code to handle boundary condition
        if n == 0:
            return False

        while n % 3 == 0:
            n = n / 3

        if n == 1:
            return True
        return False