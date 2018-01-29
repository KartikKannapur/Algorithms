"""
Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence ai, aj, ak such that i < j < k and ai < ak < aj. Design an algorithm that takes a list of n numbers as input and checks whether there is a 132 pattern in the list.

Note: n will be less than 15,000.

Example 1:
Input: [1, 2, 3, 4]

Output: False

Explanation: There is no 132 pattern in the sequence.
Example 2:
Input: [3, 1, 4, 2]

Output: True

Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
Example 3:
Input: [-1, 3, 2, 0]

Output: True

Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
"""


class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        """
        Method 1:
        Your runtime beats 71.91 % of python submissions.
        """
        if len(set(nums)) < 3:
            return False

        stack = [[nums[0], nums[0]]]
        min_value = nums[0]

        for ele in nums[1:]:

            if ele >= stack[0][1]:
                stack = [[min_value, ele]]
            elif ele < min_value:
                stack.append([ele, ele])
                min_value = ele
            elif ele == min_value:
                continue
            else:
                while stack and ele > stack[-1][0]:
                    if ele < stack[-1][1]:
                        return True
                    else:
                        stack.pop()
                stack.append([min_value, ele])

        return False