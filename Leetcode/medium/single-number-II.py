""" 
# SINGLE NUMBER II

Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3
Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99 
"""

class Solution:
    def singleNumber(self, nums) -> int:
        
        visited = {}
        for i, el in enumerate(nums):
            if el in visited:
                visited[nums[i]] += 1
            else:
                visited[nums[i]] = 1
                
        for x in visited:
            if visited[x] == 1:
                return x

# PLEASE CHECK THE BITWISE APPROACH FOR THIS