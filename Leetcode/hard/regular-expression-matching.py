"""
# REGULAR EXPRESSION MATCHING

Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*' where: 

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input: s = "aab", p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
Example 5:

Input: s = "mississippi", p = "mis*is*p*."
Output: false
 

Constraints:

0 <= s.length <= 20
0 <= p.length <= 30
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        table = [[None for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        table[0][0] = True
        
        
        for row in range(1, len(s) + 1):
            table[row][0] = False
            
        for col in range(1, len(p) + 1):
            if p[col - 1] == "*":
                table[0][col] = table[0][col - 2]
            else:
                table[0][col] = False
            
        for row in range(1, len(s) + 1):
            for col in range(1, len(p) + 1):
                if p[col - 1] == ".":
                    table[row][col] = table[row - 1][col - 1]
                elif p[col - 1] != "*":
                    table[row][col] = table[row - 1][col - 1] and s[row - 1] == p[col - 1]
                else:
                    if p[col - 2] == ".":
                        table[row][col] = table[row][col - 1] or table[row][col - 2] or table[row - 1][col - 1] or table[row - 1][col]
                    else:
                        table[row][col] = table[row][col - 1] or table[row][col - 2] or (table[row - 1][col - 1] and p[col - 2] == s[row - 1])
                    
        for row in range(len(s) + 1):
            print(table[row])
                    
        return table[-1][-1]