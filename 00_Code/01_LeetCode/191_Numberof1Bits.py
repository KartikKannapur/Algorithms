"""
Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).

For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.
"""

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        Method 1: Stings
        Your runtime beats 45.97 % of python submissions.
        """
        # return bin(n).count("1")


        """
        Method 2: Brian Kernighan’s Algorithm
        Your runtime beats 75.00 % of python submissions.
        """
        counter = 0
        while n:
            n = n & (n - 1)
            counter += 1

        return counter