"""
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".

"""

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        """
        Method 1: Python One-Liner
        Your runtime beats 66.41 % of python submissions.
        """
        return s[::-1]

        """
        Method 2: Two Pointers
        Your runtime beats 19.20 % of python submissions.
        """
        s = list(s)

        low = 0
        high = len(s) - 1

        while low < high:
            s[low], s[high] = s[high], s[low]
            low += 1
            high -= 1

        return "".join(s)

