""" 
# UNIQUE BINARY SEARCH TREES II

Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    -       -     -      - -      -
     3     2     1      1   3      2
    -     -       -                 -
   2     1         2                 3
 

Constraints:

0 <= n <= 8 
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int):
        return self.trees(1, n)
        
    def trees(self, start, end):
        if start > end:
            return None
        if start == end:
            return [TreeNode(start, None, None)]
        
        result = []
        for i in range(start, end + 1):
            root = i
            left = self.trees(start, root - 1)
            right = self.trees(root + 1, end)
            if left == None:
                for v in right:
                    temp = TreeNode(i, None, v)
                    result.append(temp)
            elif right == None:
                for v in left:
                    temp = TreeNode(i, v, None)
                    result.append(temp)
            else:
                for u in left:
                    for v in right:
                        temp = TreeNode(i, u, v)
                        result.append(temp)    
        
        return result