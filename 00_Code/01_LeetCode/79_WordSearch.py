"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.

"""


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        #         grid = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]

        #         def dfs(i, j, k):
        #             print(i,j, k)

        #             if k >= len(word): # #Indicating that we havea reached the last character
        #                 return True

        #             if (0<=i<len(board)) and (0<=j<len(board[0])) and (not grid[i][j]) and (board[i][j] == word[k]):
        #                 grid[i][j] = 1
        #                 return dfs(i+1, j, k+1) or dfs(i-1, j, k+1) or dfs(i, j+1, k+1) or dfs(i, j-1, k+1)

        #             return False

        #         # #Boundary Condition
        #         if not board:
        #             return False

        #         for i in range(len(board)):
        #             for j in range(len(board[0])):
        #                 if dfs(i, j, 0):
        #                     return True
        #         return False

        def dfs(board, word, i, j, visited, pos=0):
            if pos == len(word):
                return True

            if i < 0 or i == len(board) or j < 0 or j == len(board[0]) or visited.get((i, j)) or word[pos] != board[i][
                j]:
                return False

            visited[(i, j)] = True
            res = dfs(board, word, i, j + 1, visited, pos + 1) \
                  or dfs(board, word, i, j - 1, visited, pos + 1) \
                  or dfs(board, word, i + 1, j, visited, pos + 1) \
                  or dfs(board, word, i - 1, j, visited, pos + 1)
            visited[(i, j)] = False

            return res

        visited = {}

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(board, word, i, j, visited):
                    return True

        return False