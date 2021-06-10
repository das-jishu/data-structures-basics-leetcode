"""
# INTERLEAVING STRING

Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
Example 3:

Input: s1 = "", s2 = "", s3 = ""
Output: true
 
Constraints:

0 <= s1.length, s2.length <= 100
0 <= s3.length <= 200
s1, s2, and s3 consist of lowercase English letters.
"""

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False
    
        return self.checkInterleaving(s3, s1, s2, 0, 0, 0, {})
        
    def checkInterleaving(self, s1, s2, s3, index1, index2, index3, cache):
        #print(index1, index2, index3)
        indexStr = self.getString(index1, index2, index3)
        if indexStr in cache:
            return cache[indexStr]
        
        if index1 == len(s1):
            cache[indexStr] = True
            return True
        
        if index2 < len(s2) and s1[index1] == s2[index2]:
            check = self.checkInterleaving(s1, s2, s3, index1 + 1, index2 + 1, index3, cache)
            if check:
                return True
            
        if index3 < len(s3) and s1[index1] == s3[index3]:
            check = self.checkInterleaving(s1, s2, s3, index1 + 1, index2, index3 + 1, cache)
            if check:
                return True
            
        cache[indexStr] = False
        return False
    
    def getString(self, i1, i2, i3):
        return str(i1) + "-" + str(i2) + "-" + str(i3)