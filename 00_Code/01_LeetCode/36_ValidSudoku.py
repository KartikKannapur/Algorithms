"""
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

A partially filled sudoku which is valid.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'
"""

from collections import Counter


class Solution:
    def isValidRowColumnSquare(self, arr):
        """
        Custom method to check if a row, column or square
        is valid or not.
        A simpled Counter object is used and looped over,
        if the key != '.' and the value > 1, then we
        return False
        """
        temp_ctr = Counter(arr)
        for k, v in temp_ctr.items():
            # print(k,v)
            if k != '.' and v > 1:
                return False

        return True

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
        for row in board:
            if not self.isValidRowColumnSquare(row):
                return False

        for index in range(0, len(board)):
            row_transpose = [board[col][index] for col in range(0, len(board[0]))]
            if not self.isValidRowColumnSquare(row_transpose):
                return False

        for i in (0, 3, 6):
            for j in (0, 3, 6):
                square = [board[row_idx][col_idx] for row_idx in range(i, i + 3) for col_idx in range(j, j + 3)]
                if not self.isValidRowColumnSquare(square):
                    return False

        return True