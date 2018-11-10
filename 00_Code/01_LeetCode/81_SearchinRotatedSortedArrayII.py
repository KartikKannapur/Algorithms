"""
Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Write a function to determine if a given target is in the array.

The array may contain duplicates.

Your runtime beats 70.33 % of python submissions.
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        """
        Method 1: Linear Search
        Your runtime beats 70.33 % of python submissions.
        """

        """
        Method 2:
        Same as Q33. Search in Rotated Sorted Array.

        Your runtime beats 100.00 % of python submissions.
        """
        nums.sort()
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) / 2
            # print(mid, nums[mid])

            if nums[mid] == target:
                return True

            elif nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1


            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return False

