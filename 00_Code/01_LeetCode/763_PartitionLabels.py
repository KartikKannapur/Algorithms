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
        Method 1: Merge Overlapping Intervals

        * Create a Hash Map with a nice schema
        {letter: [first_occur_index, last_occur_index]}
        * Like in all other overlapping interval
        problems, we need to sort the hash map
        based on the first_occur_index

        [(u'a', [0, 8]),(u'b', [1, 5]),(u'c', [4, 7]),(u'd', [9, 14])]
        * Merge overlapping intervals and append the
        non-overlapping interval to the res array

        * The last step is to count the number of
        characters in each interval

        Your runtime beats 97.01 % of python submissions.

        Time Complexity: O(nlogn)
        """
        # #Create a Hash Map with a nice schema - O(n)
        d = {}
        for index, letter in enumerate(S):
            if letter in d:
                d[letter][1] = index  # #Update the latest index
            else:
                d[letter] = [index, index]

        # #Sort the Hash Map based on first_occur_index - O(nlogn)
        d = sorted(d.items(), key=lambda ele: ele[1][0])

        # #Merge Overlapping Intervals - O(n)
        res = [d[0][1]]
        for ele in d[1:]:
            if res[-1][0] < ele[1][0] < res[-1][1]:
                res[-1][1] = max(res[-1][1], ele[1][1])
            else:
                res.append(ele[1])

        return [(ele[1] - ele[0] + 1) for ele in res]
