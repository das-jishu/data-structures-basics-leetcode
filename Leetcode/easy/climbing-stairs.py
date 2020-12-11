""" 
# CLIMBING STAIRS

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45 
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        return self.step(0, n, {})
    
    def step(self, current, n, known):
        if current > n:
            return 0
        
        if current == n:
            known[current] = 1
            return 1
        
        if current in known:
            return known[current]
        
        x = self.step(current + 1, n, known) + self.step(current + 2, n, known)
        known[current] = x
        return x