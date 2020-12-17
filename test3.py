
class Node(object):
    def __init__(self, marks, id, parent=None):
        self.marks = marks
        self.id = id
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

    def insert(self, marks, id):
        if not self.root:
            self.root = Node(marks, id)
        else:
            temp = self.root
            done = False
            while not done:
                if marks < temp.marks:
                    if temp.hasLeftChild():
                        temp = temp.getLeftChild()
                    else:
                        temp.leftChild = Node(marks, id, temp)
                        done = True
                else:
                    if temp.hasRightChild():
                        temp = temp.getRightChild()
                    else:
                        temp.rightChild = Node(marks, id, temp)
                        done = True
        self.size += 1

    def length(self):
        return self.size
    
    def inorder(self, root):
        if root:
            self.inorder(root.leftChild)
            print(root.id, root.marks)
            self.inorder(root.rightChild)

    def level_traversal(self, root):
        if not root:
            return
        q = [root]
        print(root.id,root.marks)
        
        while len(q) > 0:
            q2 = []
            for x in q:
                #print(x.marks, end=" ")
                if x.hasLeftChild():
                    temp = x.leftChild
                    print(temp.id," ",temp.marks," (",x.marks,"L)", sep="", end=" ")
                    q2.append(temp)
                if x.hasRightChild():
                    temp = x.rightChild
                    print(temp.id," ",temp.marks," (",x.marks,"R)", sep="", end=" ")
                    q2.append(temp)
            print()
            q = q2

if __name__ == "__main__":
    b = BinarySearchTree()
    done = False
    while not done:
        x = input().split()
        id = int(x[0])
        if id == -1:
            done = True
            continue
        marks = int(x[1])
        b.insert(marks, id)

    print("\nOUTPUT:")
    b.inorder(b.root)
    print()
    b.level_traversal(b.root)
    