"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        """
        Method 1:
        * Start at index 1 and iterate through each word and 
        check the prefix of each element. If the prefix is common
        across all words then increment the index

        Your runtime beats 84.98 % of python3 submissions.
        """
        if not strs:
            return ""

        if strs == [""]:
            return ""

        prefix_index = 1
        max_length = max(len(ele) for ele in strs)
        while prefix_index <= max_length and len(set([ele[:prefix_index] for ele in strs])) == 1:
            print(strs[0][:prefix_index])
            prefix_index += 1

        print(prefix_index - 1)
        return strs[0][:prefix_index - 1]