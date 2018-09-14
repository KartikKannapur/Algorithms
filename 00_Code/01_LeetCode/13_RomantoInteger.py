"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
"""


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        """
        Method 1: Pointers

        * Maintain two pointers one at i and one at i+1
        * IF the ith pointer value is greater than the i+1, increment total
        * ELSE decrement total, and the i+1th value will be incremented in the
        next iteration

        Your runtime beats 76.52 % of python submissions.
        """

        romans = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        total = 0

        for index, char in enumerate(s[:-1]):

            if romans[char] >= romans[s[index + 1]]:
                total += romans[char]
            else:
                total -= romans[char]

                # print(char, s[index+1], total)
        total += romans[s[-1]]
        return total