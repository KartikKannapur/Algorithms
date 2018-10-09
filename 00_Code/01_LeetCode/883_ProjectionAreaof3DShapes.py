"""
On a N * N grid, we place some 1 * 1 * 1 cubes that are axis-aligned with the x, y, and z axes.

Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).

Now we view the projection of these cubes onto the xy, yz, and zx planes.

A projection is like a shadow, that maps our 3 dimensional figure to a 2 dimensional plane.

Here, we are viewing the "shadow" when looking at the cubes from the top, the front, and the side.

Return the total area of all three projections.

Example 1:

Input: [[2]]
Output: 5
Example 2:

Input: [[1,2],[3,4]]
Output: 17
Explanation:
Here are the three projections ("shadows") of the shape made with each axis-aligned plane.

Example 3:

Input: [[1,0],[0,2]]
Output: 8
Example 4:

Input: [[1,1,1],[1,0,1],[1,1,1]]
Output: 14
Example 5:

Input: [[2,2,2],[2,1,2],[2,2,2]]
Output: 21


Note:

1 <= grid.length = grid[0].length <= 50
0 <= grid[i][j] <= 50

"""


class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        """
        Algorithm:

        From the top, the shadow made by the shape will be 1 square for each non-zero value.
        From the side, the shadow made by the shape will be the largest value for each row in the grid.
        From the front, the shadow made by the shape will be the largest value for each column in the grid.

        ---------------------------------------------------------------
        The first iteration of my solution was O(n^2) + O(n^2) + O(n^2)
        # #Checking for non-zero values
        var_x = sum([1 for ele in grid for sub_ele in ele if sub_ele])

        # #Checking for values in each column
        var_y = 0
        for index in range(len(grid)):
            var_y += max([grid[ele][index] for ele in range(len(grid))])

        # #Checking for values in each row
        var_z = sum([max(ele) for ele in grid])

        return var_x+var_y+var_z
        ---------------------------------------------------------------

        ---------------------------------------------------------------
        Can we do this with one pass?
        Code below

        Time complexity: O(n^2)
        Space complexity: O(1)
        ---------------------------------------------------------------

        Your runtime beats 100.00 % of python submissions.
        """

        res = 0

        for i in range(len(grid)):
            max_row_wise = 0
            max_col_wise = 0
            for j in range(len(grid)):
                # #Check for non-zero values for the
                # #view from the top
                if grid[i][j]:
                    res += 1

                # #Find the maximum row_wise and col_wise
                # #acorss all the lists in the list of lists
                max_row_wise = max(max_row_wise, grid[i][j])
                max_col_wise = max(max_col_wise, grid[j][i])

            res += (max_row_wise + max_col_wise)

        return res

