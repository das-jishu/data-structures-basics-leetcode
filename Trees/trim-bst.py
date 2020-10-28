
######################################
# CHECK AGAIN. NOT WORKING ACCORDINGLY
######################################

class Node(object):
    def __init__(self, val, parent=None):
        self.val = val
        self.leftChild = None
        self.rightChild = None
        self.parent = parent

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    def getParent(self):
        return self.parent
    
    def isRoot(self):
        return self.parent != None

    def hasLeftChild(self):
        return self.leftChild != None

    def hasRightChild(self):
        return self.rightChild != None

    def hasBothChildren(self):
        return self.hasLeftChild() and self.hasRightChild()

    def hasOneChild(self):
        return self.hasLeftChild() or self.hasRightChild()

class BinarySearchTree(object):
    def __init__(self):
        self.size = 0
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = Node(val)
        else:
            temp = self.root
            done = False
            while not done:
                if val < temp.val:
                    if temp.hasLeftChild():
                        temp = temp.getLeftChild()
                    else:
                        temp.leftChild = Node(val, temp)
                        done = True
                else:
                    if temp.hasRightChild():
                        temp = temp.getRightChild()
                    else:
                        temp.rightChild = Node(val, temp)
                        done = True
        self.size += 1

    def inorder(self, root):
        if root:
            self.inorder(root.leftChild)
            print(root.val, end=" ")
            self.inorder(root.rightChild)

    def trimBST(self, tree, minVal, maxVal):
        if not tree:
            return
        
        tree.leftChild = self.trimBST(tree.leftChild, minVal, maxVal)
        tree.rightChild = self.trimBST(tree.rightChild, minVal, maxVal)
        if minVal <= tree.val <= maxVal:
            return tree
        if tree.val < minVal:
            return tree.rightChild
        if tree.val > maxVal:
            return tree.leftChild


if __name__ == "__main__":
    b = BinarySearchTree()
    b.insert(25)
    b.insert(15)
    b.insert(8)
    b.insert(20)
    b.insert(17)
    b.insert(16)
    b.insert(18)
    b.insert(40)
    b.insert(35)
    b.insert(46)
    b.insert(42)
    b.insert(50)
    b.inorder(b.root)
    print("Root:", b.root.val)
    print("After trimming:")
    b.trimBST(b.root, 20, 46)
    b.inorder(b.root)
