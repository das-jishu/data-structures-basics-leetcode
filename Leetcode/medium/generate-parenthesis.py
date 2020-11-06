""" 
# GENERATE PARENTHESIS

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:

Input: n = 1
Output: ["()"] 

Constraints:

1 <= n <= 8 
"""

class Solution:
    def __init__(self):
        self.result = []
    
    def generateParenthesis(self, n):
        if n == 1:
            return ["()"]
        
        self.traverse("(", n * 2)
        
        return self.result
    
    def traverse(self, string, n):
        if len(string) == n:
            self.result.append(string)
            return
        
        lCount   = string.count("(")
        rCount  = string.count(")")
        
        if lCount == rCount:
            string = string + "("
            return self.traverse(string, n)
        
        if lCount == n/2:
            rightBracketsLeft = n - len(string)
            string = string + ")" * rightBracketsLeft
            return self.traverse(string, n)
        
        self.traverse(string + "(", n)
        self.traverse(string + ")", n)