def isValidSudoku(board) -> bool:
        # allowed = set("1", "2", "3", "4", "5", "6", "7", "8", "9")
        i, j = 0, 0
        for x in board:
            for y in x:
                print(y,"  ", end="")
            print()
        
        while i < 9:
            visited = set()
            j = 0
            while j < 9:
                temp = board[i][j]
                if temp in visited:
                    print("FALSE IN ROW")
                    return False
                
                if temp != ".":
                    visited.add(board[i][j])
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
                print("i and j == ", i, j)
                visited = set()
                k = i
                l = j
                while k < (i + 3):
                    l = j
                    while l < (j + 3):
                        temp = board[k][l]
                        print("k and l:", k, l)
                        if temp in visited:
                            print("FALSE IN SQUARE")
                            return False

                        if temp != ".":
                            visited.add(temp)
                        l += 1

                    k += 1
                    print("i = ", i, "k = ", k)
                    
                j += 3
            i += 3
            
        return True
                
if __name__ == "__main__":
    print(isValidSudoku([[".",".",".",".",".",".","5",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],["9","3",".",".","2",".","4",".","."],[".",".","7",".",".",".","3",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".","3","4",".",".",".","."],[".",".",".",".",".","3",".",".","."],[".",".",".",".",".","5","2",".","."]]))