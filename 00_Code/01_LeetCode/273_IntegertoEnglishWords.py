"""
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

Example 1:

Input: 123
Output: "One Hundred Twenty Three"
Example 2:

Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Example 4:

Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
"""


class Solution:
    """
    Your runtime beats 94.44 % of python3 submissions.
    """

    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"
        res = self.loop(num)
        rest = ' '.join(res)
        return rest

    def loop(self, num):
        res = []
        unit = [[], ['Thousand'], ['Million'], ['Billion']]
        for i in unit:
            if num == 0:
                break
            if len(str(num % 1000)) == 3:
                if str(num % 1000) != '0':
                    res = self.threedigit(str(num % 1000)) + i + res
            if len(str(num % 1000)) == 2:
                if str(num % 1000) != '0':
                    res = self.twodigit(str(num % 1000)) + i + res
            if len(str(num % 1000)) == 1:
                if str(num % 1000) != '0':
                    res = self.onedigit(str(num % 1000)) + i + res
            num //= 1000
        return res

    def threedigit(self, num):
        res = []
        one = {'1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight',
               '9': 'Nine'}
        if num[0] != '0':
            res = res + [one[num[0]]] + ['Hundred']
            res = res + self.twodigit(num[1:3])
        else:
            res = res + self.twodigit(num[1:3])
        return res

    def twodigit(self, num):
        res = []
        two = {'10': 'Ten', '11': 'Eleven', '12': 'Twelve', '13': 'Thirteen', '14': 'Fourteen', '15': 'Fifteen',
               '16': 'Sixteen', '17': 'Seventeen', '18': 'Eighteen', '19': 'Nineteen', '2': 'Twenty', '3': 'Thirty',
               '4': 'Forty', '5': 'Fifty', '6': 'Sixty', '7': 'Seventy', '8': 'Eighty', '9': 'Ninety'}
        if num[0] != '0':
            if num[0] == '1':
                res = res + [two[num[0:2]]]
            else:
                res = res + [two[num[0]]] + self.onedigit(num[1])
        else:
            res = res + self.onedigit(num[1])
        return res

    def onedigit(self, num):
        res = []
        one = {'1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight',
               '9': 'Nine'}
        if num != '0':
            res = res + [one[num]]
        else:
            res = res
        return res