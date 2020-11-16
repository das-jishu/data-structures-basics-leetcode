""" 
# CREATE BINARY TREE FROM POSTORDER AND INORDER

Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
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
    def buildTree(self, inorder, postorder) -> TreeNode:
        if len(postorder) == 0:
            return None
        return self.tree(postorder, inorder)
        
    def tree(self, post, inorder):
        if len(post) < 1:
            return None
        if len(post) == 1:
            return TreeNode(post[0], None, None)
        
        root = post[-1]
        index = inorder.index(root)
        
        x = self.tree(post[:index], inorder[:index])
        y = self.tree(post[index:len(post)-1], inorder[index+1:])
        return TreeNode(root, x, y)