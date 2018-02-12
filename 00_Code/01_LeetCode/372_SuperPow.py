"""
Your task is to calculate ab mod 1337 where a is a positive integer and b is an extremely large positive integer given in the form of an array.

Example1:

a = 2
b = [3]

Result: 8
Example2:

a = 2
b = [1,0]

Result: 1024
"""

class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        """
        Method 1: Python One-Liner
        Your runtime beats 63.78 % of python submissions.
        """
        return pow(a, int(''.join(map(str, b))), 1337)
