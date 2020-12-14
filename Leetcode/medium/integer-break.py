""" 
# INTEGER BREAK

Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

Example 1:

Input: 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.

Example 2:

Input: 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
Note: You may assume that n is not less than 2 and not larger than 58.
"""

class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        if n == 3:
            return 2
        
        # 0 to 3 are special cases beacuse they will produce a result less than their value. We can't use that lesser value in the other calculations
        known = {0: 0, 1: 1, 2: 2, 3: 3}
        return self.breakDown(n, known) 
        
    def breakDown(self, n, known):
        if n in known:
            return known[n]
        
        else:
            maximum = 0
            for x in range(1, n // 2 + 1):
                p1 = self.breakDown(x, known)
                p2 = self.breakDown(n - x, known)
                maximum = max(maximum, p1 * p2)
                
            known[n] = maximum
            return known[n]
        