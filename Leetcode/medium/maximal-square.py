"""
# MAXIMAL SQUARE

Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

 

Example 1:


Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4
Example 2:


Input: matrix = [["0","1"],["1","0"]]
Output: 1
Example 3:

Input: matrix = [["0"]]
Output: 0
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] is '0' or '1'.
"""

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        m = len(matrix)
        n = len(matrix[0])
        table = [[0 for _ in range(n)] for _ in range(m)]
        maximum = 0
        
        for i in range(m):
            table[i][0] = int(matrix[i][0])
            maximum = max(maximum, table[i][0])
            
        for i in range(n):
            table[0][i] = int(matrix[0][i])
            maximum = max(maximum, table[0][i])
            
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '0':
                    continue
                table[i][j] = min(table[i - 1][j], table[i][j - 1], table[i - 1][j - 1]) + 1
                maximum = max(maximum, table[i][j])
    
        for row in table:
            print(row)
        return maximum ** 2
        