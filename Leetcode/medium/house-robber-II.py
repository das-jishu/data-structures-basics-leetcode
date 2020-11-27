""" 
# HOUSE ROBBER II

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 3:

Input: nums = [0]
Output: 0
 
Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 1000 
"""

class Solution:
    def rob(self, nums) -> int:
        if len(nums) == 1:
            return nums[0]
        known = [None] * len(nums)
        first = self.find(0, nums, True, known)
        known = [None] * len(nums)
        second = self.find(1, nums, False, known)
        
        return max(first, second)
        
    def find(self, n, nums, started, known):
        if n >= len(nums):
            return 0
        
        if n == len(nums) - 1:
            if started:
                return 0
            
            else:
                return nums[n]
            
        if known[n] != None:
            return known[n]
        
        current = nums[n] + self.find(n + 2, nums, started, known)
        alternate = self.find(n + 1, nums, started, known)
        known[n] = max(current, alternate)
        return known[n]