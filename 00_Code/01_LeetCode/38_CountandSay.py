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


class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        """
        Method 1:

        * Initialize the starting value to 1 & 
        repeatedly call the function until we 
        reach the given number of values.

        Core Logic
        * Convert the number to a string
        * If the digit is the last digit or not the same
        as the next digit - append the value and the count
        to ss
        * Else increment the counter

        Your runtime beats 91.31 % of python3 submissions
        """

        def func_count(num_input):
            nn = str(num_input)
            counter = 1
            ss = ""

            # #Core Logic
            for index in range(0, len(nn)):
                if index == len(nn) - 1 or nn[index] != nn[index + 1]:
                    ss += str(counter)
                    ss += nn[index]
                    counter = 1
                else:
                    counter += 1
            return ss

        # #Initialize the starting value to 1 &
        # #repeatedly call the function until we
        # #reach the given number of values.
        nn = 1
        for _ in range(n - 1):
            nn = func_count(nn)

        return str(nn)