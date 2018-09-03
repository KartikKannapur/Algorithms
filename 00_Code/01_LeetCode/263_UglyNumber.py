"""
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example 1:

Input: 6
Output: true
Explanation: 6 = 2 × 3
Example 2:

Input: 8
Output: true
Explanation: 8 = 2 × 2 × 2
Example 3:

Input: 14
Output: false
Explanation: 14 is not ugly since it includes another prime factor 7.

"""


class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """

        """
        Method 1: Standard Division

        * For each of the numbers - 2, 3, 5
        keep dividing num by 2,3 or 5, as long
        as the remainder == 0

        Your runtime beats 100.00 % of python3 submissions.
        """
        # #Code block to handle edge-cases
        if num == 0:
            return False

        for ele in 2, 3, 5:
            while num % ele == 0:
                num = num / ele

        return num == 1