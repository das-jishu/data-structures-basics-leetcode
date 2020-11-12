import copy
def exist(board, word) -> bool:
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                print("CURRENT BOARD\n", board)
                if board[i][j] == word[0]:
                    print("CHECKING", i, j)
                    if check(i, j, word, copy.deepcopy(board), m, n):
                        return True
        return False
        
def check(posx, posy, st, b, m, n):
    print("BOARD:", b, "SEARCHING:",st[0])
    if posx not in range(m) or posy not in range(n) or b[posx][posy] == None:
        print("Returning false")
        return False
    if b[posx][posy] == st[0] and len(st) == 1:
        return True
    if b[posx][posy] != st[0]:
        return False
    
    b[posx][posy] = None
    print("b at posx posy:", b)
    return check(posx+1, posy, st[1:], copy.deepcopy(b), m, n) or check(posx-1, posy, st[1:], copy.deepcopy(b), m, n) or check(posx, posy+1, st[1:], copy.deepcopy(b), m, n) or check(posx, posy-1, st[1:], copy.deepcopy(b), m, n)

if __name__ == "__main__":
    print(exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]],"ABCESEEEFS"))