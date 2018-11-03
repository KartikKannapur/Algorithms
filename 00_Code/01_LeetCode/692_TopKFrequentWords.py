"""
Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1:
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.
Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Input words contain only lowercase letters.
Follow up:
Try to solve it in O(n log k) time and O(n) extra space.
"""

from collections import Counter


class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """

        """
        Method 1: Hash Map

        * Use the built-in Counter function
        * Sort based on both key and value

        Your runtime beats 75.31 % of python3 submissions

        Time Complexity: O(NlogN), where N is the length of words. 
        We count the frequency of each word in O(N) time, 
        then we sort the given words in O(NlogN) time
        """
        # words_counter = Counter(words).items()
        # words_counter_sorted = sorted(words_counter, key=lambda x: (-x[1], x[0]))
        # return [ele[0] for ele in words_counter_sorted[:k]]

        """
        Method 2: Heap
        Your runtime beats 64.98 % of python3 submissions.

        Time Complexity: O(Nlogk), where N is the length of words. 
        We count the frequency of each word in O(N) time, 
        then we add N words to the heap, each in O(logk) time. 
        Finally, we pop from the heap up to k times.
        """
        words_counter = Counter(words)
        heap = [(-freq, word) for word, freq in words_counter.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]