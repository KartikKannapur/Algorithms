"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

1 -> A
2 -> B
3 -> C
...
26 -> Z
27 -> AA
28 -> AB

"""


class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """

        """
        Method 1:
        * While n is still postive
        * The key is to use divmod() recursively

        Your runtime beats 100.00 % of python3 submissions
        """

        res = ''
        while n:
            n, r = divmod(n - 1, 26)
            res += chr(ord('A') + r)
        return res[::-1]