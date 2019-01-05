"""
Given an array A of integers, for each integer A[i] we may choose any x with -K <= x <= K, and add x to A[i].

After this process, we have some array B.

Return the smallest possible difference between the maximum value of B and the minimum value of B.



Example 1:

Input: A = [1], K = 0
Output: 0
Explanation: B = [1]
Example 2:

Input: A = [0,10], K = 2
Output: 6
Explanation: B = [2,8]
Example 3:

Input: A = [1,3,6], K = 3
Output: 0
Explanation: B = [3,3,3] or B = [4,4,4]


Note:

1 <= A.length <= 10000
0 <= A[i] <= 10000
0 <= K <= 10000

"""


class Solution:
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """

        """
        Method: Math Intuition

        * In order to return the smallest difference
        possible in B, we need to add K to the 
        minimum value of A and subtract K from the
        maximum value of A.
        * The difference between these values would
        turn out to be the minimum difference


        Time Complexity: 
        Find min and max: O(N) + O(N) = O(N)

        Your runtime beats 34.96 % of python3 submissions
        """

        #         A_min = min(A) + K
        #         A_max = max(A) - K

        #         if A_min < A_max:
        #             return A_max-A_min
        #         else:
        #             return 0

        """
        Optimize the code above

        Your runtime beats 91.91 % of python3 submissions
        """
        return max(0, max(A) - min(A) - (2 * K))
