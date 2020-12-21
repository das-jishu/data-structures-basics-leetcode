""" 
# BALANCED BINARY TREE

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:

Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:

Input: root = []
Output: true
 
Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104 
"""

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # base case
        if root is None:
            return True
        
        # get height of both left and right subtrees
        l = self.maxdepth(root.left)
        r = self.maxdepth(root.right)
        
        # heights may not differ by no more than 1
        if not abs(l-r) <= 1:
            return False
        
        # check if both left and right subtrees are balanced
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        
    # "maxdepth" problem on leetcode. Finds maximum depth(aka height)
    def maxdepth(self,root):
        if root is None:
            return 0
        
        return max( self.maxdepth(root.left), self.maxdepth(root.right) ) + 1
        