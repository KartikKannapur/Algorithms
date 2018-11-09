"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2.

Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        """
        Method 1: Using ord() in Python

        * Reverse the string and perform element-wise
        multiplication with carry
        * This is similar to our regular multiplication
        method
        * Use the ord(char)-ord('0') to obtain the integer
        value

        Your runtime beats 59.28 % of python submissions.
        """

        res = 0
        ten_multiplier = 1

        for i in num2[::-1]:

            carry = 0
            temp_res = 0
            temp_ten_multiplier = 1

            for j in num1[::-1]:
                carry, prod = divmod(((ord(i) - ord('0')) * (ord(j) - ord('0'))) + carry, 10)
                temp_res += prod * temp_ten_multiplier
                temp_ten_multiplier *= 10
            temp_res += carry * temp_ten_multiplier  # #Add the remaining carry at the end

            res += temp_res * ten_multiplier  # #Add the product per element to the final res
            ten_multiplier *= 10

        return str(res)

