""" 
# MIN STACK

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
 

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
 

Constraints:

Methods pop, top and getMin operations will always be called on non-empty stacks. 
"""

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stk=[]
        self.min=[float('inf')]

    def push(self, x: int) -> None:
        self.stk.append(x)
        if x <= self.min[-1]: self.min.append(x)
        
    def pop(self) -> None:
        x=self.stk.pop()
        if x == self.min[-1]: self.min.pop()
        return self.stk

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.min[-1]