""" 
# MAXIMUM SWAP

Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.

Example 1:
Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.

Example 2:
Input: 9973
Output: 9973
Explanation: No swap.
Note:
The given number is in the range [0, 108] 
"""

class Solution:
    def maximumSwap(self, num: int) -> int:
        
        n = [int(i) for i in str(num)]
        i = 0
        while i < len(n) - 1:
            m = n[i]
            
            j = i + 1
            temp = max(n[j:])
            if temp <= m:
                pass
            else:
                id = str(num).rindex(str(temp))
                t = n[i]
                n[i] = temp
                n[id] = t
                break
                
            i += 1
            
        res = 0
        for x in n:
            res = res * 10 + x
            
        return res
                