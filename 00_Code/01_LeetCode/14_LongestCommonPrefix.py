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
        # #Boundary Conditions
        if not strs:
            return ""

        index = 1
        min_len = min([len(ele) for ele in strs])  # #Complexity O(n)

        while index <= min_len:  # #Complexity O(nk)
            if len(set([ele[:index] for ele in strs])) == 1:
                index += 1
            else:
                break

        return strs[0][:index - 1]

        """
        Method 2: Horizontal Scanning

        * Initialize prefix to the first element
        * For each element in the array
        check if prefix[:i] == element[:i] while
        we keep increasing i

        Your runtime beats 49.04 % of python3 submissions.
        """

#         if not strs or strs == [""]:
#             return ""

#         prefix = strs[0]
#         for ele in strs[1:]:
#             index = 1

#             # #Find the common prefix
#             while (index<len(prefix)) and (ele[:index] == prefix[:index]):
#                 index += 1

#             if ele[:index] != prefix[:index]:
#                 index -= 1
#             prefix = prefix[:index]

#         return prefix