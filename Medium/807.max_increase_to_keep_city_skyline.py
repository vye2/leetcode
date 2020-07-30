# In a 2 dimensional array grid, each value grid[i][j] represents the height of a building located there. We are allowed to increase the height of any number of buildings, by any amount (the amounts can be different for different buildings). Height 0 is considered to be a building as well.
#
# At the end, the "skyline" when viewed from all four directions of the grid, i.e. top, bottom, left, and right, must be the same as the skyline of the original grid. A city's skyline is the outer contour of the rectangles formed by all the buildings when viewed from a distance. See the following example.
#
# What is the maximum total sum that the height of the buildings can be increased?
#
# Example:
# Input: grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
# Output: 35
# Explanation:
# The grid is:
# [ [3, 0, 8, 4],
#   [2, 4, 5, 7],
#   [9, 2, 6, 3],
#   [0, 3, 1, 0] ]
#
# The skyline viewed from top or bottom is: [9, 4, 8, 7]
# The skyline viewed from left or right is: [8, 7, 9, 3]
#
# The grid after increasing the height of buildings without affecting skylines is:
#
# gridNew = [ [8, 4, 8, 7],
#             [7, 4, 7, 7],
#             [9, 4, 8, 7],
#             [3, 3, 3, 3] ]
#
# Notes:
#
# 1 < grid.length = grid[0].length <= 50.
# All heights grid[i][j] are in the range [0, 100].
# All buildings in grid[i][j] occupy the entire grid cell: that is, they are a 1 x 1 x grid[i][j] rectangular prism.


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        #check all four sides, and find suitable maxes?
        #any grid[i][j] must be smaller than the max of the current row.
        #if grid[i][j] greater than all of its row, and column, next
        #grid[i][j] will be the lesser max between rows and columns.


        total = 0
        # maxRows = list(map(max, grid))
        # maxCols = list(map(max, zip(*grid)))
        maxRows = [max(grid[rowInd]) for rowInd in range(len(grid))]
        maxCols = [max([c[colInd] for c in grid]) for colInd in range(len(grid[0]))]

        for maxRowInd in range(len(maxRows)):
            for maxColInd in range(len(maxCols)):
                newHeight = min(maxRows[maxRowInd], maxCols[maxColInd])

                total += (newHeight - grid[maxRowInd][maxColInd])

        return total
