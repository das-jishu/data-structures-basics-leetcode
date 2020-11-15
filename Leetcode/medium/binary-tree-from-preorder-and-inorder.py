""" 
# CONSTRUCT BINARY TREE FROM PREORDER AND INORDER

Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   - -
  9  20
    -  -
   15   7 
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        if len(preorder) == 0:
            return None
        return self.tree(preorder, inorder)
        
    def tree(self, pre, inorder):
        if len(pre) < 1:
            return None
        if len(pre) == 1:
            return TreeNode(pre[0], None, None)
        
        root = pre[0]
        index = inorder.index(root)
        
        x = self.tree(pre[1:index+1], inorder[:index])
        y = self.tree(pre[index+1:], inorder[index+1:])
        return TreeNode(root, x, y)
   