"""
Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.  It is guaranteed there is at least one word that isn't banned, and that the answer is unique.

Words in the list of banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not case sensitive.  The answer is in lowercase.

Example:
Input:
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
Output: "ball"
Explanation:
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph.
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"),
and that "hit" isn't the answer even though it occurs more because it is banned.

"""


class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """

        """
        Method 1:

        * Use regex to clean the input string
        * Split the string based on space and add the words
        to a hash map
        * Sort the keys by value in reverse order

        Your runtime beats 82.78 % of python3 submissions.
        """

        import re
        d = {}
        # #Create a counter-dictionary
        paragraph = re.sub('[^a-zA-Z]+', ' ', paragraph)

        for word in paragraph.lower().split():
            if word in d:
                d[word] += 1
            else:
                d[word] = 1

        # #Sort by value in the reverse order
        for word, count in sorted(d.items(), key=lambda ele: ele[1], reverse=True):
            if word not in banned:
                return word
        return -1