# #Your task is to calculate ab mod 1337 where a is a positive integer and b
# #is an extremely large positive integer given in the form of an array.
# #Your runtime beats 81.89 % of python submissions.

class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """

        return pow(a, int(''.join(map(str, b))), 1337)
