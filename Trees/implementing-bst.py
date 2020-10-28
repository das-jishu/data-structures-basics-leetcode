
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

    def length(self):
        return self.size
    
    def inorder(self, root):
        if root:
            self.inorder(root.leftChild)
            print(root.val, end=" ")
            self.inorder(root.rightChild)

    def get(self, val):
        if not self.root:
            return None
        temp = self.root
        while True:
            if temp.val == val:
                return temp
            elif val < temp.val:
                if temp.hasLeftChild():
                    temp = temp.leftChild
                else:
                    return None
            else:
                if temp.hasRightChild():
                    temp = temp.rightChild
                else:
                    return None

    def findSuccessor(self, node):
        current = node
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def delete(self, val):
        if not self.root:
            print("Empty tree.")
            return
        if self.get(val) == None:
            print("No such node.")
            return
        temp = self.get(val)
        if self.length == 1 and temp == self.root:
            self.root = None
            return

        x = temp.parent
        if not temp.hasOneChild():
            print("Inside no child case.")
            if x.leftChild == temp:
                # print("No child and left child of parent.")
                x.leftChild = None
            else:
                x.rightChild = None

        elif not temp.hasBothChildren():
            print("Inside one child case.")
            if temp.hasLeftChild():
                if x.leftChild == temp:
                    x.leftChild = temp.leftChild
                else:
                    x.rightChild = temp.leftChild
                temp.leftChild.parent = x

            else:
                if x.leftChild == temp:
                    x.leftChild = temp.rightChild
                else:
                    x.rightChild = temp.rightChild 
                temp.rightChild.parent = x

        else:
            print("Inside both child case.")
            successor = self.findSuccessor(temp.rightChild)
            if successor:
                print("Successor:", successor.val)
            else:
                print("No successor")
            self.delete(successor.val)
            temp.val = successor.val
            """ succ_parent = successor.parent
            if succ_parent.leftChild == successor:
                succ_parent.leftChild = successor.rightChild
            else:
                succ_parent.rightChild = successor.rightChild
            
            if x.leftChild == temp:
                x.leftChild = successor
            else:
                x.rightChild = successor

            successor.leftChild = temp.leftChild
            successor.rightChild = temp.rightChild """



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
    print("Length:", b.length())
    print()
    b.delete(17)
    b.inorder(b.root)
    
    
    