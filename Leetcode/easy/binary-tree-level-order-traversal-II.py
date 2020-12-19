""" 
# BINARY TREE LEVEL ORDER TRAVERSAL II

Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   - -
  9  20
    -  -
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
] 
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrderBottom(self, root: TreeNode):
        if not root:
            return []
        queue = [root]
        res = [[root.val]]
        while queue:
            q2 = []
            t = []
            while queue:
                temp = queue.pop(0)
                if temp.left:
                    q2.append(temp.left)
                    t.append(temp.left.val)
                if temp.right:
                    q2.append(temp.right)
                    t.append(temp.right.val)
            if t:
                res.append(t)
            queue = q2
            
        return res[::-1]