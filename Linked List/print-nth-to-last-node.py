
class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

def reverse(head):
    prev = None
    cur = head

    while cur != None:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp

    return prev

def printntolast(val, head):
    head = reverse(head)
    cur = head
    while val > 1:
        cur = cur.next
        val -= 1

    return cur

###############################################
#### SOLUTION WITHOUT REVERSING

""" def ntolast(n, head):
    left = head
    right = head

    for i in range(n):
        if not right.next:
            raise LookupError('ERROR: n is larger than list')
        right = right.next

    while right.next:
        left = left.next
        right = right.next

    return left """
################################################

if __name__ == "__main__":
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    a.next = b
    b.next = c
    c.next = d
    print(printntolast(1, a).value)