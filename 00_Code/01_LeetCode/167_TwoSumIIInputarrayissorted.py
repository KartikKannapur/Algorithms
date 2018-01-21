"""
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution and you may not use the same element twice.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2

Your runtime beats 86.95 % of python submissions.
"""


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        """
        Method 1
        Algo: Two Pointers
        Your runtime beats 57.67 % of python submissions.
        """
        low = 0
        high = len(numbers)-1

        while low < high:
            if (numbers[low] + numbers[high]) == target:
                return (low+1, high+1)
            elif (numbers[low] + numbers[high]) > target:
                high -= 1
            else:
                low += 1

        """
        Method 2:
        Algo: Two Sum Dictionary
        Your runtime beats 86.95 % of python submissions.
        """
        d = {}
        for i, j in enumerate(numbers):
            if j in d:
                return sorted([i + 1, d[j] + 1])
            else:
                d[target - j] = i