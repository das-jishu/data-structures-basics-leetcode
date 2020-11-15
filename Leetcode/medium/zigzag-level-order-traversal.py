""" 
# ZIGZAG LEVEL ORDER TRAVERSAL

Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   - -
  9  20
    -  -
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
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
    def zigzagLevelOrder(self, root: TreeNode):
        if not root:
            return
        q = [root]
        result = []
        i = 1
        
        while len(q) > 0:
            q2 = []
            res = []
            for x in q[::i]:
                res.append(x.val)
                if i == 1:
                    if x.left:
                        q2.append(x.left)
                    if x.right:
                        q2.append(x.right)
                
                else:
                    if x.right:
                        q2.insert(0, x.right)
                    if x.left:
                        q2.insert(0, x.left)
                        
            q = q2
            i = i * -1
            result.append(res)
            
        return result