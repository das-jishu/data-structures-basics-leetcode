""" 
# MINIMUM DEPTH OF BINARY TREE

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 2

Example 2:

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5

Constraints:

The number of nodes in the tree is in the range [0, 105].
-1000 <= Node.val <= 1000 
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.minimum = 9999999999
        
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.check(root, 1)
        return self.minimum
        
    def check(self, root, value):
        if not root:
            return
        
        if not root.left and not root.right:
            self.minimum = min(self.minimum, value)
            
        else:
            self.check(root.left, value + 1)
            self.check(root.right, value + 1)