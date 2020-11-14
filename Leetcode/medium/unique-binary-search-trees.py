""" 
# UNIQUE BINARY SEARCH TRESS

Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    -       -     -     -   -      -
     3     2    1      1      3      2
    -     -       -                    -
   2     1          2                    3
 

Constraints:

1 <= n <= 19 
"""

class Solution:
    def numTrees(self, n: int) -> int:
        dic = {}
        return self.trees(1, n, dic)
        
    def trees(self, start, end, dic):
        if start > end:
            return 0
        if start == end:
            return 1
        
        if (start, end) in dic:
            return dic[(start, end)]
        
        count = 0
        for i in range(start, end + 1):
            root = i
            left = self.trees(start, root - 1, dic)
            right = self.trees(root + 1, end, dic)
            if left == 0:
                count += right
            elif right == 0:
                count += left
            else:
                count += left * right
        
        dic[(start, end)] = count
        return count