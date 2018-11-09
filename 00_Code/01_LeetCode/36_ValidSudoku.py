"""
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

A partially filled sudoku which is valid.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'
"""


class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        """
        Method 1: Brute Force - General Logic

        - Check if each row is valid
        - Check if each column is valid
        - Create a sub-square and check if each sub-square is valid

        Your runtime beats 17.21 % of python3 submissions.
        """

        """
        Method 2: Hash set

        - Check if each row has a unique value: (i, val)
        - Check if each col has a unique value: (val, j)
        - Check if each sub-square has a unique value(i/3, j/3, val)

        Your runtime beats 91.20 % of python submissions.
        """
        s = set()

        for i in range(len(board)):
            for j in range(len(board)):

                if board[i][j] != ".":
                    if ((i, board[i][j]) in s) or ((board[i][j], j) in s) or ((i / 3, j / 3, board[i][j]) in s):
                        return False

                    s.add((i, board[i][j]))
                    s.add((board[i][j], j))
                    s.add((i / 3, j / 3, board[i][j]))
        return True