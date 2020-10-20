""" 
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
 

Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000 
"""

# O(N) solution for both time and space.
# Other solution involves generating a sequence for the numbers in each row. Rigorous calculations required.

def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        r, flag = 0, True
        res = [ [] for _ in range(numRows) ]
        for x in s:
            if flag == True:
                res[r].append(x)
                if r == numRows - 1:
                    r -= 1
                    flag = False
                else:
                    r += 1
            else:
                res[r].append(x)
                if r == 0:
                    r += 1
                    flag = True
                else:
                    r -= 1
        result = ""
        for x in res:
            for y in x:
                result += y
        return result