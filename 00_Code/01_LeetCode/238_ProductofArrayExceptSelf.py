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
        #         # #Method 1: Algo works well. But times out
        #         # #for large arrays
        #         output = []

        #         for ele in nums:
        #             temp = nums[:]
        #             temp.remove(ele)
        #             prod = 1

        #             for i in temp:
        #                 prod *= i
        #             output.append(prod)

        #         return output

        # #Method 2:
        n = len(nums)

        left = [1] * n
        right = [1] * n

        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        return ([x * y for x, y in zip(left, right)])