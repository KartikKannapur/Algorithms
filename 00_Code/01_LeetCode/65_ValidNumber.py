"""
Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true

Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.

"""


class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """

        """
        Method 1: Hack

        Your runtime beats 53.89 % of python3 submissions.
        """
        try:
            float(s)
        except ValueError:
            return False
        else:
            return True
