""" 
# WORD SEARCH

Given an m x n board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where "adjacent" cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example 1:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 
Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 200
1 <= word.length <= 103
board and word consists only of lowercase and uppercase English letters. 
"""

class Solution:
    def exist(self, board, word: str) -> bool:
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if self.check(i, j, word, board, m, n): return True
        return False
        
    def check(self, posx, posy, st, board, m, n):
        if posx not in range(m) or posy not in range(n) or board[posx][posy] == None:
            return False
        if board[posx][posy] == st[0] and len(st) == 1:
            return True
        if board[posx][posy] != st[0]:
            return False
        
        board[posx][posy] = None
        if self.check(posx+1, posy, st[1:], board, m, n) or self.check(posx-1, posy, st[1:], board, m, n) or self.check(posx, posy+1, st[1:], board, m, n) or self.check(posx, posy-1, st[1:], board, m, n): return True
        
        board[posx][posy] = st[0]
        return False
    