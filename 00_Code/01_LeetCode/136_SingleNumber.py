# #Given an array of integers, every element appears twice except for one. Find that single one.
# #Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory
# #Your runtime beats 91.85 % of python submissions

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Method 1:
        d = {}

        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        return dict((v,k) for k,v in d.items()).get(1)

        #Method 2:
        d ={}
        for i in range(0, len(nums)):
            if nums[i] in d:
                del d[nums[i]]
            else:
                d[nums[i]] = 1

        return d.popitem()[0]

        # #Method 3:
        return 2 * sum(set(nums)) - sum(nums)