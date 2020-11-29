""" 
# COUNT COMPLETE TREE NODES

Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input: 
    1
   - -
  2   3
 - -  -
4  5 6

Output: 6 
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """def __init__(self):
        self.count = 0"""
        
    def countNodes(self, root: TreeNode) -> int:
        # self.calc(root)
        # return self.count
    
        if not root:
            return 0
        
        l = root
        r = root
        depth_left = 1
        depth_right = 1
        while l.left:
            l = l.left
            depth_left += 1
            
        while r.right:
            r = r.right
            depth_right += 1
            
        if depth_left == depth_right:
            return pow(2, depth_left) - 1
        
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
    
    """def calc(self, root):
        if not root:
            return
        
        self.count += 1
        self.calc(root.left)
        self.calc(root.right)"""