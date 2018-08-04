"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""


class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        """
        Method 1: Using set() on each word/string

        * sorted(ele) create a unique ordering
        * we use this ordering as the key in the hash map

        Your runtime beats 86.77 % of python3 submissions.
        """
        d = dict()

        for ele in strs:
            ordered_word = "".join(sorted(ele))
            if ordered_word in d:
                d[ordered_word].append(ele)
            else:
                d[ordered_word] = [ele]

        return [v for k, v in d.items()]