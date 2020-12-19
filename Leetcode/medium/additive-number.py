""" 
# ADDITIVE NUMBER

Additive number is a string whose digits can form additive sequence.

A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.

Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

Example 1:

Input: "112358"
Output: true
Explanation: The digits can form an additive sequence: 1, 1, 2, 3, 5, 8. 
             1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8

Example 2:

Input: "199100199"
Output: true
Explanation: The additive sequence is: 1, 99, 100, 199. 
             1 + 99 = 100, 99 + 100 = 199
 

Constraints:

num consists only of digits '0'-'9'.
1 <= num.length <= 35
Follow up:
How would you handle overflow for very large input integers?
"""

class Solution:
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
 
        n = len(num)
        def dfs(j1, j2, j3):
            if j3 >= n:
                return False
            res = str(int(num[j1:j2]) + int(num[j2:j3]))
            if num[j3:].find(res) == 0:
                if j3+len(res) == n:
                    return True
                out = dfs(j2, j3, j3+len(res))
                if out == True:
                    return out
            return False
        k = 1
        while k < n - 1:
            i = k+1
            if num[0] == '0' and num[0:k] != '0':
                break
            while i < n:
                if num[k] == '0' and num[k:i] != '0':
                    break
                res = str(int(num[0:k]) + int(num[k:i]))
                if num[i:].find(res) == 0 and i + len(res) == n:
                    return True
                elif num[i:].find(res) == 0:
                    out = dfs(k, i, i+len(res))
                    if out == True:
                        return out
                i+= 1
            k+= 1
        return False