""" 
# SPIRAL MATRIX

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7] 
"""

def spiralOrder(matrix):
    
    res = []
    x = m = len(matrix)
    if x == 0:
        return
    y = n = len(matrix[0])
    if y == 0:
        return
    t = 0
    while len(res) < x * y:
        i = t
        print("t:", t, "m:", m, "n:", n)
        for j in range(t, n):
            res.append(matrix[i][j])

        if len(res) == x * y:
            break
        j = n - 1
        for i in range(t+1, m):
            res.append(matrix[i][j])

        if len(res) == x * y:
            break
        i = m - 1
        for j in range(n - 2, t-1, -1):
            res.append(matrix[i][j])

        if len(res) == x * y:
            break
        j = t
        for i in range(m - 2, t, -1):
            res.append(matrix[i][j])

        t += 1
        m -= 1
        n -= 1
    return res