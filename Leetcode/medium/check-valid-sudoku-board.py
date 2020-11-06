""" 
# CHECK VALIDITY OF SUDOKU BOARD

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
 
Example 1:


Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 
Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'. 
"""

def isValidSudoku(board):
    i, j = 0, 0
    
    while i < 9:
        visited = set()
        j = 0
        while j < 9:
            temp = board[i][j]
            if temp in visited:
                return False
            
            if temp != ".":
                visited.add(temp)
            j += 1
        
        i += 1
    
    i = 0
    while i < 9:
        visited = set()
        j = 0
        while j < 9:
            temp = board[j][i]
            if temp in visited:
                return False
            
            if temp != ".":
                visited.add(temp)
            j += 1
        
        i += 1
        
    i = 0
    j = 0
    while i < 9:
        j = 0
        while j < 9:
            visited = set()
            k = i
            l = j
            while k < i + 3:
                l = j
                while l < j + 3:
                    temp = board[k][l]
                    if temp in visited:
                        return False

                    if temp != ".":
                        visited.add(temp)
                    l += 1

                k += 1
                
            j += 3
        i += 3
        
    return True