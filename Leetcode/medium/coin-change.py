""" 
# COIN CHANGE

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:

Input: coins = [2], amount = 3
Output: -1

Example 3:

Input: coins = [1], amount = 0
Output: 0

Example 4:

Input: coins = [1], amount = 1
Output: 1

Example 5:

Input: coins = [1], amount = 2
Output: 2

Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104 
"""

class Solution:
    def coinChange(self, coins, amount: int) -> int:
        if amount == 0:
            return 0
        coins.sort(reverse=True)
        known = {}
        return self.coin(coins, amount, known)
        
    def coin(self, coins, amount, known):
        if amount < coins[-1]:
            return -1
        
        if amount in coins:
            known[amount] = 1
            return 1
        
        if amount in known:
            return known[amount]
        
        res = float('inf')
        i = 0
        while i < len(coins):
            target = amount - coins[i]
            x = self.coin(coins, target, known)
            if x < 1:
                i += 1
                continue
            
            res = min(res, 1 + x)
            i += 1
        
        if res == float('inf'):
            res = -1
        known[amount] = res
        return res