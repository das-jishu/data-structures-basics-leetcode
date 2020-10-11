
class Deque(object):
    def __init__(self):
        self.deq = []

    def addFront(self, item):
        self.deq.insert(0, item)

    def addRear(self, item):
        self.deq.append(item)
    
    def removeFront(self):
        return self.deq.pop(0)

    def removeRear(self):
        return self.deq.pop()

    def size(self):
        return len(self.deq)

    def display(self):
        print(self.deq)

if __name__ == "__main__":
    d = Deque()
    print('Size:',d.size())
    d.addFront(5)
    d.addRear(0)
    print(d.removeFront())
    d.addRear(8)
    d.addFront(5)
    d.addFront(5)
    d.addRear(6)
    d.addRear(6)
    d.display()
    print('Size:',d.size())
    print(d.removeFront())
    print(d.removeRear())