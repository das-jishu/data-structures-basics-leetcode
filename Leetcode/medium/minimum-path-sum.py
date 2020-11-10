""" 
# MINIMUM PATH SUM

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
 
Example 1:


Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 100 
"""

def minPathSum(grid):
    m = len(grid)
    n = len(grid[0])
    known = [[None for _ in range(0, n)] for _ in range(0, m)]
    return minSum(0, 0, m, n, known, grid)

def minSum(posx, posy, m, n, known, grid):
    if posx == m - 1 and posy == n - 1:
        known[posx][posy] = grid[posx][posy]
        return grid[posx][posy]
    if posx >= m or posy >= n:
        return float('inf')

    if known[posx][posy] != None:
        return known[posx][posy]

    sum1 = minSum(posx + 1, posy, m, n, known, grid)
    sum2 = minSum(posx, posy + 1, m, n, known, grid)
    known[posx][posy] = grid[posx][posy] + min(sum1, sum2)
    return known[posx][posy]

""" 

# MODIFYING GRID IN PLACE FOR LESSER SPACE COMPLEXITY

def minPathSum(self, grid: List[List[int]]) -> int:
        
    # the idea is to start from the right-bottom and come up with BFS?
    # or.. same thing going from left-top to bottom-right.. all sub-matrices are sub-problems of the same problem formulation
    # start from left-top and just add, O(1) space, use the given grid
    # O(mn) time
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i == 0 and j == 0:  # if in starting position
                continue
            if i - 1 < 0:  # if on the top row
                grid[i][j] += grid[i][j-1]
            elif j - 1 < 0:  # if on the leftmost column
                grid[i][j] += grid[i-1][j]
            else:  # otherwise
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
    return grid[-1][-1] 
"""