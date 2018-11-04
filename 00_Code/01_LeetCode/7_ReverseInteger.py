"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        """
        Method 1:

        * Store the input number as an string array
        * Reverse the integer part of the number
        * If the number is greater than 2**31, return 0
        Else return the number

        We could also use a stack to push and pop numbers

        Your runtime beats 75.05 % of python submissions.
        """
        arr_input = str(x)

        # #Negative Numbers
        if arr_input[0] == "-":
            result = (int("-" + arr_input[:0:-1]))

        # #Positive Numbers
        else:
            result = (int(arr_input[::-1]))

        # #Result 32-bit signed integer
        if abs(result) > 2 ** 31:
            return (0)
        else:
            return (result)