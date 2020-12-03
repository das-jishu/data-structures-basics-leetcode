""" 
# DIFFERENT WAYS TO ADD PARENTHESIS

Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.

Example 1:

Input: "2-1-1"
Output: [0, 2]
Explanation: 
((2-1)-1) = 0 
(2-(1-1)) = 2

Example 2:

Input: "2*3-4*5"
Output: [-34, -14, -10, -10, 10]
Explanation: 
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10 
"""

class Solution:
    def diffWaysToCompute(self, input: str):
        if len(input) < 0 or input.isdigit():
            return [int(input)]
        
        return self.calculate(input)
    
    def calculate(self, s):
        if s.isdigit():
            return [int(s)]
        
        ret = []
        for i, x in enumerate(s):
            if x not in "+-*":
                continue
                
            left = self.calculate(s[:i])
            right = self.calculate(s[i+1:])
            
            for l in left:
                for r in right:
                    if x == "+":
                        temp = l + r

                    elif x == "-":
                        temp = l - r

                    else:
                        temp = l * r
                
                    ret.append(temp)
            
        return ret