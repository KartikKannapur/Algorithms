"""
Determine whether an integer is a palindrome. Do this without extra space.
"""
class Solution(object):
    """
    Method 1:
    Reverse the number via sting operations and compare
    Your runtime beats 22.13 % of python submissions.

    Method 2: Two Pointer
    Your runtime beats 21.98 % of python submissions.
    """

    """
    Method 3:
    Your runtime beats 43.28 % of python submissions.
    """

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if str(x)[0] == "-":
            return False

        if str(x) == str(x)[::-1]:
            return True
        return False
