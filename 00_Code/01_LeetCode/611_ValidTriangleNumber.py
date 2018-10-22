"""
Given an array consists of non-negative integers, your task is to count the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.
Example 1:
Input: [2,2,3,4]
Output: 3
Explanation:
Valid combinations are:
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3
Note:
The length of the given array won't exceed 1000.
The integers in the given array are in the range of [0, 1000].
"""


class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        """
        Method 1: Brute Force

        The Brute Force logic of selecting all possible
        combinations(nums, 3) that contain 3 digits & then
        checking if each one of them is a triangle does 
        not scale.

        Time Limit Exceeded
        215 / 220 test cases passed.
        """

        """
        Method 2: Similar to 3Sum

        * Sort the array
        * Maintain 3 pointers - i,j,k
        * Initialize:
        k = n-1 index
        j = k-1
        i = 0

        i                  j k

        * IF nums[i] + nums[j] > k, then we instantly know
        that we have j-i combinations; decrease k by 1
        * ELSE increment i and when reach nums[i] + nums[j] > k
        we again have j-i combinations


         i                  j   k
        [3, 19, 22, 24, 35, 82, 84]


         i          j   k
        [3, 19, 22, 24, 35, 82, 84]


        Your runtime beats 95.87 % of python submissions.
        """
        nums.sort()
        res = 0

        for k in range(2, len(nums)):
            i = 0
            j = k - 1
            while (i < j):
                if nums[i] + nums[j] > nums[k]:
                    res += j - i
                    j -= 1
                else:
                    i += 1

        return res