""" 
# DECODE WAYS

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

The answer is guaranteed to fit in a 32-bit integer.

Example 1:

Input: s = "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).

Example 2:

Input: s = "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Example 3:

Input: s = "0"
Output: 0
Explanation: There is no character that is mapped to a number starting with '0'. We cannot ignore a zero when we face it while decoding. So, each '0' should be part of "10" --> 'J' or "20" --> 'T'.

Example 4:

Input: s = "1"
Output: 1

Constraints:

1 <= s.length <= 100
s contains only digits and may contain leading zero(s). 
"""

class Solution(object):
    def __init__(self):
        self.memo = {}
        
    def numDecodings(self, s):
            """
            :type s: str
            :rtype: int
            """
            if not s or s == "0":
                return 0

            return self.findCombinations(s, 0)

    def findCombinations(self, s, index):

        if index == len(s):
            return 1

        if s[index] == "0":
            return 0

        if index == len(s) - 1:
            return 1

        if index in self.memo:
            return self.memo[index]

        if int(s[index:index+2]) <= 26:
            output = self.findCombinations(s, index+1) + self.findCombinations(s, index+2)
            self.memo[index] = output
            return output
        else:
            output = self.findCombinations(s, index+1)
            self.memo[index] = output
            return output
