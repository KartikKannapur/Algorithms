"""
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

"""


class Solution():
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        """
        Method 1:

        * Create two Counters - for each nums1 and num2
        * Iterate over one of the counter objects and check if the same
        key exists in the other counter object. (Intersection)
        * IF it does, take the minimum of the values
        * Append the values to the res array

        Your runtime beats 98.97 % of python3 submissions.
        """
        from collections import Counter
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)

        res = []
        for key, value in counter2.items():
            if key in counter1:
                for _ in range(min(value, counter1[key])):
                    res.append(key)

        return res
