""" 
# MAXIMUM DEPTH OF BINARY TREE

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:

Input: root = [1,null,2]
Output: 2

Example 3:

Input: root = []
Output: 0

Example 4:

Input: root = [0]
Output: 1
 
Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100 
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.depth = 0
        
    def maxDepth(self, root: TreeNode) -> int:
        self.find(root, 0)
        return self.depth
        
    def find(self, root, count):
        if not root:
            self.depth = max(self.depth, count)
            return
            
        self.find(root.left, count + 1)
        self.find(root.right, count + 1)