"""
A zero-indexed array A of length N contains all integers from 0 to N-1. Find and return the longest length of set S, where S[i] = {A[i], A[A[i]], A[A[A[i]]], ... } subjected to the rule below.

Suppose the first element in S starts with the selection of element A[i] of index = i, the next element in S should be A[A[i]], and then A[A[A[i]]]… By that analogy, we stop adding right before a duplicate element occurs in S.

Example 1:
Input: A = [5,4,0,3,1,6,2]
Output: 4
Explanation:
A[0] = 5, A[1] = 4, A[2] = 0, A[3] = 3, A[4] = 1, A[5] = 6, A[6] = 2.

One of the longest S[K]:
S[0] = {A[0], A[5], A[6], A[2]} = {5, 6, 2, 0}
Note:
N is an integer within the range [1, 20,000].
The elements of A are all distinct.
Each element of A is an integer within the range [0, N-1].

"""


class Solution:
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        """
        Method 1

        853 / 856 test cases passed.
        """
        #         res_length = 0

        #         for index in range(len(nums)):
        #             temp_set = set()
        #             temp_index = index

        #             while temp_index not in temp_set:
        #                 temp_set.add(temp_index)
        #                 temp_index = nums[temp_index]
        #                 # print(temp_set)

        #             res_length = max(res_length, len(temp_set))

        #         return res_length

        """
        Method 2:
        """
        visited = set()
        max_len = 0
        for i in range(0, len(nums)):
            if i not in visited:
                current = set()
                while i not in current:
                    current.add(i)
                    visited.add(i)
                    i = nums[i]
            max_len = max(max_len, len(current))
        return max_len