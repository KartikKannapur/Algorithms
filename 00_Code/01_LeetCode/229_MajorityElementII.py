# #Given an integer array of size n, find all elements that appear
# #more than ⌊ n/3 ⌋ times. The algorithm should run in linear
# #time and in O(1) space.
# #Your runtime beats 82.60 % of python submissions.

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # #Method 1
        return [x for x in set(nums) if nums.count(x) > len(nums) // 3]

        # #Method 2
        arr = []
        for x in set(nums):
            if nums.count(x) > len(nums) // 3:
                arr.append(x)

        return arr