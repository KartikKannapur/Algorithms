"""
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28

Your runtime beats 44.13 % of python submissions.
"""

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        #Method 1
        sumvalue = 0
        for letter in range(0, len(s)):
            sumvalue += (ord(s[letter])-64)*(26**(len(s)-letter-1))

        return sumvalue

        # #Method 2
        return sum([(ord(s[letter]) - 64) * (26 ** (len(s) - letter - 1)) for letter in range(0, len(s))])

