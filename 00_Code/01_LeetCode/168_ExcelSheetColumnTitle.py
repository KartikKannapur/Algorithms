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

Your runtime beats 27.05 % of python submissions.
"""

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ''
        while n:
            n, r = divmod(n - 1, 26)
            res += chr(65 + r)
        return(res[::-1])