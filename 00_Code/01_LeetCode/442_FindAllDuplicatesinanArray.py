"""
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]

Your runtime beats 79.87 % of python submissions.
"""


class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """
        Method 1
        """
        new_arr = []
        arr = sorted(nums)
        for ele in range(1, len(arr)):
            if arr[ele] == arr[ele-1]:
                if arr[ele] not in new_arr:
                    new_arr.append(arr[ele])
        return(new_arr)

        """
        Method 2
        """
        set_nums = list(set(nums))
        for ele in set_nums:
            nums.remove(ele)
        return(nums)


        """
        Method 3:
        Self hashing
        """

        res = []
        for x in nums:
            if nums[abs(x) - 1] < 0:
                res.append(abs(x))
            else:
                nums[abs(x) - 1] *= -1
        return res
