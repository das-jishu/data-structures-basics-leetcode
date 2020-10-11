
class Stack(object):
    def __init__(self):
        self.st = []

    def size(self):
        return len(self.st)

    def add(self, item):
        self.st.append(item)

    def remove(self):
        return self.st.pop()

    def display(self):
        print(self.st)

    def peek(self):
        if self.size() > 0:
            return self.st[len(self.st) - 1]
    

def check(s):
    open = {')': '(', '}': '{', ']': '['}
    # close = [')', '}', ']']
    stack = Stack()
    for x in s:
        if x in open.values():
            stack.add(x)
        else:
            if open.get(x) == stack.peek():
                stack.remove()
            else:
                return False
    return stack.size() == 0

if __name__ == "__main__":
    print(check('({()})[]'))
    print(check('([]){[]}'))
    print(check(')(]{()}'))
