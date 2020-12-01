""" 
# BASIC CALCULATOR II

Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

Example 1:

Input: s = "3+2*2"
Output: 7

Example 2:

Input: s = " 3/2 "
Output: 1

Example 3:

Input: s = " 3+5 / 2 "
Output: 5
 
Constraints:

1 <= s.length <= 3 * 105
s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
s represents a valid expression.
All the integers in the expression are non-negative integers in the range [0, 231 - 1].
The answer is guaranteed to fit in a 32-bit integer. 
"""

class Solution:
    def calculate(self, s: str) -> int:
        
        s += '$'
        operators = []
        operands = []
        temp = 0
        
        for x in s:
            if x == " ":
                continue
                
            if x.isdigit():
                temp = temp * 10 + int(x)
                continue
                
            else:
                operands.append(temp)
                if operators and operators[-1] in '*/':
                    op = operators.pop()
                    b = operands.pop()
                    a = operands.pop()
                    if op == '*':
                        operands.append(a * b)
                    else:
                        operands.append(int(a / b))
                
                elif operators and operators[-1] == '-':
                    operands.append(-operands.pop())
                    
                operators.append(x)
                temp = 0
                
        return sum(operands)