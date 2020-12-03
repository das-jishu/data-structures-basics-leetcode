""" 
# UGLY NUMBER II

Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:  

1 is typically treated as an ugly number.
n does not exceed 1690. 
"""

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
        result = [1] * n
        i2 = 0
        i3 = 0
        i5 = 0
        
        next2 = 2
        next3 = 3
        next5 = 5
        
        for i in range(1, n):
            result[i] = min(next2, next3, next5)
            
            if result[i] == next2:
                i2 += 1
                next2 = result[i2] * 2
                
            if result[i] == next3:
                i3 += 1
                next3 = result[i3] * 3
                
            if result[i] == next5:
                i5 += 1
                next5 = result[i5] * 5
                
        return result[-1]