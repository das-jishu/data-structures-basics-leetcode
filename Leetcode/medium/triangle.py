""" 
# TRIANGLE

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle. 
"""

class Solution:
    def minimumTotal(self, triangle) -> int:
        space = triangle[-1]
        len_space = len(space)
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                space[j] = min(space[j], space[j + 1]) + triangle[i][j]
        return space[0]