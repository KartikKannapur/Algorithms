"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""


class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        """
        Method 1: DFS
        Although the logic works
        TLE - 39 / 588 test cases passed.

        Naive BFS failed at the same point as well.
        Then, I added a condition to keep a track of the
        number of levels that BFS runs and to go to the next level
        only if the current number of level is then a global minimum
        TLE - 502 / 588 test cases passed.
        """

        """
        Method 2: Modification of Standard BFS

        """

        # #Boundary Cases
        if n == 1:
            return 1

        # #Generate Perfect Squares Array
        arr_perfect_sq = []
        i = 1
        while i ** 2 <= n:
            arr_perfect_sq.append(i ** 2)
            i += 1

        depth = 1
        queue = [n]

        while queue:
            queue_update = []

            # #Iterate through all elements in the queue
            # #and all elements in the perfect sq. array
            for node in queue:
                for ele in arr_perfect_sq:

                    if node - ele > 0:
                        queue_update.append(node - ele)

                    elif node - ele == 0:
                        return depth
                    else:
                        break
            depth += 1
            queue = queue_update