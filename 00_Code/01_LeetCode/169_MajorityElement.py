# #Given an array of size n, find the majority element.
# #The majority element is the element that appears more than ⌊ n/2 ⌋ times.
# #You may assume that the array is non-empty and the majority element
# #always exist in the array.
# #Your runtime beats 89.88 % of python submissions.

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return [x for x in set(nums) if nums.count(x) > len(nums) // 2][0]


