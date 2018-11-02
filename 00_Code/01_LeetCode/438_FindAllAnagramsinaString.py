"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

"""


class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        """
        Method 1: Sliding window over the array

        * Create a sliding window of size = len(p)
        and traverse over the array s
        * At each window, check if the window and p
        are anagrams of each other or not
        Although this can be done in many ways i.e.
        using a hasp map, counter etc; I'll resort
        to the quick pythonic solution using the
        sorted function.

        Completed 34/36 cases. This should be okay

        Subsetting the window each time is an expensive operation;
        in order to optimize it let's try and use a hash map
        """
        #         res_index = []
        #         k = len(p) # #window length

        #         for index in range(len(s)-k+1):
        #             if sorted(s[index:index+k]) == sorted(p):
        #                 res_index.append(index)

        #         return res_index

        # #Solution from the Discussion forum
        from collections import Counter
        res = []
        pCounter = Counter(p)
        sCounter = Counter(s[:len(p) - 1])
        for i in range(len(p) - 1, len(s)):
            sCounter[s[i]] += 1  # include a new char in the window
            if sCounter == pCounter:  # This step is O(1), since there are at most 26 English letters
                res.append(i - len(p) + 1)  # append the starting index
            sCounter[s[i - len(p) + 1]] -= 1  # decrease the count of oldest char in the window
            if sCounter[s[i - len(p) + 1]] == 0:
                del sCounter[s[i - len(p) + 1]]  # remove the count if it is 0
        return res