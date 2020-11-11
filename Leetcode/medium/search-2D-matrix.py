""" 
# SEARCH 2D MATRIX

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

Example 1:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 3
Output: true

Example 2:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 13
Output: false

Example 3:

Input: matrix = [], target = 0
Output: false

Constraints:

m == matrix.length
n == matrix[i].length
0 <= m, n <= 100
-104 <= matrix[i][j], target <= 104 
"""

def searchMatrix(matrix, target: int):
        
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return False
    m = len(matrix)
    n = len(matrix[0])
        
    row = 0
    l = 0
    r = m - 1
    while l <= r:
        mid = (l + r) // 2
        if target >= matrix[mid][0] and target <= matrix[mid][n-1]:
            row = mid
            break
        
        if target < matrix[mid][n-1]:
            r = mid - 1
        else:
            l = mid + 1
            
    l = 0
    r = n - 1
    while l <= r:
        mid = (l + r) // 2
        if matrix[row][mid] == target:
            return True
        
        if target < matrix[row][mid]:
            r = mid - 1
        else:
            l = mid + 1
    
    return False