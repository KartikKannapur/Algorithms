"""
Initially, there is a Robot at position (0, 0). Given a sequence
of its moves, judge if this robot makes a circle, which means it
moves back to the original place.
The move sequence is represented by a string. And each move is
represent by a character. The valid robot moves are R (Right),
L (Left), U (Up) and D (down). The output should be true or false
representing whether the robot makes a circle.
Example 1:
Input: "UD"
Output: true
Example 2:
Input: "LL"
Output: false

Your runtime beats 77.72 % of python submissions.
"""


class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """

        """
        Method 1:

        * The robot moves back to its initial position
        IF count of left moves == count of right moves
        IF count of up moves == count of down moves

        * We could assign a cost to each of these operations
        say +1/-1 scheme and compute the cost of traversal
        map_path = {"U" : 1, "D": -1, "R": 1,  "L": -1,}

        Your runtime beats 73.96 % of python3 submissions.
        """

        # map_path = {"U" : 1, "D": -1, "R": 1,  "L": -1,}
        # return sum([map_path[var_move] for var_move in moves]) == 0


        """
        Method 2:
        * Cost computation is done via a count operation
        in a single line

        Your runtime beats 82.29 % of python3 submissions.
        """
        return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')