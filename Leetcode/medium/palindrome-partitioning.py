""" 
# PALINDROME PARTITIONING

Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
] 
"""

class Solution:
    def __init__(self):
        self.results = []
    
    def partition(self, s: str):
        self.find(s, [])
        return self.results
        
    def find(self, s, store):
        if len(s) == 0:
            self.results.append(store)
            return
        
        if len(s) == 1:
            store.append(s)
            self.results.append(store)
            
        else:
            for i in range(len(s)):
                if self.checkPalin(s[0:i+1]):
                    self.find(s[i+1:], store + [s[0:i+1]])
                    
    def checkPalin(self, s):
        return s == s[::-1]