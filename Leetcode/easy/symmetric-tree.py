""" 
# SYMMETRIC TREE

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   - -
  2   2
 - - - -
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   - -
  2   2
   -   -
   3    3
 

Follow up: Solve it both recursively and iteratively. 
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.check(root, root)
    
    def check(self, l, r):
        if not l and not r:
            return True
        if not l and r:
            return False
        if l and not r:
            return False
        
        if l.val != r.val:
            return False
        
        return self.check(l.left, r.right) and self.check(l.right, r.left)
        
        