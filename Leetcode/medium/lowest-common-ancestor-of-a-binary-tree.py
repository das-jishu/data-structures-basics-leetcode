""" 
# LOWEST COMMON ANCESTOR OF A BINARY TREE

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the tree.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.traverse = []
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.inorder(root)
        
        while True:
            x = self.traverse.index(root.val)
            left = self.traverse[:x]
            right = self.traverse[x+1:]
            
            if root.val in [p.val, q.val]:
                return root
            
            if (p.val in left and q.val in right) or (q.val in left and p.val in right):
                return root
            
            if p.val not in left and q.val not in left:
                root = root.right
                self.traverse = right
                
            else:
                root = root.left
                self.traverse = left   
        
    def inorder(self, root):
        stack = []
        temp = root
        while True:
            if temp:
                stack.append(temp)
                temp = temp.left
                continue
                
            if len(stack) == 0:
                break     
            x = stack.pop()
            self.traverse.append(x.val)
            temp = x.right