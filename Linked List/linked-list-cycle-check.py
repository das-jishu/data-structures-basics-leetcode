
class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

def cyclecheck(head):
    marker1 = head
    marker2 = head

    while(marker2 != None and marker2.next != None):
        marker1 = marker1.next
        marker2 = marker2.next.next

        if (marker1 == marker2):
            return True

    return False

if __name__ == "__main__":
    a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
a.next = b
b.next = b
c.next = d
print(cyclecheck(a))