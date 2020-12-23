""" 
# EXCEL SHEET COLUMN TITLE

Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...
Example 1:

Input: 1
Output: "A"

Example 2:

Input: 28
Output: "AB"

Example 3:

Input: 701
Output: "ZY" 
"""

class Solution:
    def convertToTitle(self, n: int) -> str:
        if n == 0:
            return ""
        
        res = ""
        while n > 0:
            rem = n % 26
            if rem == 0:
                rem = 26
            res = chr(64+rem) + res
            n = n // 26
            if rem == 26:
                n -= 1
            
        return res