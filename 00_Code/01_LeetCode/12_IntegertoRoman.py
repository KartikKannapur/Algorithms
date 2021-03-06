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
Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: 3
Output: "III"
Example 2:

Input: 4
Output: "IV"
Example 3:

Input: 9
Output: "IX"
Example 4:

Input: 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.
Example 5:

Input: 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""


class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        """
        Standard Method from the Discussion Forum

        Split each digit and check the mapping
        * num/1000
        * (num%1000)/100
        * (num%100)/10
        * num%10

        Your runtime beats 97.73 % of python3 submissions
        """
        #         M = ["", "M", "MM", "MMM"]
        #         C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        #         X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        #         I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

        #         return M[num//1000] + C[(num%1000)//100] + X[(num%100)//10] + I[num%10]

        """
        Method 2

        * Create a Hash Map for certain Roman Integers and their
        Integer conversions
        Essentially, multiples of 4,5,9,10
        * Iterate through val, moving from the largest to the smallest
        value - this makes intuitive sense while working on any number
        conversion problem.
        * When the quotient of q,  r = divmod(num, val[i]) is greater
        than 0, then add those many symbols.
        * Update the quotient, remainder and the result.

        Eg: 27
        Iterate until we get 10 in the val array
        q = 2, r = 7, val[i] = 10 --> res = XX
        Now the number is 7

        q = 1, r = 2, val[i] = 5 --> res = XXV
        Now the number is 2

        res = XXVII
        """
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4]
        sym = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV"]
        res = ""
        for i in range(len(val)):
            q, r = divmod(num, val[i])

            if q > 0:
                res += q * sym[i]
                num = r
            if num == 0:
                return res

        if num > 0:
            res += num * "I"

        return res