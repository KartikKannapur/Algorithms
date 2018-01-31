"""
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.
"""
class Solution:
    # @param {string[]} words
    # @param {string} word1
    # @param {string} word2
    # @return {integer}
    def shortestDistance(self, words, word1, word2):
        index1 = index2 = -1

        for i,j in enumerate(words):
            print(i,j)
            if j == word1:
                index1 = i
            elif j == word2:
                index2 = i

        print(abs(index1-index2))

words =  ["practice", "makes", "perfect", "coding", "makes"]
word1 = "practice"
word2 = "coding"
