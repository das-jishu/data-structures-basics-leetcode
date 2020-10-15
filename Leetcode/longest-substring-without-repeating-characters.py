""" 
Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces. 
"""

def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        maxi = 0
        temp = []
        c = 0
        for i, x in enumerate(s):
            if x not in temp:
                temp.append(x)
                c += 1
                maxi = max(maxi, len(temp))
            else:
                temp = [temp[i] for i, j in enumerate(temp) if i > temp.index(x)]
                temp.append(x)
        return maxi

# EFFICIENT SOLUTION
""" 
def lengthOfLongestSubstring(self, s: str) -> int:
        word = {}
        n,res,left = len(s),0,-1
        for i in range(n):
            if s[i] in word:left = max(left, word[s[i]])
            res = max(res,i-left)
            word[s[i]] = i
        return res 
"""