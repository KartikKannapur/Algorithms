"""
A positive integer is magical if it is divisible by either A or B.

Return the N-th magical number.  Since the answer may be very large, return it modulo 10^9 + 7.



Example 1:

Input: N = 1, A = 2, B = 3
Output: 2
Example 2:

Input: N = 4, A = 2, B = 3
Output: 6
Example 3:

Input: N = 5, A = 2, B = 4
Output: 10
Example 4:

Input: N = 3, A = 6, B = 4
Output: 8


Note:

1 <= N <= 10^9
2 <= A <= 40000
2 <= B <= 40000
"""


class Solution:
    def nthMagicalNumber(self, N, A, B):
        """
        :type N: int
        :type A: int
        :type B: int
        :rtype: int
        """

        #         """
        #         Method 1: Brute Force
        #         44 / 66 test cases passed.
        #         """

        #         counter = 0
        #         num = 1
        #         while counter < N:
        #             if (num % A == 0) or (num % B == 0):
        #                 counter += 1
        #             num += 1

        #         return (num-1)%((10**9) + 7)


        """
        Method 2: From Discussion Forums
        Your runtime beats 12.00 % of python3 submissions.
        """

        def gcd(x, y):
            while y > 0:
                x, y = y, x % y
            return x

        def lcm(x, y):
            return x * y // gcd(x, y)

        temp = lcm(A, B)
        seq = {}
        for i in range(1, temp // A + 1):
            seq[i * A] = 1
        for i in range(1, temp // B + 1):
            seq[i * B] = 1
        cand = sorted([key for key, value in seq.items()])
        ans = ((N - 1) // len(cand)) * cand[-1] + cand[N % len(cand) - 1]
        return ans % (10 ** 9 + 7)