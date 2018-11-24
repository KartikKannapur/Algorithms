"""
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example:
For num = 5 you should return [0,1,1,2,1,2].

Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
Credits:
Special thanks to @ syedee for adding this problem and creating all test cases.


"""


class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        """
        Method 1:
        Your runtime beats 53.63 % of python submissions.
        """
        # return [bin(ele).count('1') for ele in range(num+1)]

        """
        Method 2: Dynamic Programming

        [0,1,1,2,1,2,2,3,1,2,2,3,2,3,3,4,1,2,2,3,2,3,3,4,2,3,3,4,3,4,4,5]
        DP Pattern: dp[index] = dp[index - offset] + 1

        Your runtime beats 99.29 % of python submissions.
        """
        dp = [0] * (num + 1)
        offset = 1

        for i in range(1, num + 1):
            if offset * 2 == i:
                offset = offset * 2

            dp[i] = dp[i - offset] + 1

        return dp