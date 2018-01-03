# #Given a positive integer, output its complement number.
# #The complement strategy is to flip the bits of its binary representation.
# #Note:
# #The given integer is guaranteed to fit within the range of a 32-bit signed integer.
# #You could assume no leading zero bit in the integer’s binary representation.

# #Your runtime beats 53.61 % of python submissions.

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        i = 1
        while num >= i:
            num ^= i
            i <<= 1
        return num
