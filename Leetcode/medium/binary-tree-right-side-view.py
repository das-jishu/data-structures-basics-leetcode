""" 
# BINARY TREE RIGHT SIDE VIEW

Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 -  -
2     3         <---
 -      -
  5       4       <--- 
  
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: TreeNode):
        
        if not root:
            return []
        q = [root]
        res = [root.val]
        while len(q) > 0:
            q2 = []
            while len(q) > 0:
                temp = q.pop(0)
                if temp.left:
                    q2.append(temp.left)
                if temp.right:
                    q2.append(temp.right)
            
            if len(q2) > 0:
                res.append(q2[-1].val)
            q = q2
            
        return res