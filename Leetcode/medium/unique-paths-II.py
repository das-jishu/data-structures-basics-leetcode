""" 
# UNIQUE PATHS II

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and space is marked as 1 and 0 respectively in the grid.

Example 1:


Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

Example 2:

Input: obstacleGrid = [[0,1],[0,0]]
Output: 1
 
Constraints:

m == obstacleGrid.length
n == obstacleGrid[i].length
1 <= m, n <= 100
obstacleGrid[i][j] is 0 or 1. 
"""

def uniquePathsWithObstacles(obstacleGrid) -> int: 
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    if obstacleGrid[m - 1][n - 1] == 1:
        return 0
    known = [[None for _ in range(0, n)] for _ in range(0, m)]
    return unique(0, 0, m, n, known, obstacleGrid)

def unique(posx, posy, m, n, known, obstacles):
    if posx == m - 1 and posy == n - 1:
        return 1
    if posx >= m or posy >= n or obstacles[posx][posy] == 1:
        return 0

    if known[posx][posy] != None:
        return known[posx][posy]

    count = unique(posx + 1, posy, m, n, known, obstacles) + unique(posx, posy + 1, m, n, known, obstacles)
    known[posx][posy] = count
    return count