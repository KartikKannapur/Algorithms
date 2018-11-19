"""
Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.


Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
"""


class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """

        """
        Method: Sort + Insert

        * Sort the array based on DESC of h
        and if two people have the same h
        increasing order of k
        * Sorting based on height helps us push
        people into the queue and then sorting
        based on the number of people in front
        with the same height helps us obtain
        the input position

        Time Complexity: O(nlogn) + O(n)*O(n) = O(n^2)

        Your runtime beats 56.66 % of python3 submissions.
        """

        if not people:
            return []

        people_sorted = sorted(people, key=lambda ele: (-ele[0], ele[1]))
        # print(people_sorted)

        res = []
        for ele in people_sorted:
            res.insert(ele[1], ele)
            # print(res)

        return res