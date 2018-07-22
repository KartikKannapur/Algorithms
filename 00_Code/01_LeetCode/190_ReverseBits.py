"""
Reverse bits of a given 32 bits unsigned integer.

Example:

Input: 43261596
Output: 964176192
Explanation: 43261596 represented in binary as 00000010100101000001111010011100,
             return 964176192 represented in binary as 00111001011110000010100101000000.
"""

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        """
        Method 1: Using Python built-in functions
        Your runtime beats 87.84 % of python submissions.
        """
        return int(((bin(n)[2:].zfill(32))[::-1]), 2)