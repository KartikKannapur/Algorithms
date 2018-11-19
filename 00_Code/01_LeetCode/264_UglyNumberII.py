"""
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:

1 is typically treated as an ugly number.
n does not exceed 1690.
"""


class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

        """
        Method 1: Brute Force
        """
        """
        Method 2: Dynamic Programming
        """

        res = [1]

        index_ptr_2 = 0
        index_ptr_3 = 0
        index_ptr_5 = 0

        while n > 1:
            num2 = 2 * res[index_ptr_2]
            num3 = 3 * res[index_ptr_3]
            num5 = 5 * res[index_ptr_5]

            num_min = min([num2, num3, num5])
            res.append(num_min)
            n -= 1

            # #Increment Pointer
            if num_min == num2:
                index_ptr_2 += 1
            if num_min == num3:
                index_ptr_3 += 1
            if num_min == num5:
                index_ptr_5 += 1

        return res[-1]
