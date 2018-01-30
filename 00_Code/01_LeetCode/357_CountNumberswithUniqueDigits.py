"""
Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.

Example:
Given n = 2, return 91. (The answer should be the total numbers in the range of 0 ≤ x < 100, excluding [11,22,33,44,55,66,77,88,99])
"""


class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        Method 1 - Combinatorics
        _ : 10 numbers
        _ _ : 9 * 9
        _ _ _ : 9 * 9 * 8 

        Your runtime beats 52.07 % of python submissions.
        """
        choices = [9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        ans, product = 1, 1

        for i in range(n if n <= 10 else 10):
            product *= choices[i]
            ans += product

        return ans