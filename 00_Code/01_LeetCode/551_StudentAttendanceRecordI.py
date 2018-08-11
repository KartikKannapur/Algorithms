"""
You are given a string representing an attendance record for a student. The record only contains the following three characters:
'A' : Absent.
'L' : Late.
'P' : Present.
A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

You need to return whether the student could be rewarded according to his attendance record.

Example 1:
Input: "PPALLP"
Output: True
Example 2:
Input: "PPALLL"
Output: False

"""


class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        """
        Method 1:
        * Check the occurrence of "A" or "LLL" 

        Your runtime beats 99.77 % of python3 submissions.
        """
        if (s.count("A") > 1) or (s.count("LLL") > 0):
            return False
        return True
