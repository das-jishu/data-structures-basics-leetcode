""" 
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
Example 3:

Input: s = "a"
Output: "a"
Example 4:

Input: s = "ac"
Output: "a"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters (lower-case and/or upper-case), 
"""

def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        start, end = 0, 0
        for i in range(len(s)):
            l1 = self.expand(s, i, i)
            l2 = self.expand(s, i, i+1)
            m = max(l1, l2)
            if m > end - start:
                start = i - ((m - 1) // 2)
                end = i + m // 2
        return s[start:(end + 1)]
    
    def expand(self, s, left, right):
        l, r = left, right
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return r - l - 1