
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

    return cur

if __name__ == "__main__":
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    a.next = b
    b.next = c
    c.next = d
    print(a.next.value, b.next.value, c.next.value)
    print(d.next)
    reverse(a)
    print(d.next.value, c.next.value, b.next.value, a.next)