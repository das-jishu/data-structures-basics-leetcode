""" 
# MIN COST CLIMBING STAIRS

On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.

Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
Note:
cost will have a length in the range [2, 1000].
Every cost[i] will be an integer in the range [0, 999]. 
"""

class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        if not cost:
            return 0
        return min(self.costs(0, cost, {}), self.costs(1, cost, {}))
        
    def costs(self, pos, cost, known):
        if pos >= len(cost):
            return 0
        
        if pos == len(cost):
            return cost[pos]
        
        if pos in known:
            return known[pos]
        
        res = min(cost[pos] + self.costs(pos+1, cost, known), cost[pos] + self.costs(pos + 2, cost, known))
        known[pos] = res
        return res