""" 
# MINIMUM SIZE SUBARRAY SUM

Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).  
"""

class Solution:
    def minSubArrayLen(self, s: int, nums) -> int:
        
        minimal = float('inf')
        left = 0
        right = 0
        sums = 0
        while right < len(nums):
            sums += nums[right]
            while sums >= s:
                if right - left + 1 < minimal:
                    minimal = min(minimal, right - left + 1)
                sums -= nums[left]
                left += 1
            right += 1
            
        return 0 if minimal == float('inf') else minimal