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


class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        # #Method 1:
        map_path = {"U" : 1, "D": -1, "R": 1,  "L": -1,}
        return sum([map_path[var_move] for var_move in moves]) == 0

        # #Method 2:
        return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')