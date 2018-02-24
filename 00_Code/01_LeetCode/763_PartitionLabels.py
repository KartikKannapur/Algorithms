"""
A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
"""


class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """

        """
        Method 1: Overlapping Intervals
        116 / 116 test cases passed.
        Status: Accepted
        Runtime: 46 ms
        """

        d = {}

        for index, letter in enumerate(S):
            if letter in d:
                d[letter][1] = index
            else:
                d[letter] = [index, index]

        d = sorted(d.values(), key=lambda value: value[0])

        res = [(d[0])]

        for elem in d[1:]:
            res_end = res[-1]

            if res_end[0] <= elem[0] <= res_end[1]:
                res_end[1] = max(elem[1], res_end[1])
            else:
                res.append(elem)

        result = []
        for ele in res:
            result.append((ele[1] - ele[0] + 1))
        return result



