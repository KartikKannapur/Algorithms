"""
Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.

Your runtime beats 83.61 % of python submissions
"""


class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        Method 1
        Python's in-built sorting function
        """
        arr = sorted(list(set(nums)), reverse=True)
        if len(arr) > 2: return arr[2]
        else: return max(nums)

        """
        Method 2
        Find the third largest element in a single pass of the array
        Complexity: O(n)
        Assuming that the sorted function would not be allowed
        """
        nums = list(set(nums))
        max_one = max_two = max_three = float("-inf")

        for elem in nums:
            if elem > max_one:
                max_three = max_two
                max_two = max_one
                max_one = elem

            if max_one > elem > max_two:
                max_three = max_two
                max_two = elem

            if max_two > elem > max_three:
                max_three = elem

        if len(nums) < 3:
            return max_one
        else:
            return max_three
