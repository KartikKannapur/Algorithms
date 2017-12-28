class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        dict_diff = {}
        
        for elem in range(len(nums)):
            if nums[elem] in dict_diff:
                return([elem, dict_diff[nums[elem]]])
            else:
                dict_diff[target - nums[elem]] = elem
                # print(dict_diff)