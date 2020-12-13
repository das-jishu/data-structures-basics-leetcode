""" 
# IS SUBSEQUENCE

Given a string s and a string t, check if s is subsequence of t.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?

Credits:
Special thanks to @pbrother for adding this problem and creating all test cases.

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 
Constraints:

0 <= s.length <= 100
0 <= t.length <= 10^4
Both strings consists only of lowercase characters. 
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        k = 0
        if len(s) == 0:
            return True
        if len(t) == 0 and len(s) == 0:
            return True
        if len(t) == 0:
            return False
        for x in t:
            if k >= len(s):
                return True
            if x == s[k]:
                if k == len(s):
                    return True
                k += 1
                
        return True if k == len(s) else False
                