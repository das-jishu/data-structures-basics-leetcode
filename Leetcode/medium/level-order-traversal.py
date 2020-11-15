""" 
# LEVEL ORDER TRAVERSAL

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   - -
  9  20
    -  -
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
] 
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode):
        if not root:
            return
        q = [root]
        result = []
        
        while len(q) > 0:
            q2 = []
            res = []
            for x in q:
                res.append(x.val)
                if x.left:
                    q2.append(x.left)
                if x.right:
                    q2.append(x.right)
            q = q2
            result.append(res)
            
        return result