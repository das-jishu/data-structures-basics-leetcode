""" 
# MAX AREA OF ISLAND

Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.

Example 2:

[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.
"""

class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        m = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    m = max(m, self.traverse(grid, x, y))
                    
        return m
        
    def traverse(self, grid, posx, posy):
        if posx not in range(len(grid)) or posy not in range(len(grid[0])) or grid[posx][posy] == "K" or grid[posx][posy] == 0:
            return 0
        
        grid[posx][posy] = "K"
        return 1 + self.traverse(grid, posx + 1, posy) + self.traverse(grid, posx - 1, posy) + self.traverse(grid, posx, posy + 1) + self.traverse(grid, posx, posy - 1)
        
        