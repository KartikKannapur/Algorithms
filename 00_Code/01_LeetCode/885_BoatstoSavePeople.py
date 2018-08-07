"""
The i-th person has weight people[i], and each boat can carry a maximum weight of limit.

Each boat carries at most 2 people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.  (It is guaranteed each person can be carried by a boat.)



Example 1:

Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)
Example 2:

Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)
Example 3:

Input: people = [3,5,3,4], limit = 5
Output: 4
Explanation: 4 boats (3), (3), (4), (5)
Note:

1 <= people.length <= 50000
1 <= people[i] <= limit <= 30000
"""


class Solution:
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """

        """
        Method 1:

        * Since we need to iterate through the array and
        find the combination of people[i] that add upto
        or are under the limiting value, we could sort
        the array and the iterate through it by keeping
        a counter
        * Two pointer approach

        77 / 77 test cases passed.
        Status: Accepted
        Runtime: 184 ms
        """

        people.sort()

        start_ptr = 0
        end_ptr = len(people) - 1
        ans = 0

        while start_ptr <= end_ptr:
            ans += 1
            if people[start_ptr] + people[end_ptr] <= limit:
                start_ptr += 1
            end_ptr -= 1
        return ans
