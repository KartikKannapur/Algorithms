"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
"""


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        """
        Method 1: Dynamic Programming
        72 / 75 test cases passed.
        """

        if len(set(nums)) == 1:
            return True

        global flag
        flag = False

        def myJumper(nums, current_ptr, destination):
            global flag
            # print((nums, current_ptr, destination))
            if current_ptr >= destination:
                return True

            val = nums[current_ptr]
            for ele in range(1,val+1):
                # print((nums, current_ptr+ele, destination))
                flag = flag or myJumper(nums, current_ptr+ele, destination)

            return flag
        current_ptr = 0
        destination = len(nums)-1

        return myJumper(nums, current_ptr, destination)

        """
        Method 2:
        Your runtime beats 35.95 % of python submissions.
        """
        max_reach, n = 0, len(nums)
        for i, x in enumerate(nums):
            if max_reach < i: return False
            if max_reach >= n - 1: return True
            max_reach = max(max_reach, i + x)



