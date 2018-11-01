"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        """
        Algorithm: DFS

        * Iterate through each element in the 2D grid
        * If the element is a 1, then recursively call the DFS
        function horizontally and vertically; while making replacing
        the element with # once it has been visited
        * This way we start with the element that is a 1 and 
        cover the entire island with #
        * We then continue traversing the entire grid and 
        we encounter another 1, then we increment the counter
        and restart the DFS process

        Reference Video: https://www.youtube.com/watch?v=CLvNe-8-6s8

        Your runtime beats 92.20 % of python submissions.
        """

        def dfs(grid, i, j):
            # #Keep a track of indices as well as the value in the index
            if (0 <= i < len(grid)) and (0 <= j < len(grid[0])) and (grid[i][j] == "1"):
                grid[i][j] = "#"
                dfs(grid, i + 1, j)
                dfs(grid, i - 1, j)
                dfs(grid, i, j + 1)
                dfs(grid, i, j - 1)
            else:
                return None

        # #Boundary Condition
        if not grid:
            return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(grid, i, j)  # #Convert all vertical and horizontal elements to #
                    count += 1  # #Increment the counter for a new island
        return count