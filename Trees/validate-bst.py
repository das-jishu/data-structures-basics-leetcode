
class Node(object):
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def validateBST(node, min, max):
    if not node:
        return True
    if node.val < min or node.val > max:
        return False
    return validateBST(node.left, min, node.val) and validateBST(node.right, node.val, max)

def verify(node):
    return validateBST(node, float('-inf'), float('inf'))

if __name__ == "__main__":
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    print(verify(root))
    root.left.left = Node(100)
    print(verify(root))
    
