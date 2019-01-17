"""
Given an array A of positive lengths, return the largest perimeter of a triangle with non-zero area, formed from 3 of these lengths.

If it is impossible to form any triangle of non-zero area, return 0.



Example 1:

Input: [2,1,2]
Output: 5
Example 2:

Input: [1,2,1]
Output: 0
Example 3:

Input: [3,2,3,4]
Output: 10
Example 4:

Input: [3,6,2,3]
Output: 8
"""


class Solution:
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        """
        Method 1: Sort + Loop

        * Sort the numbers in reverse order
        * Iterate through the sorted array, if the
        numbers can form a triangle then return
        the sum as its perimeter.

        Complexity: O(nlogn)
        Your runtime beats 78.22 % of python3 submissions.
        """

        A = sorted(A, reverse=True)

        for ele in range(len(A) - 2):
            if A[ele] < (A[ele + 1] + A[ele + 2]):
                return A[ele] + A[ele + 1] + A[ele + 2]
        return 0