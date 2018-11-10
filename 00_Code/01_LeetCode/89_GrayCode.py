"""
The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

Example 1:

Input: 2
Output: [0,1,3,2]
Explanation:
00 - 0
01 - 1
11 - 3
10 - 2

For a given n, a gray code sequence may not be uniquely defined.
For example, [0,2,3,1] is also a valid gray code sequence.

00 - 0
10 - 2
11 - 3
01 - 1
Example 2:

Input: 0
Output: [0]
Explanation: We define the gray code sequence to begin with 0.
             A gray code sequence of n has size = 2n, which for n = 0 the size is 20 = 1.
             Therefore, for n = 0 the gray code sequence is [0].

"""


class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        """
        Algorithm:

        We need to return decimal numbers such that
        in their binary form, each of the consecutive 
        numbers differ by 1

        But is there a pattern?
        0           [0]
        1           [0,1]
        2           [0,1,3,2]
        3           [0,1,3,2,6,7,5,4]
        4           [0,1,3,2,6,7,5,4,12,13,15,14,10,11,9,8]

        Your runtime beats 54.48 % of python submissions.
        """

        res = [0]
        for i in range(n):
            # print(i, res, pow(2, i))
            res += [ele + pow(2, i) for ele in reversed(res)]
        return res