""" 
# FLATTEN BINARY TREE TO LINKED LIST

Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   - -
  2   5
 - -   -
3   4   6
The flattened tree should look like:

1
 -
  2
   -
    3
     -
      4
       -
        5
         -
          6 
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
            #return None
        
        self.flatten(root.left)
        self.flatten(root.right)
        leftTree = root.left
        rightTree = root.right
        root.left = None
        root.right = leftTree
        
        if not leftTree:
            root.right = rightTree
        else:
            while leftTree.right != None:
                leftTree = leftTree.right

            leftTree.right = rightTree

