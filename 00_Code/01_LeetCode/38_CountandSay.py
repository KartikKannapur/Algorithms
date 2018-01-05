"""
The count-and-say sequence is the sequence of integers with the
first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Your runtime beats 35.02 % of python submissions.
"""


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        # #Method 1:
        def func_count(num_input):
            nn = str(num_input)
            counter = 1
            ss = ""

            for var_digit in range(0, len(nn)):
                if var_digit == len(nn) - 1 or nn[var_digit] != nn[var_digit + 1]:
                    ss += str(counter)
                    ss += nn[var_digit]
                    counter = 1
                else:
                    counter += 1
            return ss

        nn = 1
        for _ in range(n - 1):
            nn = func_count(nn)

        return str(nn)
