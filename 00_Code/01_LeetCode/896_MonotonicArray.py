"""
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic.



Example 1:

Input: [1,2,2,3]
Output: true
Example 2:

Input: [6,5,4,4]
Output: true
Example 3:

Input: [1,3,2]
Output: false
Example 4:

Input: [1,2,4,5]
Output: true
Example 5:

Input: [1,1,1]
Output: true


Note:

1 <= A.length <= 50000
-100000 <= A[i] <= 100000
"""


class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """

        """
        Method 1:

        * Iterate through the array, by taking the 
        difference between the ith and (i-1)th
        element

        * IF condition 
        When the difference is positive, increment pos
        When the difference is negative increment neg
        When the difference is zero, pass

        * If pos and neg are both present, return False

        Your runtime beats 67.84 % of python submissions
        """
        pos = 0
        neg = 0

        for index in range(1, len(A)):

            if (A[index] - A[index - 1]) > 0:
                pos += 1
            elif (A[index] - A[index - 1]) < 0:
                neg += 1
            else:
                pass

            if pos and neg:
                return False
        return True