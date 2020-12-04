""" 
# PERFECT SQUARES

Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.

Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9. 
"""

class Solution:
    def numSquares(self, n: int) -> int:
        
        dp = [float('inf')] * (n+1)
        
        dp[0] = 0
        dp[1] = 1
        
        for i in range(2, n+1):
            j = 1
            while j * j <= i:
                x = dp[i - j * j]
                dp[i] = min(1 + x, dp[i])
                
                j += 1
                
        return dp[n]

# RECURSIVE SOLUTION

""" class Solution:
    def numSquares(self, target: int) -> int:
        def perfect(target):
            if target<=3:
                return target

            if dp[target]!=-1:
                return dp[target]

            p=float('inf')
            for i in a:
                if i*i>target:
                    break
                else:
                    p=min(p,1+perfect(target-i*i))
            dp[target]=p

            return dp[target]

        a=[]
        import math
        b=int(math.sqrt(target))
        for i in range(1,b+1):
            a.append(i)
        dp=[-1]*100001
        return perfect(target) """