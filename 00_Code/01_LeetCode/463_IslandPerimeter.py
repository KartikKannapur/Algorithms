"""
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0
represents water. Grid cells are connected horizontally/vertically (not diagonally).
 The grid is completely surrounded by water, and there is exactly one island
 (i.e., one or more connected land cells). The island doesn't have "lakes"
 (water inside that isn't connected to the water around the island). One cell is a square with side length 1.
 The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Your runtime beats 74.00 % of python submissions.
"""


class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #Method 1:
        dict_island = {}

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dict_island[(i,j)] = 1

        main_counter = 0
        for k, v in dict_island.items():
            arr_count = ([1 for ele in [(k[0] + i, k[1]) for i in [1, -1]] + \
              [(k[0], k[1] + i) for i in [1, -1]] if ele in dict_island])
            main_counter += (4 - sum(arr_count))

        return(main_counter)

        # #Method 2
        # #Your runtime beats 74.00 % of python submissions.
        main_counter = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    num = 0
                    if (i < len(grid) - 1) and (grid[i + 1][j]) == 1: num += 1
                    if (j < len(grid[i]) - 1) and (grid[i][j + 1] == 1): num += 1
                    main_counter += 4 - 2 * num
        return (main_counter)
