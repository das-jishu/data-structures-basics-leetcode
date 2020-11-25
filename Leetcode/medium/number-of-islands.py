""" 
# NUMBER OF ISLANDS

Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'. 
"""

class Solution:
    def numIslands(self, grid) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    self.traverse(grid, i, j)
                    
        return count
        
    def traverse(self, grid, i, j):
        #print("i:", i, "j:", j)
        if i not in range(len(grid)) or j not in range(len(grid[0])):
            return
        
        if grid[i][j] == "0" or grid[i][j] == "K":
            return
        
        grid[i][j] = "K"
        self.traverse(grid, i + 1, j)
        self.traverse(grid, i - 1, j)
        self.traverse(grid, i, j + 1)
        self.traverse(grid, i, j - 1)
        