
class Queue2Stacks(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()

if __name__ == "__main__":
    d = Queue2Stacks()
    for x in range(1, 10):
        d.enqueue(x)
    
    for x in range(1, 10):
        print(d.dequeue())