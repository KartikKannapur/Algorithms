"""
ount the number of segments in a string, where a segment is
defined to be a contiguous sequence of non-space characters.

Please note that the string does not contain any non-printable
characters.

Example:

Input: "Hello, my name is John"
Output: 5

Your runtime beats 84.16 % of python submissions.
"""

class Solution:
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        Your runtime beats 100.00 % of python3 submissions.
        """
        return len(s.split())