""" 
# UNIQUE PATHS

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Example 1:


Input: m = 3, n = 7
Output: 28

Example 2:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

Example 3:

Input: m = 7, n = 3
Output: 28

Example 4:

Input: m = 3, n = 3
Output: 6
 
Constraints:

1 <= m, n <= 100
It's guaranteed that the answer will be less than or equal to 2 * 109. 
"""

def uniquePaths(m: int, n: int) -> int:
    known = [[None for _ in range(0, n)] for _ in range(0, m)]
    return unique(0, 0, m, n, known)
    
def unique(posx, posy, m, n, known):
    if posx == m - 1 and posy == n - 1:
        return 1
    if posx >= m or posy >= n:
        return 0
    
    if known[posx][posy] != None:
        return known[posx][posy]
    
    count = unique(posx + 1, posy, m, n, known) + unique(posx, posy + 1, m, n, known)
    known[posx][posy] = count
    return count