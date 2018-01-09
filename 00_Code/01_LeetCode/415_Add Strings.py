"""
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.

Your runtime beats 92.30 % of python submissions
"""


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # #Method 1:
        return str(int(num1) + int(num2))

        # #Method 2:
        num1 = eval(num1)
        num2 = eval(num2)
        return str(num1 + num2)
