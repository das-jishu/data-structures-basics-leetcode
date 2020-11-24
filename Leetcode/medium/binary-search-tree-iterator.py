""" 
# BINARY SEARCH TREE ITERATOR

Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Example:

BSTIterator iterator = new BSTIterator(root);
iterator.next();    // return 3
iterator.next();    // return 7
iterator.hasNext(); // return true
iterator.next();    // return 9
iterator.hasNext(); // return true
iterator.next();    // return 15
iterator.hasNext(); // return true
iterator.next();    // return 20
iterator.hasNext(); // return false
 
Note:

next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
You may assume that next() call will always be valid, that is, there will be at least a next smallest number in the BST when next() is called. 
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = root
        self.items = []
        self.inorder(self.root)
        self.index = 0

    def next(self) -> int:
        """
        @return the next smallest number
        """
        
        val = self.items[self.index]
        self.index += 1
        return val
    
        
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            self.items.append(root.val)
            self.inorder(root.right)
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.index in range(len(self.items))
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()