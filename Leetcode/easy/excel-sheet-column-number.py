""" 
# EXCEL SHEET COLUMN NUMBER

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
Example 1:

Input: "A"
Output: 1

Example 2:

Input: "AB"
Output: 28

Example 3:

Input: "ZY"
Output: 701
 
Constraints:

1 <= s.length <= 7
s consists only of uppercase English letters.
s is between "A" and "FXSHRXW". 
"""

class Solution:
    def titleToNumber(self, s: str) -> int:
        k = 0
        res = 0
        while s:
            temp = ord(s[-1]) - 64
            res += temp * 26 ** k
            k += 1
            s = s[:-1]
            
        return res