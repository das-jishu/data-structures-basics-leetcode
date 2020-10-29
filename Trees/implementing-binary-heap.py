
# MIN HEAP IMPLEMENTATION

class BinaryHeap(object):
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def insert(self, n):
        self.heap.append(n)
        self.size += 1
        self.percolateUp(self.size)

    def deleteMin(self):
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.percolateDown(1)

    def percolateUp(self, i):
        while i // 2 > 0:
            if self.heap[i] < self.heap[i // 2]:
                t = self.heap[i]
                self.heap[i] = self.heap[i // 2]
                self.heap[i // 2] = t
            i = i // 2

    def percolateDown(self, i):
        while i * 2 <= self.size:
            minChild = self.findMinChild(i)
            if self.heap[i] > self.heap[minChild]:
                t = self.heap[i]
                self.heap[i] = self.heap[minChild]
                self.heap[minChild] = t
            i = i * 2

    def findMinChild(self, i):
        if i * 2 + 1 > self.size:
            return i * 2
        if self.heap[i * 2] < self.heap[i * 2 + 1]:
            return i * 2
        return i * 2 + 1

    def buildHeap(self, l):
        i = len(l) // 2
        self.heap = [0] + l[:]
        self.size = len(l)
        while i > 0:
            self.percolateDown(i)
            i -= 1

if __name__ == "__main__":
    b = BinaryHeap()
    b.insert(5)
    b.insert(4)
    b.insert(7)
    b.insert(1)
    b.insert(0)
    b.insert(9)
    b.insert(2)
    print("Heap", b.heap)
    b.deleteMin()
    print("After deleting", b.heap)
    b.buildHeap([5, 4, 7, 1, 0, 9, 2])
    print("Building heap from list:", b.heap)

