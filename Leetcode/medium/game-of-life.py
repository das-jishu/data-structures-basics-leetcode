""" 
# GAME OF LIFE

According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

Example:

Input: 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output: 
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
Follow up:

Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems? 
"""

class Solution:
    def gameOfLife(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.modify(board, 0, 0, set())
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "K":
                    board[i][j] = 1
                    
                if board[i][j] == "M":
                    board[i][j] = 0
        
    def modify(self, board, i, j, visited):
        if i >= len(board) or j >= len(board[0]) or (i, j) in visited:
            return
        
        visited.add((i, j))
        a = self.getNeighbors(board, i, j)
        ones = a.count(1) + a.count("M")
        if board[i][j] == 0 and ones == 3:
            board[i][j] = "K"
            
        if board[i][j] == 1:
            if ones < 2 or ones > 3:
                board[i][j] = "M"
        
        self.modify(board, i + 1, j, visited)
        self.modify(board, i, j + 1, visited)
        
    def getNeighbors(self, board, i, j):
        posx = [i - 1, i + 1, i]
        if i == 0:
            posx.remove(i - 1)
        if i == len(board) - 1:
            posx.remove(i + 1)
            
        posy = [j + 1, j - 1, j]
        if j == 0:
            posy.remove(j - 1)
        if j == len(board[0]) - 1:
            posy.remove(j + 1)
            
        res = []
        for x in posx:
            for y in posy:
                if x == i and y == j:
                    continue
                res.append(board[x][y])
                
        return res