# #Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
# #Find all unique triplets in the array which gives the sum of zero.
# #Your runtime beats 72.89 % of python submissions.

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # #Method 1
        from itertools import combinations

        arr = []
        for ele in combinations(nums, 3):
            if sum(ele) == 0:
                arr.append(ele)

        return(list((set([tuple(sorted(i)) for i in arr]))))

    def threeSum(self, nums):

        arr_result = []
        # #Sort the array so that we can selectively find the
        # #three numbers that add upto zero
        nums.sort()

        for i in range(len(nums) - 2):
            # #i>0 to handle a particular test case
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:

                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    arr_result.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1

                    l += 1;
                    r -= 1

        return arr_result