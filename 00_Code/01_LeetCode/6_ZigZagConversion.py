"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I

"""


class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        """
        Method 1: Finding patterns

        * Top and Bottom rows could be multiples of 2n-3 indices
        * Middle rows could be combination of odd numbers 1,3,5,7
        """

        """
        Method 2:

        * Create a list with numRows number of string elements.
        Therefore, if numRows=3, ['', '', '']
        * Iterate through the elements of s and append characters
        to the string in a 'pendular' manner - 0,1,2,3,2,1,0
        * Increment until we reach the upper index bound,
        decrement until we reach the lower index bound

        Your runtime beats 95.05 % of python3 submissions.
        """
        # #Handle default case
        if numRows == 1 or numRows >= len(s):
            return s

        L = [''] * numRows
        index, step = 0, 1

        for ele in s:
            L[index] += ele

            # #Lower Bound
            if index == 0:
                step = 1

            # #Upper Bound
            elif index == numRows - 1:
                step = -1

            index += step

        return ''.join(L)

