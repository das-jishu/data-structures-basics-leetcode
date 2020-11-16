""" 
# PATH SUM II

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     - -
    4   8
   -   - -
  11  13  4
 -  -    - -
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
] 
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, sum: int):
        result = self.check(root, sum)
        return [re[::-1] for re in result]
        
    def check(self, root, s):
        if not root:
            return []
        
        if not root.left and not root.right:
            if root.val == s:
                return [[root.val]]
            else:
                return []
            
        res = []
        target = s - root.val
        left = self.check(root.left, target)
        right = self.check(root.right, target)
        left.extend(right)
        if len(left) == 0:
            return []
        for x in left:
            x.append(root.val)
            res.append(x)
            
        return res