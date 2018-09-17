"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.

Your runtime beats 82.75 % of python submissions.
"""


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        Method 1
        O(n) + O(nlogn) = O(nlogn)
        Your runtime beats 52.37 % of python submissions.

        In a single pass, store the index and counts in a dict
        d = {"char" : [first_index, counts]}

        Sort the dict, if counts == 1

        Your runtime beats 73.59 % of python submissions.
        """
        d = {}
        for index, value in enumerate(s):
            if value in d:
                d[value][1] += 1
            else:
                d[value] = [index, 1]

        # #Sort the dict, if counts == 1
        arr = sorted([value[0] for key, value in d.items() if value[1] == 1])
        if arr:
            return arr[0]
        else:
            return -1