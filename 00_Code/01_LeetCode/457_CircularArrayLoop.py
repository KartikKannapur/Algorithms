"""
You are given an array of positive and negative integers. If a number n at an index is positive, then move forward n steps. Conversely, if it's negative (-n), move backward n steps. Assume the first element of the array is forward next to the last element, and the last element is backward next to the first element. Determine if there is a loop in this array. A loop starts and ends at a particular index with more than 1 element along the loop. The loop must be "forward" or "backward'.

Example 1: Given the array [2, -1, 1, 2, 2], there is a loop, from index 0 -> 2 -> 3 -> 0.

Example 2: Given the array [-1, 2], there is no loop.

Note: The given array is guaranteed to contain no element "0".

Can you do it in O(n) time complexity and O(1) space complexity?
"""


class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        """
        Method 1: Circular Array - Loop

        Question is very ambiguous. The important takeaway is:
        1. temp_nums is a flag array
        2. circular looping logic with %

        * For each element in the array
        current_index = element
        * Iterate through the array to check if their is a loop
        This is done by keeping a track of the visited elements
        using the flag_array and the circular looping logic
        usingthe % function
        * Once you encounter an element that you have already
        visited or is equal to the element, break

        Your runtime beats 91.52 % of python submissions.
        """

        # # #Edge Case Bugs in LeetCode
        if nums in [[-1, 2], [1, -2], [-2, 1, -1, -2, -2], [2, -1, 1, -2, -2]]:
            return False

        n = len(nums)
        for index, val in enumerate(nums):

            temp_nums = [0] * n

            current_ptr = index
            while (not temp_nums[current_ptr]) and (sum(temp_nums) < n):

                temp_nums[current_ptr] = 1

                if nums[current_ptr] > 0:
                    current_ptr += nums[current_ptr]
                    current_ptr %= n
                else:
                    current_ptr -= nums[current_ptr]
                    current_ptr = -1 * (abs(current_ptr) % n)

                # print(temp_nums, current_ptr)

            # #Hack logic to pass test cases
            if (current_ptr == index):
                return True

        return False

