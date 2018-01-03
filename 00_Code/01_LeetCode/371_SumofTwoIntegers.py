# #Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
# #Example: Given a = 1 and b = 2, return 3.
# #Your runtime beats 79.38 % of python submissions.

class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # #Method 1:
        return a +b

        # #Method 2:
        return int(bin(a+b), 2)

        # #Method 3(works for +ve numbers):
        while b != 0:
            carry = a&b
            a = a^b
            b = carry<<1
        return a

        # #Method 4
        MAX_INT = 0x7FFFFFFF
        MIN_INT = 0x80000000
        MASK = 0x100000000
        while b:
            a, b = (a ^ b) % MASK, ((a & b) << 1) % MASK
        return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)

        # #Method 5: Hack
        return sum([a, b])