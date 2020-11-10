""" 
# SPIRAL MATRIX II

Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
] 
"""

def generateMatrix(n: int):
    if n == 0:
        return []

    if n == 1:
        return [[1]]

    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(n):
            matrix[i].append(0)
            
    t = 0
    m = 1
    while n > 1:
        
        i = t
        for j in range(t, n):
            matrix[i][j] = m
            m += 1

        j = n - 1
        for i in range(t+1, n):
            matrix[i][j] = m
            m += 1

        i = n - 1
        for j in range(n - 2, t-1, -1):
            matrix[i][j] = m
            m += 1

        j = t
        for i in range(n - 2, t, -1):
            matrix[i][j] = m
            m += 1    

        t += 1
        n -= 1
        
    return matrix