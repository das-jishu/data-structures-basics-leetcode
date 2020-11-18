""" 
# SURROUNDED REGIONS

Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically. 
"""

class Solution:
    def __init__(self):
        self.visited = set()
        
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        m = len(board)
        if m < 1:
            return
        n = len(board[0])
        if n < 1:
            return
        
        for i in range(m):
            if board[i][0] == "O":
                self.mark(board,i,0)
            if board[i][n-1] == "O":
                self.mark(board,i,n-1)
                
        for j in range(n):
            if board[0][j] == "O":
                self.mark(board,0,j)
            if board[m-1][j] == "O":
                self.mark(board,m-1,j)
                
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and (i,j) not in self.visited:
                    board[i][j] = "X"
        
    def mark(self, b, x, y):
        if x < 0 or x >= len(b) or y < 0 or y >= len(b[0]) or b[x][y] == "X" or (x,y) in self.visited:
            return
        
        self.visited.add((x, y))
        self.mark(b, x-1, y)
        self.mark(b, x+1, y)
        self.mark(b, x, y+1)
        self.mark(b, x, y-1)
        
        
                        