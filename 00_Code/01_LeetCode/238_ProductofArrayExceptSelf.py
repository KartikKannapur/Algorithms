"""
Given an array of n integers where n > 1, nums,
return an array output such that output[i] is equal
to the product of all the elements of nums except
nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

"""


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """
        Method 2:

        Create two arrays - left and right, of size n
        leftside products
        rightside products

        Input:  [1,2,3,4]
        Output: [24,12,8,6]

        Leftside Products: [1,1,2,6]
        Rightside Products: [24,12,4,1]
        Element-wise product: [24, 12,8, 6]

        multiply them element wise to get the result
        Your runtime beats 21.92 % of python submissions.
        """
        n = len(nums)

        left = [1] * n
        right = [1] * n

        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        print(left, right)

        return ([x * y for x, y in zip(left, right)])