""" 
# PASCAL'S TRIANGLE

Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
] 
"""

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # Solution 1:
        rows = list()
        if numRows == 0:  # handle base case: layer 0
            return rows
        
        rows.append([1])
        if numRows == 1:  # handle base case: layer 1
            return rows
			
        rows.append([1, 1])
        if numRows == 2:  # handle base case: layer 2
            return rows
        
        for i in range(3, numRows+1):  # here follows the problem's row numbering instead of row indices in list
            i_row = [None] * i  # create row filled with dummy values
            i_row[0] = i_row[-1] = 1  # initialize the head and tail to 1
            for j in range(1, i-1):  # iterate through all the middle entries (non head or tail)
                i_row[j] = rows[i-1-1][j-1]+rows[i-1-1][j]  # -1 twice to handle row i has index (i-1) and to refer to previous row
            rows.append(i_row)
                
        return rows