# #Given an array of numbers nums, in which exactly two elements appear
# #only once and all the other elements appear exactly twice.
# #Find the two elements that appear only once.


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d = {}
        for i in range(0, len(nums)):
            if nums[i] in d:
                del d[nums[i]]
            else:
                d[nums[i]] = 1

        return d.keys()
